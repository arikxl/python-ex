weight = int(input('Weight: '))
unit =input('(K)g or (L)bs: ')
if unit.upper()== 'K':
    convert = weight / 0.45
    print(f'Weight in Lbs: {convert}')
else:
    convert = weight * 0.45
    print(f'Weight in Ks: {convert}')