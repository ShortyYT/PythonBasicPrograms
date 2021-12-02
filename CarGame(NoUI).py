command=""
while command !="quit":
    command=input("> ")
    if command=="start":
        print("The car has started!")

    elif command == "stop":
        print("The car has stopped!")

    elif command=="help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        help - for help """)

    elif command=="quit":
        break
 
    else:print('Sorry, i dont understand. You can use the "help" command for help')
