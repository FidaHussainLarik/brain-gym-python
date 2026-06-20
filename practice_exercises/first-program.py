name = input('Enter you beautiful name: ')
name = name.strip()
name = name.upper()

def greeting(name):
    print(f'Hello, {name} !')
    exit()

greeting(name)
print('This line should be ignored coz of exit()')




