from pexpect import pxssh
#import getpass
import sys,os
global CMD,ssh_client
#CMD='/home/vpgba/Lohith/ww26/new/otc_gen_graphics-intel-gpu-tools/build/tests/'
def LogIn(host,user,passwd):
        ssh_client = pxssh.pxssh()
        ssh_client.login(host,user,passwd,port=1340) #login credentials
        s.sendline(cmd)	 # run a command
        s.prompt()	 # match the prompt
        print (s.before)	 # print everything before the prompt.
        s.logout()

try:
	s = pxssh.pxssh()
	hostname = '10.223.161.119'
	username = 'vpgba'
	LogIn(hostname,username,'vpgba')
#    password = getpass.getpass('password: ')
#        sel=sys.argv[1]
#        test=sys.argv[2]
#        if sel=='L':
#                LogIn(hostname,username,'vpgba','ls /home/vpgba/Lohith')#(CMD+test+' --l'))
#        elif sel=='F':
#                LogIn(hostname,username,'vpgba',(CMD+test#))
#	elif sel=='FS':
#		fil=open("subtest.txt",'w')
#		x=LogIn(hostname,username,'vpgba'(CMD+test+' --l '))
#		fil.write(x)
#		for i in fil.readlines():
#			i=i.replace("\n","")
#			LogIn((hostname,username,'vpgba'(CMD+test+' --r '+i)))
#		fil.close()
 #       elif sel=='S':
 #               LogIn(hostname,username,'vpgba',(CMD+test+' --r '+sys.argv[3]));
#
except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)
finally:
	print("Test Completed")
