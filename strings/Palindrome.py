def palindrome(word):
  word=word.lower().replace(' ','')
  i=0
  j=len(word)-1
  while i<j:
    if word[i]!=word[j]:
      return False
    else:
      i+=1
      j-=1
  return True
print(palindrome("Never odd or even"))
    
    
