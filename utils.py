def fact(a): #створення функції знаходження факторіалу
    b = 1
    for i in range (1, a+1):
        b *= i
    return (b)

if __name__ == "__main__":
    print(fact(7))

