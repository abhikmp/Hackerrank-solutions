def mat(n, m):

    for i in range( 1, n, 2):
        print(str('.|.' * i).center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range( n-2, -1, -2):
        print(str('.|.' * i).center(m, '-'))

n , m = input().split()
mat(int(n),int(m))
