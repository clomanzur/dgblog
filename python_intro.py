print('Hello, Django girls!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()

def hi(name):
    print('Hi ' + name + '!')

girls = ['olga', 'carla', 'juana', 'yo']
for name in girls:
    hi(name)
    print('next girl')

for i in range(1, 6):
    print(i)
