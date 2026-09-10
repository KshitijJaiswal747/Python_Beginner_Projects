import random 

roll_count =0

while True:
  choice = input('Roll the dice? (y/n): ').lower()

  if choice == 'y':
      num_dice = int(input("Enter number of Dice?"))
      dice = [random.randint(1,6) for _ in range(num_dice)]

      print("You Rolled:",dice)

      roll_count += 1
      print("Roll Count :",roll_count)
      print()
      
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')

