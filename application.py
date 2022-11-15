from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import random
import glob
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "uploads"
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
        f.save(os.path.join(app.root_path, upload_location))
        # delete file after x time
        #later_function(upload_location, 1800)
        #return link to file
        return render_template('download.html', value=request.url_root+upload_location)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(uploads, filename)

@app.route('/delete')
def delete_uploads():
    print(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))

    files = glob.glob(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], "*"))
    for f in files:
        os.remove(f)
        
    return upload()


def generate_filename(f):
    name, ext = os.path.splitext(f.filename)
    filename = hex(random.randint(1000000000, 100000000000))[2:]
    return filename + ext

if __name__ == '__main__':
   app.run(host='0.0.0.0')
