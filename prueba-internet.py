#Solving Einstein's Puzzle with Genetic Algorithm
import random
import copy


n_population = 100000
liveness = 200
mutants = 200
fail_score = 0.5
punish_score = 1
liveness_probability = 70

### Limitations ###

#The Englishman lives in the red house. El matemático vive en la casa roja
#The Swede keeps dogs. El analista usa atoms
#The Dane drinks tea. El hacker programa en python
#The green house is just to the left of the white one. La casa verde esta a la derecha de la casa blanca
#The owner of the green house drinks coffee.
#The Pall Mall smoker keeps birds. La persona que usa Neo4J usa Sublime Text.
#The owner of the yellow house smokes Dunhills. Cassandra es utilizado en la casa amarilla
#The man in the center house drinks milk. Notepad++ es utilizado en la casa del medio
#The Norwegian lives in the first house. El dessarrollador vive en la primer casa
#The Blend smoker has a neighbor who keeps cats. 
#The man who smokes Blue Masters drinks bier. La persona que usa redis programa en java
#The man who keeps horses lives next to the Dunhill smoker.
#The German smokes Prince. El ingeniero usa mongodb
#The Norwegian lives next to the blue house. El desarrollador vive en la casa azul

colors = 		["rojo","azul", "verde", "blanco", "amarillo"]
nationality = 	["Englishman", "Swede", "Norwegian", "German", "Dane"]
ciagerette = 	["Pall Mall", "Blue Masters", "Prince", "Dunhills", "Blend"] #NOSQL
animal = 		["dogs", "birds", "cats", "horse", "fish"] #Editor de texto
drink = 		["tea", "coffee", "milk", "bier", "water"] #leng programacion

tableProto = [colors, nationality, ciagerette, animal, drink]


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

		#self.table[x][y] = random.sample(tableProto[x], 1)[0]
		#self.table[x][(y+1)%5] = random.sample(tableProto[x], 1)[0]

	def test(self):
		#Check consistency
		for x in range(0,5):
			if len(self.table[x])!=len(set(self.table[x])):
				self.score -= 2*punish_score
			pass

		#The Englishman lives in the red house.
		try:
			i = self.table[1].index('Englishman')
			if self.table[0][i] == 'red':
				#print('The Englishman lives in the red house.')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The Swede keeps dogs.
		try:
			i = self.table[1].index('Swede')
			if self.table[3][i] == 'dogs':
				#print('The Swede keeps dogs')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The Dane drinks tea.
		try:
			i = self.table[1].index('Dane')
			if self.table[4][i] == 'tea':
				#print('The Dane drinks tea')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The green house is just to the left of the white one.
		try:
			i = self.table[0].index('green')
			if self.table[0][i+1] == 'white':
				#print('The green house is just to the left of the white one.')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The owner of the green house drinks coffee.
		try:
			i = self.table[0].index('green')
			if self.table[4][i] == 'coffee':
				#print('The owner of the green house drinks coffee.')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The Pall Mall smoker keeps birds.
		try:
			i = self.table[2].index('Pall Mall')
			if self.table[3][i] == 'birds':
				#print('The Pall Mall smoker keeps birds.')
				self.score += 1	
				self.approve +=1
			else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The owner of the yellow house smokes Dunhills.
		try:
			i = self.table[0].index('yellow')
			if self.table[2][i] == 'Dunhills':
				#print('The owner of the yellow house smokes Dunhills.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The man in the center house drinks milk.
		try:
			if self.table[4][2] == 'milk':
				#print('The man in the center house drinks milk.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The Norwegian lives in the first house.
		try:
			if self.table[1][0] == 'Norwegian':
				#print('The Norwegian lives in the first house.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The Blend smoker has a neighbor who keeps cats.
		try:
			i = self.table[2].index('Blend')
			if i==0:
				if self.table[3][i+1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
			elif i==4:
				if self.table[3][i-1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
			else:
				if self.table[3][i+1] == 'cats' or self.table[3][i-1] == 'cats':
					#print('The Blend smoker has a neighbor who keeps cats.')
					self.score += 1
					self.approve +=1
				else:
					self.score -= fail_score
		except:
			self.score -= punish_score

		#The man who smokes Blue Masters drinks bier.
		try:
			i = self.table[2].index('Blue Masters')
			if self.table[4][i] == 'bier':
				#print('The man who smokes Blue Masters drinks bier.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The man who keeps horses lives next to the Dunhill smoker.
		try:
			i = self.table[3].index('horse')
			if self.table[2][i-1] == 'Dunhills':
				#print('The man who keeps horses lives next to the Dunhill smoker.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The German smokes Prince.
		try:
			i = self.table[1].index('German')
			if self.table[2][i] == 'Prince':
				#print('The German smokes Prince.')
				self.score += 1	
				self.approve +=1
			else:
				self.score -= fail_score
		except:
			self.score -= punish_score

		#The Norwegian lives next to the blue house.
		try:
			i = self.table[1].index('Norwegian')
			if self.table[0][i+1] == 'blue':
				#print('The Norwegian lives next to the blue house.')
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
            

            if approve >= 3:
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
