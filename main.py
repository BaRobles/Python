from random import randint

while True:

  attempts = 0
  num = randint(1, 25)
  
  while attempts < 6:
  
    x = int(input("Try to guess! Enter a number between 1 or 25: "))

    if(num < x): 
      print("Too high!")
      
    elif(num > x): 
      print("Too low!")
      
    else: 
      print("Correct!")
      break
  
    attempts += 1
  
  if attempts == 6:
    print(f"The correct answer is: {num}")