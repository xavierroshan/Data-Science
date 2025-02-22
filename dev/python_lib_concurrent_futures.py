"""import concurrent.futures
import requests

def fetch_url(url):
    response = requests.get(url)
    return response.status_code


urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com',
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(fetch_url, url):url for url in urls}
    for future in concurrent.futures.as_completed(futures):
        print(type(future))
        url = futures[future]
        status_code = future.result()
        print(f"{url} status code is {status_code}")
        print(f"{url} status code is {status_code}")"""


import concurrent.futures


def compute_square(n):
    return n*n


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(compute_square, number):number for number in numbers}
        for future in concurrent.futures.as_completed(futures):
            number = futures[future]
            square = future.result()
            print(f"square of {number} is {square}")