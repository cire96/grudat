import time

def pow1(n):
	"""Return 2**n, where n is a nonnegative integer."""
	if n == 0:
		return 1
	x = pow1(n//2)
	if n%2 == 0:
		return x*x
	return 2*x*x


def sum1(a):
	"""Return the sum of the elements in the list a."""
	n = len(a)
	if n == 0:
		return 0
	if n == 1:
		return a[0]
	return sum1(a[:n//2]) + sum1(a[n//2:])



def sum2(a):
	"""Return the sum of the elements in the list a."""
	return _sum(a, 0, len(a)-1)

def _sum(a, i, j):
	"""Return the sum of the elements from a[i] to a[j]."""
	if i > j:
		return 0
	if i == j:
		return a[i]
	mid = (i+j)//2
	return _sum(a, i, mid) + _sum(a, mid+1, j)




N = [10, 100, 1000, 10000, 100000, 1000000]
T_pow = []
T_sum1 = []
T_sum2 = []


for i in range (0,len(N)):

    start = time.time()
    pow1(N[i])
    temp = time.time() - start
    T_pow.append(temp)

    start = time.time()
    sum1(N[i])
    temp = time.time() - start
    T_sum1.append(temp)

    start = time.time()
    sum2(N[i])
    temp = time.time() - start
    T_sum2.append(temp)


    
    
