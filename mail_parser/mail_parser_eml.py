import email
import mimetypes
import colors
from email.parser import Parser
from numpy import asarray
from time import sleep

fileRead=open('./sencillo.msg', 'r')
msg_headers = Parser().parse(fileRead)
fileRead.close()

print(type(msg_headers))
print(len(msg_headers))
print(colors.bcolors.VIOLET + str(msg_headers) + colors.bcolors.ENDC)

print(colors.bcolors.FAIL_RED)
print(list(msg_headers.values()))
print(colors.bcolors.OKBLUE)
print(list(msg_headers.keys()))
print(colors.bcolors.ENDC)

headers_keys = list(msg_headers.keys())
headers_values = list(msg_headers.values())

for i in range(len(headers_keys)):
     print(msg_headers[i])
