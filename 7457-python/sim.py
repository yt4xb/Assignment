import numpy as np
import time


#Assume large files are over 200 GB
#------------------Class Definitions------------------------#
with open("trunc10M.txt") as text_file:
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
large_thresh = 200
large_time = 300 # 5min
arrival_rate = 1.11

interface1=Interface(1)
interface2=Interface(2)
interface_list=[interface1,interface2]

def generate_file():
    global t,fileID, arrival_rate
    t_int = np.random.exponential(arrival_rate)
    f_pareto = pareto[fileID]
    t=t+t_int
    new_file=File(f_pareto,t,t_int,fileID)
    fileID=fileID+1
    #print(new_file)
    return new_file

def check_interface():
    freeInterfaceID=[]
    for interface in interface_list:
        if not interface.busy:
            #print "Interface %d is not busy" %interface.id
            freeInterfaceID.append(interface.id)
        #return freeInterfaceID
    #print "Both interfaces are busy"
    return freeInterfaceID

if __name__ == '__blah__':
    global large_thresh, thresh_count, interface_list
    st_time = time.time()
    queue=[]
    file_list = []
    comp_file_list = []
    #global thres_count, t, fileID
    while thresh_count < 100 :
        #1. Generate new file
        new_file = generate_file()
        file_list.append(new_file)
        queue.append(new_file)

        #2. Remove any completed files from interfaces before current time t
        for interface in interface_list:
            # if the interface is empty, interfaceId will be none
            # if the interface is busy
            #print "In Interface %d"%interface.id
            
            if interface.fileID is not None:
                #print "interface is busy processing file %d" % interface.fileID
                #print "current time%f"%t
                #print "departure time%f"%file_list[interface.fileID].departureTime  
                #if file has been processed by now, remove it
                #cur_file = file_list[interface.fileID]
                while file_list[interface.fileID].departureTime <= t:
                    comp_file_list.append(file_list[interface.fileID])
                    #print "File complete:"
                    #print file_list[interface.fileID]
                    if file_list[interface.fileID].departureTime - file_list[interface.fileID].arrivalTime > large_time:
                        thresh_count +=1
                        print file_list[interface.fileID]
                        print "Thresh count is:%d" %thresh_count
                    finishedID = interface.fileID
                    interface.clear()
                    #if there are files in the waiting list
                    if not len(queue) == 0:
                        serving_file = queue.pop(0)
                        serving_file.departureTime = file_list[finishedID].departureTime + serving_file.serviceTime
                        try:
                            interface.addFile(serving_file.id)
                        except:
                            print "error. queue-len: " + str(len(queue)) + ", int_state: " + str(interfaceState)
                    else: 
                        break


        #3. check if interfaces are available. If so, pop from queue and add to interface
        interfaceState = check_interface()
        #print "interface_state: " + str(interfaceState)

        for interfaceID in interfaceState:
            #print "Queue size %d" %len(queue)
            if not len(queue) == 0:
                serving_file = queue.pop(0)
                #print "Poping file %d"%serving_file.id
                serving_file.departureTime = t+serving_file.serviceTime
                file_list[serving_file.id].departureTime = serving_file.departureTime 
                try:
                    interface_list[interfaceID-1].addFile(serving_file.id)
                except:
                    print "error. queue-len: " + str(len(queue)) + ", int_state: " + str(interfaceID)

        #4. Update waiting times of files in queue
        for f in queue: f.waitingTime += new_file.timeInterval
    duration = time.time() - st_time
    print "duration: " + str(duration)
    print "total files: " + str(fileID)

def exportData():        
    simOut = open('simOutput.csv', 'w')
    simOut.write(','.join(comp_file_list[0].__dict__.keys()) + '\n')
    for fc in comp_file_list:
        fvals = [str(v) for v in fc.__dict__.values()]
        outstr = ','.join(fvals) + '\n'
        simOut.write(outstr)
    simOut.close()
    
        



