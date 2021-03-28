#!/usr/bin/env python3

import json

# TODO: look into EXPERT1 set, for now users should always use the standard_legality filter


def load_card_data():
    file = open("cards.collectible.json", "r")
    data = json.load(file)
    file.close()
    return data


def display_sorted_card_data(card_data):
    for i in sorted(card_data, key=lambda card_info: (card_info['cost'], card_info['name'])):
        print('(' + str(i['cost']) + ') ' + i['name'])

def filter_card_data_by_race(card_data, race):
    return [x for x in card_data if 'race' in x and (x['race'] in [race, 'ALL'])]


def filter_card_data_by_type(card_data, type):
    return [x for x in card_data if x['type'] == type]


def filter_card_data_by_standard_legality(card_data):
    return [x for x in card_data if x['set'] in ['BLACK_TEMPLE', 'SCHOLOMANCE', 'DARKMOON_FAIRE', 'THE_BARRENS', 'CORE']]


def filter_card_data_by_class(card_data, class_name, include_neutrals=True):
    return [x for x in card_data if x['cardClass'] == class_name or
            ('classes' in x and class_name in x['classes']) or
            (include_neutrals and (not ('classes' in x) and x['cardClass'] == 'NEUTRAL'))]


def filter_card_data_by_min_cost(card_data, min_cost):
    return [x for x in card_data if x['cost'] >= min_cost]


def filter_card_data_by_max_cost(card_data, max_cost):
    return [x for x in card_data if x['cost'] <= max_cost]


my_card_data = load_card_data()

# only consider standard cards
standard_card_data = filter_card_data_by_standard_legality(my_card_data)

# filter for shaman and neutral cards first, then filter further on minions, then on cost
shaman_and_neutral_cards = filter_card_data_by_class(standard_card_data, 'SHAMAN', True)
shaman_and_neutral_minions = filter_card_data_by_type(shaman_and_neutral_cards, 'MINION')
shaman_and_neutral_cheap_minions = filter_card_data_by_max_cost(shaman_and_neutral_minions, 1)

# filter on priest cards first, then filter further on spells
priest_cards = filter_card_data_by_class(standard_card_data, 'PRIEST', False)
priest_spells = filter_card_data_by_type(priest_cards, 'SPELL')

# display the examples
display_sorted_card_data(shaman_and_neutral_cheap_minions)
print()
display_sorted_card_data(priest_spells)
