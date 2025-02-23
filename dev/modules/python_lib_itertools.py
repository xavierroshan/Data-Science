import itertools
import random

# for x in itertools.count(10,2):
#     if x >100:
#         breakpoint
#     print(x)


lst = ["red", "green", "blue"]
n = random.randint(1,15)
for i, color in zip(range(n), itertools.cycle(lst)):
    print(color)


for val in itertools.repeat('roshan', 3):
    print(val)
