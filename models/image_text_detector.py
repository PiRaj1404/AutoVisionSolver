import os
from google.cloud import vision

class ImageTextDetector:
    def __init__(self, credential_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
        self.vision_client = vision.ImageAnnotatorClient()

    def detect_text_from_file(self, file):
        image_content = file.read()
        return self._detect_text_from_content(image_content)

    def _detect_text_from_content(self, image_content):
        image = vision.Image(content=image_content)
        response = self.vision_client.text_detection(image=image)
        if response.error.message:
            raise Exception(f"{response.error.message}\nFor more info on error messages, check: https://cloud.google.com/apis/design/errors")
        if response.text_annotations:
            return response.text_annotations[0].description
        return ''
