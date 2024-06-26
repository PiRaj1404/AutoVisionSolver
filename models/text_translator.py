from google.cloud import translate_v2 as translate

class TextTranslator:
    def __init__(self):
        self.translate_client = translate.Client()

    def translate_text(self, text, target_lang='en'):
        translation_result = self.translate_client.translate(text, target_language=target_lang)
        return translation_result['translatedText']
