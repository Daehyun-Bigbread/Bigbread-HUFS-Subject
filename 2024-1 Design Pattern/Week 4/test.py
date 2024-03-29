class A():
    def a1(self):
        print('a1')

class B(A):
    def b1(self):
        print('B')

b = B()
b.a1()