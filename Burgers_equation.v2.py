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
    nt50=5
    nx=150
    dt=1./nt
    dx=10./nx

    # Initial data structure
    u=np.zeros((nx+1,nt+1))
    uff=np.zeros((nx+1,nt+1))#FTFS
    ufb=np.zeros((nx+1,nt+1))#FTBS
    x=np.linspace(0,1,nx+1)

    # Initial condition
    u[:,0]=initialBell(x)
    u[:,1]=u[:,0]
    uff[:,0]=initialBell(x)
    uff[:,1]=u[:,0]
    ufb[:,0]=initialBell(x)
    ufb[:,1]=u[:,0]

    u0=u[:,0]
    print(np.size(uff[1:nx,0]))
    print(np.size(uff[1:nx,0]))
    # Loop over all time-steps
    for n in range(1,nt):
        u[1:nx,n+1]=u[1:nx,n-1]+u[1:nx,n]*(u[2:nx+1,n]-u[:nx-1,n])*dt/dx
        uff[:nx,n+1]=uff[:nx,n]+uff[:nx,n]*(uff[1:nx+1,n]-uff[:nx,n])*dt/dx
        ufb[:nx,n+1]=ufb[:nx,n]+ufb[:nx,n]*(ufb[:nx,n]-ufb[1:nx+1,n])*dt/dx

    # save ua = u(n+1) to draw u that is in final timestep.
    ua=u[:,nt]
    uffa=uff[:,nt]
    ufba=ufb[:,nt]
    u500=u[:,nt50]
# Plot
    title='nt='+str(nt)
    title500='nt='+str(nt50)
    plt.title("Burger's equation in CTCS(u=initial Bell)")
    plt.plot(x,u0,'black',label='initial')
    plt.plot(x,ua,'b',label=title)
    plt.plot(x,u500,'r',label=title500)
    plt.plot(x,uffa,'g',label="FTFS")
    plt.plot(x,ufba,'c',label="FTBS")
    plt.legend(loc='upper right')
    plt.ylabel('u')
    plt.xlabel('x')

#    import matplotlib.cm as cm
#    colour=iter(cm.rainbow(np.linspace(0,10,nt)))
#    for i in range(0,nt,10):
#        c=next(colour)
#        title='nt='+str(i)
#        plt.plot(x,u[:,i],c,label=title)
#        plt.legend(loc='upper right')
#        plt.ylabel('u')
#        plt.xlabel('x')
#        plt.axhline(0,linestyle=':',color='black')
#        plt.show()
    plt.show()
#    plot_convection(u,x,nt,'test')
# hello!
main()

