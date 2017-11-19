#!/usr/bin/python

def diviseur(n):
    div = []
    for i in range(1,n+1):
        if n % i == 0:
            div.append(i)
    return div

def nb_parfait(n):
    li = diviseur(n)
    sum = 0
    for k in li[:-1]:
        sum = sum + k

    if sum == n:
        print("Nombre parfait")
    else:
        if sum < n:
            print("Nombre deficient")
        else:
            print("Nombre abondant")


if __name__=='__main__':
    nb_parfait(7)


#appel du script depuis la console et la valeur en argument
