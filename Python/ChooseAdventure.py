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

import time

print("Hey, there! This is a 'choose your own adventure game.'Patch You'll be playing with Patch.")
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

print(f"\nYou're in a dark and haunted forest. You hear animals and critters. Lucking you have your trusty pup {name} by your side.")

choice = input(f"\nYou see a snake, do you 1. Run or 2. Sick {name} on the snake? ")

if choice == "1":
    print("You run as fast as you can and arrive at a river.")
    print("Suddenly an evil being appears out of the water.")
    print(f"I am the evil {badGuy}. You are trespassing in my territory.")
    
    time.sleep(2)
    print('Game Over. Next time let Patch sick the dog.')
elif choice == "2":
    print(f"That's the spirit. {name} knows how to get a snake and make it pay.")
    print("Nice, way to be bold. You kill the snake and were able to absorb its life force.")
else:
    print("Invalid choice. Game over anyway.")