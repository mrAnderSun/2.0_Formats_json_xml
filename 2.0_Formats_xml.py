import xml.etree.ElementTree as ET
from pprint import pprint


#  поиск нужного текста
def main_xml():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    channel = root.find("channel")
    items = channel.findall("item")
    big_string(items)


#  объединения фрагментов описания
def big_string(items):
    description_tree = ""
    for item in items:
        text = item.find("description").text
        description_tree = description_tree + " " + text
    six_and_more(description_tree)


#  создание словаря {частота попадния слова : слово (len от 6 и выше)}
def six_and_more(description_tree):
    words = {}
    description_total = ""
    for word in description_tree.split():
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
            print("Top 10 words:")
            top = words_top
            pprint(top)
            break


#  Begin
main_xml()
