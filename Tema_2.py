counter = 1

while True:
    try:
        age = int(input('Age: '))
    except ValueError:
        print('Invalid input. Try again.')
        continue

    if age >= 18:
        print('Welcome!')
        break

    else:
        counter = counter + 1
        if counter <= 3:
            print('You must be an adult!')
        else:
            print('Maximum number of attempts.')
            break









