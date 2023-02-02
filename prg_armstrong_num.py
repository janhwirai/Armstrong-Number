#Armstrong number
num = int(input("Enter a number: "))
sum = 0
i = num
while i > 0:
   a=i% 10
   sum += a** 3
   i//= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")