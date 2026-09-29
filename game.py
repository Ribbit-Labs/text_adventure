def p(*x):
  print(str(x))
game_name = "Text Adventure"
user_name = ""
choice = ""
print("Welcome to " + game_name + " .")
def run_game():
  global user_name
  print("Starting: ")
  print("Would you like the tutorial? Y/N")
  tut_choice = input().upper()
  if tut_choice == "Y":
    print("OK! Good choice")
    print("So, first, we will ask you a question. Like, for example, what's your name?")
    user_name = input()
    print("Good! You got it!")
    print("Just to get that right, it's " + user_name + " right?")
    print("When it's not Yes or No, we will tell you the choices, like this:")
    print("Did you eat cereal or toast for breakfast? Cereal/Toast")
    choice = input()
    print("Mmm.. " + choice + ". Lucky! I'm eating a yogurt right now.")
    print("Ok, and always remember, follow the Magic!")
  elif tut_choice == "N":
    pass
  print("You wake up, early in the morning. The birds are singing, and you think it's just a normal day.")\
  print("You go out to check the mail.")
  print("You find one unnamed envelope, which is probably just a bunch of bills.")
  print("Do you open it now, or do you open it after breakfast? Breakfast/Now")
  choice = input().lower()
  if choice == "breakfast":
    print("Ok.")
    print("The life's substance. Coffee.")
    print("30 minutes later.")
    print("Ok, lets check that mail!")
  print("It's in the hall.")
run_game()
