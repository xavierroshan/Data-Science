# import collections
# from typing import List
# lst1: List[int]= [1, 2, 3, 4, 5]
# dq = collections.deque(lst1)
# dq.append(100)
# dq.appendleft(200)
# print(list(dq))
# dq.pop()
# dq.popleft()
# print(list(dq))
# letter_count=collections.Counter("My name is roshan xavier")
# print(dict(letter_count))
# data: List[str] = ["red", "blue", "red", "green", "blue", "blue"]
# item_count = dict(collections.Counter(data))
# print(item_count)

# import uuid

# uuid_1 = uuid.uuid1()
# print(uuid_1)
# uuid_4 = uuid.uuid4()
# print(uuid_4)
# uuid_3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
# print(uuid_3)
# uuid_5 = uuid.uuid5(uuid.NAMESPACE_URL, 'https://timesofindia.indiatimes.com/us')
# print(uuid_5 )


# import uuid

# def create_session() -> str:
#     session_id = uuid.uuid1()
#     return session_id

# session_id = create_session()
# print(session_id)


# import uuid

# def create_product(name: str) -> str:
#     product_id = uuid.uuid3(uuid.NAMESPACE_OID, name)
#     return product_id


# product_id = create_product("Apple")
# print(product_id)
# print(product_id)


# import uuid


# def create_filenames(ext : str)->str:
#     unique_id = uuid.uuid4()
#     filename = f"{unique_id}.{ext}"
#     return filename

# filename = create_filenames("txt")
# print(filename)


#https://refactoring.guru/design-patterns/python

#Absract factory pattern
