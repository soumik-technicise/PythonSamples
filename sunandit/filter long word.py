def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)


print filter_long_words(['test', 'not', 'this should'], 5)
