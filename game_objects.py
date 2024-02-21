class Card():
    def __init__(self, suit: str, rang: str, power: int) -> None:
        self.suit = suit
        self.rang = rang
        self.power = power

    def __gt__(self, other):
        return self.power > other.power


if __name__ == '__main__':
    eight_heart = Card('♥️', '8', 8)
    queen_clubs = Card('♣️', 'Q', 12)

    print(queen_clubs > eight_heart)
    print(queen_clubs < eight_heart)
