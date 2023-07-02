n=int(input('Введите число элементов массива '))
mas=list(map(int,input().split()))
mas=mas[-1:]+mas[:-1]
print(*mas)

    

