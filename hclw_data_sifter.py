import json
import matplotlib.pyplot as plt
import numpy as np

#this will do stuff like graph the data, show the average length, etc
def get_data():
    hclw_chapters_txt = open("hclw_chapters.txt","r")
    raw_data_arr = hclw_chapters_txt.readlines()
    return raw_data_arr

def get_average_len(data_arr):
    total = 0
    sum_of_lengths = 0
    for data in data_arr:
        data = json.loads(data)
        total += 1
        sum_of_lengths += data['length']
    return sum_of_lengths/total

def get_stats(data_arr):
    stats = {
        'longest': {
            'name': '',
            'length': 0
        },
        'shortest': {
            'name': '',
            'length': json.loads(data_arr[0])['length']
        }
    }
    
    for data in data_arr:
        data = json.loads(data)
        if data['length'] > stats['longest']['length']:
            stats['longest']['length'] = data['length']
            stats['longest']['name'] = data['name'] 
        if data['length'] < stats['shortest']['length']:
            stats['shortest']['length'] = data['length']
            stats['shortest']['name'] = data['name'] 
    return stats


def plot_data(data_arr):
    fig, ax = plt.subplots()
    labels = []
    lengths = []
    ax.legend()
    for data in data_arr:
        labels.append(data_arr.index(data) + 1)
        data = json.loads(data)
        lengths.append(data['length']/1000)
        
    ax.set_ylabel('Chapter Length(1000px)')
    ax.set_xlabel('Chapter Number')
    plt.xticks(rotation=90)
    ax.set_title('HCLW Chapter Length Bar Graph')
    ax.bar(labels,lengths)
    plt.show()

def get_arcs_data(data_arr):
    return [
        { 'name': 'reset', 'arc_arr': data_arr[:6] },
        { 'name': 'dungeon_of_black_magic', 'arc_arr': data_arr[6:12] },
        { 'name': 'leaf_dungeon', 'arc_arr': data_arr[12:21] },
        { 'name': 'personal_attribute', 'arc_arr': data_arr[21:25] },
        { 'name': 'combat_tournament_prelude', 'arc_arr': data_arr[25:28] },
        { 'name': 'preliminary_round', 'arc_arr': data_arr[28:35] },
        { 'name': 'subjagation_round', 'arc_arr': data_arr[35:50] },
        { 'name': 'zara_guild', 'arc_arr': data_arr[50:57] },
        { 'name': 'hohoian', 'arc_arr': data_arr[57:61] },
        { 'name': 'undead_in_cobalt_castle', 'arc_arr': data_arr[61:67] },
        { 'name': 'seige_round_prelude', 'arc_arr': data_arr[67:74] },
        { 'name': 'genisis', 'arc_arr': data_arr[74:77] },
        { 'name': 'seige_round', 'arc_arr': data_arr[77:87] },
        { 'name': 'pooh_upooh_retrieval', 'arc_arr': data_arr[87:98] },
        { 'name': 'dark_birthday', 'arc_arr': data_arr[98:109] },
        { 'name': 'post_dark_birthday', 'arc_arr': data_arr[109:117] },
        { 'name': 'pvp_round_prelude', 'arc_arr': data_arr[117:123] },
        { 'name': 'pvp_round_quarterfinals', 'arc_arr': data_arr[123:136] },
        { 'name': 'trial_of_a_dragon', 'arc_arr': data_arr[136:143] },
        { 'name': 'pvp_round_semifinals', 'arc_arr': data_arr[143:159] },
        { 'name': 'escape_from_seoul', 'arc_arr': data_arr[159:163] },
        { 'name': 'pvp_round_final', 'arc_arr': data_arr[163:168] },
        { 'name': 'ragnarok', 'arc_arr': data_arr[168:174] },
        { 'name': 'exodus', 'arc_arr': data_arr[174:176] },
        { 'name': 'after_episode', 'arc_arr': data_arr[176:183] },
        { 'name': 'reunion', 'arc_arr': data_arr[183:187] },
        { 'name': 'sleep_walking', 'arc_arr': data_arr[187:191] },
        { 'name': 'lucid_adventure', 'arc_arr': data_arr[192:199] },
        { 'name': 'dark', 'arc_arr': data_arr[199:205] },
        { 'name': 'finding_the_lucky_coin_pieces', 'arc_arr': data_arr[205:213] },
        { 'name': 'summit', 'arc_arr': data_arr[213:222] },
        { 'name': 'the_great_war_begins', 'arc_arr': data_arr[222:228] },
        { 'name': 'beyond_the_boundary', 'arc_arr': data_arr[228:241] },
        { 'name': 'demon_world_prelude', 'arc_arr': data_arr[241:244] },
        { 'name': 'demon_world', 'arc_arr': data_arr[244:253] },
        { 'name': 'advent_of_the_demon_king', 'arc_arr': data_arr[253:262] },
        { 'name': 'retribution', 'arc_arr': data_arr[262:269] },
        { 'name': 'current', 'arc_arr': data_arr[269:272] },
    ]

def plot_arcs(arcs_arr):
    fig, ax = plt.subplots()
    labels = []
    lengths = []
    ax.legend()
    ax.set_ylabel('Arc Length(10000px)')
    plt.xticks(rotation=90)
    ax.set_title('HCLW Arc Length Bar Graph')
    for arc in arcs_arr:
        labels.append(arc['name'])
        arc_length_sum = 0
        for chapter in arc['arc_arr']:
            chapter = json.loads(chapter)
            arc_length_sum += chapter['length']
        lengths.append(arc_length_sum/10000)
    ax.bar(labels,lengths)
    plt.show()

if __name__ == "__main__":
    data = get_data()
    arcs_data = get_arcs_data(data)
    average = get_average_len(data)
    stats = get_stats(data)
    plot_data(data)
    plot_arcs(arcs_data)
