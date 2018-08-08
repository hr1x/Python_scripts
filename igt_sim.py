#!/usr/bin/python3
from pexpect import pxssh
import sys,os
ssh_client=''
hostname= '10.223.161.28'       # host IP Address
username = 'vpgba'              # User name
passwd = 'vpgba'                # passsword
port = 1340                     # port Address
IGT_Path = 'sudo /home/vpgba/otc_gen_graphics-intel-gpu-tools_ww20/build/tests/'
class LogSession():
        def IGT_EXE_GRID(self):
                print("IGT executed")
                return IGT_Path+'testdisplay'
        def IFT_EXE_GRID(self):
                print("IFT executed")
                return 'sudo cat /sys/kernel/debug/dri/0/i915_display_info'
        def CMD(self):
                print("CMD executed")
                return 'ls'
        def LOGIN(self,host,user,pswd,prt):
                global ssh_client
                ssh_client = pxssh.pxssh()
                ssh_client.force_password = True
                ssh_client.login(host,user,passwd,port = prt) #login credentials
        def send_cmd(self,cmd):
                ssh_client.sendline(cmd)         # run a command
                ssh_client.prompt()      # match the prompt
                print((ssh_client.before).decode('utf-8'))#print (ssh_client.after)        # print everything before the prompt.
        def LOGOUT(self):
                ssh_client.logout()

if __name__ == "__main__":
        log=LogSession()        # Declaration of LogSession class in main program
        try:
                value=sys.argv[1].upper()
                print(str(hostname)+' *** '+username+' *** '+passwd+' *** '+str(port))
                log.LOGIN(hostname,username,passwd,port)
                if (value=='-CMD'):
                        log.send_cmd(log.CMD())
                elif (value=='-IGT'):
                        log.send_cmd(log.IGT_EXE_GRID())
                elif (value=='-IFT'):
                       log.send_cmd(log.IFT_EXE_GRID())
                else:
                        raise ValueError('\n 1. python3 simple.py -cmd --> for manual command \n 2. python3 simple.py -igt --> for IGT execution \n 3. python3 simple.py -ift --> for IFT execution')
                log.LOGOUT()
        except pxssh.ExceptionPxssh as e:
                print("pxssh failed on login.")
                print(e)
        finally:
                print("Session Logged out")
