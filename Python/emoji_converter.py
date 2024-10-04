def emoji_converter(input_message):
    words = input_message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output

message = input("Write a message: ")

new_message = emoji_converter(message)

print(new_message)
