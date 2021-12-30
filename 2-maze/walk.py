directions_file = "directions.txt"
maze_file = "maze.txt"

directions_string = ""
with open(directions_file, 'r') as df:
    for line in df.readlines():
        directions_string += line

directions = [direction.strip() for direction in directions_string.split(',')]

cardinal_map = {
    'N': (0,-1), 'E': (1,0), 'S': (0,1), 'W': (-1,0)
}
current_loc = [3, 21]

# parse maze: False = wall, True = path
maze = []
with open(maze_file, 'r') as mf:
    for line in mf.readlines():
        maze.append([c in {" ", 'I'} for c in line])

for movement in directions:
    direction = cardinal_map[movement]
    target_loc = (current_loc[0] + direction[0], current_loc[1] + direction[1])
    if maze[target_loc[1]][target_loc[0]]:
        current_loc = target_loc

print("Final location: ", current_loc)
