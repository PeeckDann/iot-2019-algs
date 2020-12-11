def count(word, words, word_sequence):

    word_sequence += [word]
    if len(word) == 1:
        return word_sequence

    all_word_sequences = []
    for i in range(0, len(word)):
        next_word = word.replace(word[i], "")
        for another_word in words:
            if another_word == next_word and another_word not in word_sequence:
                new_word_sequences = count(another_word, words, word_sequence)
                for new_word_sequence in new_word_sequences:
                    all_word_sequences.append(new_word_sequence)

    return all_word_sequences


def final_count(words):
    results = []

    for word in words:
        word_sequence = []
        result = count(word, words, word_sequence)
        if len(result) == 0:
            results.append(1)
        else:
            results.append(len(result))

    return max(results)
