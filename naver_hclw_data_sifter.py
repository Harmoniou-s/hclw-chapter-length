import json
import matplotlib.pyplot as plt
import numpy as np
import random
import codecs

#this will do stuff like graph the data, show the average length, etc
def get_data():
    naver_hclw_chapters_txt = open("naver_hclw_chapters.txt","r", encoding="utf-16")
    raw_data_arr = naver_hclw_chapters_txt.readlines()
    return raw_data_arr

def get_stats(data_arr):
    naver_hclw_stats_txt = open("naver_hclw_stats.txt","w", encoding="utf-16")
    total_chapters = 0
    sum_of_lengths = 0
    sum_of_participation = 0
    sum_of_comments = 0
    for data in data_arr:
        data = json.loads(data)
        total_chapters += 1
        sum_of_lengths += data['length']
        sum_of_participation += int(data['participation'])
        sum_of_comments += data['comments']
    
    stats = {
        'longest': {
            'name': '',
            'length': 0
        },
        'shortest': {
            'name': '',
            'length': json.loads(data_arr[0])['length']
        },
        'average_length': sum_of_lengths/total_chapters,
        'average_participation': sum_of_participation/total_chapters,
        'average_comments': sum_of_comments/total_chapters,
    }
    
    for data in data_arr:
        data = json.loads(data)
        if data['length'] > stats['longest']['length']:
            stats['longest']['length'] = data['length']
            stats['longest']['name'] = data['name'] 
        if data['length'] < stats['shortest']['length']:
            stats['shortest']['length'] = data['length']
            stats['shortest']['name'] = data['name'] 
    naver_hclw_stats_txt.write(str(stats))


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

def plot_participation(data_arr):
    fig, ax = plt.subplots()
    labels = []
    lengths = []
    ax.legend()
    for data in data_arr:
        labels.append(data_arr.index(data) + 1)
        data = json.loads(data)
        lengths.append(int(data['participation']))
        
    ax.set_ylabel('Chapter participation Count')
    ax.set_xlabel('Chapter Number')
    plt.xticks(rotation=90)
    ax.set_title('HCLW Chapter participation Bar Graph')
    ax.bar(labels,lengths)
    plt.show()

def plot_comments(data_arr):
    fig, ax = plt.subplots()
    labels = []
    lengths = []
    ax.legend()
    for data in data_arr:
        labels.append(data_arr.index(data) + 1)
        data = json.loads(data)
        lengths.append(data['comments'])
        
    ax.set_ylabel('Chapter Comment Count')
    ax.set_xlabel('Chapter Number')
    plt.xticks(rotation=90)
    ax.set_title('HCLW Chapter Comments Bar Graph')
    ax.bar(labels,lengths)
    plt.show()

def get_arcs_data(data_arr):
    return [
        { 'name': 'reset', 'arc_arr': data_arr[:6], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'dungeon_of_black_magic', 'arc_arr': data_arr[6:12], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'leaf_dungeon', 'arc_arr': data_arr[12:21], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'personal_attribute', 'arc_arr': data_arr[21:25], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'combat_tournament_prelude', 'arc_arr': data_arr[25:28], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'preliminary_round', 'arc_arr': data_arr[28:35], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'subjagation_round', 'arc_arr': data_arr[35:50], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'zara_guild', 'arc_arr': data_arr[50:57], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'hohoian', 'arc_arr': data_arr[57:61], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'undead_in_cobalt_castle', 'arc_arr': data_arr[61:67], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'seige_round_prelude', 'arc_arr': data_arr[67:74], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'genisis', 'arc_arr': data_arr[74:77], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'seige_round', 'arc_arr': data_arr[77:87], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'pooh_upooh_retrieval', 'arc_arr': data_arr[87:98], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'dark_birthday', 'arc_arr': data_arr[98:109], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'post_dark_birthday', 'arc_arr': data_arr[109:117], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'pvp_round_prelude', 'arc_arr': data_arr[117:123], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'pvp_round_quarterfinals', 'arc_arr': data_arr[123:136], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'trial_of_a_dragon', 'arc_arr': data_arr[136:143], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'pvp_round_semifinals', 'arc_arr': data_arr[143:159], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'escape_from_seoul', 'arc_arr': data_arr[159:163], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'pvp_round_final', 'arc_arr': data_arr[163:168], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'ragnarok', 'arc_arr': data_arr[168:174], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'exodus', 'arc_arr': data_arr[174:176], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'after_episode', 'arc_arr': data_arr[176:183], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'reunion', 'arc_arr': data_arr[183:187], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'sleep_walking', 'arc_arr': data_arr[187:191], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'lucid_adventure', 'arc_arr': data_arr[192:199], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'dark', 'arc_arr': data_arr[199:205], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'finding_the_lucky_coin_pieces', 'arc_arr': data_arr[205:213], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'summit', 'arc_arr': data_arr[213:222], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'the_great_war_begins', 'arc_arr': data_arr[222:228], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'beyond_the_boundary', 'arc_arr': data_arr[228:241], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'demon_world_prelude', 'arc_arr': data_arr[241:244], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'demon_world', 'arc_arr': data_arr[244:253], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'advent_of_the_demon_king', 'arc_arr': data_arr[253:262], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'retribution', 'arc_arr': data_arr[262:269], 'color': (random.random(), random.random(), random.random()) },
        { 'name': 'current', 'arc_arr': data_arr[269:276], 'color': (random.random(), random.random(), random.random()) },
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


def plot_x_in_arcs(arcs_arr, x, offset, label):
    fig = plt.figure()
    gs = fig.add_gridspec(1, 38, wspace=0)
    axs = gs.subplots(sharey='row')
    plt.subplots_adjust(left=0.07, right=0.98, top=0.7, bottom=0.155)
    i = 0
    for arc in arcs_arr:
        if i==38:
            continue
        first_arc_chapter = json.loads((arc['arc_arr'])[0])
        for chapter in arc['arc_arr']:
            index = arc['arc_arr'].index(chapter)
            chapter = json.loads(chapter)
            axs[arcs_arr.index(arc)].bar(chapter['name'], float(chapter[x]), color=arc['color'])
            axs[arcs_arr.index(arc)].set_title(arc['name'], rotation=90)
            axs[arcs_arr.index(arc)].set_xticklabels([])
            axs[arcs_arr.index(arc)].set_xlabel(first_arc_chapter['name'], rotation=90)
        i+=1
    axs[0].set_ylabel("Chapter " + label)
    plt.suptitle('Naver HCLW Chapter ' + label + ' Seperated By Arc')
    plt.show()

if __name__ == "__main__":
    data = get_data()
    arcs_data = get_arcs_data(data)
    get_stats(data)
    plot_x_in_arcs(arcs_data, 'length', 0, 'Length(px)')
    plot_x_in_arcs(arcs_data, 'comments', 0, 'Comments')
    plot_x_in_arcs(arcs_data, 'participation', 0, 'Participation')
    plot_x_in_arcs(arcs_data, 'rating', 0, 'Rating')
