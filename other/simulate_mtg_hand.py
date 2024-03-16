""" If it requires any explanation, I was a little annoyed (rage-quit) that I couldn't make it into
Top 1200 (within Mythic) in MTGA to compete professionally for this season.

In the last matches that was the final blow, I didn't get any 'sweepers' in 8 games out of 10 while playing a control
deck against "aggressive" decks.
    - 'Control' decks generally have powerful cards, but have slow build-up curve.
    - 'Aggressive' decks summon a lot of cheap creatures early on in the game.
So it's important that control decks draw up sweepers to respond to aggressive decks.

Note:
    - I've discounted match-ups against control decks, but they weren't frequent in that 10

I believe I can solve this statistically, but like there was any excuse to write up a program that simulates my
favourite game (at the time) After this, I stopped MTGA, which probably is better for my career and wallet.
"""
import re
from dataclasses import dataclass
from random import randint


class Deck:
	def __init__(self):
		self.companion = None
		self.card_entries = []

	def total_card_count(self):
		return sum(entry.count for entry in self.card_entries)

	def __str__(self):
		string = ''
		if self.companion is not None:
			string += 'Companion\n'
			string += str(DeckEntry(1, self.companion)) + '\n\n'

		string += 'Deck\n'
		for deck_entry in self.card_entries:
			string += str(deck_entry) + '\n'

		return string

	def card_at(self, index):
		cumulative_count = 0
		for entry in self.card_entries:
			cumulative_count += entry.count
			if cumulative_count >= index:
				return entry.card

		return self.card_entries[-1].card


class Card:
	def __init__(self, display_text, expansion_code, id_within_set):
		self.display_text = display_text
		self.expansion_code = expansion_code
		self.id_within_set = id_within_set

	def id(self):
		return f'{self.expansion_code}::' + str(self.id_within_set)

	def __str__(self):
		return f'{self.display_text} ({self.expansion_code}) {self.id_within_set}'


@dataclass
class DeckEntry:
	count: int
	card: Card

	def __str__(self):
		return f'{self.count} {self.card}'


def read_input(filename='mtg_sultai_ultimatum_deck.txt'):
	with open(filename) as input_file:
		lines = input_file.readlines()
		mode = None

		raw_data = {}
		for line in lines:
			processed_line = line.lower().strip('\n')
			if processed_line in ('companion', 'deck', 'sideboard'):
				mode = processed_line
				raw_data[mode] = []

			if matched := re.match(r'(\d) (.*) \((.*)\) (\d*)', line):
				card = Card(matched.group(2), matched.group(3), int(matched.group(4)))
				entry = DeckEntry(int(matched.group(1)), card)

				assert mode is not None, f'Mode cannot be None: Line={line}'
				raw_data[mode].append(entry)

	deck = Deck()
	if raw_data['companion']:
		deck.companion = raw_data['companion'][0].card

	for entry in raw_data['deck']:
		deck.card_entries.append(entry)

	return deck


def generate_random_hand(deck: Deck, count=7):
	random_numbers = set()
	while len(random_numbers) < count:
		random_numbers.add(randint(0, deck.total_card_count()))

	return [deck.card_at(random_number) for random_number in random_numbers]


def simulate_card(number_of_matches=10, card_indices=(8, 13), time_mulligan=1):
	deck = read_input()
	desired_cards = [deck.card_entries[index].card for index in card_indices]
	print('These are the cards we are simulating')
	print(list(map(str, desired_cards)))

	desired_ids = set(map(Card.id, desired_cards))
	good_match_count = 0

	for match_index in range(number_of_matches):
		print(f'\nMatch {match_index}')

		for hand_count in range(1, time_mulligan + 2):
			hand = generate_random_hand(deck)
			if any(card.id() in desired_ids for card in hand):
				print(f'Golden hand::{list(map(str, hand))}')
				good_match_count += 1
				break
			else:
				print(f'Mulligan {hand_count}::{list(map(str, hand))}')
		else:
			print('Tough Luck man')

	print(f'\nGood Match Count = {good_match_count}')
	return number_of_matches, good_match_count


def single_run():
	deck = read_input()
	shadows_verdict = deck.card_entries[8].card
	extinction_event = deck.card_entries[13].card

	were_cards_desired_in_hand = False

	for _ in range(3):
		hand = generate_random_hand(deck)
		print(list(map(str, hand)))

		if any(card.id() in (shadows_verdict.id(), extinction_event.id()) for card in hand):
			were_cards_desired_in_hand = True

	print()
	if were_cards_desired_in_hand:
		print('You were right - it should have been in there')
	else:
		print('Sorry, RNG says no')


def simulate_n_times(n=100):
	for _ in range(n):
		number_of_matches, good_match_count = simulate_card()


def run():
	simulate_n_times()


if __name__ == '__main__':
	run()
