def non_repeating(char):
  char=char.lower()
  freq={}
  for ch in char:
    freq[ch]=freq.get(ch,0)+1
  for ch in char:
    if freq[ch]==1:
      return ch
print(non_repeating("Python"))
      
