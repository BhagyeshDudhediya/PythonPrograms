class A:
    def __init__(self,i):
        self.i=i
    def fn1(self):
        print "In fn1"

class B:
    def __init__(self, j):
        self.j=j
    def fn2(self):
        print "In fn2"

class C(A, B):
    def __init__(self, i, j, k):
        A.__init__(self, i)
        B.__init__(self, j)
        self.k = k
    def fn3(self):
        print "In fn3"

c=C(10, 20, 30)
c.fn1()
c.fn2()
c.fn3()
print c.i
print c.j
print c.k

