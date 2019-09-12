import matplotlib
import numpy as np              #External library for numerical calculations
import matplotlib .pyplot as plt#plotting library

#Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*np.pi),2),0)

def main():
    #Burger's equation in CTCS
    # Setup parameters
    nt   = 100
    nt50 = 1
    nx   = 150
    dt   = 1./nt
    dx   = 10./nx

    # Initial data structure
    u  = np.zeros((nx+1, nt+1))#CTCS
    uff= np.zeros((nx+1, nt+1))#FTFS
    ufb= np.zeros((nx+1, nt+1))#FTBS
    x  = np.linspace(0,1,nx+1)

    # Initial condition
    u[:,  0]  = initialBell(x)
    uff[:,0]  = initialBell(x)
    ufb[:,0]  = initialBell(x)
    u[:nx,  1] = u[:nx,0] - u[:nx,0]*(u[1:nx+1,0] - u[:nx,0])*dt/dx
    uff[:nx,1] = u[:nx,0] - u[:nx,0]*(u[1:nx+1,0] - u[:nx,0])*dt/dx
    ufb[:nx,1] = u[:nx,0] - u[:nx,0]*(u[1:nx+1,0] - u[:nx,0])*dt/dx

    u0=u[:,0]

    # Loop over all time-steps
    for n in range(1,nt):
        for j in range(1,nx):
            u[j,  n+1] = u[j,  n-1] - u[j,  n] * ( u[j+1,  n] - u[j-1,  n])*dt/dx
            uff[j,n+1] = uff[j,n  ] - uff[j,n] * ( uff[j+1,n] - uff[j,  n])*dt/dx
            ufb[j,n+1] = ufb[j,n  ] - ufb[j,n] * ( ufb[j,  n] - ufb[j-1,n])*dt/dx

# Plot
    detailed_info='nt='+str(nt)+' nx='+str(nx)+' courant='+str(dt/dx)
    plt.title("Burger's equation (u=initial Bell)\n "+detailed_info)
    plt.plot(x,u0,       'k',label='initial')
    plt.plot(x,u[:,nt],  'b',label='CTCS')
    plt.plot(x,uff[:,nt],'g',label="FTFS")
    plt.plot(x,ufb[:,nt],'c',label="FTBS")
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
#    plt.savefig('initialBell.png')
#    plot_convection(u,x,nt,'test')
# hello!
main()

