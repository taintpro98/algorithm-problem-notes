def flat(arr, depth):
  res = []
  for item in arr:
    if isinstance(item, list):
      if depth == 0:
        res.append(item)
      else:
        res.extend(flat(item, depth-1))
    else:
      res.append(item)
  return res

input = [1, 2, 3, [6, 5], [9, 8, [0]], 7] 
depth = 10

a = flat(input, depth)
print(a)