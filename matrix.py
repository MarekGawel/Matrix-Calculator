from enum import Enum
import tkinter as tk

# Kalkulator macierzowy
# Wymagania:
# • Dodawanie[x], odejmowanie[x], mnożenie[x], odwracanie[] i dzielenie macierzy[] (mnożenie przez macierz
# odwrotną).
# • Macierze mogą być dowolnego rozmiaru[x].
# • Wyświetlanie komunikatu kiedy operacja jest niemożliwa[x]
# • Wczytywanie macierzy z plików[x] i zapis wyników[]




class Choice(Enum):
    """
    used to determine which __init__ to use in class Matrix
    """
    fixed = 0
    console = 1
    file = 2


class MatrixError(Exception):
    print("Operation not possible!")
    
    pass




class Matrix:
    def __init__(self, Choice, a, b):
        if Choice == 1:
            """
            user creates matrix from console
            
            """
            arr = []
            row = input("Write row, each number followed by space, if end write 'end':")
            w = row.split()
            check = len(w)
            arr.append(w)
            while row != "end":
                row = input("Write row, each number followed by space, if end write 'end':")
                w = row.split()
                while check != len(w) and row != "end":
                    row = input("error, put once more!")
                    w = row.split()
                if row != 'end':
                    arr.append(w)

            for i in range(len(arr)):
                for j in range(check):
                    arr[i][j] = int(arr[i][j])

            self.matrix = arr
            self.length = check  # number of elements in every array
            self.height = len(arr)  # number of arrays
        elif Choice == 0:
            """
            new matrix is created, when two matrixes multiply
            """
            arr = []

            for i in range(b):
                temp = []
                for j in range(a):
                    temp.append(0)

                arr.append(temp)

            self.length = a
            self.height = b
            for i in range(b):
                for j in range(a):
                    arr[i][j] = 0
            self.matrix = arr

        elif Choice == 2:
            arr = []
            fileName = input("File Name: ")
            f = open(fileName, 'r')
            for line in range(sum(1 for line in open(fileName))):
                line = f.readline().split()
                arr.append(line)

            self.length = len(line)
            self.height = len(arr)
            self.matrix = arr





    def print(self):
        elementsRow = [0 for el in range(self.height)]  # contains number of chars in each array, without spaces

        # trying to display matrix with fixed spaces (brackets will be parallel)
        for i in range(self.height):
            for j in range(self.length):
                x = len(str(self.matrix[i][j]))
                elementsRow[i] += x

        areEqual = True

        TODO: "end display function, when rows have different character numbers"
        for i in range(len(elementsRow)):
            for j in range(len(elementsRow)):
                if elementsRow[i] == elementsRow[j]:
                    continue
                else:
                    areEqual = False

        max = 0
        if not areEqual:
            for i in range(len(elementsRow)):
                if elementsRow[i] > max:
                    max = elementsRow[i]

        # actual display block
        if self.height == 1:
            line = "["
            for i in range(self.length):
                line += str(self.matrix[0][i]) + ' '

            line = line[:-1]

            line += ']'
            print(line)

        else:
            line = "⎡"
            for i in range(self.height):
                for j in range(self.length):
                    if j == self.length - 1:
                        line += str(self.matrix[i][j])
                    else:
                        line += str(self.matrix[i][j]) + " "
                if i == 0:
                    line += "⎤"
                elif i == self.height - 1:
                    line += '⎦'
                else:
                    line += "⎥"

                print(line)

                if i == self.height - 2:
                    line = '⎣'
                else:
                    line = '⎢'

    def multiplyByNumber(self, number):
        for i in range(self.height):
            for j in range(self.length):
                self.matrix[i][j] = self.matrix[i][j] * number
        self.print()

    def savingFile(self, what):
        line = ''
        if input("Do you want to save the result to file? [y / n]") == 'y':
            f = open(input("write file name: "), 'w')
            if type(what) == int:
                f.write(what)
            elif type(what) == Matrix:
                for i in range(self.height):
                    for j in range(self.length):
                        if j == self.length - 1:
                            line += str(self.matrix[i][j])
                        else:
                            line += str(self.matrix[i][j]) + " "
                    if i == 0:
                        line += "⎤"
                    elif i == self.height - 1:
                        line += '⎦'
                    else:
                        line += "⎥"

                    f.write(line)

                    if i == self.height - 2:
                        line = '⎣'
                    else:
                        line = '⎢'

    #bugged
    def determinant(self):
        if self.height != self.length:
            raise MatrixError
        else:

            n = self.height
            if (n > 2):
                i = 1
                t = 0
                sum = 0
                while t <= n - 1:
                    d = {}
                    t1 = 1
                    while t1 <= n - 1:
                        m = 0
                        d[t1] = []
                        while m <= n - 1:
                            if (m == t):
                                u = 0
                            else:
                                d[t1].append(self.matrix[t1][m])
                            m += 1
                        t1 += 1
                    l1 = [d[x] for x in d]
                    sum = sum + i * (self.matrix[0][t]) * self.determinant()
                    i = i * (-1)
                    t += 1
                return sum
            else:
                return (int(self.matrix[0][0]) * int(self.matrix[1][1]) - int(self.matrix[0][1]) * int(self.matrix[1][0]))


class set:
    def __init__(self, A, B):

        self.A = A
        self.B = B

    def add(self):
        """
        checking if operation is possible
        """
        if self.A.height != self.B.height or self.A.length != self.B.length:
            raise MatrixError

        else:
            x = self.A.length
            y = self.A.height

            print("Sum of:")
            self.A.print()
            print("and")
            self.B.print()
            print("is:")
            for i in range(y):
                for j in range(x):
                    self.A.matrix[i][j] += self.B.matrix[i][j]

            self.A.print()

    def sub(self):
        """
        checking if operation is possible
        """
        if self.A.height != self.B.height or self.A.length != self.B.length:
            raise MatrixError

        else:
            x = self.A.length
            y = self.A.height

            print("Sum of:")
            self.A.print()
            print("and")
            self.B.print()
            print("is:")
            for i in range(y):
                for j in range(x):
                    self.A.matrix[i][j] -= self.B.matrix[i][j]

            self.A.print()


    def multiply(self):
        if self.A.length != self.B.height or self.B.length != self.A.height:
            raise MatrixError

        else:
            C = Matrix(0, self.A.height, self.B.length)
            for i in range(C.height):
                for j in range(C.length):

                    for x in range(self.A.length):
                        C.matrix[i][j] += self.A.matrix[i][x] * self.B.matrix[x][j]
            print("Multiplication:")
            self.A.print()
            print("and")
            self.B.print()
            print("is:")
            C.print()


