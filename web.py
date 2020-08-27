from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, abort, jsonify
import os
TEMPLATE_DIR = os.path.abspath('./dist')
STATIC_DIR = os.path.abspath('./dist/static')
print(TEMPLATE_DIR)
print(STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR) # template_folder='/Users/cake/Desktop/Projects/kidbrightAI/testVue/kidbrightai/dist')
run_with_ngrok(app)   #starts ngrok when the app is run
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

app.run()
