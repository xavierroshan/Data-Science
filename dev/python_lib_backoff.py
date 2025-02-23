import backoff 
import random

def work():
    x = random.random()
    if x < .6:
        print(x)
        raise ValueError("Temporary error")
    else:
        return ("Suceess")
    



@backoff.on_exception(backoff.constant, ValueError, max_tries=10 )
def do_work():
     return work()

do_work()

try:
    result = do_work()
    print(result)
except ValueError:
    print("failed after 3 attempts")



