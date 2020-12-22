def find_matches(text, pattern, prime_number):
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1
    j = 0
    characters_number = 256
    matches = []

    for i in range(pattern_length - 1):
        h = (h * characters_number) % prime_number

    for i in range(pattern_length):
        pattern_hash = (characters_number * pattern_hash + ord(pattern[i])) % prime_number
        text_hash = (characters_number * text_hash + ord(text[i])) % prime_number

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1
            if j == pattern_length:
                matches.append(int(i))
        if i < text_length - pattern_length:
            text_hash = (characters_number * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime_number
            if text_hash < 0:
                text_hash = text_hash + prime_number

    return matches
