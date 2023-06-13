'''
For a given text input, return the following properties as a dictionary:
total number of characters, number of words, number of sentences,
number of alpha characters
'''

text_input = "I am a student. I love to code."


def parse_text(text, delimiter=None):
    match delimiter:
        case None:
            return len(text.split())
        case "sentences":
            trimmed = text.rstrip('.')
            return len(trimmed.split('.'))
        case "letter":
            alphabetic_chars = "".join(filter(str.isalpha, text))
            return len(alphabetic_chars)


def analyse_text(text):
    text_data = {}
    text_data["num_chars"] = len(text)
    text_data["num_words"] = parse_text(text)
    text_data["num_sentences"] = parse_text(text, "sentences")
    text_data["letters"] = parse_text(text, "letter")
    return text_data


print(analyse_text(text_input))
