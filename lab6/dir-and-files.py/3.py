import os

def task3(path):
    res = {
        'existence' : os.path.exists(path),
        'filename' : '',
        'dirname' : ''
    }
 
    if not res['existence']:
        return res
    
    if not os.path.isfile(path):
        res['dirname'] = os.path.dirname(os.path.abspath(path))
        res['filename'] = os.path.basename(os.path.abspath(path))

        return res
    

user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6\dir-and-files'
print(task3(user_path))