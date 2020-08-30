from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, abort, jsonify
import os
import glob
TEMPLATE_DIR = os.path.abspath('./dist')
STATIC_DIR = os.path.abspath('./dist/static')
print(TEMPLATE_DIR)
print(STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR) # template_folder='/Users/cake/Desktop/Projects/kidbrightAI/testVue/kidbrightai/dist')
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




@app.route('/putdata', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': 2,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

#app.run(host='0.0.0.0', port=80)
app.run()
