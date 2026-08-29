import math
from scipy.stats import norm

from abc import ABC, abstractmethod 


class BSMOption(ABC):
    def __init__(self, s, x, t, sigma, rf, div):
        self.s = s
        self.x = x
        self.t = t
        self.sigma = sigma
        self.rf = rf
        self.div = div

    def set_sigma(self, new_sigma):
        self.sigma = new_sigma
        self.compute_d1()
        self.compute_d2()
        self.compute_nd1()
        self.compute_nd2()
        
    def compute_d1(self):
        self.d1 = (math.log(self.s / self.x) + (self.rf - self.div + 0.5*self.sigma**2)*self.t)/(self.sigma * math.sqrt(self.t))
        return self.d1

    def compute_d2(self):
        self.d2  = self.d1 - self.sigma * math.sqrt(self.t)
        return self.d2
        
    def compute_nd1(self):
        self.nd1 = norm.cdf(self.d1)
        return self.nd1

    def compute_nd2(self):
        self.nd2 = norm.cdf(self.d2)
        return self.nd2

    @abstractmethod
    def compute_value(self):
       pass 

    @abstractmethod
    def compute_delta(self):
       pass 

    def __repr__(self):
        return (
            f"x={self.x!r}, t={self.t!r}, "
            f"sigma={self.sigma!r}, rf={self.rf!r}, div={self.div!r}"
        )        


class BSMEuroCallOption(BSMOption):
    def __init__(self, s, x, t, sigma, rf, div):
        super().__init__(s, x, t, sigma, rf, div)
        self.compute_d1()
        self.compute_d2()
        self.compute_nd1()
        self.compute_nd2()
        self.compute_value()
        self.compute_delta()
        
        
    def compute_value(self):
        self.value = self.s * math.exp(-self.div * self.t) * self.nd1 - self.x * math.exp(-self.rf * self.t) * self.nd2 
        return self.value 
    
    def compute_delta(self):
        self.delta = math.exp(-self.div * self.t) * self.nd1
        return self.delta
    
    def __repr__(self):
        return (
            f"This is a European call with value = {self.value()!r} \n"
            f"details = ({super().__repr__()})"
        )


class BSMEuroPutOption(BSMOption):
    def __init__(self, s, x, t, sigma, rf, div):
        super().__init__(s, x, t, sigma, rf, div)
        self.compute_d1()
        self.compute_d2()
        self.compute_nd1()
        self.compute_nd2()
        self.compute_value()
        self.compute_delta()
        
    def compute_value(self):
        self.value = -(self.s * math.exp(-self.div * self.t) * (1-self.nd1) - self.x * math.exp(-self.rf * self.t) * (1-self.nd2))
        return self.value
        
    def compute_delta(self):
        self.delta = -math.exp(-self.div * self.t) * (1-self.nd1)
        return self.delta
    
    def __repr__(self):
        return (
            f"This is a European put with value = {self.value()!r} \n"
            f"details = ({super().__repr__()})"
        )


