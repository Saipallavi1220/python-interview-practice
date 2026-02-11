def anagram(word1,word2):
  word1=word1.lower()
  word2=word2.lower()
  if len(word1)!=len(word2):
    return False
  freq={}
  for ch in word1:
    freq[ch]=freq.get(ch,0)+1
  for ch in word2:
    if ch not in freq or freq[ch]==0:
      return False
    freq[ch]-=1
  return True
print(anagram("Silent","Listen"))
