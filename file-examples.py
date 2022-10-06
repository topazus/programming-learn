import os
import pathlib

# check if a file is existed
is_existed = os.path.exists("/home/ruby/.bashrc")
print(is_existed)
is_existed = os.path.isfile("/home/ruby/.bashrc")
print(is_existed)
is_existed = pathlib.Path("/home/ruby/.bashrc").exists()
print(is_existed)
