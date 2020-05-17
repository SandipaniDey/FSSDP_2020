names = ['Mary', 'Isla', 'Sam']
secret_names = list(map(hash, names))
print(secret_names)