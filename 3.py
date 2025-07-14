#Print Numbers 1 to 10

i=0
for i in range(1,11):
    print(i)

#Multiplication Table
num =  int(input("Enter a Number"))
for i in range(1,11):
    mul=num*i
    print(f"{num} X {i} = {mul}")

#Q3 Factorial 
num = int(input("Enter a number"))
factorial=1
if num<0:
    print("The factorial of negative number is not defined")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial *= i
        print(f"The factorial of {num} is {factorial}")

#Q4 Sum of N Numbers

n = int(input("Enter a Number"))
sum=0
for i in range (1, n + 1):
    sum += i
    print(f"The sum of first {n} natural number is {sum}")

# Q5 Reverse a number
n=int(input("Enter a Number"))
while n:
 print(n)
 n -=1

#Q6 Count digits in Number
def calculate_count(n):
   
    if n==0:
     return 1
    count =0
    while n !=0:
       n = n//10
       count +=1
       return count
n= int(input("Enter a Number"))
result = calculate_count(n)
print(f"The count of digits in the Number is {result}")   

# Q7 Palindrome Number
num = int(input("Enter a Number"))
reverse=0
temp = num

while temp>0:
    digit = temp%10
    reverse= (reverse*10)+digit
    temp = temp//10
if num == reverse:
        print(f"{num} is Palindrome")
else:
        print(f"{num} is not palindrome") 

#Q8 Armstrong Number

num = int(input("Enter a Number"))
order=len(str(num))
sum=0
temp=num


while temp>0:
    digit = temp%10
    sum += digit**order
    temp = temp//10

if num == sum:
        print(f"{num} is Armstrong Number")
else:
      print(f"{num} is not Armstrong Number")

# Q9 Print prime 1 to 100
print("The Prime numbers between 1 to 100 are: ")

for num in range(2,101):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num==0:
          is_prime=False
          break
    if num !=0:
       print(num,end=" ")

# Q10 Number guessing game
import random

secret_number=random.randint(1,100)
attempts=0
print("🎲 welcome to the Samiksha's Number Guessing Game")
print("Guess a Number between 1 to 100")
while True:
    guess = int(input("Enter Your guess: "))
    attempts += 1
    if guess==secret_number:
        print("Congratulations!! Your Guessed it Correct in attempts {attempts} tries.You Won the Game")
        break
    elif guess>secret_number:
        print("Too Highh!Better luck next time")
    else :
        print("Too Low! Better luck next time")


           






    

