name=input('Enter words: ')
x=name.rsplit()
y=x[0],x[1]=x[1],x[0]
z=' '.join(y)

print(z)