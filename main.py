import xml.dom.minidom
from random import randint
import math
import numpy as np
import matplotlib.pyplot as plt


def first():
    s = input()
    l = list(map(int, s.split()))
    min = 99999
    max = -99999
    for i in l:
        if i > max:
            max = i
        if i < min:
            min = i

    imax = l.index(max)
    imin = l.index(min)
    l[imax] = min
    l[imin] = max
    return l


def second():
    l = list()
    n = int(input())
    m = int(input())
    ls = list()
    for i in range(n):
        lh = [randint(10, 50) for _ in range(m)]
        print(lh)
        summa = 0
        for j in lh:
            summa += j
        ls.append(summa)
        lh.insert(0, summa)
        l.append(lh)

    print()

    max = 0

    for i in range(len(l)):
        min = 99999
        for j in l:
            if min > j[0] > max:
                min = j[0]
        imin = ls.index(min)
        print(l[imin])
        max = min

    print()

    max = 0
    for i in range(len(l)):
        min = 99999
        for j in l:
            if min > j[0] > max:
                min = j[0]
        imin = ls.index(min)

        for j in range(m + 1):
            if j != 0:
                print(l[imin][j], end=" ")
        print()

        max = min


def third():
    l = list(map(str, input().split()))
    s = l[0]
    for i in l:
        if len(i) < len(s):
            s = i
    return s


def forth():
    sh = input()
    s = ""
    for i in sh:
        if i != ' ':
            s += i

    if len(s) == 0:
        return True
    summ = 0
    it1 = 0
    it2 = len(s) - 1
    while summ < len(s):
        if s[it1] != s[it2]:
            return False
        else:
            summ += 2
            it1 += 1
            it2 -= 1
    return True


def eighth():
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    return s1 & s2


def ninth():
    s = list(map(int, input().split()))
    for i in s:
        if s.count(i) == 1:
            print(i, end=" ")
    return "complete"


def tenth():
    s = list(map(str, input().split()))
    st = ""
    for i in range(len(s) - 1, -1, -1):
        st += s[i] + " "
    return st


def eleventh():
    s = list(map(int, input().split()))
    for i in s:
        if i % 2 == 0:
            print(i, end=" ")
    return "Complete"


def fortieth():
    n = int(input())
    m = int(input())
    l = []
    for i in range(n):
        lh = []
        for j in range(m):
            lh.append(0)
        l.append(lh)

    x = 0
    y = 0
    np = 1

    for i in range(1, n * m + 1):
        if np == 1:
            l[y][x] = i
            if x == n - 1:
                np = 2
                y += 1
            elif l[y][x + 1] != 0:
                np = 2
                y += 1
            else:
                x += 1
        elif np == 2:
            l[y][x] = i
            if y == m - 1:
                np = 3
                x -= 1
            elif l[y + 1][x] != 0:
                np = 3
                x -= 1
            else:
                y += 1
        elif np == 3:
            l[y][x] = i
            if x == 0:
                np = 4
                y -= 1
            elif l[y][x - 1] != 0:
                np = 4
                y -= 1
            else:
                x -= 1
        elif np == 4:
            l[y][x] = i
            if l[y - 1][x] != 0:
                np = 1
                x += 1
            else:
                y -= 1

    for i in l:
        for j in i:
            print('{0:5d}'.format(j), end=" ")
        print()
    return "Complete"


def twelfth():
    c = 0.0
    for i in range(0, 51, 5):
        f = float(c * 9 / 5 + 32)
        print(f'C = {c:5.2f}  F={f:5.2f}')
        c += 5.0
    return "Complete"


def thirteenth():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{(i * j):3d}', end=" ")
        print()
    return "Complete"


def fifteenth():
    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({int(l[0]): l[1]})

    f = open('cities.txt', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))
        l[2] = l[2].replace('\n', "")
        print(f'В стране {d.get(int(l[1]))} есть город {l[2]}')

    return "Complete"


def sixteenth():
    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({l[0]: l[1]})

    dk = dict()

    f = open('cities.txt', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))

        if d.get(l[1]) in dk.keys():
            dk.update({d.get(l[1]): dk.get(d.get((l[1]))) + 1})
        else:
            dk.update({d.get(l[1]): 1})

    for i in dk:
        print(i, end=" ")
        print(dk.get(i))

    return "Complete"


def seventeenth():
    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({l[0]: l[1]})

    dk = dict()

    f = open('cities.txt', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))

        if d.get(l[1]) in dk.keys():
            dk.update({d.get(l[1]): dk.get(d.get((l[1]))) + 1})
        else:
            dk.update({d.get(l[1]): 1})

    for i, j in zip(sorted(dk.values()), sorted(dk, key=dk.__getitem__)):
        print(j, end=" ")
        print(i)

    return "Complete"


def eighteenth(a=0):
    if a <= 1:
        return False
    for i in range(2, a, 1):
        if a % i == 0:
            return False
    return True


def nineteenth():
    m = int(input())
    for i in range(1, m + 1):
        summ = 0
        for j in range(1, i):
            if i % j == 0:
                summ += j
        if summ == i:
            print(summ, end=" ")
    return "Complete"


def twentieth(n=0):
    if n == 1:
        return 1
    else:
        return twentieth(n - 1) * n


def twenty_first(n=0):
    if n < 12:
        return 0
    else:
        return 1 + twenty_first(n - 9)


def twenty_second():
    f = open("19", "r", encoding="utf8")
    fk = open("19k", "w")
    for i in f:
        if eighteenth(int(i)):
            fk.write(i)
    return "Complete"


def twenty_third():
    f = open("20", "r", encoding="utf8")
    fk = open("20k", "w")
    l = list()
    for i in f:
        if i != "\n":
            l.append(int(i))
            if int(i) % 2 == 0:
                l.append(randint(-30, 40))
    for i in l:
        if i % 10 != 3:
            fk.write(str(i) + " ")
    return "Complete"


def twenty_forth():
    f = open("21", "r", encoding="utf8")
    fk = open("21k", "w")
    l = list()
    for i in f:
        lh = list(map(float, i.split()))
        l.append(lh)

    x1 = float(l[0][0])
    y1 = float(l[0][1])
    x2 = float(l[1][0])
    y2 = float(l[1][1])
    x3 = float(l[2][0])
    y3 = float(l[2][1])
    x = float(l[3][0])
    y = float(l[3][1])

    s1 = float(math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))
    s2 = float(math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)))
    s3 = float(math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)))
    p = float((s1 + s2 + s3) / 2)
    s = float(math.sqrt((p - s1) * (p - s2) * (p - s3) * p))

    sk = 0

    s1k1 = float(math.sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2)))
    s2k1 = float(math.sqrt((x - x3) * (x - x3) + (y - y3) * (y - y3)))
    s3k1 = float(math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)))
    pk1 = float((s1k1 + s2k1 + s3k1) / 2)
    sk += float(math.sqrt((pk1 - s1k1) * (pk1 - s2k1) * (pk1 - s3k1) * pk1))

    s1k1 = float(math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1)))
    s2k1 = float(math.sqrt((x - x3) * (x - x3) + (y - y3) * (y - y3)))
    s3k1 = float(math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)))
    pk1 = float((s1k1 + s2k1 + s3k1) / 2)
    sk += float(math.sqrt((pk1 - s1k1) * (pk1 - s2k1) * (pk1 - s3k1) * pk1))

    s1k1 = float(math.sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2)))
    s2k1 = float(math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1)))
    s3k1 = float(math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)))
    pk1 = float((s1k1 + s2k1 + s3k1) / 2)
    sk += float(math.sqrt((pk1 - s1k1) * (pk1 - s2k1) * (pk1 - s3k1) * pk1))

    if int(sk) <= int(s):
        fk.write("Inside")
        return "Inside"
    else:
        fk.write("Outside")
        return "Outside"


def dop1(s):
    a = ""
    for i in s:
        if i.isdigit():
            a += i
    return a


def dop2(s=""):
    a = ""
    for i in s:
        if i != "\n":
            a += i
        else:
            break
    return a


def twenty_fifth():
    f = open("страны.csv", "r", encoding="utf8")
    cities = dict()  # номер города: название города
    regions = dict()  # номер региона: название региона
    countries = dict()  # номер страны: название страны
    city2region = dict()  # номер города: номер региона
    region2country = dict()  # номер региона: номер страны
    for i in f:
        l = list(map(str, i.split(";")))
        countries.update({int(dop1(l[0])): dop2(l[2])})
    f.close()
    f1 = open("регионы (1).csv", "r", encoding="utf8")

    for i in f1:
        l1 = list(map(str, i.split(";")))
        regions.update({int(dop1(l1[0])): dop2(l1[2])})
        region2country.update({int(dop1(l1[0])): int(l1[1])})

    f1.close()
    f2 = open("города.csv", "r", encoding="utf8")

    for i in f2:
        l2 = list(map(str, i.split(";")))
        cities.update({int(dop1(l2[0])): dop2(l2[3])})
        city2region.update({int(dop1(l2[0])): int(l2[2])})

    for i in cities:
        print(f'{cities[i]}  {regions[city2region[i]]}  {countries[region2country[city2region[i]]]}')

    return "Complete"


def twenty_sixth(s):
    f = open("страны.csv", "r", encoding="utf8")
    cities = dict()  # номер города: название города
    regions = dict()  # номер региона: название региона
    countries = dict()  # номер страны: название страны
    city2region = dict()  # номер города: номер региона
    region2country = dict()  # номер региона: номер страны

    for i in f:
        l = list(map(str, i.split(";")))
        countries.update({dop2(l[2]): int(dop1(l[0]))})
    f.close()
    f2 = open("города.csv", "r", encoding="utf8")

    n = countries[s]

    for i in f2:
        l2 = list(map(str, i.split(";")))
        if n == int(l2[1]):
            print(l2[3])

    return ""


def twenty_seventh():
    f = open("страны.csv", "r", encoding="utf8")
    cities = dict()  # номер города: название города
    regions = dict()  # номер региона: название региона
    countries = dict()  # номер страны: название страны
    city2region = dict()  # номер города: номер региона
    region2country = dict()  # номер региона: номер страны
    for i in f:
        l = list(map(str, i.split(";")))
        countries.update({int(dop1(l[0])): dop2(l[2])})
    f.close()
    f1 = open("регионы (1).csv", "r", encoding="utf8")

    for i in f1:
        l1 = list(map(str, i.split(";")))
        regions.update({int(dop1(l1[0])): dop2(l1[2])})
        region2country.update({int(dop1(l1[0])): int(l1[1])})

    f1.close()
    f2 = open("города.csv", "r", encoding="utf8")

    for i in f2:
        l2 = list(map(str, i.split(";")))
        cities.update({int(dop1(l2[0])): dop2(l2[3])})
        city2region.update({int(dop1(l2[0])): int(l2[2])})

    where = input("Введите город, регион или страна >> ")
    what = input("Введите номер или название >> ")
    why = input("Введите условие >> ")

    ## 1 - <, 2 - <=, 3 - >, 4- >=, 5 - ==

    if where == "город":
        if what == "номер":
            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in cities:
                    if int(i) < chis:
                        print(i)
            elif sim == 2:
                for i in cities:
                    if int(i) <= chis:
                        print(i)
            elif sim == 3:
                for i in cities:
                    if int(i) > chis:
                        print(i)
            elif sim == 4:
                for i in cities:
                    if int(i) >= chis:
                        print(i)
            elif sim == 5:
                for i in cities:
                    if int(i) == chis:
                        print(i)
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in cities:
                        b = True
                        for j in range(len(st)):
                            if st[j] != cities[i][j]:
                                b = False
                                break
                        if b:
                            print(i)
                else:
                    for i in cities:
                        if chis == cities[i]:
                            print(i)

        else:
            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in cities:
                    if int(i) < chis:
                        print(cities[i])
            elif sim == 2:
                for i in cities:
                    if int(i) <= chis:
                        print(cities[i])
            elif sim == 3:
                for i in cities:
                    if int(i) > chis:
                        print(cities[i])
            elif sim == 4:
                for i in cities:
                    if int(i) >= chis:
                        print(cities[i])
            elif sim == 5:
                for i in cities:
                    if int(i) == chis:
                        print(cities[i])
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in cities:
                        b = True
                        for j in range(len(st)):
                            if st[j] != cities[i][j]:
                                b = False
                                break
                        if b:
                            print(cities[i])


                else:
                    for i in cities:
                        if chis == cities[i]:
                            print(cities[i])

    elif where == "регион":
        if what == "номер":
            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in regions:
                    if int(i) < chis:
                        print(i)
            elif sim == 2:
                for i in regions:
                    if int(i) <= chis:
                        print(i)
            elif sim == 3:
                for i in regions:
                    if int(i) > chis:
                        print(i)
            elif sim == 4:
                for i in regions:
                    if int(i) >= chis:
                        print(i)
            elif sim == 5:
                for i in regions:
                    if int(i) == chis:
                        print(i)
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in regions:
                        b = True
                        for j in range(len(st)):
                            if st[j] != regions[i][j]:
                                b = False
                                break
                        if b:
                            print(i)
                else:
                    for i in regions:
                        if chis == regions[i]:
                            print(regions[i])

        else:

            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in regions:
                    if int(i) < chis:
                        print(regions[i])
            elif sim == 2:
                for i in regions:
                    if int(i) <= chis:
                        print(regions[i])
            elif sim == 3:
                for i in regions:
                    if int(i) > chis:
                        print(regions[i])
            elif sim == 4:
                for i in regions:
                    if int(i) >= chis:
                        print(regions[i])
            elif sim == 5:
                for i in regions:
                    if int(i) == chis:
                        print(regions[i])
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in regions:
                        b = True
                        for j in range(len(st)):
                            if st[j] != regions[i][j]:
                                b = False
                                break
                        if b:
                            print(regions[i])
                else:
                    for i in regions:
                        if chis == regions[i]:
                            print(regions[i])

    else:
        if what == "номер":

            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in countries:
                    if int(i) < chis:
                        print(i)
            elif sim == 2:
                for i in countries:
                    if int(i) <= chis:
                        print(i)
            elif sim == 3:
                for i in countries:
                    if int(i) > chis:
                        print(i)
            elif sim == 4:
                for i in countries:
                    if int(i) >= chis:
                        print(i)
            elif sim == 5:
                for i in countries:
                    if int(i) == chis:
                        print(i)
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in countries:
                        b = True
                        for j in range(len(st)):
                            if st[j] != countries[i][j]:
                                b = False
                                break
                        if b:
                            print(i)
                else:
                    for i in countries:
                        if chis == countries[i]:
                            print(i)

        else:

            sim, chis = obratka_usloviy(why)
            if sim == 1:
                for i in countries:
                    if int(i) < chis:
                        print(countries[i])
            elif sim == 2:
                for i in countries:
                    if int(i) <= chis:
                        print(countries[i])
            elif sim == 3:
                for i in countries:
                    if int(i) > chis:
                        print(countries[i])
            elif sim == 4:
                for i in countries:
                    if int(i) >= chis:
                        print(countries[i])
            elif sim == 5:
                for i in countries:
                    if int(i) == chis:
                        print(countries[i])
            elif sim == 0:
                if chis[len(chis) - 1] == "*":
                    st = ""
                    it = 0
                    while chis[it] != "*":
                        st += chis[it]
                        it += 1

                    for i in countries:
                        b = True
                        for j in range(len(st)):
                            if st[j] != countries[i][j]:
                                b = False
                                break
                        if b:
                            print(countries[i])
                else:
                    for i in countries:
                        if chis == countries[i]:
                            print(countries[i])


def obratka_usloviy(s):
    l = list(map(str, s.split()))
    if l[0] == "название":
        return 0, l[2]
    elif l[0] == "номер":
        if l[1] == "<":
            return 1, int(l[2])
        elif l[1] == "<=":
            return 2, int(l[2])
        elif l[1] == ">":
            return 3, int(l[2])
        elif l[1] == ">=":
            return 4, int(l[2])
        elif l[1] == "==":
            return 5, int(l[2])


def twenty_eigth():
    print(np.linspace(10, 20, 21))


def twenty_nineth():
    n = np.linspace(-2 * np.pi, 2 * np.pi, 20)
    print(n)
    nk = np.sin(n) * np.sin(n) + np.cos(n) * np.cos(n)
    print(nk)
    return nk.all()


def thirtieth():
    n = int(input())
    m = int(input())
    n1 = np.empty((n, m), dtype=np.int64)
    n2 = np.empty((n, m), dtype=np.int64)
    ar = int(0)
    for i in range(n):
        for j in range(m):
            n1[i][j] = randint(1, 51)
            n2[i][j] = randint(1, 51)
            ar += n1[i][j] + n2[i][j]
    ar /= (2 * n * m)
    a = np.array([])
    for i in n1.flat:
        if i > ar:
            a = np.append(a, i)
    for i in n2.flat:
        if i > ar:
            a = np.append(a, i)
    a.sort()
    print(n1)
    print(n2)
    print(ar)
    return a


def thirty_first():
    n = int(input())
    n1 = np.empty((n, n), dtype=np.int64)
    n2 = np.empty((n, n), dtype=np.int64)
    for i in range(n):
        for j in range(n):
            n1[i][j] = randint(1, 51)
            n2[i][j] = randint(1, 51)

    nk = n1 * n2
    print(n1)
    print(n2)
    print(nk)

    for i in range(n):
        print(nk[i][i])


def thirty_second():
    planets = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
    x_axis = np.arange(len(planets))
    y_axis = [4879.4, 12103.6, 12742.0, 6780.0, 139822, 116464, 50724, 49244]
    plt.pie(y_axis, labels=planets)
    plt.show()


def thirty_third():
    f = open("33", "r", encoding="utf8")
    x = []
    y = []
    for i in f:
        l = i.split(",")
        x.append(float(l[0]))
        y.append(float(l[1]))

    plt.bar(x, y, width=0.05, alpha=0.5)
    plt.show()

def thirty_forth():
    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({l[0]: l[1]})

    dk = dict()

    f = open('cities.txt', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))

        if d.get(l[1]) in dk.keys():
            dk.update({d.get(l[1]): dk.get(d.get((l[1]))) + 1})
        else:
            dk.update({d.get(l[1]): 1})
    it = 0
    l = len(dk.values())
    x = []
    y = []

    for i, j in zip(sorted(dk.values()), sorted(dk, key=dk.__getitem__)):
        if it >=l-10:
            x.append(j)
            y.append(i)

        it+=1

    plt.bar(x, y)
    plt.xticks(x, rotation=45)
    plt.show()

def thirty_forth():
    x = np.linspace(-1, 1, 251)
    y = x*x
    plt.plot(x, y, label = "x^2")
    y = x*x*x
    plt.plot(x, y, label = "x^3")
    y = np.cbrt(x)
    plt.plot(x, y, label="cbrt(3)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")
    plt.legend(fontsize=16)
    plt.show()

def thirty_fifth():
    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({l[0]: l[1]})

    dk = dict()

    f = open('cities.txt', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))

        if d.get(l[1]) in dk.keys():
            dk.update({d.get(l[1]): dk.get(d.get((l[1]))) + 1})
        else:
            dk.update({d.get(l[1]): 1})
    it = 0
    l = len(dk.values())
    x = []
    y = []

    for i, j in zip(sorted(dk.values()), sorted(dk, key=dk.__getitem__)):
        if it >= l - 10:
            x.append(j)
            y.append(i)

        it += 1
    fig = plt.figure(num =None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    ax1 = fig.add_subplot(1, 2, 1)
    line1 = ax1.bar(x, y)
    ax1.set_xlabel("Countries")
    ax1.set_ylabel("Города")
    plt.xticks(x, rotation=45)

    f = open('countries.txt', 'r', encoding="utf8")
    d = dict()
    for i in f:
        l = list(map(str, i.split(';')))
        l[1] = l[1].replace("\n", "")
        d.update({l[0]: l[1]})

    dk = dict()

    f = open('регионы (1).csv', 'r', encoding="utf8")
    for i in f:
        l = list(map(str, i.split(';')))

        if d.get(l[1]) in dk.keys():
            dk.update({d.get(l[1]): dk.get(d.get((l[1]))) + 1})
        else:
            dk.update({d.get(l[1]): 1})

    it = 0
    l = len(dk.values())
    x = []
    y = []

    for i, j in zip(sorted(dk.values()), sorted(dk, key=dk.__getitem__)):
        if it >= l - 10:
            x.append(j)
            y.append(i)

        it+=1
    ax2 = fig.add_subplot(1, 2, 2)
    line2 = ax2.bar(x,y)
    ax2.set_xlabel("Countries")
    ax2.set_ylabel("Регионы")
    plt.xticks(x, rotation=45)
    plt.show()


def thirty_seventh():
    r = 50
    h = 30
    l = np.linspace(0, 50, 500)
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r * l - h * np.sin(l)
    ly = r - h * ly
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")

    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(lx, ly, label="r>h")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")
    h = 50
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r * l - h * np.sin(l)
    ly = r - h * ly
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(lx, ly, label="r==h")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    h = 70
    lx = np.sin(l)
    ly = np.cos(l)
    lx = r*l - h*np.sin(l)
    ly = r - h* ly
    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(lx, ly, label="r<h")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    plt.show()

def thirty_eigth():
    t = np.linspace(0, 2*np.pi, 100)
    a = 5
    b = 15
    lx = a * np.cos(t) * np.cos(t) +  b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(lx, ly, label="b > 2a")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")

    a = 5
    b = 7
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(lx, ly, label="a<b<2a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 5
    b = 3
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.plot(lx, ly, label="b<a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 5
    b = 5
    lx = a * np.cos(t) * np.cos(t) + b * np.cos(t)
    ly = a * np.cos(t) * np.sin(t) + b * np.sin(t)
    ax2 = fig.add_subplot(2, 2, 4)
    ax2.plot(lx, ly, label="b==a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.show()

def thirty_nineth():
    t = np.linspace((-2)*np.pi, 2*np.pi, 501)
    a = 5
    b = 15
    lx = (a+b)*np.cos(t)-a*np.cos((a+b)*t/a)
    ly = (a+b)*np.sin(t) - a * np.sin((a+b)* t/a)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(lx, ly, label="b == 3a")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.title("Graphics")
    a = 4
    b = 6
    lx = (a + b) * np.cos(t) - a * np.cos((a + b) * t / a)
    ly = (a + b) * np.sin(t) - a * np.sin((a + b) * t / a)
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(lx, ly, label="b == 3/2a")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")
    plt.show()


def fortieth():
    t = np.linspace((-1)*np.pi, np.pi, 201)
    a = 1
    b = 1
    d = np.pi/2
    lx = a * np.sin(a*t+d)
    ly = b * np.sin(b*t)
    fig = plt.figure(num=None, figsize=(10, 5), dpi=96, facecolor="w", edgecolor="b")
    fig.suptitle("Graphics")
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(lx, ly, label="a==b, d = PI/2")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")


    a = 1
    b = 2
    d = np.pi / 4
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(lx, ly, label="b == 2a, d = PI/4")

    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 1
    b = 8
    d = np.pi / 2
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(lx, ly, label="b == 8a, d = PI/2")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    a = 1
    b = 3
    d = np.pi / 2
    lx = a * np.sin(a * t + d)
    ly = b * np.sin(b * t)

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(lx, ly, label="b == 3a, d = PI/2")
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
    plt.legend()
    plt.grid(which="major")
    plt.grid(which="minor", linestyle=":")

    plt.show()

if __name__ == "__main__":
    print(fortieth())
