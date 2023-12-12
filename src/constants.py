disk_color = ['white', 'red', 'orange']
disks = list()

player_type = ['human']
for i in range(42):
    player_type.append('AI: alpha-beta level ' + str(i + 1))

width = 700
row_width = width // 7
row_height = row_width
height = row_width * 6
row_margin = row_height // 10
