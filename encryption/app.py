from flask import Flask, request, render_template, send_file
import numpy as np
import os
from encryption import process_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            file.save('uploaded_image.png')
            key_array = process_image('uploaded_image.png', encrypt=True)
            np.save('key.npy', key_array)
            return render_template('result.html', image='encrypted_image.png', key='key.npy')
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
