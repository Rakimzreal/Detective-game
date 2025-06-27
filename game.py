def game_intro():
    print("You're Detective Riley Stone, called to the scene of a high-profile case: the disappearance of Clara Voss, a tech CEO staying at the Verdant Hotel.A storm is rolling in. You light a cigarette and step inside.")


def hotel_room():
    print("It's spotless. Too clean. A half-burned note is in the trash. The balcony door is open.\n")

def note():
    print('''Note says: “Meet me at 3 a.m. - R” 
You check the timestamp—it's 2:45 a.m. now.\n''')
    
def roof_top():
    print("You find a dropped earring and a scratched phone. You call the last number dialed—it belongs to Clara's CFO. Suspicious. \n")

def confront_cfo():
    print(''' You storm the CFO's apartment. He's burning files when you arrive.
He tries to flee—but backup arrives just in time.
He confesses: He planned to take over Clara's company.
You recover stolen data and close the case.
✅ Case closed. Good job, detective.
''')
    
def back_to_office():
    print('''You dig deeper and discover that Clara faked her disappearance to expose illegal activity from inside.
She contacts you anonymously with a flash drive.
You help publish her findings and arrest half the board.
🔥 Secret ending unlocked: The Whistleblower.
''')
    
def press_harder():
    print('''He panics and says she left with a man in gray. You access security footage.
You get a license plate. Time to chase a new lead. 🎉 ''')

print('The Vanishing at Verdant Hotel - Extended Cut' )
play_again = 'yes'
while play_again == 'yes':
    name = input('Your name: ')
    inventory = []
    print(f'Hi {name}! Welcome to my game. Do you wanna play? (yes/no)' )
    answer = input('> ').lower().strip()
    if answer == 'yes':
        print('Game on! \n')
        game_intro()
        print('''Do you want to ?  
        1. Investigate Clara's hotel room ? 
        2. Interrogate the night clerk ?      
            ''')
        answer = input("Enter '1' or '2': ").lower().strip()
        if answer == '1':
            hotel_room()
            print('''Do you want to ?
            1. 📄 Read the note
            2. 🔍 Search the balcony
            ''')
            answer = input("Enter '1' or '2': ").lower().strip()
            if answer == '1':
                note()
                inventory.append('note')
                print('You read the note ')
                print('''Do you want to ? 
                1. 🕒 Go to the rooftop early?
                2. 👁️ Wait and watch the balcony to see who arrives?
                ''')
                answer = input("Enter '1' or '2': ").lower().strip()
                if answer == '1':
                    roof_top()
                    print('''Do you want to? 
                    1. 🚨 Confront the CFO immediately?
                    2.🧠 Return to your office to investigate quietly?
                    ''')
                    answer = input("Enter '1' or '2': ").lower().strip()
                    if answer == '1':
                        confront_cfo()
                    elif answer == '2':
                        back_to_office()
                    else:
                        print('Invalid command! ')
                elif answer == '2':
                    print('You see a shadowy figure arrive and drop something—a flash drive.')
                    print('''Do you want to? 
                        1. 💾 Grab the drive and flee?
                        2. 🥷 Follow the figure? ''')
                    answer = input("Enter '1' or '2': ").lower().strip()
                    if answer == '1':
                        inventory.append('flash drive' )
                        print(f'Inventory: {inventory}')
                        print('You examine the flash drive...')
                        print('Inside the flash drive are company secrets Clara uncovered. You expose a conspiracy. Case closed. 🎉')
                    elif answer == '2':
                        print("You lose them in the streets. You're mugged and left in an alley. Game Over.")
                    else:
                        print('Invalid command! ')
            elif answer == '2':
                print("It's slick with rain. You slip and hit your head. Fade to black.🩸 Game Over 😔")
            else:
                print("Invalid command! ")
        elif answer == '2':
            print('He seems on edge. Says Clara left at midnight.') 
            print('''Do you want to ?
                1. 🗯️ Press him harder
                2. 💵 Bribe him ''')  
            answer = input("Enter '1' or '2': ").lower().strip()   
            if answer == '1':
                press_harder()
                print('''Do you want to?
                    1. 🚗 Chase the plate at the warehouse district
                    2. ☎️ Call backup and wait ''')
                answer = input("Enter '1' or '2': ").lower().strip()
                if answer == '1':
                    print("You go solo. It's a trap. You're ambushed by thugs. Game Over. 😔")
                elif answer == '2':
                    print('You catch the CFO trying to burn evidence. Arrest made. 🎉')
                else:
                    print('Invalid command! ')
            elif answer == '2':
                print('He gives fake info. You waste hours. When you return, the real lead is gone. ❌ Game Over')
            else:
                print('Invalid command!')
        else:
            print('Invalid command! ')   
    elif answer == 'no':
        print("We're not playing...")
        quit()
    else:
        print('Invalid command! ')

    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again != 'yes':
        print('Game Over! Bye Detective. 🫡')
