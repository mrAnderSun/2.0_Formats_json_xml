import json
from pprint import pprint


#  поиск нужного текста
def main_json():
    description_news_str = ""
    data = json.load(fjson)
    description_tree = data["rss"]["channel"]["items"]
    for desc in description_tree:
        description_new = desc["description"]
        description_news_str = description_news_str + " " + str(description_new)
    six_and_more(description_news_str)


#  создание словаря {частота попадния слова : слово (len от 6 и выше)}
def six_and_more(description_news_str):
    words = {}
    description_total = ""
    for word in description_news_str.split():
        if len(word) > 6:
            description_total = description_total + " " + word
    total_words = len(description_total)
    for word in description_total.split():
        word_count = description_total.count(word)
        word_percent = word_count / total_words * 100
        words[word_percent] = word
    sorted_top_words(words)


#  вывод top 10
def sorted_top_words(words):
    words_top = {}
    for k, v in sorted(words.items(), reverse=True):
        words_top.update([(k, v)])
        if len(words_top) < 10:
            continue
        else:
            pprint(words_top)
            break


#  Begin
with open(r"Files/newsafr.json", encoding="utf-8") as fjson:
    main_json()
