secretnumber=7
guesscount=0
guesslimit=3
while guesscount<guesslimit:
      ng=int(input('Guess: '))
      guesscount+=1
      if ng==secretnumber:
        print("You won!")
        break
      else:
          print("Sorry. Try again?")

       
