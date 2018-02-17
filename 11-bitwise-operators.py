#!/usr/bin/python3 
 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
print ('a=',a,':',bin(a),'b=',b,':',bin(b)) 
c = 0 
 
c = a & b;        # 12 = 0000 1100 
print ("result of a AND b is ", c,':',bin(c)) 
 
c = a | b;        # 61 = 0011 1101  
print ("result of a OR b is ", c,':',bin(c)) 
 
c = a ^ b;        # 49 = 0011 0001 
print ("result of a EXOR b is ", c,':',bin(c)) 
 
c = ~a;           # -61 = 1100 0011 
print ("result of a COMPLEMENT is ", c,':',bin(c)) 
 
c = a << 2;       # 240 = 1111 0000 
print ("result of a LEFT SHIFT 2 is ", c,':',bin(c)) 
 
c = a >> 2;       # 15 = 0000 1111 
print ("result of a RIGHT SHIFT 2 is ", c,':',bin(c)) 
