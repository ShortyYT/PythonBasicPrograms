def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "đ",
        ":(": "âšī¸",
        ";)": "đ"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ""
    return output


message = input(">")
print(emoji_converter(message))
