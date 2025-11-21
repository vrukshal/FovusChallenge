from flask import Flask, request, abort
from werkzeug.utils import secure_filename
import os
from utils.upload_utils import upload_file_to_s3

app = Flask(__name__)

@app.route('/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, description="No file found in request")

    file = request.files['file']

    if file.filename == '':
        abort(400, description="No selected file")

    # Save file temporarily
    filename = secure_filename(file.filename)
    temp_path = os.path.join("temp_uploads", filename)

    os.makedirs("temp_uploads", exist_ok=True)
    file.save(temp_path)

    # Upload to S3
    uploaded = upload_file_to_s3(temp_path)

    # Remove temp file
    os.remove(temp_path)

    if uploaded:
        return {"message": f"File '{filename}' uploaded successfully"}, 201
    else:
        return {"message": "Upload failed"}, 500

if __name__ == '__main__':
    app.run(debug=True)
