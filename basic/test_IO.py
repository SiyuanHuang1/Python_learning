# -*- coding: utf-8 -*-
import os

file_path = "test_IO.txt"

"""
读取整个文件或者一行一行地读取文件。下面两种方法均可，但with open更保险
"""

file = open(file_path)
#data = file.read()
#print(data)
for line in file:
    print(line.rstrip())
file.close()

with open(file_path) as file_object:
#    contents = file_object.read()
#    print(contents)
    for line in file_object:
        print(line.rstrip())

"""
需要注意的是，当读取完文件之后，“光标”处在文件的最后，因此不能再读一次，除非重置；
在这种读取文件的语句的外部，文件对象是不存在的，因为文件已经关闭
"""

"""
如何在程序的任意位置调用文件内容：先存到列表里面
"""

file_name = "test_IO.txt"
with open(file_name) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

"""
写入或追加
"""
outfile_name = "test_IO_out.txt"
with open(outfile_name, "w") as file:
#    for line in lines:
#        file.write(line)
    file.writelines(lines)

"""
调用shell命令
"""
os.system('rm -f test_IO_out.txt')