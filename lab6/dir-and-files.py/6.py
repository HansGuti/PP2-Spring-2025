import os

def task6(path):
    for i in range(26):
        filename = f"{chr(ord('A') + i)}.txt"  
        file_path = os.path.join(path, filename) 
        f = open(file_path, "w+")  


for_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6\checker\for_dir_6'
task6(for_path)
