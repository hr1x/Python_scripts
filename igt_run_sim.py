import sys
import os,subprocess
from subprocess import PIPE,Popen
import datetime
import time
class IgtFun:
        global CMD_PREFIX,IGT_DIR
        IGT_DIR='"echo vpgba | sudo -S /home/vpgba/Lohith/ww26/new/otc_gen_graphics-intel-gpu-tools/build/'
        CMD_PREFIX='sshpass -p "vpgba" ssh -p 1340 vpgba@localhost '
        def Modprobe(self):
                os.system('sshpass -p "vpgba" ssh -p 1340 vpgba@localhost "echo vpgba | sudo -S /home/vpgba/modprobe.sh"')
        def ListSubTest(self,ts,s):
                cmd=CMD_PREFIX + IGT_DIR +('tests/%s --l"'%ts)                
                x=os.popen("%(cmd)s" % locals())
                if s == "-FS":
                        l=open("subtest.txt",'w')
                        l.write("%s" %(x.read()))
                        l.close()
                elif s == "-L":
                        print("\n%s" %(x.read()))
        def FullTest(self,test):
                os.system('mkdir -p test_temp')
                cmd=CMD_PREFIX + IGT_DIR + ("tests/%s\""%test)
                print (cmd)
                start=datetime.datetime.now()
                process=Popen(cmd, stdout=PIPE, stderr=PIPE,shell=True)
                stdout, stderr =process.communicate()
                out=(stdout.decode('ascii'))
                err=(stderr.decode('ascii'))               
                n=open(("test_temp/%s.txt"%test),'w')
                n.write("\n%s \n%s"%(out,err))
                n.close()
                exec_time=datetime.datetime.now()-start
                print ("test : %s e_time : %s" %(test,exec_time))
                log=open("time.log",'a')
                log.write("\n%s e_time: %s \n" % (test,exec_time))
                log.close()
        def SubTest(self,test,subtest,s):
                os.system('mkdir -p test_temp')
                cmd=CMD_PREFIX + IGT_DIR +("tests/%s"%test)+ ' --r '+("%s\"" %subtest)                       
                start=datetime.datetime.now()           
                process=Popen(cmd, stdout=PIPE, stderr=PIPE,shell=True)
                stdout, stderr =process.communicate()
                out=(stdout.decode('ascii'))
                err=(stderr.decode('ascii'))
                if s == "-S":
                        n=open(("test_temp/%s.txt"%subtest),'w')
                elif s == "-FS":
                        n=open(("test_temp/%s_FS.txt"%test),'a')
                n.write("\n%s \n%s" %(out,err))
                n.close()
                exec_time=datetime.datetime.now()-start
                if s == "-S":
                        ex=('grep \"Subtest %s:\" test_temp/%s.txt'%(subtest,subtest))
                elif s == "-FS":
                        ex=('grep \"Subtest %s:\" test_temp/%s_FS.txt'%(subtest,test))
                y=os.popen("%(ex)s"%locals())
                y1=str(y.read())
		y1=y1.replace("\n","")
                print ("\ntest : %s %s time:%s\n" %(test,y1,exec_time))
                lg=open("time_s.log",'a')
                lg.write("\n%s time : %s"%(subtest,exec_time))
                lg.close()
                log=open("time.log",'a')
		log.write("\nSubtest: %s time: %s "%(y1,exec_time))
                log.close()
                return (exec_time)
        def Time_Space(self,t):
                ts=open("time.log",'a')
                ts.write("\n%s\n"%t)
                ts.close()
                lg=open("time_s.log",'a')
                lg.write("\n%s\n"%t)
                lg.close()
                

if __name__ == "__main__":
        f=IgtFun()
        global cmd_ts        
        try:
                n=sys.argv[1].upper()
                if n == "-H":
                        print('''1. igt_run_sim.py -s <test_name> <subtest> --> to execute single subtest \n
2. igt_run_sim.py -l <testname> --> to print subtests on console \n 
3. igt_run_sim.py -fs <testname> --> to execute all subtest in the test and capture log for each subtest \n
4. igt_run_sim.py -f <testname> --> to execute whole test and cature all log in single file \n ''')
                elif n == "-S":
                        f.Modprobe()
                        f.SubTest(sys.argv[2],sys.argv[3],n)
                elif n == "-L":
                        f.ListSubTest(sys.argv[2],n)
                elif n == "-FS":
                        f.Modprobe()
                        f.ListSubTest(sys.argv[2],n)                        
                        z=open("subtest.txt",'r')
                        x1=z.readlines()
                        cmd_ts='-'*40 + '\n' + ' '*10 +('test : %s'%sys.argv[2]) + ' '*10 + '\n' + '-'*40
                        f.Time_Space(cmd_ts)
                        total_time=datetime.timedelta(seconds=0)
                        for i in x1:
				i=i.replace("\n","")
                                x = (f.SubTest(sys.argv[2],i,n))
                                print(x)
                                total_time=total_time + x
                        print(("Total Execution Time for %s : %s"%(sys.argv[2],total_time)))
                        f.Time_Space('-'*40 + '\n'+("Total Execution Time for %s : %s"%(sys.argv[2],total_time))+ '\n'+ '-'*40)
                        z.close()
                elif n == "-F":
                        f.Modprobe()
                        f.FullTest(sys.argv[2])
                else:
                        print('*'*30 + "\n\n igt_run_sim.py -h  --> for help \n\n" + '*'*30)
        except NameError as name:
                print('*'*30 + "\n\n igt_run_sim.py -h  --> for help \n\n" + '*'*30 ,name)
        finally:
                print("test completed")
