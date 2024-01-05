from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

def translate_texts_to_swahili(texts, to_language):
    translator = Translator(to_lang=to_language)
    translations_swahili = []

    for text in texts:
        translation = translator.translate(text)
        translations_swahili.append(translation)

    return translations_swahili

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # get the request from the client
        data = request.get_json()

        supported_languages = {"english": "en", "french": "fr", "spanish": "es", "german": "de", "swahili": "sw"}
        
        try:  # Put the default to Swahili if any error occurs

            lang = supported_languages.get(data.get("language", "").lower(), "sw")
        except Exception:
            lang = "sw"



        # Get sentences if it is only text ( lists )
        if 'sentences' in data and isinstance(data['sentences'], list):
            texts_to_translate = data['sentences']
            translated_texts_swahili = translate_texts_to_swahili(texts_to_translate, lang)

            result = {
                "success": True,
                "translations_swahili": translated_texts_swahili
            }

            return jsonify(result)

        else:
            result = {
                "success": False,  # -> error occurred
                "error": "Invalid input format"  # -> the data came is not lists
            }

            return jsonify(result), 400

    except Exception as e:
        result = {
            "success": False,
            "error": str(e)
        }
        return jsonify(result), 500

if __name__ == '__main__':
    app.run(debug=True)
