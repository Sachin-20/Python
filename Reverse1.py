
NOS=[]
print()
print("Enter SIX numbers below:-")
for i in range(0,6):
	NOS.append(int(input()))
def Reverse(NOS): 
    NOS.reverse() 
    return NOS
print()
print(Reverse(NOS))
print()