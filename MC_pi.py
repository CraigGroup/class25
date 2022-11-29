#----------------------------------------------------------------------------
#    PROGRAM NAME:  MC_pi.py
#    PURPOSE:       Playing with random numbers.  
#    CREATED:       Craig Group  2022
#
#    Class 25
#    UVA Honor Pledge
#   
#    To run me:  python MC_pi.py  100000 1 
#    To run me:  python MC_pi.py  N_loop seed 
#____________________________________________________________________________

#------------------------------------------------
#                  IMPORTS
#------------------------------------------------
import sys
import random
from datetime import datetime
import time
import math


#------------------------------------------------
#               GLOBAL CONSTANTS
#------------------------------------------------



PROGRAM_NAME=sys.argv[0]
START = time.time()

YMIN=-1
YMAX=1
XMIN=-1
XMAX=1

n_int=0
seed=1

#Input validation
if (len(sys.argv)==3):

   print(f"\n-->User input: N:{sys.argv[1]} seed:{sys.argv[2]}\n")
   try:
       n_int=int(sys.argv[1])
       seed=int(sys.argv[2])
   except:
       print("ALERT: Prameters should be integers!\n")
       n_int=0  #This makes sure the program won't try to run

else:
   print("ALERT:  Please re-run the program with 2 parameters: N and seed.\n")
   
#------------------------------------------------
#               METHODS
#------------------------------------------------
#None

def in_fnc(x,y):
    if (math.sqrt(x*x+y*y)<1):
        return 1
    else:
        return 0


#------------------------------------------------
#                   MAIN FUNCTION
#------------------------------------------------
def main(n_int,seed):


   n_in=0
   for i in range(0,int(n_int)):
        x=random.uniform(XMIN,XMAX)
        y=random.uniform(YMIN,YMAX)
        #print(x,"  ",y)
        if in_fnc(x,y):
            n_in+=1
    
   area=(XMAX-XMIN)*(YMAX-YMIN)*n_in/float(n_int)
   print(area)
   print(f"\n\npi={area:15.14f} with n_int={n_int} \n ")



#Only run the main function is n_int is not zero
if n_int:
    START = time.time()
    random.seed(int(seed))
    print("-->You are running the program: "+PROGRAM_NAME+"\n\n")
    #print(PROGRAM_NAME)       
    main(int(n_int),seed)
    #print info about how long it takes...  
    print(f"  --- {(time.time() - START):6.2f} seconds ---" )

