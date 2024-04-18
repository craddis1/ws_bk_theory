import numpy as np

# get newtonian tree level covariances...

class COV:
    def N00(params,nbar,Ntri):
        k1,k2,k3,theta,Pk1,Pk2,Pk3,Pkd1,Pkd2,Pkd3,Pkdd1,Pkdd2,Pkdd3,d,K,C,f,D1,b1,b2,g2 = params
        
        cos = lambda x: np.cos(x)
        sin = lambda x: np.sin(x)
        
        expr = (D1*Pk1*nbar*(D1*Pk2*nbar*(D1*Pk3*nbar*(105*b1**3*k3**2 + 35*b1**2*f*k1**2 + 35*b1**2*f*k2**2 + 70*b1**2*f*k3**2 + 35*b1*f**2*k1**2 + 35*b1*f**2*k2**2 + 14*b1*f**2*k3**2 + 9*f**3*k1**2 + 3*f**3*k1*k2*cos(3*theta) + 9*f**3*k2**2 + f**2*(7*b1*(k1**2 + k2**2 + k3**2) + 6*f*(k1**2 + k2**2))*cos(2*theta) + f*k1*k2*(70*b1**2 + 84*b1*f + 27*f**2)*cos(theta)) + 7*k3**2*(15*b1**2 + 10*b1*f + f**2*cos(2*theta) + 2*f**2)) + 7*D1*Pk3*nbar*(15*b1**2*k3**2 + 5*b1*f*k1**2 + 5*b1*f*k2**2 + 5*b1*f*k3**2 + 3*f**2*k1**2 + f**2*k2**2*cos(2*theta) + 2*f**2*k2**2 + 2*f*k1*k2*(5*b1 + 3*f)*cos(theta)) + 7*k3**2*(15*b1 + 5*f)) + 7*D1*Pk2*nbar*(D1*Pk3*nbar*(15*b1**2*k3**2 + 5*b1*f*k1**2 + 5*b1*f*k2**2 + 5*b1*f*k3**2 + f**2*k1**2*cos(2*theta) + 2*f**2*k1**2 + 3*f**2*k2**2 + 2*f*k1*k2*(5*b1 + 3*f)*cos(theta)) + k3**2*(15*b1 + 5*f)) + 35*D1*Pk3*nbar*(3*b1*k3**2 + 2*f*k1*k2*cos(theta) + f*(k1**2 + k2**2)) + 105*k3**2)/(105*Ntri*k3**2*nbar**3)
        return expr
    
    def N10(params,nbar,Ntri):
        k1,k2,k3,theta,Pk1,Pk2,Pk3,Pkd1,Pkd2,Pkd3,Pkdd1,Pkdd2,Pkdd3,d,K,C,f,D1,b1,b2,g2 = params
        
        cos = lambda x: np.cos(x)
        sin = lambda x: np.sin(x)
        
        expr = (3*D1*Pk1*nbar*(D1*Pk2*nbar*(D1*Pk3*nbar*(105*b1**3*k3**2 + 63*b1**2*f*k1**2 + 42*b1**2*f*k2**2 + 105*b1**2*f*k3**2 + 72*b1*f**2*k1**2 + 9*b1*f**2*k1*k2*cos(3*theta) + 54*b1*f**2*k2**2 + 27*b1*f**2*k3**2 + 20*f**3*k1**2 + 10*f**3*k1*k2*cos(3*theta) + f**3*k2**2*cos(4*theta) + 18*f**3*k2**2 + 3*f*k1*k2*(42*b1**2 + 57*b1*f + 20*f**2)*cos(theta) + f*(21*b1**2*(k2**2 + k3**2) + 18*b1*f*(k1**2 + 2*k2**2 + k3**2) + f**2*(15*k1**2 + 16*k2**2))*cos(2*theta)) + 3*k3**2*(35*b1**2 + 35*b1*f + 9*f**2 + f*(7*b1 + 6*f)*cos(2*theta))) + 3*D1*Pk3*nbar*(35*b1**2*k3**2 + 21*b1*f*k1**2 + 14*b1*f*k2**2 + 21*b1*f*k3**2 + 15*f**2*k1**2 + 9*f**2*k2**2 + 6*f*k1*k2*(7*b1 + 5*f)*cos(theta) + f*k2**2*(7*b1 + 6*f)*cos(2*theta)) + 3*k3**2*(35*b1 + 21*f)) + 9*D1*Pk2*nbar*(D1*Pk3*nbar*(35*b1**2*k3**2 + 21*b1*f*k1**2 + 14*b1*f*k2**2 + 14*b1*f*k3**2 + 9*f**2*k1**2 + 3*f**2*k1*k2*cos(3*theta) + 9*f**2*k2**2 + 3*f*k1*k2*(14*b1 + 9*f)*cos(theta) + f*(7*b1*(k2**2 + k3**2) + 6*f*(k1**2 + k2**2))*cos(2*theta)) + 7*k3**2*(5*b1 + f*cos(2*theta) + 2*f)) + 63*D1*Pk3*nbar*(5*b1*k3**2 + 3*f*k1**2 + 6*f*k1*k2*cos(theta) + f*k2**2*cos(2*theta) + 2*f*k2**2) + 315*k3**2)/(35*Ntri*k3**2*nbar**3)
        return expr
    
    def N11(params,nbar,Ntri):
        k1,k2,k3,theta,Pk1,Pk2,Pk3,Pkd1,Pkd2,Pkd3,Pkdd1,Pkdd2,Pkdd3,d,K,C,f,D1,b1,b2,g2 = params
        
        cos = lambda x: np.cos(x)
        sin = lambda x: np.sin(x)
        
        expr = 3*D1*f*(Pk2*(D1*Pk1*nbar*(D1*Pk3*nbar*(21*b1**2*k2**2 + 21*b1**2*k3**2 + 3*b1*f*k1**2 + 21*b1*f*k2**2 + 3*b1*f*k3**2 + f**2*k1**2 + 2*f**2*k2**2*cos(2*theta) + 4*f**2*k2**2 + 6*f*k1*k2*(3*b1 + f)*cos(theta)) + k3**2*(21*b1 + 3*f)) + 3*D1*Pk3*nbar*(7*b1*(k2**2 + k3**2) + 6*f*k1*k2*cos(theta) + f*(k1**2 + 6*k2**2)) + 21*k3**2) + 3*Pk3*k2**2*(D1*Pk1*nbar*(7*b1 + f) + 7))*sin(theta)**2/(35*Ntri*k3**2*nbar**2)
        return expr