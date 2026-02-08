def reverse_words(sentence):
    words = sentence.split()
    print(words)
    result = []

    for word in words:
        rev = ""
        for ch in word:
            rev = ch + rev   # build reverse manually
        result.append(rev)

    return " ".join(result)


print(reverse_words("I love Python"))
