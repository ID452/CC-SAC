##This Software is not supossed to made public, any disclosure, in partial or as whole prohipted
##


import socket, random, sys

try:
    import json
except ImportError: # for outdated Python versions before 2.5
	import simplejson as json

xcert_Path = ('/xcert') #path to keys




def get_serv_ID():
	ID_hashkey = ()
	serv_NAME = socket.getservbyname('domain')
	sec_ports_lst = [400, 452, 888, 1234]
	return ID_hashkey

 

max_socket = 65535

qualified_HName= socket.getfqdn()

print (a)
print (b)
