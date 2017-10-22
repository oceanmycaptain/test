class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        def gcd(p,q):
            if q==0:
                return p
            return gcd(q,p%q)
        self.r=gcd(p,q) #这里为什么要赋值给self.r??为什么赋值给g,或者a之类的不行？这怎么解释？？？
 
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
 
    def __sub__(self, r):
        return Rational(self.p*r.q-r.p*self.q,self.q*r.q)
 
    def __mul__(self, r):
        return Rational(self.p*r.p,self.q*r.q)
 
    def __div__(self, r):
        return Rational(self.p*r.q,self.q*r.p)
 
    def __str__(self):
        return '%s/%s'%(self.p/self.r,self.q/self.r)
 
    __repr__ = __str__
 
r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
