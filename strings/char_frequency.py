def freq_char(word):
    freq={}
    for i in word:
        freq[i]=freq.get(i,0)+1
    return freq
print(freq_char("Programming"))
