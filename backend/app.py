from flask import Flask

app = Flask(__name__)

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

    return {"message": f"File '{file.filename}' successfully found!"}, 201

if __name__ == '__main__':
    app.run(debug=True)

