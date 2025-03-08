def task4(path):
    f = open(path, 'r')
    lines = 0
    for _ in f:
        lines += 1

    return lines

path_for_lab6 = r'C:\Users\HUAWEI\Desktop\PP2\lab6\checker\sample4.txt'
print(task4(path_for_lab6))