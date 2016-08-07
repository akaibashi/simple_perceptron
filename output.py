def dot(vec0, vec1):
  tmp = 0
  for i in range(len(vec0)):
    tmp += vec0[i] * vec1[i]
  return tmp

def step(num):
  if num > 0:
    return 1
  else:
    return 0

i = [1,2,3,4,5]
w = [1,2,3,4,5]

o = step(dot(i, w))

print o
