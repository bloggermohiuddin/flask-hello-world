from flask import Flask, request, jsonify
import cv2
import numpy as np
import json

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    # Read image as numpy array
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Example: convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # For demo: return image shape
    return jsonify({'shape': gray.shape})

if __name__ == "__main__":
    app.run()
