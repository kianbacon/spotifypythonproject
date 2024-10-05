import billboard

# get da songs
chart = billboard.ChartData('hot-100')
top100 = []
for i in range(100):
    song = chart[i]
    print(song)

