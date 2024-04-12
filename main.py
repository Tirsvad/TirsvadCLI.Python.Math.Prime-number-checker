# Write your code below this line 👇

def prime_checker(number):
  for i in range(2,number):
    if int(list(str(number))[-1]) in ['0' ,'2', '4', '6', '8']:
      return False
    if number > 5 and int(list(str(number))[-1]) in ['5']:
      return False
    if number % i == 0:
      return False
  if number == 1:
    return False
  return True
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
#n = int(input()) # Check this number
#prime_checker(number=n)

for x in range(1, 500):
  if prime_checker(number=x):
    print(x)