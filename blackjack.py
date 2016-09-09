from __future__ import print_function
import random
from IPython.display import clear_output
cards = ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'J' , 'Q' , 'K']

cards_value = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

suits = ['Heart' , 'Diamond' , 'Club' , 'Spade']

"""       Heart     Diamond     club     spades"""
    
balance = 2500

bet = 0

player_choice_options = ['double' , 'hit' , 'stand']
 
 
def player():
    name = raw_input('Enter your name ')
    return name 
    
def player_account(balance,bet,player_name):
    
    clear_output()
    print('hello %s' %(player_name))
    print('Your Balance is %s ' %(balance))
    print('Your Bet is %s ' %(bet))    

    
def player_bet(balance,bet):
    betting = True
    
    while betting:
        try:
            bet = int(raw_input('Set Bet not more than %s ' %(balance)))
            if bet>balance:
                print("Bet must be less than %s" %(balance))
                continue
        
        except ValueError:
            print('input must be a number less than %s ' %(balance))
        else:
            print('Your Bet is %s ' %(bet))
            bet_test = raw_input("sure for deal with %s, press 'y' for yes " %(bet)).lower().startswith('y')
            clear_output()
            if bet_test:
                balance = balance-bet
                return (balance ,bet)     
                """ this return balance and bet"""
            else:
                continue
    
def player_choice(options=player_choice_options):
    set_option = True    
    
    while set_option:
        try:
            choice_option = int(raw_input("Enter 1 for %s ,2 for %s ,3 for %s " %(options[0],options[1],options[2])))
            if choice_option > 3 or choice_option < 1:
                continue
        except:
            continue
        else:
            if choice_option == 1:
                
                return options[0]
            elif choice_option == 2:
                
                return options[1]
            elif choice_option == 3:
                
                return options[2]
            
            
def random_card_generator(suits,cards):
    suit_selected = random.choice(suits)
    for suit in suits:
        if suit == suit_selected:
            card_selsected = random.choice(cards)
            return {suit:card_selsected}
        else:
            continue
    
def card_checker(game_cards,generated_card,suits,cards):    
    for element in game_cards :
        if element == generated_card:
            generated_card =random_card_generator(suits,cards)
            try:
                generated_card = card_checker(game_cards,generated_card,suits,cards)
            except: 
                print('error generated')
    return generated_card
    

def player_initial_suffled(suits,cards):
    player_cards = []
    dealer_cards = []
    game_cards = []

    
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)

    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)

    player_cards.append(game_cards[0])
    player_cards.append(game_cards[1])

    dealer_cards.append(game_cards[2])
    dealer_cards.append(game_cards[3])
    
    return (player_cards,dealer_cards,game_cards)
        


def card_total(cards_in_any_side):
    num = []
    
    cards_value = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    
    total = 0
    for element in cards_in_any_side:
        for key in element:
            num_element = int(cards_value[element[key]])
            num.append(num_element)
    if len(num) == 2:
        if num.count(11) == 2:
            total = 11 + 1
        else:
            for element in num:
                total +=element
    elif len(num) > 2:
        for element in num:
            if num.count(11) >1 and element == 11:
                total = 11 +num.count(11) - 1
                continue
            else:
                total +=element
                continue
    return total
  
"""card_total([{'spade':'A'},{'Diamond': 'A'},{'Diamond': 'A'},{'Diamond': 'A'},{'Diamond': '6'}])"""
  
def replay():
    player_input = raw_input("do you want to play more. Enter y for 'Yes'").lower().startswith('y')
    return player_input



def player_card_show(player_cards , dealer_cards , player_name):
    print('%s Your cards are %s' %(player_name , [element for element in player_cards]))
    print('\ndealer cards are [%s ,{Hidden}]' %(dealer_cards[0]))
    
def double(player_cards,game_cards):
    
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    game_card_length = len(game_cards) - 1
    player_cards.append(game_cards[game_card_length])
    return (player_cards , game_cards)
    
    
def hit(player_cards,game_cards):
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    game_card_length = len(game_cards)
    game_card_length = game_card_length - 1
    player_cards.append(game_cards[game_card_length])
    return (player_cards,game_cards)

def person_card_show(cards,name=0):
    if name == 0:
        print('dealer cards are %s' %([element for element in cards]))
    else :
        print('%s ,Your cards are %s' %(name,[element for element in cards]))

def stand(player_cards,dealer_cards,player_cards_total,dealer_cards_total,name,bet,balance):
    person_card_show(dealer_cards)
    print('and')
    person_card_show(player_cards,name)
    print('\n')
    if player_cards_total == dealer_cards_total:
        print('%s, you push' %(name))
        balance = balance + bet
    elif player_cards_total < dealer_cards_total:
        print('%s, you Lost' %(name))
    elif player_cards_total > dealer_cards_total:
        print('%s, you won' %(name))
        balance = balance + bet + bet
    else:
        print('Technical error occur sorry')
        balance = balance + bet
    return (balance,bet)
        
def dealer_more_card_provider(player_cards_total, dealer_cards_total , dealer_cards , game_cards):
    dealer_smaller = True
    while dealer_smaller:
        if dealer_cards_total < 17 and player_cards_total > dealer_cards_total:
            generated_card = random_card_generator(suits,cards)
            generated_card = card_checker(game_cards,generated_card,suits,cards)
            game_cards.append(generated_card)
            game_card_length = len(game_cards)
            game_card_length = game_card_length - 1
            dealer_cards.append(game_cards[game_card_length])
            dealer_cards_total = card_total(dealer_cards)
            continue
        elif dealer_cards_total > 17:
            return (dealer_cards,game_cards)
            
def split_check(player_cards):
    num = []
    for keys in player_cards:
        for elements in keys:
            num.append(keys[elements])
    
    if num[0] == num[1]:
        return True
    else:
        return False
          
def split_ask():
    player_input = raw_input('do you want split your cards, enter y for yes').lower().startswith('y')
    return player_input
          
def check_win(dealers_cards,player_cards_one,player_name):
    player_cards_total = card_total(player_cards_one)
    player_cards_total = card_total(dealers_cards)
    
    game = True
        
    while game:
           
        if player_cards_total == 21 and player_cards_total == dealer_cards_total:
            print('%s , you are push' %(player_name))
            return 'draw'
        elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
            print('%s , you are push' %(player_name))  
            return 'draw'
        elif player_cards_total == 21 and palyer_cards_length<3:
            print('\n%s you won, it`s blackjack\n' %(player_name))
            person_card_show(dealer_cards)
            game = False
            return 'won'
            
        elif dealer_cards_total == 21:
            print('\n%s you lost,dealer get blackjack\n' %(player_name))
            person_card_show(dealer_cards)
            game = False
            return 'lose'
            
        elif player_cards_total > 21 and dealer_cards_length < 3:
            print('\n%s you are busted, dealers win\n' %(player_name))
            person_card_show(player_cards)
            print('\n')
            person_card_show(dealer_cards)
            game = False
            return 'lose'
            
        elif dealer_cards_total > 21:
            print('\n%s you won, dealer is busted\n' %(player_name))
            person_card_show(dealer_cards)
            game = False
            return 'won'
        
        else:
            player_choose = player_choice()
            if player_choose == 'double':
                player_cards , game_cards = double(player_cards,game_cards)
                
                player_cards_total = card_total(player_cards)
                dealer_cards_total = card_total(dealer_cards)
                palyer_cards_length = len(player_cards)
                dealer_cards_length = len(dealer_cards)
                
                if player_cards_total == 21 and player_cards_total == dealer_cards_total:
                    print('%s , you are push' %(player_name))
                    return 'draw'
                elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
                    print('%s , you are push' %(player_name))
                    return 'draw'
                elif player_cards_total == 21 and palyer_cards_length<3:
                    print('\n%s you won, it`s blackjack\n' %(player_name))
                    person_card_show(dealer_cards)
                    game = False
                    return 'win'
                elif dealer_cards_total == 21:
                    print('\n%s you lost,dealer get blackjack\n' %(player_name))
                    person_card_show(dealer_cards)
                    game = False
                    return 'lose'
                elif player_cards_total > 21 and dealer_cards_length < 3:
                    print('\n%s you are busted, dealers win\n' %(player_name))
                    person_card_show(player_cards)
                    print('\n')
                    person_card_show(dealer_cards)
                    game = False
                    return 'lose'
                elif dealer_cards_total > 21:
                    print('\n%s you won, dealer is busted\n' %(player_name))
                    person_card_show(dealer_cards)
                    game = False
                    return 'win'
                
                if dealer_cards_total < 17 and player_cards_total > dealer_cards_total and player_cards_total < 22:
                    dealer_cards , game_cards = dealer_more_card_provider(player_cards_total, dealer_cards_total , dealer_cards , game_cards)
                    dealer_cards_total = card_total(dealer_cards)
                    
                print(player_cards_total)
                print(dealer_cards_total)
                balance , bet = stand(player_cards,dealer_cards,player_cards_total,dealer_cards_total,player_name,bet,balance)
                game = False
                
            elif player_choose == 'hit':
                    player_cards , game_cards = hit(player_cards,game_cards)
                    person_card_show(player_cards,player_name)
                    continue
            elif player_choose == 'stand':
                if dealer_cards_total < 17 and player_cards_total > dealer_cards_total and player_cards_total < 22:
                    dealer_cards , game_cards = dealer_more_card_provider(player_cards_total, dealer_cards_total , dealer_cards , game_cards)
                    dealer_cards_total = card_total(dealer_cards)
                    
                dealer_cards_length = len(dealer_cards)
                
                if player_cards_total == 21 and player_cards_total == dealer_cards_total:
                    print('%s , you are push' %(player_name))
                    return 'draw'
                elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
                    print('%s , you are push' %(player_name))
                    return 'draw'
                elif dealer_cards_total == 21 and dealer_cards_length < 3:
                    print('\n%s you lost,dealer get blackjack\n' %(player_name))
                    person_card_show(dealer_cards)
                    game = False
                    return 'lose'
                elif dealer_cards_total > 21:
                    print('\n%s you won, dealer is busted\n' %(player_name))
                    person_card_show(dealer_cards)
                    game = False
                    return 'lose'
                person_card_show(player_cards,player_name)
                print(player_cards_total)
                print(dealer_cards_total)
                balance , bet = stand(player_cards,dealer_cards,player_cards_total,dealer_cards_total,player_name,bet,balance)
                game = False
                if player_cards_total > dealer_cards_total:
                    return 'win'
                elif player_cards_total < dealer_cards_total:
                    return 'lose'
                elif player_cards_total == dealer_cards_total:
                    return 'draw'

          
def split(player_cards,dealer_cards,game_cards,player_name,balance,bet):
    player_cards_one = player_cards[0]
    player_cards_two = player_cards[1]
    player_choice_options = ['double' , 'hit' , 'stand']
    
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    player_cards_one.append(generated_card)
    generated_card = random_card_generator(suits,cards)
    generated_card = card_checker(game_cards,generated_card,suits,cards)
    game_cards.append(generated_card)
    player_cards_two.append(generated_card)
    one_card = person_card_show(player_cards_one)
    two_card = person_card_show(player_cards_two)
    print('%s , your cards are %s , %s' %(player_name,one_card,two_card))
    print('\ndealer cards are [%s ,{Hidden}]' %(dealer_cards[0]))
    result_array = []
    result = check_win(dealers_cards,player_cards_one,player_name)
    result_array.append(result)
    
    result = check_win(dealers_cards,player_cards_two,player_name)
    result_array.append(result)
    
    if result[0] == 'win' or result[1] == 'win':
        balance = balance + bet + bet
        bet = 0
        return (balance,bet)
    elif result[0] == 'lose' or result[1] == 'lose':
        bet = 0
        return (balance,bet)
    elif result[0] == 'draw' or result[1] == 'draw':
        bet = 0
        balance = balance + bet
        return (balance,bet)
        
    
def desk(cards,cards_value,suits,balance,bet,player_choice_options):
    player_name = player()
    
    while True:
        player_cards = []
        dealer_cards = []
        game_cards = []
        player_choice_options = ['double' , 'hit' , 'stand']
        if balance <=0:
            print('%s, your balance is zero' %(player_name))
            break
        
        player_account(balance,bet,player_name)
        
        balance , bet = player_bet(balance,bet)
        player_cards , dealer_cards , game_cards = player_initial_suffled(suits,cards)
        if split_check(player_cards):
            split = split_ask()
            if split:
                player_choice_options = ['double' , 'hit' , 'stand','split']
                
            
        player_card_show(player_cards , dealer_cards , player_name)
        
        
        game = True
        
        while game:
            
            player_cards_total = card_total(player_cards)
            dealer_cards_total = card_total(dealer_cards)
            palyer_cards_length = len(player_cards)
            dealer_cards_length = len(dealer_cards)
            if player_cards_total == 21 and player_cards_total == dealer_cards_total:
                print('%s , you are push' %(player_name))
            elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
                print('%s , you are push' %(player_name))            
            elif player_cards_total == 21 and palyer_cards_length < 3:
                print('\n%s you won, it`s blackjack\n' %(player_name))
                person_card_show(dealer_cards)
                balance = balance + bet + bet
                bet = 0
                game = False
                continue
            elif dealer_cards_total == 21 and dealer_cards_length < 3:
                print('\n%s you lost,dealer get blackjack\n' %(player_name))
                person_card_show(dealer_cards)
                bet = 0
                game = False
                continue
            elif player_cards_total > 21:
                print('\n%s you are busted, dealers win\n' %(player_name))
                person_card_show(player_cards,player_name)
                print('\n')
                person_card_show(dealer_cards)
                bet = 0
                game = False
                continue
            elif dealer_cards_total > 21:
                print('\n%s you won, dealer is busted\n' %(player_name))
                person_card_show(dealer_cards)
                balance = balance + bet + bet
                bet = 0
                game = False
                continue
            
            else:
                player_choose = player_choice()
                if player_choose == 'double':
                    player_cards , game_cards = double(player_cards,game_cards)
                    
                    player_cards_total = card_total(player_cards)
                    dealer_cards_total = card_total(dealer_cards)
                    palyer_cards_length = len(player_cards)
                    dealer_cards_length = len(dealer_cards)
                    
                    if player_cards_total == 21 and player_cards_total == dealer_cards_total:
                        print('%s , you are push' %(player_name))
                    elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
                        print('%s , you are push' %(player_name))            
                    elif player_cards_total == 21 and palyer_cards_length<3:
                        print('\n%s you won, it`s blackjack\n' %(player_name))
                        person_card_show(dealer_cards)
                        balance = balance + bet + bet
                        bet = 0
                        game = False
                        continue
                    elif dealer_cards_total == 21:
                        print('\n%s you lost,dealer get blackjack\n' %(player_name))
                        person_card_show(dealer_cards)
                        bet = 0
                        game = False
                        continue
                    elif player_cards_total > 21 and dealer_cards_length < 3:
                        print('\n%s you are busted, dealers win\n' %(player_name))
                        person_card_show(player_cards)
                        print('\n')
                        person_card_show(dealer_cards)
                        bet = 0
                        game = False
                        continue
                    elif dealer_cards_total > 21:
                        print('\n%s you won, dealer is busted\n' %(player_name))
                        person_card_show(dealer_cards)
                        balance = balance + bet + bet
                        bet = 0
                        game = False
                        continue
                    
                    if dealer_cards_total < 17 and player_cards_total > dealer_cards_total and player_cards_total < 22:
                        dealer_cards , game_cards = dealer_more_card_provider(player_cards_total, dealer_cards_total , dealer_cards , game_cards)
                        dealer_cards_total = card_total(dealer_cards)
                        
                    print(player_cards_total)
                    print(dealer_cards_total)
                    balance , bet = stand(player_cards,dealer_cards,player_cards_total,dealer_cards_total,player_name,bet,balance)
                    bet = 0
                    game = False
                    
                elif player_choose == 'hit':
                        player_cards , game_cards = hit(player_cards,game_cards)
                        person_card_show(player_cards,player_name)
                        continue
                elif player_choose == 'stand':
                    if dealer_cards_total < 17 and player_cards_total > dealer_cards_total and player_cards_total < 22:
                        dealer_cards , game_cards = dealer_more_card_provider(player_cards_total, dealer_cards_total , dealer_cards , game_cards)
                        dealer_cards_total = card_total(dealer_cards)
                        
                    dealer_cards_length = len(dealer_cards)
                    
                    if player_cards_total == 21 and player_cards_total == dealer_cards_total:
                        print('%s , you are push' %(player_name))
                    elif dealer_cards_total == 21 and player_cards_total == dealer_cards_total:
                        print('%s , you are push' %(player_name))
                    elif dealer_cards_total == 21 and dealer_cards_length < 3:
                        print('\n%s you lost,dealer get blackjack\n' %(player_name))
                        person_card_show(dealer_cards)
                        bet = 0
                        game = False
                        continue
                    elif dealer_cards_total > 21:
                        print('\n%s you won, dealer is busted\n' %(player_name))
                        person_card_show(dealer_cards)
                        balance = balance + bet + bet
                        bet = 0
                        game = False
                        continue
                    person_card_show(player_cards,player_name)
                    print(player_cards_total)
                    print(dealer_cards_total)
                    balance , bet = stand(player_cards,dealer_cards,player_cards_total,dealer_cards_total,player_name,bet,balance)
                    bet = 0
                    game = False
                elif player_choose == 'split':
                    split(player_cards,dealer_cards,game_cards)

        clear_output()
        if not replay():
            break
    
    
    
desk(cards,cards_value,suits,balance,bet,player_choice_options)

        
        
        
        
        
        
        
        
        
        
        
        
        