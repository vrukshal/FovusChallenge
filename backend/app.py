from flask import Flask
from utils.upload_utils import upload_file
from flask import Flask, request, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, description="No file part in the request")

    file = request.files['file']

    if file.filename == '':
        abort(400, description="No selected file")

    response = upload_file(file)
    if response:
        return {"message": f"File '{file.filename}' successfully uploaded to S3!"}, 201
    else:
        return {"message" : "Failed to upload file to S3"}, 500

if __name__ == '__main__':
    app.run(debug=True)

