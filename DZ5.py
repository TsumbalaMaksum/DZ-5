import colorama

print(colorama.__name__) #як називається бібліотека

for met in dir(colorama):
    print(met) #як взнати всі команди в бібліотеці

data = 'string'
print(hasattr(colorama, 'reverse')) #чи є ця команда в бібліотеці

print(getattr(colorama, 'forwardsdfsd', 'no')) #перевірити що робитить ця фунція