import random
print("ROCK, PAPER, SCISSOR GAME")
user_score=0
computer_score=0

def winner(user,computer):
    if computer==user:
        print("It's a Tie!")
    elif (computer=='rock' and user=='scissors')or(computer=='scissors' and user=='paper')or(computer=='paper' and user=='rock'):
        print("you lose!")
        global computer_score
        computer_score += 1
    elif (user=='rock' and computer=='scissors')or(user=='scissors' and computer=='paper')or(user=='paper' and computer=='rock'):
        print("you win!")
        global user_score
        user_score += 1
    
def game():
    
    while True:
        print("Choose one: rock ,paper,scissors")
        
        #u=user choice, c= computer choice
        u=input("Choose an option from above:").lower()
        if u not in ['rock','paper','scissors']:
            print("Invalid choice..\nEnter valid choice from choices given..")
            continue
        c=random.choice(['rock','paper','scissors'])
        print("user choice:",u)
        print("computer choice:",c)
        winner(u,c)
        print("user score:",user_score,"computer score:",computer_score)
        play_again =input("Do you want to play again? (YES /NO):").lower()
        if play_again != 'yes':
            break
game()
        
        
