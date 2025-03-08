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


path_lab6 = r'C:\Users\HUAWEI\Desktop\PP2\lab_6'
print('Directories:', task1(path_lab6, only_directories=True))
print('Files:', task1(path_lab6, only_files=True))
print('Following items:', task1(path_lab6))


def task2(path):
    res = {
        'existence' : False,
        'readability' : False,
        'writability' : False,
        'executability' : False
    }

    res['existence'] = os.access(path, os.F_OK)
    if not res['existence']:
        return res
    res['readability'] = os.access(path, os.R_OK)
    res['writability'] = os.access(path, os.W_OK)
    res['executability'] = os.access(path, os.X_OK)

    return res


user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6'
print(task2(user_path))

import os

def task3(path):
    if not os.path.exists(path):
        return {  
            'existence': False,
            'filename': '',
            'dirname': ''
        }

    res = {
        'existence': True,
        'filename': '',
        'dirname': ''
    }

    if os.path.isfile(path):  
        res['filename'] = os.path.basename(path)
        res['dirname'] = os.path.dirname(path)
    else:  
        res['dirname'] = os.path.abspath(path)

    return res

    

user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order'
print(task3(user_path))

def task4(path):
    f = open(path, 'r')
    lines = 0
    for _ in f:
        lines += 1

    return lines

path_for_lab6 = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order\sample4.txt'
print(task4(path_for_lab6))

def task5(path, a):
    f = open(path, 'w')
    for i, el in enumerate(a):
        f.write(str(el))
        if i + 1 != len(a):
            f.write('\n')


user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order\sample5.txt'
print(task5(user_path, [1, 2, 3, 4, 'A', 'B']))

def task6(path):
    for i in range(26):
        filename = f"{chr(ord('A') + i)}.txt"  
        file_path = os.path.join(path, filename) 
        f = open(file_path, "w+")  


for_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order\for_dir_6'
task6(for_path)

def task7(path_from, path_to):
    stat_from = task3(path_from)
    stat_to = task3(path_to)

    if not stat_from["filename"]:
        raise "Specified source path is not a file"
    filename = stat_from["filename"]

    if not stat_to["dirname"]:
        raise "Specified destination path does not exists"

    file_from = open(path_from, "r")
    file_new = open(os.path.join(path_to, filename), "w+")

    for line in file_from:
        file_new.write(line)

this_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\\dir-and-files.py'
another_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order'
task7(this_path, another_path)


def task8(path):
    stat = task3(path)
    if not stat["dirname"]:
        return

    if stat["filename"]:
        os.remove(path)
    else:
        os.rmdir(path)


file_to_path = r'C:\Users\HUAWEI\Desktop\PP2\lab_6\order\for_dir_6\B.txt'
task8(file_to_path)