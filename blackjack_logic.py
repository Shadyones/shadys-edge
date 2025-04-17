def get_blackjack_action(player_cards, dealer_card):
    total = sum(player_cards)
    soft = 11 in player_cards and total <= 21

    explanation = ""

    # Pair splitting
    if player_cards[0] == player_cards[1]:
        pair = player_cards[0]
        if pair == 11:
            return "Split", "Always split Aces. You can't bust, and your upside is massive."
        elif pair == 8:
            return "Split", "Always split 8s. Two 8s is a hard 16, which sucks. Splitting gives you a shot to improve both hands."
        elif pair == 2 and dealer_card in [4, 5, 6, 7]:
            return "Split", "Split 2s against weak dealer upcards. Gives you a better chance to build two solid hands."

    # Soft hands
    if soft:
        if total == 18 and dealer_card in [9, 10, 11]:
            return "Hit", "Soft 18 isn't strong enough vs. high dealer cards. You need to improve it."
        elif total <= 17:
            return "Hit", "Soft totals under 18 need to be improved. Dealer still has strong drawing potential."

    # Hard totals
    if not soft:
        if total >= 17:
            return "Stand", "Hard 17 or more — you're better off chilling and letting the dealer try to bust."
        elif 13 <= total <= 16 and dealer_card <= 6:
            return "Stand", "Dealer has a weak upcard. You stand and hope they bust."
        elif total == 12 and dealer_card in [4, 5, 6]:
            return "Stand", "Standing on 12 vs. weak dealer upcards is standard — dealer likely to bust."
        elif total == 11:
            return "Double", "You have 11 — best doubling hand in the game. You’re likely to win and want more $$ on the table."
        elif total == 10 and dealer_card <= 9:
            return "Double", "Hard 10 vs. dealer's 9 or less — time to double your bet and take advantage."
        elif total == 9 and dealer_card in [3, 4, 5, 6]:
            return "Double", "Hard 9 vs. 3-6 is prime double-down territory."
        elif total <= 11:
            return "Hit", "You can't bust yet — keep improving your hand."
        else:
            return "Hit", "Too low to stand. Dealer could beat that easily."

    return "Hit", "Defaulting to hit — better than standing with a weak hand."
