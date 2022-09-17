def xor_chars(c1,c2):
  minn = ord('A')
  maxx = ord('z')
  x = ord(c1)-minn
  y = ord(c2)-minn
  return chr(minn + ((x^y)%(maxx-minn)) )

def xor_chain(text):
  lst = [ c for c in text]
  return text[0]+''.join([ xor_chars(lst[i],lst[i+1]) for i in range(len(text)-1)])

def xor_pairwise(text):
  lst = [ c for c in text]
  lst2 = [lst[0]]
  for i in lst[1:]:
    lst2.append(xor_chars(lst2[-1],i))
  return ''.join([ i for i in lst2 ])


import math

def hash1(word):
  x = 'a'
  for c in word:
    x = xor_chars(x,c)
  return x

def hash(word,n=64):
  x = hash1(word)
  for i in range(1+math.floor(n/len(word))):
    x = hash1(x) + xor_pairwise( x + word )
  return x[:n]
