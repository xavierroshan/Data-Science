# import requests
# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)
# print("*****************************************")
# print(x.status_code)
# print("*****************************************")
# print(x.headers)

# import requests
# response=requests.get("https://api.github.com")
# if response.status_code == 200:
#     print("Success")
# else:
#     print("Not found")

# if response:
#     print("success")
# else:
#     raise Exception(f"Non success status code: {response.status_code}")


# import requests
# response = requests.get("https://api.github.com/invalid")
# if response:
#     print ("Success")
# else:
#     raise Exception(f"Non success status code: {response.status_code}")


# import requests
# from requests.exceptions import HTTPError
# urls = ["https://api.github.com", "https://api.github.com/invalid"]

# for url in urls:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print (f"HTTP error occured: {http_err}")
#     except Exception as err:
#         print(f"other error occured: {err}")
#     else:
#         print("Success !!")

# import requests
# response = requests.get("https://api.github.com")
# x=response.content
# print(x)
# print(type(x))
# response.encoding="utf-8" #
# y=response.text
# print(y)
# print(type(y))
# z=response.json()
# print(z)
# print(type(z))

# import requests
# response=requests.get("https://api.github.com")
# print(response.headers)
# print(response.headers["Content-Type"])

# import requests
# #search github's repository for popular python projects
# params = {"q":"language:python", "sort":"stars", "order":"desc"}
# response = requests.get("https://api.github.com/search/repositories", params=params)


# #inspect some attributes of the first three repositories
# json_response = response.json()
# popular_repositories = json_response["items"]
# for repo in popular_repositories:
#     print(repo["name"])
#     print(repo["description"])
#     print(repo["stargazers_count"])
#     print("***********************************************************************************")

# import requests

# # Search GitHub's repositories for popular Python projects with more than 1000 forks
# # created in the last year
# query = "language:python forks:>1000 created:>2024-01-01 solana in:name,description "

# response = requests.get(
#     "https://api.github.com/search/repositories",
#     params={"q": query, "sort": "stars", "order": "desc"},
# )

# # Inspect some attributes of the first three repositories
# json_response = response.json()
# popular_repositories = json_response["items"]
# for repo in popular_repositories[:3]:
#     print(f"Name: {repo['name']}")
#     print(f"Description: {repo['description']}")
#     print(f"Stars: {repo['stargazers_count']}")
#     print(f"Forks: {repo['forks_count']}") # Adding the number of forks
#     print(f"Created at: {repo['created_at']}") # Adding the creation date
#     print("***********************************************************************************")


# import requests

# # Search GitHub's repositories for popular Python projects with more than 1000 forks
# # created in the last year
# query = "user:xavierroshan"

# response = requests.get(
#     "https://api.github.com/search/repositories",
#     params={"q": query, "sort": "stars", "order": "desc"},
# )

# # Inspect some attributes of the first three repositories
# json_response = response.json()
# popular_repositories = json_response["items"]
# for repo in popular_repositories[:3]:
#     print(f"Name: {repo['name']}")
#     print(f"Description: {repo['description']}")
#     print(f"Stars: {repo['stargazers_count']}")
#     print(f"Forks: {repo['forks_count']}") # Adding the number of forks
#     print(f"Created at: {repo['created_at']}") # Adding the creation date
#     print("***********************************************************************************")


import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": '"real python"'},
    headers={"Accept": "application/vnd.github.text-match+json"},
)
# View the new `text-matches` list which provides information
# about your search term within the results
json_response = response.json()
#print(json_response)
first_repository = json_response["items"][0]
print(first_repository["text_matches"][0]["matches"])
