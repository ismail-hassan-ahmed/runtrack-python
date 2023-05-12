
import re

file = open('domains.xml', 'r')
file2 = open('domains.xml', 'r') 

net = '.net'
com = '.com'
dot_net_number = re.findall(".net",  file.read())
dot_com_number = re.findall(".com",  file2.read())
print('dot_net_number', ':')
print(len(dot_net_number))
print('dot_com_number', ':')
print(len(dot_com_number))
file.close()