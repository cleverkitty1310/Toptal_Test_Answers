# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

S = """photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""

def date2int(date):
    parts = date.split(' ')
    y, m, d = map(int, parts[1].split('-'))
    hh, mm, ss = map(int, parts[2].split(':'))
    return ss + mm * 60 + hh * 3600 + (10000 * y + 100 * m + d) * 100000

def sort(tuples, dir):
    return sorted (tuples, key=lambda last : last[dir])

def solution(S):
    # write your code in Python 3.6
    strs = S.split('\n')
    photo_names = []
    places = []
    dates = []
    for str in strs:
        cols = str.split(',')
        photo_names.append(cols[0])
        places.append(cols[1][1:])
        dates.append(date2int(cols[2]))
    dit = {}
    dit_cnt = {}
    cnt = 0
    for i in range(places.__len__()):
        if places[i] in dit:
            dit[places[i]].append([cnt, photo_names[i], dates[i]])
            dit_cnt[places[i]] += 1
        else:
            dit[places[i]] = [[cnt, photo_names[i], dates[i]]]
            dit_cnt[places[i]] = 1
        cnt += 1
    for i in dit:
        dit[i] = sort(dit[i], -1)
    
    for i in dit:
        len = 1
        for item in dit[i]:
            item.append(i + "{0}".format(len.__str__().zfill(dit_cnt[i].__str__().__len__())) + item[1][-4:])
            len += 1

    all_items = []
    for i in dit:
        for item in dit[i]:
            all_items.append(item)
    all_items = sort(all_items, 0)
    
    for i in all_items:
        print(i[3])
    
solution(S)