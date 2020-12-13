def count(final_length, word, results):
    current_length = 1
    for i in range(0, len(word)):
        next_word = word.replace(word[i], "")
        if next_word in results:
            current_length = max(current_length, results[next_word])

    results[word] = current_length + 1
    return max(current_length, final_length)


def final_count(words, results):
    final_length = 0
    for word in words:
        final_length = count(final_length, word, results)

    return final_length
