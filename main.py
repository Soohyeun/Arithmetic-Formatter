import arithmetic_arranger as aa

while True:
    pytest = input('Input \'pytest\' to run: ')

    if pytest == 'pytest':
        break

aa.arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
