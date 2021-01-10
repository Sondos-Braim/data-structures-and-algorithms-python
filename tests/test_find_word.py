from data_structures_and_algorithms.challenges.repeated_word.repeated_word import find_word
def test_normal_string():
    string = 'Once upon a time, there was a brave princess who...'
    assert find_word(string) == 'a'
def test_anothor_regular_string():
    string = 'Hello, my name is joudi. What id your name ?'
    assert find_word(string) == 'name'
def test_punctuation_marks():
    string = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    assert find_word(string) == 'summer'
def test_capital_words():
    string = 'Good morning, it feels good to see you again'
    assert find_word(string) == 'good'