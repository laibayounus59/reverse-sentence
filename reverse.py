
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.insert(0, word)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
sentence = "Python is fun"
output = reverse_sentence(sentence)
print(output)
