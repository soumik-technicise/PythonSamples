def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]


if __name__ == "__main__":
    words = ['abv', 'try me', 'test']
    print map_to_lengths_for(words)
    print map_to_lengths_map(words)
    print map_to_lengths_lists(words)
