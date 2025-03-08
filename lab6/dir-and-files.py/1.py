import os

def task1(path, only_directories = False, only_files = False):
    if not os.path.exists(path):
        print('The path {path} does not exist.')
        return []


    if(only_directories and only_files) or os.path.isfile(path):
        return []
    
    res = []
    for name in os.listdir(path):
        if not only_directories and os.path.isfile(os.path.join(path, name)):
            res.append(name)
        elif not only_files and os.path.isdir(os.path.join(path, name)):
            res.append(name)

    return res


path_lab6 = r'C:\Users\HUAWEI\Desktop\PP2\lab6'
print('Directories:', task1(path_lab6, only_directories=True))
print('Files:', task1(path_lab6, only_files=True))
print('Following items:', task1(path_lab6))