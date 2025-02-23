import base64

print("**************************************************")
original_str = "Hello World"
print("**************************************************")

print(f"first encode the string to byte using utf-8 scheme")
utf_encoded_original_str = original_str.encode('utf-8')
print(f"utf encoded byte")
print(utf_encoded_original_str)
print("**************************************************")


print(f"then encode the bytes using base 64")
b64_encoded_byte = base64.b64encode(utf_encoded_original_str)
print(f"base64 encode bytes")
print(b64_encoded_byte)
print("**************************************************")


print(f"decoding the base64 byte to string")
decoded_str = b64_encoded_byte.decode('utf-8')
print(f"printing the decoded string")
print(decoded_str)
print("**************************************************")

print(f"decoding the base64 string")
base64_decoded_str = base64.b64decode(decoded_str)
print(base64_decoded_str)
print("**************************************************")

print(f"decoding to original string")
original_str_v2 = base64_decoded_str.decode('utf-8')
print(original_str_v2)
print("**************************************************")


