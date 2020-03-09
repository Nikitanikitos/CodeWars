import re


def top_3_words(text):
    top_3, res = {}, []
    text = re.sub(r"[\-.,_#%!/@*;:]", " ", text)
    for word in text.lower().split():
        if re.search(r"[a-zA-Z]", word):
            top_3[word] = top_3.get(word, 0) + 1
    for key, value in sorted(top_3.items(), key=lambda item: item[1], reverse=True):
        if len(res) == 3:
            return res
        res += [key]
    return res


print(top_3_words("  //'wont won't won't "))