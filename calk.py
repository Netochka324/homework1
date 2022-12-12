msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v).is_integer():
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == '*':
        msg = msg + msg_7
    if (float(v1) == 0 or float(v2) == 0) and v3 in '*+-':
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def read_input(txt):
    oper = [x for x in txt if x in punctuation][0]
    sp = [int(x) for x in txt.split(oper)]
    return sp[0], oper, sp[1]


flag = 0
memory = 0
while flag == 0:
    print(msg_0)
    calc = input('Input equation(вы можете использовать значение из memory(М): ')
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    if str(x).isalpha() or str(y).isalpha():
        print(msg_1)
    else:
        if oper in '+-*/':
            check(x, y, oper)
            flag = 1
            x, y = float(x), float(y)
            if oper == '+':
                result = x + y
                print(result)
            elif oper == '-':
                result = x - y
                print(result)
            elif oper == '*':
                result = x * y
                print(result)
            else:
                if y != 0 and oper == '/':
                    result = x / y
                    print(result)
                else:
                    flag = 0
                    print(msg_3)
        else:
            print(msg_2)
    flag2 = 0
    while flag2 == 0 and flag == 1:
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                flag4 = 0
                while flag4 == 0:
                    print(msg_[msg_index])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index = msg_index + 1
                        else:
                            flag4 = 1
                            memory = result
                    elif answer == 'n':
                        flag4 = 1
                    else:
                        flag4 = 0
                flag2 = 1
            else:
                memory = result
                flag2 = 1
        elif answer == 'n':
            flag2 = 1
        else:
            flag2 = 0
    flag3 = 0
    while flag3 == 0 and flag2 == 1 and flag == 1:
        print(msg_5)
        answer = input()
        if answer == 'y':
            flag = 0
        elif answer == 'n':
            flag3 = 1
        else:
            flag3 = 0
