class Node(object):
	def __init__(self, name):
		""" Assumes name is a string"""
		self.name = name

	def getName(self):
		return self.name

	def __str__(self):
		return self.name

class Edge(object):
	def __init__(self, src, dest):
		""" Assumes src and dest are nodes"""
		self.src = src
		self.dest = dest

	def getSource(self):
		return self.src

	def getDestination(self):
		return self.dest

	def __str__(self):
		return self.src.getName() + ' -> ' + self.dest.getName()

class Digraph(object):
	""" edges is a dict mapping each node to a list of its children """
	def __init__(self):
		self.edges = {}

	def addNode(self, node):
		if node in self.edges:
			raise ValueError('Duplicate node')
		else:
			self.edges[node] = []

	def addEdge(self, edge):
		src = edge.getSource()
		dest = edge.getDestination()
		if not (src in self.edges and dest in self.edges):
			raise ValueError('Node not in graph')
		self.edges[src].append(dest)

	def childrenOf(self, node):
		return self.edges[node]

	def hasNode(self, node):
		return node in self.edges

	def getNode(self, name):
		for n in self.edges:
			if n.getName() == name:
				return n
		raise NameError(name)

	def __str__(self):
		result = ''
		for src in self.edges:
			for dest in self.edges[src]:
				result = result + src.getName() + ' -> ' + dest.getName() + '\n'
		return result[:-1] # omit final newline

class Graph(Digraph):
	""" Any program that works with a digraph will also work with a graph, but not vice versa.
	"""

	def addEdge(self, edge): #overwrite the add
		Digraph.addEdge(self, edge)
		rev = Edge(edge.getDestination(), edge.getSource())
		Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
	g = graphType()
	for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
		g.addNode(Node(name))
	g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
	g.addEdge(Edge(g.getNode('Boston'),g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Providence'),g.getNode('Boston')))
	g.addEdge(Edge(g.getNode('Providence'),g.getNode('New York')))
	g.addEdge(Edge(g.getNode('New York'),g.getNode('Chicago')))
	g.addEdge(Edge(g.getNode('Chicago'),g.getNode('Denver')))
	g.addEdge(Edge(g.getNode('Denver'),g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Denver'),g.getNode('New York')))
	g.addEdge(Edge(g.getNode('Chicago'),g.getNode('Phoenix')))
	g.addEdge(Edge(g.getNode('Los Angeles'),g.getNode('Boston')))
	return g

def printPath(path):
	""" Assumes path is a list of nodes """
	result = ''
	for i in range(len(path)):
		result = result + str(path[i])
		if i != len(path) - 1:
			result = result + ' --> '
	return result

def BFS(graph, start, end, toPrint = False):
	initPath = [start]
	pathQueue = [initPath]

	if toPrint:
		print('Current BFS path:', printPath(pathQueue))

	while len(pathQueue) != 0:
		# Get and remove oldest element in pathQueue
		tmpPath = pathQueue.pop(0)
		if toPrint:
			print('Current BFS path:', printPath(tmpPath))
		lastNode = tmpPath[-1]
		if lastNode == end:
			return tmpPath
		for nextNode in graph.childrenOf(lastNode): ### ERROR
			if nextNode not in tmpPath:
				newPath = tmpPath + [nextNode]
				pathQueue.append(newPath)
	return None

def shortestPath(graph, start, end, toPrint = False):
	""" Assumes graph is Digraph; start and end are nodes;
		Returns a shortest path from start to end in graph """
	return BFS(graph, start, end, toPrint)

def testSP(source, destination):
	g = buildCityGraph(Digraph)
	sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)

	if sp != None:
		print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
	else:
		print('There is no path from', source, 'to', destination)

testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')