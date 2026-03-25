a = int(input('Enter an integer value:'))
b = int(input('Enter an integer value:'))
c = int(input('Enter an integer value:'))
for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
                a_squared = a * a
                b_squared = b * b
                c_squared = c * c
                if (a_squared + b_squared == c_squared):
                      print('You have a Pythagorean triple.',a,b,c)
or a in range(1,a_range):
    for b in range(1,b_range):
        for c in range(1,c_range):