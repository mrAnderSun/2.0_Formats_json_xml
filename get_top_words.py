from pprint import pprint


def words_count(description):
    words = {}
    for word in description:
        word_count = description.count(word)
        words[word_count] = word
    #print(len(description))
    return words


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