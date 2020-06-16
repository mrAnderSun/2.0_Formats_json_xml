import xml.etree.ElementTree as ET
import get_top_words


#  поиск нужного текста
def xml_parser():
    description = []
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    channel = root.find("channel")
    items = channel.findall("item")
    get_words_more_6(items, description)
    get_top_words.sorted_top_words(get_top_words.words_count(description))


def get_words_more_6(items, description):
    for item in items:
        text = item.find("description").text
        for word in text.casefold().split():
            if len(word) > 6:
                description.append(word)
    return description


#  Begin
xml_parser()
