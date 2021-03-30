#!/usr/bin/env python3

import json


def load_card_data():
    file = open("cards.collectible.json", "r")
    data = json.load(file)
    file.close()
    return data


def display_sorted_card_data(card_data):
    for i in sorted(card_data, key=lambda card_info: (card_info['cost'], card_info['name'])):
        print('(' + str(i['cost']) + ') ' + i['name'])
    print()


# filter by minion tribe, race can be 'ALL', 'BEAST', 'DEMON', 'DRAGON', 'ELEMENTAL', 'MECHANICAL', 'MURLOC', 'PIRATE' or 'TOTEM'
def filter_card_data_by_race(card_data, race):
    return [x for x in card_data if 'race' in x and (x['race'] in [race, 'ALL'])]


# filter by card type, type can be 'HERO', 'MINION', 'SPELL' or 'WEAPON'
def filter_card_data_by_type(card_data, type):
    return [x for x in card_data if x['type'] == type]


# filter by standard legality in Forged of the Barrens, users should always use this until I have looked into EXPERT1 set
def filter_card_data_by_standard_legality(card_data):
    return [x for x in card_data if x['set'] in ['BLACK_TEMPLE', 'SCHOLOMANCE', 'DARKMOON_FAIRE', 'THE_BARRENS', 'CORE']]


def filter_card_data_by_class(card_data, class_name, include_neutrals=True):
    return [x for x in card_data if x['cardClass'] == class_name or
            ('classes' in x and class_name in x['classes']) or
            (include_neutrals and (not ('classes' in x) and x['cardClass'] == 'NEUTRAL'))]


# filter by mana cost
def filter_card_data_by_min_cost(card_data, min_cost):
    return [x for x in card_data if x['cost'] >= min_cost]


def filter_card_data_by_max_cost(card_data, max_cost):
    return [x for x in card_data if x['cost'] <= max_cost]


# filter by Mean Streets of Gadgetzan tri-classes, tri_class can be 'GRIMY_GOONS', 'JADE_LOTUS' or 'KABAL'
def filter_card_data_by_tri_class(card_data, tri_class):
    return [x for x in card_data if 'multiClassGroup' in x and x['multiClassGroup'] == tri_class]


# just used for Keywarden Ivory pool, for now
def filter_card_data_by_dual_class(card_data):
    return [x for x in card_data if 'multiClassGroup' in x and not x['multiClassGroup'] in ['GRIMY_GOONS', 'JADE_LOTUS', 'KABAL']]


# filter by mechanics, mechanic can be:
#   AFFECTED_BY_SPELL_POWER (spells that don't deal a set amount of damage but do scale with Spell Damage)
#   AURA
#   BATTLECRY
#   CANT_ATTACK
#   CANT_BE_TARGETED_BY_HERO_POWERS
#   CANT_BE_TARGETED_BY_SPELLS
#   CHARGE
#   CHOOSE_ONE
#   COMBO
#   CORRUPT
#   DEATHRATTLE
#   DISCOVER
#   DIVINE_SHIELD
#   ECHO
#   ENRAGED ("while damaged")
#   FREEZE
#   FRENZY
#   HEROPOWER_DAMAGE
#   ImmuneToSpellpower (spells that scale abnormally with Spell Damage, e.g. Arcane Missiles)
#   INSPIRE
#   InvisibleDeathrattle (mostly "If you discard this, " effects)
#   LIFESTEAL
#   OUTCAST
#   OVERKILL
#   OVERLOAD
#   POISONOUS
#   QUEST
#   REBORN
#   RUSH
#   SECRET
#   SILENCE
#   SPELLBURST
#   SPELLPOWER
#   START_OF_GAME
#   STEALTH
#   TAUNT
#   TOPDECK ("When you draw this, " effects)
#   TRIGGER_VISUAL (grab bag of other triggered effects that have animations)
#   TWINSPELL
#   WINDFURY
def filter_card_data_by_mechanic(card_data, mechanic):
    return [x for x in card_data if 'mechanics' in x and mechanic in x['mechanics']]


# merges two filtered sets, doesn't eliminate potential duplicates, so merge wisely
def merge_card_data(card_data_left, card_data_right):
    return (card_data_left + card_data_right)


my_card_data = load_card_data()

# only consider standard cards
standard_card_data = filter_card_data_by_standard_legality(my_card_data)

# filter for shaman and neutral cards first, then filter further on minions, then on cost
shaman_and_neutral_cards = filter_card_data_by_class(
    standard_card_data, 'SHAMAN', True)
shaman_and_neutral_minions = filter_card_data_by_type(
    shaman_and_neutral_cards, 'MINION')
shaman_and_neutral_cheap_minions = filter_card_data_by_max_cost(
    shaman_and_neutral_minions, 1)

# filter on priest cards first, then filter further on spells
priest_cards = filter_card_data_by_class(standard_card_data, 'PRIEST', False)
priest_spells = filter_card_data_by_type(priest_cards, 'SPELL')

# display the examples
display_sorted_card_data(shaman_and_neutral_cheap_minions)
print()
display_sorted_card_data(priest_spells)
