import random
import time

cards = []
dealer = []
originaldeck = []
deck = originaldeck

# Create the deck with all the cards
for ii in ['hearts', 'clubs', 'spades', 'diamonds']:
    for i in range(2, 11):
        originaldeck.append(str(i) + " of " + str(ii))
    originaldeck.append("A of " + str(ii))


def get_card():
    r = random.choice(deck)
    deck.remove(r)
    return r


def get_total_without_A(isdealer):
    total = int()
    if isdealer:
        for card in dealer:
            if 'A' not in card[0]:
                total += get_card_number(card, isdealer)
    else:
        for card in cards:
            if 'A' not in card[0]:
                total += get_card_number(card, isdealer)
    return total


def get_card_number(card, isdealer):
    index = str()
    if '10' in card:
        index = 10
    else:
        index = card[0]
    if index == 'A':
        if get_total_without_A(isdealer) + 10 > 21:
            index = 1
        else:
            index = 10
    else:
        index = int(index)
    return index


def get_total(isdealer):
    total = int()
    if isdealer:
        for card in dealer:
            total += get_card_number(card, isdealer)
    else:
        for card in cards:
            total += get_card_number(card, isdealer)
    return total


hitting = bool()
standing = False

print("\nGame started!\n\nThe dealer is drawing a card for you...")
time.sleep(3)

newcard = get_card()
cards.append(newcard)
print("You got a " + newcard)
time.sleep(2)

print("\nThe dealer is drawing his card...")
time.sleep(3)

newcard = get_card()
dealer.append(newcard)
print("The dealer got a " + newcard)
time.sleep(1)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

print("The dealer is drawing your second card...")
time.sleep(3)

newcard = get_card()
cards.append(newcard)
print("You got a " + newcard)
time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) == 21:
    print("Blackjack on the second round! You're a natural!")
    standing = True

############
# Round 3
############

if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("\n\nThe dealer is drawing your third card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("You got a " + newcard)
    time.sleep(2)
else:
    print("\nYou chose to stand.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his third card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

###########
# Round 4
###########
if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    hitting = bool()
    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("The dealer is drawing your fourth card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("You got a " + newcard)
    time.sleep(2)
else:
    print("\n\nYou are standing.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his fourth card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

###########
# Round 5
###########
if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    hitting = bool()
    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("The dealer is drawing your fifth card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("\n\nYou got a " + newcard)
    time.sleep(2)
else:
    print("You are standing.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his fifth card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

###########
# Round 6
###########
if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    hitting = bool()
    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("The dealer is drawing your sixth card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("You got a " + newcard)
    time.sleep(2)
else:
    print("\n\nYou are standing.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his sixth card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

###########
# Round 7
###########
if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    hitting = bool()
    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("The dealer is drawing your seventh card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("You got a " + newcard)
    time.sleep(2)
else:
    print("\n\nYou are standing.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his seventh card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

###########
# Round 8
###########
if not standing:
    choice = input("Do you want to hit (h) or stand (s) ? ")
    choice = choice[0]

    hitting = bool()
    if choice.lower() == "h":
        hitting = True
    elif choice.lower() == "s":
        hitting = False
        standing = True
    else:
        if 'h' in choice.lower():
            hitting = True
        elif 's' in choice.lower():
            hitting = False
            standing = True
        else:
            print("Invalid option. Terminating program.")
            exit(0)

if hitting:
    print("The dealer is drawing your eith card...")
    time.sleep(3)

    newcard = get_card()
    cards.append(newcard)
    print("You got a " + newcard)
    time.sleep(2)
else:
    print("\n\nYou are standing.")

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(False) > 21:
    print("Game Over. You busted. Good luck next time.")
    exit(0)

if get_total(True) < 18:
    print("The dealer is drawing his eith card...")
    time.sleep(3)

    newcard = get_card()
    dealer.append(newcard)
    print("The dealer got a " + newcard)
    time.sleep(2)

print(f"\n\nYou: {get_total(False)}\nDealer: {get_total(True)}\n\n")
time.sleep(2)

if get_total(True) > 21:
    print("Game Over. The dealer busted. You won!")
    exit(0)

if get_total(True) == 17:
    if get_total(False) == 17 and standing:
        print("Game Over. The dealer had to stand. It's a tie!")
        exit(0)
    elif get_total(False) > get_total(True):
        print("Game Over. The dealer had to stand. You won!")
        exit(0)

if get_total(False) < get_total(True) and standing:
    print("Game Over. The dealer won. Good luck next time!")
    exit(0)

# More rounds are probably not needed?!

# # # #
# END #
# # # #
