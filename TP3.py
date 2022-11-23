#TP3 Algoritmo Genético
import random
import copy


""" 
Pistas:
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

¿Quien usa vim?

Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim """

n_population = 100000
liveness = 200
mutants = 200
fail_score = 0.5
punish_score = 1
liveness_probability = 70

colors = ['roja', 'azul', 'verde', 'blanca', 'amarilla']
profesiones = ['Matematico', 'Hacker', 'Ingeniero', 'Analista', 'Developer']
bd = ['Cassandra', 'MongoDB', 'HBase', 'Neo4j', 'Redis']
animal = ['Brackets', 'Sublime Text', 'Vim', 'Atom', 'Notepad++']
editor = ['Python', 'C#', 'Java', 'C++', 'Javascript']

tableProto = [colors, profesiones, bd, animal, editor]


class Table:

	def __init__(self):
		self.table = [[0 for x in range(5)] for x in range(5)] 
		self.score = 20
		self.approve = 0

	def getTable(self, x, y):
		return self.table[x][y]

	def randFill(self):
		for x in range(0,5):
			for y in range(0,5):
				self.table[x][y] = random.sample(tableProto[x], 1)[0] 
				pass
			pass

	def mutate(self):
		x  = random.randint(0,4)
		y = random.randint(0,4)
		temp = self.table[x][y]
		self.table[x][y] = self.table[x][(y+1)%5]
		self.table[x][(y+1)%5] = temp
		random.shuffle(self.table[x])

	def test(self):
		#Check consistency
		for x in range(0,5):
			if len(self.table[x])!=len(set(self.table[x])):
				self.score -= 2*punish_score
			pass

		#El matematico vive en la casa roja.
		try:
			i = self.table[1].index('Matematico')
			if self.table[0][i] == 'roja':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#El hacker programa python
		try:
			i = self.table[1].index('Hacker')
			if self.table[2][i] == 'Python':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#Brackets es utilizado en la casa verde.
		try:
			i = self.table[0].index('verde')
			if self.table[4][i] == 'Brackets':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#El analista usa Atom.
		try:
			i = self.table[1].index('Analista')
			if self.table[4][i] == 'Atom':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#La casa verde esta a la derecha de la casa blanca.
		try:
			i = self.table[0].index('verde')
			if self.table[0][i-1] == 'blanca':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#La persona que usa Redis programa en Java.
		try:
			i = self.table[2].index('Redis')
			if self.table[3][i] == 'Java':
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#Cassandra es utilizado en la casa amarilla.
		try:
			i = self.table[0].index('amarilla')
			if self.table[2][i] == 'Cassandra':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#Notepad++ es usado en la casa del medio.
		try:
			if self.table[4][2] == 'Notepad++':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#El Desarrollador vive en la primer casa.
		try:
			if self.table[1][0] == 'Hacker':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#La persona que usa HBase vive al lado de la que programa en Javascript
		try:
			i = self.table[3].index('HBase')
			if i==0:
				if self.table[2][i+1] == 'Javascript':
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
			elif i==4:
				if self.table[2][i-1] == 'Javascript':
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
			else:
				if self.table[2][i+1] == 'Javascript' or self.table[2][i-1] == 'Javascript':
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#La persona que usa Cassandra es vecina de la que programa en C#.
		try:
			i = self.table[3].index('Cassandra')
			if i==0:
				if self.table[2][i+1] == 'C#':
					self.score += 1
					self.approve += 1
				else:
					self.score -= fail_score
			elif i ==4:
				if self.table[2][i-1] == 'C#':
					self.score += 1
					self.approve += 1
				else:
					self.score -= fail_score
			else:
				if self.table[2][i+1] == 'C#' or self.table[2][i-1] == 'C#':
					self.score += 1
					self.approve += 1
				else:
					self.score -= fail_score
		except:
			self.score -= punish_score
			
		#La persona que usa Neo4J usa Sublime Text.
		try:
			i = self.table[3].index('Neo4j')
			if self.table[4][i] == 'Sublime Text':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#El Ingeniero usa MongoDB.
		try:
			i = self.table[1].index('Ingeniero')
			if self.table[3][i] == 'MongoDB':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#EL desarrollador vive en la casa azul.
		try:
			i = self.table[1].index('Hacker')
			if self.table[0][i+1] == 'azul':
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#print(self.table)
		#print(self.score)

class Puzzle:

    def __init__(self):
            self.population = []

    def solve(self):

        self.generate(n_population)
        x = 0

        while True:
            x += 1
            print('Iteration  %d' %x)
            self.test()
            approve =  self.population[0].approve
            self.crossOver(liveness, n_population)
            self.mutate()
            

            if approve >= 4:  #chequear iteraciones
                break
            pass

        self.test()
        
        list = [self.population[0].table, self.population[0].approve]
        return list

    def mutate(self):
        for x in range(0,mutants):
            y = random.randint(0,len(self.population)-1)
            self.population[y].mutate()
            pass
		

    def generate(self, i):
        for x in range(0,i):
            newborn = Table()
            newborn.randFill()
            self.population.append(newborn)
            pass

    def crossOver(self, i, limit):
        
        goodPopulation = []
        i = 0
        while len(goodPopulation)<liveness:
            if random.randint(0,100)<liveness_probability:
                goodPopulation.append(self.population[i])
            i += 1 
            i %= len(self.population)

        newGeneration = []
        while len(newGeneration) <= limit:
            first = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            second = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            third = goodPopulation[random.randint(0,len(goodPopulation)-1)]
            newborn = self.cross(first, second, third)
            newGeneration.append(newborn)

        self.population = newGeneration

    def cross(self, first, second, third):
        newborn = Table()
        #newborn.randFill()
        for x in range(0,5):
            for y in range(0,5):

                i = random.randint(0,2)
                if i == 0:
                    newborn.table[x][y] = first.getTable(x,y)
                elif i == 1:
                    newborn.table[x][y] = second.getTable(x,y)
                else:
                    newborn.table[x][y] = third.getTable(x,y)
                pass
            pass
        return newborn

    def test(self):
        for x in range(0,len(self.population)):
            self.population[x].test()
            pass

        self.population.sort(key=lambda x: x.score, reverse=True)
        for x in range(0,1):
            print (self.population[x].approve)
            pass


puz = Puzzle()
solution = puz.solve()
sol1=[]
sol2=[]
sol3=[]
sol4=[]
sol5=[]
cont=0
for i in solution[0]: #separa en listas las posiciones
	for j in i:
		if(cont==0):
			sol1.append(j)
		if(cont==1):
			sol2.append(j)
		if(cont==2):
			sol3.append(j)
		if(cont==3):
			sol4.append(j)
		if(cont==4):
			sol5.append(j)
		cont=cont+1
	cont=0

print(sol1[1]+": "+sol1[0]+", "+sol1[2]+", "+sol1[3]+", "+sol1[4])
print(sol2[1]+": "+sol2[0]+", "+sol2[2]+", "+sol2[3]+", "+sol2[4])
print(sol3[1]+": "+sol3[0]+", "+sol3[2]+", "+sol3[3]+", "+sol3[4])
print(sol4[1]+": "+sol4[0]+", "+sol4[2]+", "+sol4[3]+", "+sol4[4])
print(sol5[1]+": "+sol5[0]+", "+sol5[2]+", "+sol5[3]+", "+sol5[4])
