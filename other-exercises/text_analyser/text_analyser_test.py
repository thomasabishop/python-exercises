import text_analyser


def test_text_analyser():
    input_text = "I am become Death. Destroyer of worlds."
    expected = {
        "num_chars": 39,
        "num_words": 7,
        "num_sentences": 2,
        "letters": 31,
    }
    assert text_analyser.analyse_text(input_text) == expected
