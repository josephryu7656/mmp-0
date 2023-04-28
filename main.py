money_history = []
balance = 0


print('||||| Money Management Program |||||')
print('|---------Commands List ------------')
print('| 0 : exit program                 |')
print('| 1 : deposit                      |')
print('| 2 : withdraw                     |')
print('| 3 : balance                      |')
print('| 4 : history                      |')
print('|----------------------------------|')


while True:
    command = input('Enter your command > ')

    if command == '1':
        print('[Deposit Money]')
        money = input('How much do you want to deposit?')
        money_history.append(money)
        print(f'you deposited ${money} ')
        print('------------------------------------')

    elif command == '2':
        print('[Withdraw money]')
        money = input('How much money do you want to withdraw?')

        if int(money) > balance: 
            print('Insufficient Funds')
        else:
            money_history.append('-' + money)
            print(f'you withdrawed ${money}')
        print('------------------------------------')

    elif command == '3':
        print('[Check Balance]')
        balance = 0
        for i in money_history:
            balance = balance +int(i)
        print(f'You have ${money} ')
        print('------------------------------------')

    elif command == '4':
        print('[Account History]')
        print(money_history)
        print('------------------------------------')
        
    elif command == '0':
        break

    