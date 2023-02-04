from functools import reduce
from operator import add

# 1:
f = open("names.txt", "rt")
print(reduce(lambda s1, s2: s1 if len(s1) > len(s2) else s2, [x[:-1] for x in f]))
f.close()

# 2:
f = open("names.txt", "rt")
print(reduce(add, [len(x[:-1]) for x in f]))
f.close()

# 3:
f = open("names.txt", "rt")
names_list = [name for name in f]
# with reduce(): min_len = len(reduce(lambda s1, s2: s1 if len(s1) < len(s2) else s2, names_list))
min_len = len(min(names_list, key=len))
print(reduce(add, [name for name in names_list if len(name) == min_len]))
f.close()

# 4:
f1 = open("names.txt", "rt")
f2 = open("lengths.txt", "w")
for name in f1:
    f2.write(str(len(name[:-1])) + "\n")
f1.close()
f2.close()

# 5:
f = open("names.txt", "rt")
inp = input("Write a length: ")
print(reduce(add, [name for name in f if len(name) - 1 == int(inp)], ""))
f.close()
