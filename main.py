# print out numbers 1 - 10

counter = 1
while(counter <= 10): # or (counter < 11)
  print(counter)  
  counter += 1

# print out all even numbers between 0 - 20

counter = 2
while(counter <= 20):
  print(counter)
  counter += 2

# ask user for a number
# print all the numbers up to the user's number starting at 1
usernumber = int(input("choose a number: "))
counter = 1
while(counter <= usernumber):
  print(counter)
  counter += 1

# while () :
#    if(condition) 
#            print

# alternite way to print even numbers 
counter = 1 
while(counter <= 20): 
  if(counter % 2 == 0): 
    print(counter)
  counter += 1

# print all the numbers between 1-100 that are divisble by 3 or 7
# BUT NOT BOTH
counter = 1
while(counter <= 100):
  if (counter % 3 == 0 or counter % 7 == 0):
    if not(counter % 7 ==0 and):
    print(counter)
  counter += 1

# print all the numbers between 1-100
# if the number is divisable by 3, print out "fizz"
#if the number is divisable by 5, print out "buzz"
# if the number is divisable by 80TH, print out "fizzbuzz"
counter = 1
while(counter <= 100):
  if(counter % 3 == 0):
    print("fizz")
  if(counter % 5 == 0):
    print("buzz")
    if(counter % 3 == counter % 5):
      print("fizzbuzz")
    print(counter)
    counter += 1



