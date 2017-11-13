import numpy as np
import time


#Assume large files are over 200 GB
#------------------Class Definitions------------------------#
with open("trunc.txt") as text_file:
    lines=text_file.read().split()
    pareto=[float(i) for i in lines]

class File():
    def __init__(self, fsize, at, interval, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.timeInterval = interval
        self.serviceTime = fsize / 1.25
        self.departureTime = 0

    def __str__(self):
        return str(self.__dict__)


class Interface():
    def __init__(self, interface_id):
        self.id = interface_id
        self.availableTime = None
        self.fileID = None

    def __str__(self):
        return str(self.__dict__)

#--------------Global Variables/params------------------#
t = 0
fileID = 0
num_symbols = 10
large_time = 300 # 5min
arrival_rate = 2
run_rounds = 1
interface1=Interface(1)
interface2=Interface(2)
#interface_list=[interface1,interface2]
def trunc_pareto():
	u = np.random.uniform(0,1,1)
	temp = (-(u*pow(1000,2)-u*pow(1,2)-pow(1000,2)))/(pow(1000,2)*pow(1,2))
	x = pow(temp,-0.5)
	return x

def generate_file():
	global t,fileID, arrival_rate
	t_int = np.random.exponential(arrival_rate)
    	f_pareto = trunc_pareto()
    	t=t+t_int
    	new_file=File(f_pareto,t,t_int,fileID)
    	fileID=fileID+1
 	print(new_file)
    	return new_file

def check_interface(interface1, interface2):
	if interface1.availableTime < interface2.availableTime:
		return interface1
    	else:
		return interface2

if __name__ == '__main__':
	run_count = 0
	st_time = time.time()
    	queue=[]
    	file_list = []
	callResponseTime = []
    	#global thres_count, t, fileID
    	while run_count < run_rounds:
		for fileID in range(0,num_symbols,1):
			#1. Generate new file
			new_file = generate_file()
			cur_interface = check_interface(interface1, interface2)	
			if new_file.arrivalTime >= cur_interface.availableTime:
				new_file.departureTime = new_file.arrivalTime + new_file.serviceTime
				responseTime = new_file.departureTime - new_file.serviceTime
				print "Rst:"+str(responseTime)
				callResponseTime.append(responseTime)
				cur_interface.availableTime = new_file.departureTime
			else:
				new_file.departureTime = cur_interface.availableTime + new_file.serviceTime
				responseTime = new_file.departureTime - new_file.serviceTime
                                print "Rst:"+str(responseTime)
				callResponseTime.append(responseTime)
				cur_interface.availableTime = new_file.departureTime
			#file_list.append(new_file)
		run_count+=1
	print "Simulation Finished"


