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
    return [x for x in card_data if 'race' in x and (x['race'] == race or x['race'] == 'ALL')]


def filter_card_data_by_type(card_data, type):
    return [x for x in card_data if x['type'] == type]


def filter_card_data_by_standard_legality(card_data):
    return [x for x in card_data if x['set'] == 'BLACK_TEMPLE' or
            x['set'] == 'SCHOLOMANCE' or
            x['set'] == 'DARKMOON_FAIRE' or
            x['set'] == 'THE_BARRENS' or
            x['set'] == 'CORE']


def filter_card_data_by_class(card_data, class_name, include_neutrals=True):
    multi_class_groups = {}
    multi_class_groups['ROGUE'] = ['JADE_LOTUS', 'ROGUE_WARRIOR', 'MAGE_ROGUE']
    multi_class_groups['MAGE'] = ['KABAL', 'MAGE_ROGUE', 'MAGE_SHAMAN']
    multi_class_groups['SHAMAN'] = [
        'JADE_LOTUS', 'MAGE_SHAMAN', 'DRUID_SHAMAN']
    multi_class_groups['DRUID'] = [
        'JADE_LOTUS', 'DRUID_SHAMAN', 'DRUID_HUNTER']
    multi_class_groups['HUNTER'] = [
        'GRIMY_GOONS', 'DRUID_HUNTER', 'HUNTER_DEMONHUNTER']
    multi_class_groups['DEMONHUNTER'] = [
        'HUNTER_DEMONHUNTER', 'WARLOCK_DEMONHUNTER']
    multi_class_groups['WARLOCK'] = [
        'KABAL', 'WARLOCK_DEMONHUNTER', 'PRIEST_WARLOCK']
    multi_class_groups['PRIEST'] = [
        'KABAL', 'PRIEST_WARLOCK', 'PALADIN_PRIEST']
    multi_class_groups['PALADIN'] = [
        'GRIMY_GOONS', 'PALADIN_PRIEST', 'PALADIN_WARRIOR']
    multi_class_groups['WARRIOR'] = [
        'GRIMY_GOONS', 'PALADIN_WARRIOR', 'ROGUE_WARRIOR']

    return [x for x in card_data if x['cardClass'] == class_name or
            ('multiClassGroup' in x and x['multiClassGroup'] in multi_class_groups[class_name]) or
            (include_neutrals and (not 'multiClassGroup' in x and x['cardClass'] == 'NEUTRAL'))]


my_card_data = load_card_data()

# example filters
my_card_data = filter_card_data_by_standard_legality(my_card_data)
my_card_data = filter_card_data_by_class(my_card_data, 'SHAMAN', True)
my_card_data = filter_card_data_by_type(my_card_data, 'MINION')
my_card_data = filter_card_data_by_race(my_card_data, 'DRAGON')

display_sorted_card_data(my_card_data)
