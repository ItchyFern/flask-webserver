from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import random
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r".\uploads"
app.config['MAX_CONTENT_PATH'] = 1048576

@app.route('/upload')
def upload():
    #return os.getcwd()
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      upload_location = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(generate_filename(f)))
      f.save(upload_location)
      return f'<a href = http://localhost:5000/{upload_location}>http://localhost:5000/{upload_location}</a>'

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads, filename)

def generate_filename(f):
    name, ext = os.path.splitext(f.filename)
    filename = hex(random.randint(1000000000, 100000000000))[2:]
    return filename + ext

    
    

if __name__ == '__main__':
   app.run(debug = True)