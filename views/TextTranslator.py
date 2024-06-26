from flask import request, jsonify
from flask.views import MethodView
from models.text_translator import TextTranslator

class TranslateTextView(MethodView):
    def __init__(self):
        self.translator = TextTranslator()

    def post(self):
        data = request.json
        text = data.get('text')
        target_lang = data.get('target_lang', 'en')
        try:
            translated_text = self.translator.translate_text(text, target_lang)
            return jsonify({"translated_text": translated_text})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
