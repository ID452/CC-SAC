##This Software is not supossed to made public, any disclosure, in partial or as whole prohipted
##


import socket, random, sys

try:
    import json
except ImportError: # for outdated Python versions before 2.5
	import simplejson as json

xcert_Path = ('/xcert') #path to keys




def get_NODE_ID():
	ID_Node = ()
	qualified_HName= socket.getfqdn()
	
	
	return ID_Node

print (get_NODE_ID)
