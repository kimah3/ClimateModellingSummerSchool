import numpy as np
import matplotlib .pyplot as plt

def main():
    #Semi-implicit solution of the Shallow Water Equations

    # Setup parameters
    nx = 10
    ny = 10
    nt = 10
    it = 2
    dx = 10./nx
    dy = 10./ny
    dt = 1./nt
    g  = 9.81 # m s-2
    f  = 1.e-4
    pi = 2*np.arcsin(1)
    # Initial data structure
    u = np.zeros((nx+1,ny+1,nt+1))
    v = np.zeros((nx+1,ny+1,nt+1))
    h = np.zeros((nx+1,ny+1,nt+1))
    up= np.zeros((nx+1,ny+1))#u'
    vp= np.zeros((nx+1,ny+1))#v'
    hp= np.zeros((nx+1,ny+1))#h'
    x = np.linspace(0,1,nx+1)
    y = np.linspace(0,1,ny+1)
    # Initial condition
    for i in range(0,nx+1):
        for j in range(0,ny+1):
            u[i,j,0]=np.cos(x[i]*2.*pi)
            v[i,j,0]=np.sin(y[j]*2.*pi)
    
    # Loop over all time-steps
    for k in range(1,it):
        for n in range(0,nt):
            for i in range(1,nx-1):
                for j in range(1,ny-1):
                    up[i,j]=u[i,j,n]-dt*(u[i,j,n]*(u[i,j,n]-u[i-1,j,n])/dx+u[i,j,n]*(v[i,j,n]-v[i,j-1,n])/dy+f*v[i,j,n])
                    vp[i,j]=v[i,j,n]-dt*(v[i,j,n]*(u[i,j,n]-u[i-1,j,n])/dx+v[i,j,n]*(v[i,j,n]-v[i,j-1,n])/dy+f*v[i,j,n])
                    hp[i,j]=h[i,j,n]-dt*(u[i,j,n]*(h[i,j,n]-h[i-1,j,n])/dx+v[i,j,n]*(h[i,j,n]-h[i,j-1,n])/dy+\
                                           h[i,j,n]*(u[i+1,j,n]-u[i,j,n])/dx+h[i,j,n]*(v[i,j+1,n]-v[i,j,n])/dy)
                    h[i,j,n+1]=hp[i,j]+dt*dt*g*h[i,j,n]*(h[i+2,j,n+1]+h[i-2,j,n+1]-2*h[i,j,n+1])/(8*dx*dx)+\
                                         dt*dt*g*h[i,j,n]*(h[i,j+2,n+1]+h[i-2,j,n+1]-2*h[i,j,n+1])/(8*dy*dy) 
                    u[i,j,n+1]=up[i,j]-dt*g*(h[i+1,j,n]-h[i-1,j,n])/(2*dx)
                    v[i,j,n+1]=vp[i,j]-dt*g*(h[i,j+1,n]-h[i,j-1,n])/(2*dy)

    plt.contour(x,y,u[:,:,0],cmap="RdBu_r")
    plt.show()


main()


