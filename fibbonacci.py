def dec2fib(dec):
	sayi = int(dec)
	i=1
	j=0
	dizi1,dizi2 =[],[]
	while dec>=1:
		while fib[i][-1] < dec:
			i=i+1
		i=i-1     
		if dec==sayi:     
			p=i+1 
		dizi2.append(fib[i][-1])     
		dec=dec-fib[i][-1]
		i = 1
	while j< p+1:     
		if fib[p][j] in dizi2:
			dizi1.append("1") 
		else:
			dizi1.append("0")
		j=j+1
		sonuc = ''.join(dizi1)     
	return str(sonuc)
	

def fib2dec(fib):
	dizi1= str(fib)
	j=0
	dec=0
	while j<len(dizi1):
		if dizi1[j] == "1":    
			dec=dec+fib[len(dizi1)][j]
		j=j+1
	return dec
 
if dec2fib(fib2dec(('100101000110010'))==100101000110010:
  print("test1 OK")
 
if dec2fib(100) == '101001000010':
  print("test2 OK")
 	
