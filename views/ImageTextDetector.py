from flask import request, jsonify
from flask.views import MethodView
from models.image_text_detector import ImageTextDetector
import os

class DetectTextView(MethodView):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        credential_path = os.path.join(current_dir,'..', 'gcpKeys.json')
        self.detector = ImageTextDetector(credential_path)

    def post(self):
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        try:
            detected_text = self.detector.detect_text_from_file(file)
            return jsonify({"detected_text": detected_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
