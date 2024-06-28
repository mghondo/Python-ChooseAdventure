print("""
              
       :|           . ,
       :|           _)/'/
       :|         ,/'/,'<,
       :|       .-'\\_.-` 
       :|      ///'\\
       .|      |e^e-?                            
      (/\      `.=,'._    .      
      `: L   _.-J   L '\.' `.
       :|/`.'  / \ /'_.'     \     
       :|\   .-\__V__<    \/  L     
       :| `-'   \  ,  \   /\  |                    
       :|        \._.=-\.     F                      
       :|        )\_/   `-.__J                        
       :|       /  |    |                              
       .|      /   |   /
 ____  :|___  (   <|' | _______________________________________
       :|      \  '\  \                     ~           
   ~   :|       `. |   |  ~          ___..._          ~    
       :|         `J  /   ...--..---'     _ ""------......____   
       :|     ,    _)_|>.__,_            c")_              
-.b'ger '-.,-.+- cC\\_\  "'-=-i"-.       (__/                 
  VK/a:f         _,. -'''         `-.                         
""")

print("Hey, hun! This is game number two. You'll be playing by making choices.")
print("\nHere's the story, you're on an adventure. You have your trusty dog with you, select the name.")

name = input("Enter your dog's name: ")

if name.lower() == "patch":
    print("Of course you picked Patch, who else would you pick.")
else:
    print(f"I guess you don't love Patch. Whatever. {name} it is I guess. Let's play!!")

badGuy = input("\nWho's the bad guy in your story? ")

print(f"Oh wow {badGuy} sounds like a real bad apple. Let's see what happens.")

if badGuy.lower() == "biden":
    print("And of course Biden is the bad guy.")

print(f"\nYou're in a dark and haunted forest. You hear animals and critters. Luckily you have your trusty pup {name} by your side.")

choice = input(f"\nYou see a snake, do you 1. Run or 2. Sick {name} on the snake? ")

if choice == "1":
    print("Why Run you have a tough dog.")
elif choice == "2":
    print(f"That's the spirit. {name} knows how to get a snake and make it his bitch.")
else:
    print("Invalid choice. Game over anyway.")

print("\nGame Over.")