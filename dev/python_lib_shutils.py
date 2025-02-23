import shutil

# #copy file
# src = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder1\inner\file.txt"
# dst = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder3" 
# shutil.copy(src,dst)
# shutil.copy(r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder1\inner\file.txt", r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder3" )

# #copy folder
# src = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder1"
# dst = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder3"
# shutil.copytree(src, dst)

# #move file
# src = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder1\file.txt"
# dst = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder3\inner"
# shutil.move(src,dst)

# #remove a folder
# src = r"C:\Users\xavie\OneDrive\Documents\PythonProjrct\folder3\inner"
# shutil.rmtree(src)

# #check the disk usage
# usage = shutil.disk_usage('/')
# print(f"Total Space = {usage.total}: used = {usage.used}: free = {usage.free} ")


# #return list of supported archive format
# supported_list = shutil.get_archive_formats()
# print(supported_list)
# j=0
# for i in supported_list:
#     print ({i[0]}, {i[1]})