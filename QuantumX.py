guess = 'heads'
import random

score = 0

for i in range(10):
    coin_toss = random.random()

    if(coin_toss > 0.5):
        print('It is tails!')
        if(guess == 'tails'):
            score = score+1
    else:
        print('It is heads!')
        if(guess == 'heads'):
            score = score+1

print('Your score is:',score)
print(random.randint(0, 2))

import qiskit
from qiskit import execute, Aer
from math import pi

circuit = qiskit.QuantumCircuit(1,1)

circuit.h(0)

circuit.measure(range(1),range(1))

job = execute(circuit,Aer.get_backend('qasm_simulator'),shots=1000)
counts = job.result().get_counts(circuit)
print(counts)

circuit.draw(output='mpl')

position_of_the_ship = random.randint(0, 9)

#print(position)

drawing = ''
for i in range(10):
    if(position_of_the_ship == i):
        drawing = drawing + 'X'
    else:
        drawing = drawing + '#'
print(drawing)


number_of_moves = 0
shooting_position = 8

if(shooting_position == position_of_the_ship):
    print('You hit the ship!')
else:
    print('Miss!')
number_of_moves = number_of_moves + 1

print('Number of moves:', number_of_moves)
print('Your score is:', 10-number_of_moves)

position_of_the_ship = random.randint(0, 7)

import qiskit
from qiskit import execute, Aer
from math import pi

circuit = qiskit.QuantumCircuit(3,3)

circuit.h(0)
circuit.h(1)
circuit.h(2)

circuit.measure(range(3),range(3))

job = execute(circuit,Aer.get_backend('qasm_simulator'),shots=1000)
counts = job.result().get_counts(circuit)
print(counts)

circuit.draw(output='mpl')


format_string = '0' + str(3) + 'b'
binary_value = format(position_of_the_ship, format_string)

if binary_value in counts:
    print('You hit the ship!')
else:
    print('Miss!')
hp_of_ships = []
position = random.randint(0, 7)

for i in range(8):
    if(position == i):
        hp_of_ships.append(1000)
    else:
        hp_of_ships.append(0)

print(hp_of_ships)


number_of_moves = 0


import qiskit
from qiskit import execute, Aer
from math import pi

circuit = qiskit.QuantumCircuit(3,3)

circuit.h(0)
circuit.x(1)
#circuit.h(2)
#circuit.cx(0,1)


circuit.measure(range(3),range(3))

job = execute(circuit,Aer.get_backend('qasm_simulator'),shots=1000)
counts = job.result().get_counts(circuit)
#print(counts)



format_string = '0' + str(3) + 'b'
shooting_locations = []
for i in range(8):
    binary_value = format(i, format_string)
    if binary_value in counts:
        shooting_locations.append(counts[binary_value])
    else:
        shooting_locations.append(0)
print(shooting_locations)

circuit.draw(output='mpl')

for i in range(8):
    if(hp_of_ships[i] > 0 and shooting_locations[i] > 0):
        print('You hit the ship!')
        hp_of_ships[i] = hp_of_ships[i] - shooting_locations[i]
        if(hp_of_ships[i] <= 0):
            print('You won!')
            print(hp_of_ships)
number_of_moves = number_of_moves+1
print('Move has been performed!')

print('Number of moves:', number_of_moves)
#print(hp_of_ships)


for i in range(8):
    if(hp_of_ships[i] > 0 and shooting_locations[i] > 0):
        print('You hit the ship!')
        hp_of_ships[i] = hp_of_ships[i] - shooting_locations[i]
        if(hp_of_ships[i] <= 0):
            print('You won!')
            print(hp_of_ships)
number_of_moves = number_of_moves+1
print('Move has been performed!')

import numpy as np

hp_of_ships = []
position_x = random.randint(0, 7)
position_y = random.randint(0, 7)

hp_of_ships = np.zeros((8, 8))

hp_of_ships[position_y][position_x] = 1000
#print(hp_of_ships)

#print(position_x,position_y)
number_of_moves = 0

import qiskit
from qiskit import execute, Aer
from math import pi

circuit_x = qiskit.QuantumCircuit(3,3)

circuit_x.h(0)
circuit_x.h(1)
circuit_x.cx(0,2)


circuit_x.measure(range(3),range(3))

job = execute(circuit_x,Aer.get_backend('qasm_simulator'),shots=1000)
counts_x = job.result().get_counts(circuit_x)
print(counts_x)

import qiskit
from qiskit import execute, Aer
from math import pi

circuit_y = qiskit.QuantumCircuit(3,3)

circuit_y.h(0)
circuit_y.h(1)
circuit_y.cx(0,2)


circuit_y.measure(range(3),range(3))

job = execute(circuit_y,Aer.get_backend('qasm_simulator'),shots=1000)
counts_y = job.result().get_counts(circuit_y)
print(counts_y)

hit_table = np.zeros((8, 8))

format_string = '0' + str(3) + 'b'

for i in range(8):
    binary_value_y = format(i, format_string)
    if binary_value_y in counts_y:
        for j in range(8):
            binary_value_x = format(j, format_string)
            if binary_value_x in counts_x:
                hit_table[i][j] = (counts_y[binary_value_y] * counts_x[binary_value_x])/1000

print(hit_table)
