# import tempfile
# import os

# with tempfile.TemporaryFile(mode = 'w+t') as file:
#     file.write("This is a temperory file")
#     file.seek(0)
#     data = file.read()
#     print(data)
# file_list = os.listdir()
# for file in file_list:
#     print(file)


# import tempfile

# with tempfile.NamedTemporaryFile(mode = 'w+t', delete=False) as file:
#     print(f"Temporary file is created with{file.name}")
#     file.write("This is a temporary file")
#     file.seek(0)
#     data = file.read()
    # print(data)


# import tempfile

# # get the location of tempfile
# temp_dir = tempfile.gettempdir()
# print(temp_dir)


# import tempfile
# # create a temp directory
# temp_dir = tempfile.mkdtemp()
# print(temp_dir)

# import tempfile
# temp_prefix = tempfile.gettempprefix()
# print(temp_prefix)


# import tempfile
# import os

# temp_dir = tempfile.mkdtemp()
# print(temp_dir)
# temp_file_path = os.path.join(temp_dir, "file.txt")
# print(temp_file_path)
# with open(temp_file_path, 'w') as temp_file:
#     temp_file.write("Some content in the temporary directory.")
# print(f"temp file created at {temp_file_path}")

