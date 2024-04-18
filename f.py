def hasInverse(a,b):
	
	while a>0:
		t=a
		a=b%a
		b=t
	if b==1:
		return True
	else:
		return False

def mcd(a,b):
	
	while a>0:
		t=a
		a=b%a
		b=t

	return b
	
def inverse(a, p):
	u=a 
	v=p 
	x1=1 
	x2=0
	while u!=1:
		q=v/u
		r=v-q*u
		x=x2-q*x1
		v=u
		u=r
		x2=x1
		x1=x
	return x1%p

def remove_space(plain):
	ret=''
	for i in plain:
		if i!=' ' and i!='\n':
			ret=ret+i	
	return ret	
    
