import random

#defines global variables
global collection_cards
global priority_list
global player_name
global player_cards
global bot1_cards
global bot2_cards
global bot3_cards
global winner

final_list = []

#defines priority order of cards
def prior_arrange(lis):
    j = []
    for k in priority_list:
        for i in lis:
            if i[1:] == k:
                j.append(i)
    return j

#defines calls of bots
def call_bots(lis):
    call = 0
    for i in lis:
        if i[1] == 'A' or i[1] == 'K' or i[1] == 'Q' or i[1] == 'J':
            call = call+1
    return call

#defines winner_cards
def win_cards(): 
    if winner == 'bot1':
        return bot1_cards
    elif winner == 'bot2':
        return bot2_cards
    elif winner == 'bot3':
        return bot3_cards

#defines card selection for winners
def card_selection_winner():
    x = win_cards()
    if winner != player_name:
        y = x.pop(0)
        return y

#defines card selection for non winners:
def card_selection_nonWinner():
    response = {}
    z = card_selection_winner()
    if winner == 'bot1':
        response['bot1'] = z
        print('bot1->', z)
        
        for i in bot2_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot2'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot2_cards:
                        if j[0] == z[0]:
                            response['bot2'] = j 
                    break
			
            else:
                response['bot2'] = i
        print('bot2->',response['bot2'])
        bot2_cards.remove(response['bot2'])

        inp2 = input('Play your card ')
        if inp2 in player_cards:
            response[player_name] = inp2
            print(f'{player_name}->{response[player_name]}')
            player_cards.remove(inp2)
        else:
            print('Enter valid card!!!')
        

        for i in bot3_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot3'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot3_cards:
                        if j[0] == z[0]:
                            response['bot3'] = j
                    break
			
            else:
                response['bot3'] = i
        print('bot3->',response['bot3'])
        bot3_cards.remove(response['bot3'])
    
    if winner == 'bot2':
        response['bot2'] = z
        print('bot2->', z)
 
        inp2 = input('Play your card ')
        if inp2 in player_cards:
            response[player_name] = inp2
            print(f'{player_name}->{response[player_name]}')
            player_cards.remove(inp2)
        else:
            print('Enter valid card!!!')

        for i in bot3_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot3'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot3_cards:
                        if j[0] == z[0]:
                            response['bot3'] = j
                    break
			
            else:
                response['bot3'] = i
        print('bot3->',response['bot3'])
        bot3_cards.remove(response['bot3'])
        
        for i in bot1_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot1'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot1_cards:
                        if j[0] == z[0]:
                            response['bot1'] = j
                    break
			
            else:
                response['bot1'] = i
        print('bot1->', response['bot1'])
        bot1_cards.remove(response['bot1'])
    
    if winner == player_name:
        inp2 = input('Play your card ')
        if inp2 in player_cards:
            response[player_name] = inp2
            print(f'{player_name}->{response[player_name]}')
            player_cards.remove(inp2)
        else:
            print('Enter valid card!!!')
        
        for i in bot3_cards:
            if i[0] == response[player_name][0]: 
                if priority_list.index(i[1:]) < priority_list.index(response[player_name][1:]):
                    response['bot3'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(response[player_name][1:]):
                    for j in bot3_cards:
                        if j[0] == response[player_name][0]:
                            response['bot3'] = j
                    break
			
            else:
                response['bot3'] = i
        print('bot3->',response['bot3'])
        bot3_cards.remove(response['bot3'])

       	for i in bot1_cards:
            if i[0] == response[player_name][0]: 
                if priority_list.index(i[1:]) < priority_list.index(response[player_name][1:]):
                    response['bot1'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(response[player_name][1:]):
                    for j in bot1_cards:
                        if j[0] == response[player_name][0]:
                            response['bot1'] = j
                    break
			
            else:
                response['bot1'] = i
        print('bot1->', response['bot1'])
        bot1_cards.remove(response['bot1'])
        
        for i in bot2_cards:
            if i[0] == response[player_name][0]: 
                if priority_list.index(i[1:]) < priority_list.index(response[player_name][1:]):
                    response['bot2'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(response[player_name][1:]):
                    for j in bot2_cards:
                        if j[0] == response[player_name][0]:
                            response['bot2'] = j 
                    break
			
            else:
                response['bot2'] = i
        print('bot2->',response['bot2'])
        bot2_cards.remove(response['bot2'])

    if winner == 'bot3':  
        response['bot3'] = z
        print('bot3->', z)
        
        for i in bot1_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot1'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot1_cards:
                        if j[0] == z[0]:
                            response['bot1'] = j
                    break
			
            else:
                response['bot1'] = i
        print('bot1->', response['bot1'])
        bot1_cards.remove(response['bot1'])

        for i in bot2_cards:
            if i[0] == z[0]: 
                if priority_list.index(i[1:]) < priority_list.index(z[1:]):
                    response['bot2'] = i
                    break
                elif priority_list.index(i[1:]) >= priority_list.index(z[1:]):
                    for j in bot2_cards:
                        if j[0] == z[0]:
                            response['bot2'] = j 
                    break
			
            else:
                response['bot2'] = i
        print('bot2->',response['bot2'])
        bot2_cards.remove(response['bot2'])

        inp2 = input('Play your card ')
        if inp2 in player_cards:
            response[player_name] = inp2
            print(f'{player_name}->{response[player_name]}')
            player_cards.remove(inp2)
        else:
            print('Enter valid card!!!')
    return response

#takes player inputs
player_name = input("Enter your name ")
print('\nHello', player_name, '\nLet\'s get started!\n')   

#beginning of a while loop to define one complete game        
while True:
    collection_cards = ['HA','HK','HQ','HJ','H10','H9','H8','H7','H6','H5','H4','H3','H2','SA','SK','SQ','SJ','S10','S9','S8','S7','S6','S5','S4','S3','S2','DA','DK','DQ','DJ','D10','D9','D8','D7','D6','D5','D4','D3','D2','CA','CK','CQ','CJ','C10','C9','C8','C7','C6','C5','C4','C3','C2']
    priority_list = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    
    #for file data reading
    file= open('input_file.txt', 'r')
    lines = file.readlines()
    file.close()
    
    #asks for file input or random distribution of cards
    inp = input("Enter 'F' to read data from file or 'R' for random distribution of cards ")
    if inp.lower() == 'f':
        collection_cards_copy = lines[6][:-1].split(',')
        player_cards = collection_cards_copy[0:13]
    elif inp.lower() == 'r':
        #shuffles cards
        collection_cards_copy = collection_cards[:]
        random.shuffle(collection_cards_copy)
        player_cards = prior_arrange(collection_cards_copy[0:13])
    
    copy2 = collection_cards_copy[:]
    bot1_cards_copy = copy2[13:26]
    bot2_cards_copy = copy2[26:39]
    bot3_cards_copy = copy2[39:53]

    #distribution of shuffled cards
    bot1_cards = prior_arrange(collection_cards_copy[13:26])
    bot2_cards = prior_arrange(collection_cards_copy[26:39])
    bot3_cards = prior_arrange(collection_cards_copy[39:53])
    
    print('\nYour cards are', player_cards)

    #Takes user call 
    player_call = int(input('\nEnter your call(number of times you can possibly win) '))

    #prints the call of each player
    print(f'calls of players bot1->{call_bots(bot1_cards)},bot2->{call_bots(bot2_cards)},bot3->{call_bots(bot3_cards)},{player_name}->{player_call}\n')
    
    players = ['bot1', 'bot2', player_name, 'bot3']
    players_copy = players[:]
    
    #generates seating arrangement and decides the player to start the game
    inp0 = input("Enter 'F' to read data from file or 'R' for random seating arrangement ") 
    if inp0.lower() == 'f':
        print()
        print(lines[9][:-1])
        winner = lines[12]
    elif inp0.lower() == 'r':
        random.shuffle(players_copy)
        print(f'\ncyclic order {players_copy[0]}->{players_copy[1]}->{players_copy[2]}->{players_copy[3]}->{players_copy[0]}........')
        winner = players_copy[0]

    print('\nGame starts from ',winner)
    winner_list = []
    
    #defines turns
    for i in range(1, 14):
        print(f'\nTurn{i}')
        print('Your cards are ',player_cards)
        dict = card_selection_nonWinner()
        
        #decides winner of each round
        for j, k  in dict.items():
            if k[0] == dict[winner][0]:
                if priority_list.index(k[1:])<priority_list.index(dict[winner][1:]):
                    winner = j
            else:
                winner = winner
        print()
        print(winner+' wins')
        winner_list.append(winner)
    
    #prints the score for the round
    score_dict = {}
    print('\nscores:')
    if call_bots(bot1_cards_copy)>winner_list.count('bot1'):
        scoreBot1 = -10*(call_bots(bot1_cards_copy))
        score_dict['bot1'] = scoreBot1
    else:
        scoreBot1 = 10*(call_bots(bot1_cards_copy))+(winner_list.count('bot1')-call_bots(bot1_cards_copy))
        score_dict['bot1'] = scoreBot1
    print('bot1 = ',scoreBot1)

    if call_bots(bot2_cards_copy)>winner_list.count('bot2'):
        scoreBot2 = -10*(call_bots(bot2_cards_copy))
        score_dict['bot2'] = scoreBot2
    else:
        scoreBot2 = 10*(call_bots(bot2_cards_copy))+(winner_list.count('bot2')-call_bots(bot2_cards_copy))
        score_dict['bot2'] = scoreBot2
    print('bot2 = ',scoreBot2)

    if call_bots(bot3_cards_copy)>winner_list.count('bot3'):
        scoreBot3 = -10*(call_bots(bot3_cards_copy))
        score_dict['bot3'] = scoreBot3
    else:
        scoreBot3 = 10*(call_bots(bot3_cards_copy))+(winner_list.count('bot3')-call_bots(bot3_cards_copy))
        score_dict['bot3'] = scoreBot3
    print('bot3 = ',scoreBot3)

    if player_call>winner_list.count(player_name):
        scorePlayer = -10*(player_call)
        score_dict[player_name] = scorePlayer
    else:
        scorePlayer = 10*(player_call)+(winner_list.count(player_name)-(player_call))
        score_dict[player_name] = scorePlayer
    print(f'{player_name} = {scorePlayer}')
    
    #displays the winner of each round
    score_list = []
    for j, k in score_dict.items():
        score_list.append(k)
    def GetKey(val):
        for key, value in score_dict.items():
            if val == value:
                return key        
    x = max(score_list)
    print(f'\n{GetKey(x)} is the winner!!!!!!!')

    final_list.append(score_dict)
    
    #asks the user to continue/quit
    inp3 = input('\nContinue(Y/N): ')
    if inp3.lower() == 'y':
        print('-'*50)
        continue
    else:
        print("Thanks for playing!!!")
        break

#prints final scores of players
final_dict = {}
print('\nTotal scores:')

sum1 = 0
for i in range(len(final_list)):
    sum1 += final_list[i][player_name]
final_dict[player_name] = sum1
print(f'{player_name}->{sum1}')    

sum2 = 0
for i in range(len(final_list)):
    sum2 += final_list[i]['bot1']
final_dict['bot1'] = sum2
print(f'bot1->{sum2}') 

sum3 = 0
for i in range(len(final_list)):
    sum3 += final_list[i]['bot2']
final_dict['bot2'] = sum3
print(f'bot2->{sum3}') 

sum4 = 0
for i in range(len(final_list)):
    sum4 += final_list[i]['bot3']
final_dict['bot3'] = sum4
print(f'bot3->{sum4}') 

#decides the final winner
max = player_name
for j, k in final_dict.items():
    if k > final_dict.get(max):
        max = j
    else:
        max = max

#displays the final winner of the series
print('\nCongrats!!!'+max+' wins the series.')
print('Thanks for playing.')
print('='*50)