import numpy as np              #External library for numerical calculations
import matplotlib .pyplot as plt#plotting library

#Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*np.pi),2),0)

def main():
#Burger's equation in CTCS
    # Setup parameters
    nt=7
    nx=40
    dt=10.
    dx=1./nx

    # Initial conditions (in meters or m/s)
    
    # characteristics equation
    c=1.0
    c1=0.0
   u=c*np.ones(nt+1)           #initialBell(u)
   x=u*np.linspace(1,nt+1,nt+1)+c1          #initialBell(u)
#    x=np.linspace(0,1,nx+1)
#    x=initialBell(x)
#    x=c*np.linspace(0,nt+1,nt+1)+c1
#    u=x.copy()
#    u[0]=0.0
#    x[0]=c1
#    print(x)
#    for k in range(nx):
#        u[k]=(x[k+1]-x[k])/dt
#    x=u*np.linspace(1.0,nx+1,nx+1)+c1
#    u=c*np.linspace(1.0,nx+1,nx+1)+c1
#    x=2*dt*u
#    u[nx]=u[nx-1]
    print(u)
    print(x)
    xorg=x.copy()
    uorg=u.copy()
    # Store all locations for plotting and store initial locations
    #Spatial variable going fro m zero to one inclusive
    x[0]=x[1]
    u[0]=u[1]
    xNew=x.copy()
    xOld=x.copy()
    uNew=u.copy()
    uOld=u.copy()

    # Loop over all time-steps
    # here, ua = u(n+1)
    for n in range(1,nt):
        for j in range(1,nx):
            x[nx]=x[nx-1]
            u[nx]=u[nx-1]
            uNew=uOld+u*(u[j+1]-u[j-1])*dt/dx
            xNew=xOld+2.*dt*u
            uOld=u.copy()
            u=uNew.copy()
            xOld=x.copy()
            x=xNew.copy()

    print(u)
    print(x)
    # plot the solution in comparison to the analytic solution
    plt.plot(xorg, uorg,'r',label='original x and u')
    plt.plot(x, u,'b',label='CTCS')
    plt.legend(loc='best')
    plt.ylabel('u')
    plt.xlabel('x')
    plt.axhline(0,linestyle=':',color='black')
    plt.show()


main()



