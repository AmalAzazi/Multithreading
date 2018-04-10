import threading 
from queue import Queue
import time
import shutil
thread_lock = threading.Lock ()
def copy_op(file_data):
    with thread_lock:
	print("Starting thread: {}".
	format(threading.
	current_thread().name))
	
mydata= threading.local()
mydata.ip, mydata.op = next(iter(file_date.items()))

shutil.copy(mydata.ip,mydata.op)

    with thread_lock:
    print("Finished thread: {}".format(threading.
	current_thread().name))
	
def process_queue():
    while True:
	   file_data = compress_queue.get()
	   copy_op(file_data)
	   compress_queue.task_done()
	   
compress_queue = Queue()
file_name = [{"test.csv":"test_copied.csv"}, {
"test1.csv":"test1_copied.csv"},{
"test2.csv":"test2_copied.csv"}]

for i in range(2):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()
	
start = time.time()
	
for name in file_name:
    compress_queue.put(name)
	
compress_queue.join()

print ("Execution time: (0:5f)".format(time.time() - start)) 