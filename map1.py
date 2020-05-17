import random
names = ['Mary', 'Isla', 'Sam']
secret_names = list(map(lambda x: random.choice(['Mr. Pink','Mr. Orange','Mr. Blonde']),names))
print(secret_names)