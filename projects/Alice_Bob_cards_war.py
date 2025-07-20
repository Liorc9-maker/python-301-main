from __future__ import print_function, division
import random


class Card:
    """Represents a standard playing card."""

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)


class Deck:
    """Represents a deck of cards."""

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in range(4)
                      for rank in range(1, 14)]

    def __str__(self):
        return '\n'.join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for _ in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand(name)

    def has_cards(self):
        return len(self.hand.cards) > 0

    def play_card(self):
        return self.hand.pop_card(0)

    def add_cards(self, won_cards):
        self.hand.cards.extend(won_cards)

    def __str__(self):
        return f"{self.name} has {len(self.hand.cards)} cards."


def play_war(player1, player2, deck):
    # Shuffle and split the deck fairly
    deck.shuffle()
    mid = len(deck.cards) // 2
    player1.hand.cards = deck.cards[:mid]
    player2.hand.cards = deck.cards[mid:]

    round_num = 1
    while player1.has_cards() and player2.has_cards():
        print(f"\n-- Round {round_num} --")
        round_num += 1

        table_cards = []

        card1 = player1.play_card()
        card2 = player2.play_card()
        table_cards.extend([card1, card2])

        print(f"{player1.name} plays {card1}")
        print(f"{player2.name} plays {card2}")

        if card1.rank > card2.rank:
            print(f"{player1.name} wins the round.")
            player1.add_cards(table_cards)
        elif card2.rank > card1.rank:
            print(f"{player2.name} wins the round.")
            player2.add_cards(table_cards)
        else:
            print("WAR!")
            result = war_battle(player1, player2, table_cards)
            if result:
                war_winner, table_cards = result
                war_winner.add_cards(table_cards)

        print(player1)
        print(player2)

    if player1.has_cards():
        print(f"\n🏆 {player1.name} wins the game!")
    else:
        print(f"\n🏆 {player2.name} wins the game!")


def war_battle(player1, player2, war_pile):
    if len(player1.hand.cards) < 4:
        print(f"{player1.name} can't continue war. {player2.name} wins!")
        player2.add_cards(war_pile + player1.hand.cards)
        player1.hand.cards.clear()
        return None

    if len(player2.hand.cards) < 4:
        print(f"{player2.name} can't continue war. {player1.name} wins!")
        player1.add_cards(war_pile + player2.hand.cards)
        player2.hand.cards.clear()
        return None

    print("Each player puts 3 cards face-down and 1 face-up...")

    war_pile.extend([player1.play_card() for _ in range(3)])
    war_pile.extend([player2.play_card() for _ in range(3)])

    war_card1 = player1.play_card()
    war_card2 = player2.play_card()
    war_pile.extend([war_card1, war_card2])

    print(f"{player1.name} plays {war_card1} for war")
    print(f"{player2.name} plays {war_card2} for war")

    if war_card1.rank > war_card2.rank:
        print(f"{player1.name} wins the war!")
        return player1, war_pile
    elif war_card2.rank > war_card1.rank:
        print(f"{player2.name} wins the war!")
        return player2, war_pile
    else:
        print("Another war!")
        return war_battle(player1, player2, war_pile)


# --- Run the Game ---
if __name__ == '__main__':
    deck = Deck()
    player1 = Player("Alice")
    player2 = Player("Bob")
    play_war(player1, player2, deck)
