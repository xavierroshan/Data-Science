# import json

# complex_dict = '''
# {
#     "name": "Alice",
#     "age": 30,
#     "is_student": false,
#     "address": {
#         "street": "123 Wonderland Ave",
#         "city": "Dreamville",
#         "postal_code": "12345",
#         "country": {
#             "name": "Imaginationland",
#             "continent": "Fantasy",
#             "languages": ["English", "Imaginary"]
#         }
#     },
#     "courses": [
#         {
#             "course_name": "Python Programming",
#             "course_code": "CS101",
#             "credits": 3,
#             "instructors": [
#                 {"name": "Dr. John Doe", "role": "Lead Instructor", "office": "Room 101"},
#                 {"name": "Prof. Jane Smith", "role": "Teaching Assistant", "office": "Room 102"}
#             ]
#         },
#         {
#             "course_name": "Data Science",
#             "course_code": "DS201",
#             "credits": 4,
#             "instructors": [
#                 {"name": "Dr. Emily Clark", "role": "Lead Instructor", "office": "Room 203"},
#                 {"name": "Prof. Michael Lee", "role": "Teaching Assistant", "office": "Room 204"}
#             ]
#         }
#     ],
#     "friends": [
#         {"name": "Bob", "age": 32, "location": "Fantasyland"},
#         {"name": "Charlie", "age": 28, "location": "Imaginary Village"}
#     ],
#     "preferences": {
#         "food": ["Pizza", "Sushi", "Ice Cream"],
#         "hobbies": {"reading": true, "coding": true, "traveling": false},
#         "favorite_color": "blue",
#         "pet": {
#             "type": "cat",
#             "name": "Whiskers",
#             "age": 5
#         }
#     },
#     "active_projects": [
#         {"name": "AI Chatbot", "status": "In Progress", "team_size": 3},
#         {"name": "Website Redesign", "status": "Completed", "team_size": 5}
#     ]
# }
# '''

# # Printing the dictionary
# parsed_dict = json.loads(complex_dict)
# print(f"data type is {type(parsed_dict)}")
# print(parsed_dict)
# pretty_json = json.dumps(parsed_dict, indent=4)
# print(f"data type is {type(pretty_json)}")
# print(pretty_json)


#json.loads: convert json string to a dict
#json.load: read json from file
#json.dump: load json string or dict to file.json and check the file content
#json.dumps: make json pretty



import json

##json.loads: convert json string to a dict
# str1 = '''{"name": "Alice", "age": 25, "city": "Wonderland"}'''
# dict1 = json.loads(str1)
# print(dict1)

##json.load: read json from file
# with open("file.json", 'r') as f:
#     data = json.load(f)
# print(data)

# #json.dump: load json string or dict to file.json and check the file content
# #str1 = '''{"name": "Alice", "age": 25, "city": "Wonderland"}'''
# str1 = {"name": "Alice", "age": 25, "city": "Wonderland"}
# with open ("file1.json", 'w') as f:
#     json.dump(str1,f)
# with open ("file1.json", 'r') as f:
#     data = json.load(f)
# print(data)

# #json.dumps: make json pretty
# data = {"name": "Alice", "age": 25, "city": "Wonderland"}
# pretty_json = json.dumps(data, indent=4)
# print(pretty_json)

## appending this line as reference for linux learning
## appending this line as reference for linux learning
## appending this line as reference for linux learning
