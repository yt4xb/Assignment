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
    print(new_file)
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
    for fileID in 100
		#1. Generate new file
        new_file = generate_file()
        file_list.append(new_file)
        queue.append(new_file)
	
        



