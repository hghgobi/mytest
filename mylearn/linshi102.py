d = 300
while d > 0:
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    if (a > 0 and b > 0) or b == 0 or a == 0:
        pass
    else:
        if a % b == 0:
            num0 = a
            num1 = b
            c = int(a / b)
            answer = str(c)
            ornot = 0
            Xxqs23.addqs3(num0, num1, yunsuan, answer, ornot)
            d = d - 1

        else:
            if abs(a) > abs(b):
                e = 0
                f = 0
                for i in range(2, abs(a)):
                    while a % i == 0 and b % i == 0:
                        e = a // i
                        f = b // i
                if a * b > 0:
                    c = str(abs(e)) + 'V' + str(abs(f))
                else:
                    c = '-' + str(abs(e)) + 'V' + str(abs(f))
                num0 = a
                num1 = b
                answer = str(c)
                ornot = 0
                Xxqs23.addqs3(num0, num1, yunsuan, answer, ornot)
                d = d - 1
            else:
                e = 0
                f = 0
                for i in range(2, abs(b)):
                    while a % i == 0 and b % i == 0:
                        e = a // i
                        f = b // i
                if a * b > 0:
                    c = str(abs(e)) + 'V' + str(abs(f))
                else:
                    c = '-' + str(abs(e)) + 'V' + str(abs(f))
                answer = str(c)
                ornot = 0
                num0 = a
                num1 = b
                Xxqs23.addqs3(num0, num1, yunsuan, answer, ornot)
                d = d - 1