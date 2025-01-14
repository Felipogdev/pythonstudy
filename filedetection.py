import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location of {file_path} exists")
else:
    print(f"It dosen't exists")
