import json, os

_cache = {}
chat_langs = {}

def get_strings(lang_code):
    if lang_code in _cache:
        return _cache[lang_code]
    path = f"locales/{lang_code}.json"
    if not os.path.exists(path):
        path = "locales/en.json"
    with open(path) as f:
        _cache[lang_code] = json.load(f)
    return _cache[lang_code]

def set_lang(chat_id, lang):
    chat_langs[chat_id] = lang

def get_lang(chat_id):
    return chat_langs.get(chat_id, "en")
