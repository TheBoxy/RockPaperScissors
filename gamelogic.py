from random import randrange

rock = 0
paper = 1
scissor = 2

tie = 0
user_win = 1
bot_win = 2



def create_random():
    rand = randrange(0,3)
    return rand

def rules(user,bot):
    if user == bot:
        return tie
    elif user == rock and bot == scissor:
        return user_win
    elif user == scissor and bot == paper:
        return user_win
    elif user == paper and bot == rock:
        return user_win
    else:
        return  bot_win 




