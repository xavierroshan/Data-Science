import base64


# Encoding and decoding with UTF-8
original_string = "Hello, 世界"
encoded_string_with_UTF = original_string.encode("UTF-16")
print(f"printing the encoded string {encoded_string_with_UTF}")
decoded_byte_with_UTF = encoded_string_with_UTF.decode("UTF-16")
print(f"printing the decoded byte {decoded_byte_with_UTF}")


encoded_byte_with_base64 = base64.b64encode(encoded_string_with_UTF)
print(encoded_byte_with_base64)
decoded_byte_with_base64 = base64.b64decode(encoded_byte_with_base64)
print(decoded_byte_with_base64)

#Base64 cannot directly encode and decode strings like UTF encoding (UTF-8, UTF-16, etc.). 
#Instead, Base64 only works with byte data. However, you can first convert a string to bytes (using UTF encoding) before applying Base64, 
#and then reverse the process to decode.

# Use Base64 when:
#     You need to store or transmit binary data (e.g., images, videos, files) as text.
#     You want to embed binary data into text-based formats like JSON, XML, or email.
#     You need to send data through text-based protocols (like email, HTTP, or databases that only support text).

# Use UTF encodings when:
#     You are storing, processing, or transmitting text data.
#     You want to support multilingual text (Unicode characters).
#     You need to preserve the meaning of characters (not just convert to ASCII).