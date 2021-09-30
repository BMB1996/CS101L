########################################################################
##
## CS 101 Lab
## Program 4
## Brandon Barber
## bmbct7@umsystem.edu
##
## PROBLEM : Creating a slot machine. The user inputs their bank, then a wager and tries to get matches on the reels
##           Then gets a payout depending on the number of matches
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random


def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play = input('Would you like to play again?\n')
    if play.lower() == 'y' or play.lower() == 'yes':
        return True
    else:
        return False

    return True
     
def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager_amount = int(input('How many chips would you like to wager this round?'))
    while (wager_amount < 1 or wager_amount > bank):
        wager_amount = int(input('How many chips would you like to wager this round?'))

    return wager_amount

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reela = random.randint(1,10)
    reelb = random.randint(1,10)
    reelc = random.randint(1,10)

    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb and reela == reelc):
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    starting_chips = -1
    while starting_chips < 1 or starting_chips > 100:
        starting_chips = int(input('How many chips would you like to play with?\n'))

    return starting_chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        payout = wager * 10
    elif matches == 2:
        payout = wager * 3
    else:
        payout = wager * -1
    return payout     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        chip_totals = [bank]
        round_count = 0

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            chip_totals.append(bank)
            round_count += 1
           
        print("You lost all", chip_totals[0], "in", round_count, "spins")
        print("The most chips you had was", max(chip_totals))
        playing = play_again()
