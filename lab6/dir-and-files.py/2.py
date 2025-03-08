import os

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


user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6'
print(task2(user_path))