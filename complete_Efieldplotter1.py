#DIFFERS FROM 4 BY CHANGED COEFFICIENTS - NOW USES THOSE IN IPHONE PHOTO FROM BOARD 26th Oct
#HAS LATEST REC RELS. SO IS DIFFERENT FROM 7 ONLY in terms of COEFFICIENTS

from scipy.special import *
from math import *
from cmath import *
import time

#FUNCTION FOR CONVERTING CARTESIAN TO POLAR
def make_polar(x,y):

    r=abs(sqrt((x**2)+(y**2))) #abs() takes the absolute value

    if r>0:
        if y>=0:
            phi=acos(x/r)
        else:
            phi=(2*pi)-acos(x/r)
        
    else: #at the origin/centre
        r=0
        phi=0
        
    return r,real(phi) 

#FUNCTION THAT PRODUCES J'(m,x)
def J_diff(m,x): #m is the order of the Bessel function.

    #this is like a switch/case statement. 
    if m==0:
        return -1*jn(1,x) #Makes use of the speciaal identity for when m=0
    elif m>=1:
        return 0.5*(jn((m-1),x)-jn((m+1),x))
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
    
    top=(complex(0,1)**m)*((n*jn(m,kr)*J_diff(m,kpr))-(jn(m,kpr)*J_diff(m,kr))) #numerator
    bottom=(jn(m,kpr)*H_diff(m,kr))-(n*hankel1(m,kr)*J_diff(m,kpr)) #denominator
  
    ans=top/bottom

    return ans

#d_m
def d_m(m,mu,k,kp,n,r):

    kr=k
    kpr=kp

    top=(H_diff(m,kr)*jn(m,kr))-(J_diff(m,kr)*hankel1(m,kr)) #numerator
    bottom=(H_diff(m,kr)*jn(m,kpr))-(n*J_diff(m,kpr)*hankel1(m,kr)) #denominator
    
    ans=top/bottom

    return ans

#----------------MAIN CODE----------------------

#Defining the permitivity & permeability -----
mu=1 #this is the non-magnetic case so there is only one mu.
eps=1 


n=sqrt(eps*mu) #sqrt(eps*mu) # The refractive index. In this case 10.
#----

for u in range (3,10):

    loop_start_time=time.time()
    
    str_u=str(u)
    filename='/home/des/Desktop/dsktp/project maps/T2/Emu1_eps-100_data%s.txt' %str_u
    f = open(filename,'w')

    print "File Opened. Beginning to produce data for u=%s" %str_u
    
    u=u*0.01
    k=u #k is the wavevector outside the material
    kp=n*u #kp is the wavevector inside the material

    #Loop over cartesian co-ordinates coordinates
    for x in range(-100,101):

        if x==0:
            print "Almost half way through the case for u=%s" %str_u

        x=0.05*x #This is just because the range() function only iterates over intergers

        for y in range(-100,101):

            y=0.05*y #This is just because the range() function only iterates over intergers

            E=0 #The electric field strength is set to zero

            r,phi=make_polar(x,y) #Gets r and phi from x and y.

            kpr=kp*r 
            kr=k*r

            Et=0 #The total electric field at a point
            
            for m in range(-5,6):
            
                if r<=1: #inside
                    
                    E=d_m(m,mu,k,kp,n,1)*jn(m,kpr)*(complex(0,1)**m)*(e**(complex(0,1)*m*phi))
                    E=abs(E)
                    

                else: #outside
                
                    E_inc=jn(m,kr)*(complex(0,1)**m)*(e**(complex(0,1)*m*phi))
                    E_scat=c_m(m,mu,k,kp,n,1)*hankel1(m,kr)*(e**(complex(0,1)*m*phi))

                    E=abs(E_inc+E_scat) #no abs() currently

                Et=Et+E #Et is a 'running total'. 
            
            Ef=Et**2 # (NO currently) squaring of the value. Absolute has already been taken using abs().

            #writing to a file
            outstr=''.join([str(x),"\t",str(y),"\t",str(Ef),"\n"]) 
            f.write(outstr) #print to a .cvs file
        
    #closing the file
    f.close()
    print "file closed succesfully on u=%s" %str_u

    time_now=time.time()
    elapsed_time=time_now-loop_start_time
    print ("That run took %f seconds to complete") %elapsed_time
    rem_time=(18-u)*elapsed_time
    print ("Estimated time to complete code is %f hours") %(rem_time/3600)

print "DONE!" 


    
    
