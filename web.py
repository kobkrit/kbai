
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from google.protobuf import text_format
from object_detection.protos.string_int_label_map_pb2 import StringIntLabelMap, StringIntLabelMapItem
from object_detection.protos import pipeline_pb2
from object_detection.utils import dataset_util
from base64 import encodebytes

from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, abort, jsonify, send_file
import os
import glob
from xml.etree import ElementTree as ET
import xmltodict
import shutil
import io
import numpy as np
from PIL import Image
from collections import namedtuple, OrderedDict

import random

TEMPLATE_DIR = os.path.abspath('./dist')
STATIC_DIR = os.path.abspath('./dist/static')
print(TEMPLATE_DIR)
print(STATIC_DIR)

import tensorflow as tf
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        #print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            
            try:
              #print(member[0].text)
              value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
              xml_list.append(value)
            except IndexError:
              pass
    
            
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def create_tf_example(group, path, label_dict):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = [] 
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(label_dict[row['class']])

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


import urllib
import tarfile
from requests import get

#ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz


#MODEL = 'ssd_mobilenet_v1_coco_2018_01_28'
MODEL = 'ssd_mobilenet_v2_coco_2018_03_29'
#http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz

MODEL_FILE = MODEL + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
DEST_DIR = 'pretrained_model'

if not (os.path.exists(MODEL_FILE)):
  with open(MODEL_FILE, "wb") as file:
    # get request
    response = get(DOWNLOAD_BASE + MODEL_FILE)
    # write to file
    file.write(response.content)
    #opener = urllib.URLopener()
    #opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)

tar = tarfile.open(MODEL_FILE)
tar.extractall(path="./dist")
tar.close()


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

def run_inference_for_single_image(image, graph):
  with graph.as_default():
    with tf.Session() as sess:
      # Get handles to input and output tensors
      ops = tf.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
      ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
              tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[0], image.shape[1])
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

      # Run inference
      output_dict = sess.run(tensor_dict,
                             feed_dict={image_tensor: np.expand_dims(image, 0)})

      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.uint8)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
  return output_dict

  


def gen_tfrecord(image_dir, csv_input, output_path, label_dict):
    writer = tf.python_io.TFRecordWriter(output_path)
    path = os.path.join(image_dir)
    examples = pd.read_csv(csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path, label_dict)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


def parseXmlToJson(xml):
  response = {}

  for child in list(xml):
    if len(list(child)) > 0:
      response[child.tag] = parseXmlToJson(child)
    else:
      response[child.tag] = child.text or ''

    # one-liner equivalent
    # response[child.tag] = parseXmlToJson(child) if len(list(child)) > 0 else child.text or ''

  return response

def list_paths(path):
    directories = [x[1] for x in os.walk(path)]
    non_empty_dirs = [x for x in directories if x] # filter out empty lists
    return [item for subitem in non_empty_dirs for item in subitem] # flatten the list

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR) # template_folder='/Users/cake/Desktop/Projects/kidbrightAI/testVue/kidbrightai/dist')
#run_with_ngrok(app)   #starts ngrok when the app is run

NUM_OF_TRAINING_STEP = 1000
#from flask_ngrok import run_with_ngrok
gl = []
is_done = True

def run(cmd):
  global gl
  os.system(cmd)


from flask_cors import CORS, cross_origin

#TEMPLATE_DIR = os.path.abspath('./templates')
#STATIC_DIR = os.path.abspath('./static')
TEMPLATE_DIR = os.path.abspath('./dist')
STATIC_DIR = os.path.abspath('./dist/static')
print(TEMPLATE_DIR)
print(STATIC_DIR)
detection_graph = tf.Graph()
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR) # template_folder='/Users/cake/Desktop/Projects/kidbrightAI/testVue/kidbrightai/dist')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/getDrive', methods=['GET'])
def getDrive():
    drive = {
                  'drives': 'OK',
          'mountPoints': TEMPLATE_DIR
    }
    return jsonify(drive), 201


@app.route('/createProject', methods=['POST'])
def createProject():
    #data = request.form
    STATIC_DIR
    content = request.json
    print(content["projectDir"])
    try:
        os.mkdir(os.path.join(STATIC_DIR, content["projectDir"]))
        os.mkdir(os.path.join(STATIC_DIR, content["projectDir"], "images"))
        os.mkdir(os.path.join(STATIC_DIR, content["projectDir"], "imgclass"))
        f = open(os.path.join(STATIC_DIR, content["projectDir"], "imclass.json"), "a")
        f.write("{}")
        f.close()
        fxml = open(os.path.join(STATIC_DIR, content["projectDir"], "project.xml"), "a")
        fxml.write(" ")
        fxml.close()
        res = {'status': 'OK', 'mountPoints': content["projectDir"]}
    except OSError:
        print ("Creation of the directory  failed")
        res = {
            'status': 'not OK',
            'mountPoints': TEMPLATE_DIR
        }
  
        return jsonify(res), 201
    else:
        print ("Successfully created the directory")
        res = {
            'status': 'OK',
            'mountPoints': TEMPLATE_DIR
        }
  
        return jsonify(res), 201


@app.route('/getFiles', methods=['POST'])
def getFiles():
    allfiles = []
    for file in glob.glob("./dist/static/ruri/images/*.png"):
        
                
        #(os.path.relpath(file, 'dist'))

        allfiles.append({'file': os.path.relpath(file, 'dist'),
            'id': 1,
            'isAnotated': False,
            'class': 'totoro',
            'classCounts': 5})

        
    
    print(allfiles)

    res = {
        'status': 'OK',
        'mountPoints': TEMPLATE_DIR,
        'files': allfiles
    }
  
    return jsonify(res), 201



@app.route('/getProjects', methods=['GET'])
def getProjects():
    dds = []
    for x in os.listdir('./dist/static'):
        for fname in os.listdir('./dist/static/' + x):
            if fname.endswith('.xml'):
                # do stuff on the file
                print(x)
                dds.append(x)
                break
            else:
            # do stuff if a file .true doesn't exist.
                pass
            
    res = {
        'status': 'OK',
        'projects': dds
    }
  
    return jsonify(res), 201


@app.route('/writeXml', methods=['POST'])
def writeXml():
    rjson = request.json
    filename = TEMPLATE_DIR + "/" + rjson["filename"]
    xml_data = rjson["data"]
    print(xml_data)
    root = ET.fromstring(xml_data)
    print(filename)

    tree = ET.ElementTree(root)
    tree.write(filename)

    res = {
        'status': 'OK'
    }
  
    return jsonify(res), 201

@app.route('/checkXmlFile', methods=['POST'])
def checkXmlFile():
    rjson = request.json
    filename = TEMPLATE_DIR + "/" + rjson["filename"]
    print(filename)
    if(os.path.isfile(filename) == True):
        tree    = ET.parse(filename)
        xml = tree.getroot()
        xmlstr = ET.tostring(xml, encoding='utf8', method='xml')
        
        #parsed = xmljson.badgerfish.data(xml)
        parsed = xmltodict.parse(xmlstr)
        print(xml)
        res = {
            'status': 'OK',
            'data' : parsed
        }
    else:
        res = {
            'status': 'FAIL'
        }
    return jsonify(res), 201



@app.route('/imclassAnotaion', methods=['POST'])
def imclassAnotaion():
    req = request.json
    dirname = os.path.join(STATIC_DIR, req["projectpath"], "imgclass", req["dirname"])
    try:
        os.mkdir(dirname)
        res = {
            'status': 'OK',
        }
    except OSError:
        res = {
            'status': 'FAIL',
        }
    return jsonify(res), 201


@app.route('/getAnotaions', methods=['POST'])
def getAnotaions():
    req = request.json
    dirname = os.path.join(STATIC_DIR, req["projectpath"], "imgclass")
    try:
        dds = list_paths(dirname)
        print("get dds")
        print(dds)
        res = {
            'classes': dds,
            'status': 'OK'
        }
    except OSError:
        res = {
            'status': 'FAIL',
        }
    return jsonify(res), 201



@app.route('/addClass', methods=['POST'])
def addClass():
    content = request.json
    filePath = os.path.join(STATIC_DIR, content["projectpath"], "imclass.json")
    print(filePath)
    res = {
        'status': 'OK'
    }
    return jsonify(res), 201


@app.route("/upload", methods=['POST'])
def upload_file():
    content = request.json
    filePath = os.path.join(STATIC_DIR, content["projectpath"])
    tfpath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata")

    print(tfpath)
    if(os.path.isdir(tfpath) == True):
      print("Directory exist!!!!!!")
      try:  
        shutil.rmtree(tfpath)  
        print("% s removed successfully" % tfpath)  
      except OSError as error:  
        print(error)  
        print("File path can not be removed") 
    trainPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "images", "train")
    testPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "images", "test")
    dataPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "data")
    pretrainPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "pretrained_model")
    trainedPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "trained")
    
    os.mkdir(os.path.join(STATIC_DIR, content["projectpath"], "tfdata"))
    os.mkdir(os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "images"))
    os.mkdir(testPath) 
    os.mkdir(trainPath) 
    os.mkdir(dataPath) 
    os.mkdir(pretrainPath)
    os.mkdir(trainedPath)
    imagesPath = os.path.join(STATIC_DIR, content["projectpath"],'images') + '/*.* ' + os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "images", "train")
    os.system('cp ' + imagesPath)
    print('ls -Q ' + trainPath + ' | head -10 | xargs -i mv ' + trainPath + '{} ' + testPath)
    os.system('ls -Q ' + trainPath + ' | head -10 | xargs -i mv ' + trainPath + '/{} ' + testPath)

    #Copy pretained model
    copytree(os.path.join(TEMPLATE_DIR, MODEL),  os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "pretrained_model"))

    xml_df=xml_to_csv(trainPath)
    xml_df.to_csv(os.path.join(dataPath, 'train_labels.csv'), index=None)
    xml_df=xml_to_csv(testPath)
    xml_df.to_csv(os.path.join(dataPath, 'test_labels.csv'), index=None)


    #log("Getting number of labels...")
    csv_file_train = pd.read_csv(os.path.join(dataPath, 'train_labels.csv')) 
    column_val_list_train = csv_file_train['class']
    all_labels_train = set(column_val_list_train) 

    csv_file_test = pd.read_csv(os.path.join(dataPath, 'test_labels.csv')) 
    column_val_list_test = csv_file_test['class']
    all_labels_test = set(column_val_list_test) 

    all_labels = all_labels_train.union(all_labels_test)
    #log("All labels = "+ str(all_labels))

    s_labels = list(all_labels)
    #log("All classes = "+ str(s_labels))

    NUM_OF_CLASS = len(s_labels)
    print(NUM_OF_CLASS)

    #log("Number of classes = "+ str(NUM_OF_CLASS))
    #log("Number of training steps = "+ str(NUM_OF_TRAINING_STEP))

    def convert_classes(classes, start=1):
      msg = StringIntLabelMap()
      label_dict = {}
      for id, name in enumerate(classes, start=start):
        msg.item.append(StringIntLabelMapItem(id=id, name=name))
        label_dict[name] = id

      text = str(text_format.MessageToBytes(msg, as_utf8=True), 'utf-8')
      return text, label_dict

    txt, label_dict = convert_classes(s_labels)
    print(txt)

    with open(os.path.join(dataPath, 'object-detection.pbtxt'), 'w') as f:
      f.write(txt)

    gen_tfrecord(image_dir=trainPath, csv_input=os.path.join(dataPath, 'train_labels.csv'), output_path=os.path.join(dataPath, 'train.record'), label_dict=label_dict)
    
    gen_tfrecord(image_dir=testPath , csv_input=os.path.join(dataPath, 'test_labels.csv'), output_path=os.path.join(dataPath, 'test.record'), label_dict=label_dict)
 
    os.environ['CONFIG_FILE'] = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "pipeline_mobilenet_v1_ssd_retrain_last_few_layers_edited.config")
    filenameOut = os.environ['CONFIG_FILE']

    #filename = '/root/tfdata/pipeline_mobilenet_v1_ssd_retrain_last_few_layers.config'
    #filename = '/root/TPU-MobilenetSSD/colaboratory/gpu/pipeline_mobilenet_v1_ssd_retrain_last_few_layers.config'
    filename = '/home/pi/TPU-MobilenetSSD/colaboratory/gpu/pipeline_mobilenet_v2_ssd_retrain_last_few_layers.config'
    #filename = '/root/tfdata/pipeline_mobilenet_v2_ssdlite_retrain_last_few_layers.config'

    filenameOut = os.environ['CONFIG_FILE']

    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig() 

    

    with tf.gfile.GFile(filename, "r") as f:                                                                                                                                                                                                                     
      proto_str = f.read()                                                                                                                                                                                                                                          
      text_format.Merge(proto_str, pipeline_config)


    pipeline_config.model.ssd.num_classes = NUM_OF_CLASS
    pipeline_config.train_config.num_steps = NUM_OF_TRAINING_STEP
    pipeline_config.train_config.fine_tune_checkpoint=os.path.join(pretrainPath, "model.ckpt")
    pipeline_config.train_input_reader.label_map_path=os.path.join(dataPath, 'object-detection.pbtxt')
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[0]=os.path.join(dataPath, "train.record") 
    pipeline_config.eval_input_reader[0].label_map_path=os.path.join(dataPath, 'object-detection.pbtxt')
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[0]=os.path.join(dataPath,"test.record") 
    pipeline_config.train_config.batch_size=4

    config_text = text_format.MessageToString(pipeline_config)   
    print(config_text)                                                                                                                                                                                                    
    with tf.gfile.Open(filenameOut, "wb") as f:                                                                                                                                                                                                                       
      f.write(config_text)   
    cmd_train = 'python3 ~/models/research/object_detection/model_main.py \
    --pipeline_config_path=' + filenameOut + ' \
    --model_dir='+trainedPath + ' \
    --alsologtostderr \
    --num_train_steps='+str(NUM_OF_TRAINING_STEP)+' \
    --num_eval_steps=0'

    print(cmd_train)
    os.system(cmd_train)

    outputFineTuned = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "fine_tuned_model")


    #log("[Training Thread] Exporting Check point to Saved model...")
    trained_checkpoint_prefix = trainedPath+'/model.ckpt-'+str(NUM_OF_TRAINING_STEP)
    export_dir = os.path.join(trainedPath, '0')

    graph = tf.Graph()
    with tf.compat.v1.Session(graph=graph) as sess:
      # Restore from checkpoint
      loader = tf.compat.v1.train.import_meta_graph(trained_checkpoint_prefix + '.meta')
      loader.restore(sess, trained_checkpoint_prefix)

      # Export checkpoint to SavedModel
      builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(export_dir)
      builder.add_meta_graph_and_variables(sess,
                                          [tf.saved_model.TRAINING, tf.saved_model.SERVING],
                                          strip_default_attrs=True)
      builder.save()  


    lst = os.listdir(trainedPath)
    lf = filter(lambda k: 'model.ckpt-' in k, lst)
    last_model = sorted(lf)[-1].replace('.meta', '')
    #log(last_model)
    os.environ['last_model']=last_model

   

    os.system('python3 /root/models/research/object_detection/export_inference_graph.py \
      --input_type=image_tensor \
      --pipeline_config_path=$CONFIG_FILE \
      --output_directory=' + outputFineTuned + ' \
      --trained_checkpoint_prefix=' + trainedPath +'/$last_model')
    PATH_TO_FROZEN_GRAPH = os.path.join(outputFineTuned, 'frozen_inference_graph.pb')
    with detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


    res = {
        'status': 'OK'
    }
    return jsonify(res), 201

 
@app.route("/detect", methods=['POST'])
def detect():
    content = request.json
    testPath = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "images", "test")
    PATH_TO_LABELS = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "data", "object-detection.pbtxt")
    #testPath = os.path.join(STATIC_DIR, content["projectpath"], "images")
    png_files = []
    for file in os.listdir(testPath):
        if file.endswith(".png"):
            png_files.append(file)
    
    #image_path = os.path.join(testPath, content["filename"])
    image_path = os.path.join(testPath, random.choice(png_files))
    
    image = Image.open(image_path)
    image = image.convert("RGB")
    image_np = load_image_into_numpy_array(image)
    # convert numpy array to PIL Image
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)


    vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks'),
      use_normalized_coordinates=True,
      line_thickness=8)
    
    img = Image.fromarray(image_np.astype('uint8'))

    # create file-object in memory
    file_object = io.BytesIO()

    # write PNG in file-object
    img.save(file_object, 'PNG')

    # move to beginning of file so `send_file()` it will read from start    
    file_object.seek(0)

    encoded_img = encodebytes(file_object.getvalue()).decode('ascii')
    res =  { 'Status' : 'Success', 'ImageBytes': encoded_img}

    return jsonify(res), 201
    #return send_file(file_object, mimetype='image/PNG')



@app.route("/loadFrozenGraph", methods=['POST'])
def loadFrozenGraph():
   
    content = request.json
    outputFineTuned = os.path.join(STATIC_DIR, content["projectpath"], "tfdata", "fine_tuned_model")

    PATH_TO_FROZEN_GRAPH = os.path.join(outputFineTuned, 'frozen_inference_graph.pb')
    with detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
 


    res = {
      'status': 'OK'
    }
    return jsonify(res), 201 



#app.run()

app.run(host='0.0.0.0', port=80)


