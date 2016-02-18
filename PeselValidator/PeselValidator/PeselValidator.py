ControlValue = 0
WagesArray = [1,3,7,9,1,3,7,9,1,3]
PeselNumber = input()
PeselLastNumber = int(PeselNumber[-1])

for i in range(int(len(PeselNumber)) - 1):
	ControlValue += WagesArray[i] * int(PeselNumber[i])

VerifyValue = ControlValue % 10
VerifyValue = 10 - VerifyValue 
if(VerifyValue == PeselLastNumber):
	print("1")
else:
	print("0")






