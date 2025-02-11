def fact(a): #створення функції знаходження факторіалу
    b = 1
    for i in range (1, a+1):
        b *= i
    return (b)

def power_five(a): #створення функції чи є число степенем 5
    if a <= 0:
        return False
    while a % 5 == 0:
        a //= 5
    return a == 1

if __name__ == "__main__":
    print(fact(7))

