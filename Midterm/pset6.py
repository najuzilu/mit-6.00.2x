import random

nodes = []
for i in range(5):
    nodes.append(i)

print('NODES=', nodes)

for i in range(len(nodes)):
	w = random.choice(nodes)
	x = random.choice(nodes)
	y = random.choice(nodes)
	z = random.choice(nodes)
	print(w, '->', x, '->', y, '->', w)

