import os

def task3(path):
    res = {
        'existence' : os.path.exists(path),
        'filename' : '',
        'dirname' : ''
    }
 
    if not res['existence']:
        return res
    
    if os.path.isfile(path):
        res['dirname'] = os.path.dirname(os.path.abspath(path))
        res['filename'] = os.path.basename(os.path.abspath(path))

        return res
    

user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6\dir-and-files'
print(task3(user_path))



def task7(path_from, path_to):
    start_from = task3(path_from)
    start_to = task3(path_to)

    if not start_from['filename']:
        raise 'Specified source path is not a file'
    filename = start_from['filename']

    if not start_to['dirname']:
        raise 'Specified destination path does not exists'
    
    file_from = open(path_from, 'r')
    file_new = open(os.path.join(path_to, filename), 'w+')

    for line in file_from:
        file_new.write(line)


this_path =  r'C:\Users\HUAWEI\Desktop\PP2\lab6\dir-and-files'
another_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6\checker'
task7(this_path, another_path)