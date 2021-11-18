#!/usr/bin/python3
print(*("{} = {:#x}".format(i, i) for i in range(99)), sep='\n')
