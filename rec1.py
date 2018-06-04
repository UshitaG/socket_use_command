#!/usr/bin/python2
import socket
import os
import commands
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#will atleast run once
k='y'
j=("127.0.0.1",9999)

#to bind the server
s.bind(j)			

#if user wants to enter again
while k[0]=='y':
	a=s.recvfrom(100)
	if a[0]=='1':
		s.sendto('0',a[1])
		s.recvfrom(100)
		x=commands.getoutput('date')
		print x
	if a[0]=='2':
		s.sendto('0',a[1])
		s.recvfrom(100)
		x=commands.getoutput('cal')
		print x
	if a[0]=='3':
		s.sendto('0',a[1])
		s.recvfrom(100)
		os.system('firefox')
	if a[0]=='4':
		s.sendto('1',a[1])
		g=s.recvfrom(100)
		os.mkdir(g[0])
	s.sendto("Do you want to enter again?",a[1])	#ask user if he wants to send again
	k=s.recvfrom(100)
