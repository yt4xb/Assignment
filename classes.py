#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:02:18 2017

@author: babraham
"""

class File():
    def __init__(self, fsize, at, fid):
        self.id = fid
        self.fileSize = fsize
        self.arrivalTime = at
        self.serviceTime = at + fsize / 10
        self.waitingTime = 0
        self.departureTime
    def __str__(self):
        return str(self.__dict__)

class Interface():
    def __init__(self, interface_id):
        self.id = interface_id
        self.busy = False
        self.fileID = None
    def __str__(self):
        return self.__dict__
    def isBusy(self):
        return self.busy
    def addFile(self, fid):
        self.fileID = fid
        self.busy = True
    def clear(self):
        self.fileID = None
        self.busy = False
        
import Queue as q 


if fileList[interface1.fileID].depatureTime <= t:
    interface1.clear()
fqueue = list()
int1 = Interface(1)
int2 = Interface(2)

t = 0
num_files = 0
thresh_count = 0

def function():
    global int1, int2, fqueue
    fqueue.append(3)

    
while thresh_count < 100:
    

        
        