import json
import matplotlib.pyplot as plt

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
        'longest_chapter_name': '',
        'longest_chapter_length': 0
    }
    for data in data_arr:
        data = json.loads(data)
        if data['length'] > stats['longest_chapter_length']:
            stats['longest_chapter_length'] = data['length']
            stats['longest_chapter_name'] = data['name'] 
    print(stats)
    return stats


def plot_data(data_arr, stats):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    bottom = []
    lengths = []
    for data in data_arr:
        data = json.loads(data)
        lengths.append(data['length']/1000)
        bottom.append(data['name'])
    ax.bar(bottom,lengths)
    plt.show()

if __name__ == "__main__":
    data = get_data()
    average = get_average_len(data)
    print(average)
    stats = get_stats(data)
    plot_data(data, stats)
