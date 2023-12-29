import random
num = random.randint(1,100)
print('random',num)
guesses = [0]
while True:
    try:
     guess = int(input("""I'm thinking of a number between 1 and 100
      Can you guess it?   """))
     if guess <1 or guess >100:
              print('OUT OF BOUNDS! please try again:')
              continue
     if guess == num:
        print(f'CONGRATULATION, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
     guesses.append(guess)
     print("guessed Number are ",guesses)

     if guess < num:
         print("Too low. Try Again! ")
     else:
         print("Too high. Try Again ")
    except:
       print('Enter valid Number ')
