'''
Condiciones
~~~~~~~~~~~
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

Quien usa vim?


Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim
'''

import random
import time


colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
prefession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

class Phenotype:

    def __init__(self):
        # crear un individuo
		print("programame")
        self.chromosome = 
        self.score   = 

    def decode(self):
        ''' traduce 0's y 1's (conjunto de genes: 3) en valores segun un diccionario '''
        return [[colors[self.chromosome[i*5+0]], 
                 prefession[self.chromosome[i*5+1]],
                 languaje[self.chromosome[i*5+2]],
                 database[self.chromosome[i*5+3]],
                 editor[self.chromosome[i*5+4]]] for i in range(5)]
        

    def encode(self):
        pass


    def mutate(self):
        ''' muta un fenotipo, optimizado'''
        print("programame")
        pass

    def fitness_function(self):
        ''' calcula el valor de fitness del cromosoma segun el problema en particular '''

        self.score = 0

        ok_score = 1
        fail_score = -1
        punish_score = -1 
        
        chromosome = self.decode()

        print("programame")
        pass

class Riddle:

    def __init__(self):
        self.start_time = time.time()
        self.population = []


    '''
    proceso general
    '''
    def solve(self, n_population):
        
        self.generate(n_population)
        print(f"Población creada con {len(self.population)} individuos")

        ''' descomentame '''
        #print(self.population[0].chromosome)
        #print(self.population[0].decode())

        print("Inicio del proceso iterativo")
        fit, indi = self.iterar()

        print(f"Fin del proceso, mejor resultado \n - Fitness: {fit} \n - Individuo {indi.chromosome} \n - Individuo {indi.decode()}")
        

    def iterar(self):

        counter = 0
        break_condition = False

        crossover_prop = 0.80
        
        while not(break_condition):
            
            if counter % 100 == 0:
                print("--------------------------------")
                print(counter)
                print(self.population[0].decode())
            
            # seleccion
            for i, x in enumerate(self.population):                
                print("programame")
                pass

            
            # crossover
            for s in range(0, N, 2):
                print("programame")
                pass
       
            # mutate
            print("programame")
            pass

            # condicion de corte
            if counter > N2 :
                print("programame")
                pass
                break_condition = True


            counter += 1

        return self.population[0].score, self.population[0]

    '''
    operacion: generar individuos y agregarlos a la poblacion
    '''
    def generate(self, i):
        for x in range(0,i):
            newbie = Phenotype()
            self.population.append(newbie)

    '''
    operacion: mutación. Cambiar la configuración fenotipica de un individuo
    '''
    def mutate(self, crossed, prob=0.5):
        print("programame")
        pass


    '''
    operacion: cruazamiento. Intercambio de razos fenotipicos entre individuos
    '''
    def crossOver(self, progenitor_1, progenitor_2, limit):
        print("programame")
        pass

start = time.time()

rid = Riddle()
rid.solve(n_population = 2000)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))