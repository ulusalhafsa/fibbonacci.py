

#!/usr/bin/env python
# - coding=UTF-8  -
def fibonacci(n):     
        i = 0
	dizi1= []
	while i <= n:     
		if i < 2:
			dizi1.append(1)
		else:
			dizi1.append(dizi1[i-1] + dizi1[i-2])
		i=i+1
	return dizi1
 
def dec2fib(decimal):
	x= int(decimal)
	i = 1
        j = 0
        dizi2= []
        dizi3= []
 
	while decimal > 0:
		while fibonacci(i)[-1] < decimal:
			i=i+1
		i=i-1   
		if decimal == x:     
			k = i +1 
		dizi3.append(fibonacci(i)[-1])     
		decimal=decimal-fibonacci(i)[-1]
		i = 1
	
        while k+1>j:     
		if fibonacci(k)[j] in dizi3:
			dizi2.append("1")
			dizi3[-1] = 0.5     
		else:
			dizi2.append("0")
		j=j+1
		sonuc = ''.join(dizi2)     
	
	return sonuc
 
def fib2dec(fib):
	dizi1= str(fib)
	i=0
        decimal=0
 
	while len(dizi1)>i:
		if dizi1[i] == "1":     
            		decimal=decimal+fibonacci(len(dizi1))[i]
		i=i+1
	return decimal
 
if dec2fib(fib2dec('1010001010'))=='1010001010':
  print("test1 OK")
 
if dec2fib(100) == '101001000010': 
  print("test2 OK")
 
	


 	
