import random
from game_objects import Card


def create_card_deck(
    suits: list[str],
    rangs: list[str],
    powers: list[int]
) -> list[Card]:
    card_deck = []
    for suit in suits:
        for rang, power in zip(rangs, powers):
            card = Card(suit, rang, power)
            card_deck.append(card)
    return card_deck


def create_one_suit_standard_deck(suit: str) -> list[Card]:
    suits = [suit]
    rangs = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    powers = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    return create_card_deck(suits, rangs, powers)


def create_standard_deck() -> list[Card]:
    suits = ['♣️', '♦️', '♥️', '♠️']
    rangs = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    powers = [6, 7, 8, 9, 10, 11, 12, 13, 14]
    return create_card_deck(suits, rangs, powers)


def compare_cards_and_take(player1_deck: list[Card],
                           player2_deck: list[Card],
                           card_deck: list[Card]) -> list[int]:
    while card_deck:  # пока в колоде есть карты
        card1 = card_deck.pop()
        card2 = card_deck.pop()
        if card1 > card2:
            player1_deck.extend((card1, card2))
        elif card1 < card2:
            player2_deck.extend((card1, card2))
        else:
            print('draw')
    result = [len(player1_deck), len(player2_deck)]
    return result


def winner_is(game_result: list[int]) -> str:
    if game_result[0] > game_result[1]:
        return 'Первый игрок выиграл!'
    elif game_result[1] > game_result[0]:
        return 'Второй игрок выиграл!'
    else:
        return 'Победила дружба!'


def main() -> None:
    player1_deck = []
    player2_deck = []
    main_deck = create_standard_deck()
    random.shuffle(main_deck)
    game_result = compare_cards_and_take(player1_deck, player2_deck, main_deck)
    winner = winner_is(game_result)
    print(f'{game_result}\n{winner}')


if __name__ == '__main__':
    main()
