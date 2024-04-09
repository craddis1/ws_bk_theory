import numpy as np

#1st order terms
class WA1:
    def l1(params,mu,phi,r=0,s=0):
        k1,k2,k3,theta,Pk1,Pk2,Pk3,Pkd1,Pkd2,Pkd3,Pkdd1,Pkdd2,Pkdd3,d,K,C,f,D1,b1,b2,g2 = params
        st = np.sin(theta)
        ct= np.cos(theta)
        
        perm12 =
        perm13 =
        perm23 =
        return (perm12+perm13+perm23) # 2 was missed from original running
    
class RR1:    
    def l1(params,derivs,mu,phi,r=0,s=0):
        k1,k2,k3,theta,Pk1,Pk2,Pk3,Pkd1,Pkd2,Pkd3,Pkdd1,Pkdd2,Pkdd3,d,K,C,f,D1,b1,b2,g2 = params
        fd,Dd,gd2,bd2,bd1,fdd,Ddd,gdd2,bdd2,bdd1 = derivs
        st = np.sin(theta)
        ct= np.cos(theta)
        
        perm12 = 
        perm13 =
        perm23 =
        return (perm12+perm13+perm23)
    
    
    
    
    