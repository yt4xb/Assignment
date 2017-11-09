import numpy as np
import time


#Assume large files are over 200 GB
#------------------Class Definitions------------------------#
with open("trunc5M.txt") as text_file:
    lines=text_file.read().split()
    pareto=[float(i) for i in lines]

class File():
    def __init__(self, fsize, at, interval, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.timeInterval = interval
        self.serviceTime = fsize / 1.25
        self.waitingTime = 0
        self.departureTime = 0

    def __str__(self):
        return str(self.__dict__)


class Interface():
    def __init__(self, interface_id):
        self.id = interface_id
        self.busy = False
        self.fileID = None

    def __str__(self):
        return str(self.__dict__)

    def isBusy(self):
        return self.busy

    def addFile(self, fid):
        self.fileID = fid
        self.busy = True

    def clear(self):
        self.fileID = None
        self.busy = False

#--------------Global Variables/params------------------#
t = 0
fileID = 0
thresh_count = 0
large_time = 300
interface1=Interface(1)
interface2=Interface(2)
interface_list=[interface1,interface2]

def generate_file():
    global t,fileID
    t_int = np.random.exponential(1)
    f_pareto = pareto[fileID]
    t=t+t_int
    new_file=File(f_pareto,t,t_int,fileID)
    fileID=fileID+1
    print(new_file)
    return new_file

def check_interface():
    for interface in interface_list:
        if not interface.busy:
            return interface.id
    return 0

if __name__ == '__main__':
    global large_thresh, thresh_count, interface_list
    st_time = time.time()
    queue=[]
    file_list = []
    comp_file_list = []
    #global thres_count, t, fileID
    while pareto[fileID] :
        #1. Generate new file
        new_file = generate_file()
        file_list.append(new_file)
        queue.append(new_file)
        #2. Remove any completed files from interfaces
        for interface in interface_list:
            if interface.fileID is not None:
                #if file has been processed by now, remove it
                cur_file = file_list[interface.fileID]
                if cur_file.departureTime <= t:
                    comp_file_list.append(file_list[interface.fileID])
                    #if file_list[interface.fileID].fileSize > large_thresh:
                    #   thresh_count +=1
                    if (cur_file.departureTime - cur_file.arrivalTime) > large_time
                        thresh_count +=1
                    interface.clear()
        #3. check if interfaces are available. If so, pop from queue and add to interface
        interfaceState = check_interface()
        print "interface_stte: " + str(interfaceState)
        if interfaceState == 1 :
            #update departure time and add file to interface
            serving_file = queue.pop(0)
            serving_file.departureTime = t +  serving_file.serviceTime
            interface_list[interfaceState-1].addFile(serving_file.id)
        elif interfaceState == 2:
            serving_file=queue.pop(0)
            serving_file.departureTime = t +  serving_file.serviceTime
            try:
                interface_list[interfaceState-1].addFile(serving_file.id)
            except:
                print "error. queue-len: " + str(len(queue)) + ", int_state: " + str(interfaceState)
        #4. Update waiting times of files in queue
        for f in queue: f.waitingTime += new_file.timeInterval
    duration = time.time() - st_time
    print "duration: " + str(duration)
    print "total files: " + str(fileID)
        
        
        



