from scipy.special import *
from math import *
from cmath import *

#FUNCTION THAT PRODUCES J'(m,x)
def J_diff(m,x): #m is the order of the Bessel function.

    #this is like a switch/case statement. 
    if m==0:
        return -1*jv(1,x) #Makes use of the special identity for when m=0
    elif m>=1:
        return 0.5*(jv((m-1),x)-jv((m+1),x))
    else:
        return ((-1)**m)*J_diff(abs(m),x)

#FUNCTION THAT PRODUCES H'(m,x)
def H_diff(m,x):
    #This is like a switch/case statement
    if m==0:
        return -1*hankel1(1,x)
    elif m>=1:
        return 0.5*(hankel1((m-1),x)-hankel1((m+1),x))
    else:
        return ((-1)**m)*H_diff(abs(m),x)

#c_m (E POL)
def c_m(m,mu,k,kp,n,r):

    kr=k
    kpr=kp #kp is the wavevector inside the cylinder
    
    top=(complex(0,1)**m)*((n*jv(m,kr)*J_diff(m,kpr))-(jv(m,kpr)*J_diff(m,kr))) #numerator
    bottom=(jv(m,kpr)*H_diff(m,kr))-(n*hankel1(m,kr)*J_diff(m,kpr)) #denominator
  
    ans=top/bottom

    return ans


#----------------MAIN CODE----------------------

#Defining the permitivity & permeability -----
mu=-1 #this is the non-magnetic case so there is only one mu.
eps=100

n=sqrt(eps*mu) #sqrt(eps*mu) # The refractive index. 
#----

filename='/home/des/Desktop/dsktp/project maps/T2/CS_mun1_eps100_10.txt'
f = open(filename,'w')

for u in range (1,10000):

    u=u*0.001
    k=u #k is the wavevector outside the material
    kp=n*u #kp is the wavevector inside the material

    coefficient_total=0
    for m in range(-5,6):
        coefficient_total=coefficient_total+((abs(c_m(m,mu,k,kp,n,1)))**2)

    scs=(2/k)*coefficient_total

    #writing to a file
    outstr=''.join([str(u),"\t",str(scs),"\n"]) 
    f.write(outstr) #print to a .cvs file
        
#closing the file
f.close()




    
    

