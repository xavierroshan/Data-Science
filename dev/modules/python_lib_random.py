"""import random

print(random.random())
print(random.randint(1,10))
print(random.uniform(1.0,100.0))
print(random.choice(["rock", "paper", "scissors"]))
print(random.choices(["rock", "paper", "scissors"], k=2))
print(random.sample(["rock", "paper", "scissors"], k=2))
numbers = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numbers)
print(numbers)"""

import random
import random

random.seed(42)  # Seed the random number generator with a fixed value

print(random.random())  # Output will be the same every time you run this script
print(random.randint(1, 10))  # Output will be the same every time you run this script
