__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

def clean_cache():
    path_files = "C:\\Users\\Laura\\Documents\\Winc\\Assignments\\files"
    dir_cache = "cache"
    path_cache = os.path.join(path_files, dir_cache)
    if os.path.exists(path_cache) == False:
        os.mkdir(path_cache)
    elif os.path.exists(path_cache) == True:
        if len(os.listdir(path_cache)) != 0:
            for i in os.listdir(path_cache):
                os.remove(os.path.join(path_cache,i))

def cache_zip(zip_file_name, cache_dir_name):
    path_files = "C:\\Users\\Laura\\Documents\\Winc\\Assignments\\files"
    dir_cache = cache_dir_name
    path_cache = os.path.join(path_files, dir_cache)
    clean_cache()
    shutil.unpack_archive(zip_file_name, path_cache)

def cached_files():
    path_files = "C:\\Users\\Laura\\Documents\\Winc\\Assignments\\files"
    dir_cache = "cache"
    path_cache = os.path.join(path_files, dir_cache)
    file_list = []
    file_list2 = []
    for f in os.listdir(path_cache):
        file_list.append(f"{path_cache}\{f}")
    for f in file_list:
        if os.path.isfile(f) == True:
            file_list2.append(f)
    return file_list2

def find_password(list_with_files):
    password_list = []
    for f in list_with_files:
        with open(f, "r") as file:
            if 'password' in file.read():
                password_list.append(f)
    with open(password_list[0],"r") as file:
        for f, x in enumerate(file):
            if 'password' in x:
                return x[x.find(" ")+1:x.find("\n")]
