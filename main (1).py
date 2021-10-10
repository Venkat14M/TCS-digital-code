def getSum(X):

	sum=0

	for i in X:

		sum+=i

	return sum


# Function to prints elements to be swapped

def findSwapValues(A,B):

	# Calculation if sums from both lists

	sum1=getSum(A)

	sum2=getSum(B)


	# Boolean variable used to reduce further iterations

	# after the pair is found

	k=False


	# Lool for val1 and val2, such that

	# sumA - val1 + val2 = sumB -val2 + val1

	val1,val2=0,0

	c = 0

	for i in A:

		for j in B:

			newsum1=sum1-i+j

			newsum2=sum2-j+i
			if newsum1%2==0 and newsum2%2==0:

				val1=i

				val2=j



				# Set to True when pair is found

				k=True

				break

		c += 1

		


                                     # If k is True, it means pair is found.

		# So, no further iterations.


		if k==True:

			break
	print("no.of swaps:",c)

	return



#main

A =[]

B = []

print("no.of elements :")

n=int(input())
print("A:")

for i in range(0,n):

    A.append(int(input()))

print("B:")


for i in range(0,n):

    B.append(int(input()))

c = sum(A)

d = sum(B)

if n%2!= 0 and m%2!=0:

    if c%2 != 0 and d%2 != 0:

        print("-1")

elif c%2 == 0 and d%2==0:

    print("0")

else:

    findSwapValues(A,B)

