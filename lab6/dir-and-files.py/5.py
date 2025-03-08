def task5(path, a):
    f = open(path, 'w')
    for i, el in enumerate(a):
        f.write(str(el))
        if i + 1 != len(a):
            f.write('\n')


user_path = r'C:\Users\HUAWEI\Desktop\PP2\lab6\checker\sample5.txt'
print(task5(user_path, [1, 2, 3, 4, 'A', 'B']))
