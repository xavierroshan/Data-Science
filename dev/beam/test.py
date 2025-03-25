import base64


# Encoding and decoding with UTF-8
original_string = "Hello, 世界"
encoded_string_with_UTF = original_string.encode("UTF-16")
print(encoded_string_with_UTF)
decoded_byte_with_UTF = encoded_string_with_UTF.decode("UTF-16")
print(decoded_byte_with_UTF )


encoded_byte_with_base64 = base64.b64encode(original_string)
# print(decoded_byte_with_base64)