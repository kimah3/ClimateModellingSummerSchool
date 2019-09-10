import numpy as np              #External library for numerical calculations
import matplotlib .pyplot as plt#plotting library

#Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*np.pi),2),0)

def plot_convection(u,x,nt,title):
#   """
#   Plots the 1D velocity field
#   """

   import matplotlib.pyplot as plt
   import matplotlib.cm as cm
   plt.figure()
   colour=iter(cm.rainbow(np.linspace(0,10,nt)))
   for i in range(0,nt,10):
      c=next(colour)
      plt.plot(x,u[:,i],c=c)
      plt.xlabel('x (m)')
      plt.ylabel('u (m/s)')
      plt.ylim([0,2.2])
      plt.title(title)
      plt.show()

def main():
#Burger's equation in CTCS
    # Setup parameters
    nt=10
    nx=150
    dt=1./nt
    dx=10./nx

    # Initial data structure
    u=np.zeros((nx+1,nt+1))
    x=np.linspace(0,1,nx+1)
    # Initial condition
    u[:,0]=initialBell(x)
    u[:,1]=initialBell(x)
    u0=u[:,0]
    # Loop over all time-steps
    # here, ua = u(n+1)
    for n in range(1,nt):
        for m in range(1,nx):
            u[m,n+1]=u[m,n-1]+u[m,n]*(u[m+1,n]-u[m-1,n])*dt/dx
    ua=u[:,nt]
    #u0=u[:,0]
    print(u[:,nt])
    print(x)
    title='nt='+str(nt)
    plt.plot(x,ua,'b',label=title)
    plt.plot(x,u0,'r',label='initial')
    plt.legend(loc='upper right')
    plt.ylabel('u')
    plt.xlabel('x')
    plt.axhline(0,linestyle=':',color='black')
    plt.show()
#    plot_convection(u,x,nt,'test')
# hello!
main()

