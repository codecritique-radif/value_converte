from googletrans import Translator

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text

# Example usage:
source_language = "en"  # English
target_language = "es"  # Spanish
text_to_translate = "Hello, how are you?"
translated_text = translate_text(text_to_translate, source_language, target_language)
print(f"Translated: {translated_text}")