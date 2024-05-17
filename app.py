from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Create an 'uploads' directory if it doesn't exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        # Ensure a safe filename
        filename = secure_filename(file.filename)

        # Save the file to the 'uploads' folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

    return render_template('upload.html')  # Provide the HTML template
if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Listen on all interfaces
