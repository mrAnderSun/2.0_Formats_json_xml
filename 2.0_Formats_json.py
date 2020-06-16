import json
import get_top_words


#  парсинг json, 
def json_parser():
    description_new = []
    data = json.load(fjson)
    description_tree = data["rss"]["channel"]["items"]
    for desc in description_tree:
        description = desc["description"]
        for word in description.casefold().split():
            if len(word) > 6:
                description_new.append(word)
    get_top_words.sorted_top_words(get_top_words.words_count(description_new))


#  Begin
with open(r"Files/newsafr.json", encoding="utf-8") as fjson:
    json_parser()
