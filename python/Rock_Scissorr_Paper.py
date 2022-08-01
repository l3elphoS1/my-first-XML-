def paoying():
    while True:
    ## input random choice 
        import random
        bot_hand = ['rock', 'scissor', 'paper']
        ran_bot_hand = random.choice(bot_hand)

    ## user hand
        hand = ['rock', 'scissor', 'paper']
        user_hand = input(f"select you hand{hand}")
        
        print(f"user: {user_hand}")
        print(f"bot: {ran_bot_hand}")

        if user_hand == ran_bot_hand:
            print("Draw!")
        elif user_hand == 'rock' and ran_bot_hand == 'scissor':
            return "You win!"
        elif user_hand == 'rock' and ran_bot_hand == 'paper':
            return "You lose!"
        elif user_hand == 'scissor' and ran_bot_hand == 'paper':
            return "You win!"
        elif user_hand == 'scissor' and ran_bot_hand == 'rock':
            return "You lose!"
        elif user_hand == 'paper' and ran_bot_hand == 'rock':
            return "You win!"
        elif user_hand == 'paper' and ran_bot_hand == 'scissor':
            return "You lose!"
        elif user_hand == "quit":
            return "Thank you for playing!"
            break
            
