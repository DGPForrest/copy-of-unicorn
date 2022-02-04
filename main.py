#Unicorn
import time                             
import os                               

def loading_bar(seconds):                
  for loading in range(0,seconds+1):
    percent = (loading * 100) // seconds
    print("\n")
    print("Your animals is...")
    print("Loading...")
    print("<" + ("-" * loading) + " " * (seconds-loading) + ">" + str(percent) + "%")
    print("\n")
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

error = "\n Told you to type in a number betwenn 1 to 10"
try:                                                                          
  bet=float(input(" How much money you would like to spend (1-10) >>>"))        
except ValueError:                                                         
  quit(error)

  
if bet == 1.00 or bet == 2.00 or bet == 3.0 or bet == 4.0 or bet == 5 or bet == 6 or bet == 7 or bet == 8 or bet == 9 or bet == 10:               
  while True:                        
    
    print("\nWelcome: You have %.2f dollars" % bet)          
    print("Every bet cost 1 dollor")                          
    print("Press Q or q and enter to quit the game\n")       
    customerNum = input("You ready? press enter to start >>>")   
    if customerNum == 'Q' or customerNum == 'q':             
      print("Sorry to see you go so soon")                   
      print("You won %.2f dollars" % bet)                    
      break                                                   
    bet-=1                                                    
    
  
    from random import*                                    
    animal=["zebra","horse","donkey","unicorn"]

    
  
    outcome = choice(animal)                                      
  
    time.sleep(1)
    loading_bar(10)                                         
    print("#######")
    print(outcome)                                                 
    print("#######")
    if outcome =="horse" :                                          
      print("\ncongrats, you won 50c")                     
      time.sleep(2)                                       
      bet+=0.5                                            
    if outcome =="donkey":                                           
      print("congrats, you won no money")
      time.sleep(2)
    if outcome =="zebra":
      print("congrats, you won 50c")
      time.sleep(2)
      bet+=0.5
    if outcome =="unicorn":
      print("system error, you won $5, congrats")
      time.sleep(2)
      bet+=5
    if bet < 1:
      print("You only have %.2f dollars" % bet)
     
     
      break                                                   
  print("Restart to try again")
  
else:                                                         
  print("error 1: Your bet does not meet the current requirements")
  print("Please restart the program")
  

