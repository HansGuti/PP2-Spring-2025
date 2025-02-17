def even_nums(n):
   for i in range(0, n + 1, 2):
       yield i


n = int(input('Type in a number: '))
res = ', '.join(str(x) for x in even_nums(n))
print(res)
