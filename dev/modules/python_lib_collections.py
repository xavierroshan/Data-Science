import collections
lst1= [1, 2, 3, 4, 5]
dq = collections.deque(lst1)
dq.append(100)
dq.appendleft(200)
print(list(dq))
dq.pop()
dq.popleft()
print(list(dq))
letter_count=collections.Counter("My name is roshan xavier")
print(dict(letter_count))
data = ["red", "blue", "red", "green", "blue", "blue"]
item_count = dict(collections.Counter(data))
print(item_count)