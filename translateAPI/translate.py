from google.cloud import translate

EN = "en-US"
TR = "tr"
PROJECT_ID = "valid-flow-412916"
client = translate.TranslationServiceClient()

def translate_text(text="Hello, world!", source_language="en-US", target_language="tr"):

    location = "global"
    parent = f"projects/{PROJECT_ID}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": source_language,
            "target_language_code": target_language,
        }
    )
    for translation in response.translations:
        return translation.translated_text
    

translate_text(text="", source_language=EN, target_language=TR)

"""
{
  "translations": [
    {
      "translatedText": "TRANSLATED_TEXT",
    }
  ]
}
"""