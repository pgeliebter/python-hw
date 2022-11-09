import numpy as n
import pandas as pd

# boo = np.random.rand(5, 5)
# cee = np.random.rand(5, 5)

# add = boo+cee
# multiply = boo*cee
# print(add)
# print(multiply)

# flat = multiply.flatten()
# calculations = {'std': np.std(flat), 'mean': np.mean(flat)}
# print(calculations)

data = {'name':
        ['Magnus Carlsen', 'Ding Liren', 'Ian Nepomniachtchi',
         'Alireza Firouzja', 'Hikaru Nakamura'], 'country':
        ['Norway', 'China', 'Russia', 'France', 'United States'], 'score':
             [2859, 2811, 2793, 2785, 2768], 'rank':
             [1, 2, 3, 4, 5]}

frame = pd.DataFrame(data)
print(frame)
newPlayer = {'name': ['Fabiano Caruana'], 'country': ['United States'],
             'score': [2766], 'rank':
             [6]}
# print(pd.DataFrame(newPlayer))
newFrame = pd.concat([frame, pd.DataFrame(newPlayer)], ignore_index=True)
print(newFrame)

# pd.concat([frame, ], ignore_index=True)

# frame.concat(newPlayer)
# print(frame)
