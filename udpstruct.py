# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import socket
import sys
import struct
from ctypes import*
 
class Payload(Structure):
    _fields_ = [("integer", c_uint32),
                ("charecter", c_wchar)]
    
Payload_out=Payload(1,'c');


serverAddressPort   = ("127.0.0.1",1774)

# Create a UDP socket at client side

sock= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket
sock.sendto(Payload_out, serverAddressPort)
print("Data sent successfully")
 

buff = sock.recvfrom(sizeof(Payload))
payload_in=Payload.from_buffer_copy(buff[0])

print("int:{} char:{}".format(payload_in.integer,payload_in.charecter))

sock.close()