particles_file = "particles.txt"

particle_coords = []
with open(particles_file, 'r') as pf:
    for y, line in enumerate(pf.readlines()):
        for x, char in enumerate(line):
            if char == '•':
                particle_coords.append((x, y))

def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

center = (51,26)
sum = 0
for p in particle_coords:
    sum += manhattan_distance(p, center)

print(sum)
