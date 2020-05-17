sname = ['Alabama','California','Oklahoma','Florida']
vowel = ['a','e','i','o','u']
statename = list()
for state in sname:
    states = ''
    for letter in state:
        if letter.lower() in vowel:
            continue
        states = states + letter.lower()
    statename.append(states)
print(statename)