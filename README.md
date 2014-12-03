
´´´python def dec2fib(dec):
	sayi = int(dec)
	i=1
	j=0
	dizi1, dizi2 =[], []
	while dec >=1:
		while fib(i)[-1] < dec:
		
			i=i+1
		i=i-1     
		if dec == sayi:     
			p= i +1 
		dizi2.append(fib(i)[-1])     
		dec=dec-fib(i)[-1]
		i = 1
	while j< p+1:     
		if fib(p)[j] in dizi2:
			dizi1.append("1") 
		else:
			dizi1.append("0")
		j=j+1
		sonuc = ''.join(dizi1)     
	return str(sonuc)
