def get_blackjack_action(player_cards, dealer_card):
    player_cards = [10 if x in [11, 12, 13] else x for x in player_cards]
    dealer_card = 10 if dealer_card in [11, 12, 13] else dealer_card

    if player_cards[0] == player_cards[1]:
        return pair_strategy(player_cards[0], dealer_card)

    if 11 in player_cards:
        other_card = sum(player_cards) - 11
        if other_card <= 10:
            return soft_strategy(11 + other_card, dealer_card)

    return hard_strategy(sum(player_cards), dealer_card)

def hard_strategy(player_total, dealer_card):
    if player_total <= 8:
        return 'Hit'
    if player_total == 9:
        return 'Double' if 3 <= dealer_card <= 6 else 'Hit'
    if player_total == 10:
        return 'Double' if 2 <= dealer_card <= 9 else 'Hit'
    if player_total == 11:
        return 'Double' if dealer_card != 11 else 'Hit'
    if player_total == 12:
        return 'Stand' if 4 <= dealer_card <= 6 else 'Hit'
    if 13 <= player_total <= 16:
        return 'Stand' if 2 <= dealer_card <= 6 else 'Hit'
    if player_total >= 17:
        return 'Stand'

def soft_strategy(soft_total, dealer_card):
    if soft_total <= 17:
        return 'Hit'
    if soft_total == 18:
        if dealer_card in [2, 7, 8]:
            return 'Stand'
        elif 3 <= dealer_card <= 6:
            return 'Double'
        else:
            return 'Hit'
    if soft_total >= 19:
        return 'Stand'

def pair_strategy(card_value, dealer_card):
    if card_value == 11:  # AA
        return 'Split'
    if card_value == 10:
        return 'Stand'
    if card_value == 9:
        if dealer_card in [2, 3, 4, 5, 6, 8, 9]:
            return 'Split'
        else:
            return 'Stand'
    if card_value == 8:
        return 'Split'
    if card_value == 7:
        return 'Split' if dealer_card <= 7 else 'Hit'
    if card_value == 6:
        return 'Split' if 2 <= dealer_card <= 6 else 'Hit'
    if card_value == 5:
        return hard_strategy(10, dealer_card)
    if card_value == 4:
        return 'Split' if dealer_card in [5, 6] else 'Hit'
    if card_value in [2, 3]:
        return 'Split' if 2 <= dealer_card <= 7 else 'Hit'
