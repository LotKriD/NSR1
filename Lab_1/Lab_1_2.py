def rpn(s):
    lex = parse(s)
    s2 = []
    r = []
    oper = ["+", "-", "*", "/", "(", ")"]

    for a in lex:
        if a == "(":
            s2 = [a] + s2
        elif a in oper:
            if s2 == []:
                s2 = [a]
            elif a == ")":
                while(True):
                    q = s2[0]
                    s2 = s2[1:]
                    if q == "(":
                        break
                    r += [q]
            elif prty(s2[0]) < prty(a):
                s2 = [a] + s2
            else:
                while(True):
                    if s2 == []:
                        break
                    q = s2[0]                
                    if prty(q) < prty(a):
                        break
                    r += [q]
                    s2 = s2[1:]
                s2 = [a] + s2
        else:
            r += [a]

    while(s2 != []):
        q = s2[0]
        r += [q]
        s2 = s2[1:]
    return r
 
def prty(o):
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "(":
        return 0
 
def parse(s):
    delims = ["+", "-", "*", "/", "(", ")"]
    lex = []
    tmp = ""
    for a in s:
        if a != " ":
            if a in delims:
                if tmp != "":
                    lex += [tmp]
                lex += [a]
                tmp = ""
            else:
                tmp += a
    if tmp != "":
        lex += [tmp]

    return lex
    
def rpn_calc(formula):
    s = []
    for lex in formula:
        if lex[0].isdigit():
            s.append(float(lex))
        else:
            a2 = s.pop()
            a1 = s.pop()
            if lex == '+':
                s.append(a1 + a2)
            if lex == '-':
                s.append(a1 - a2)
            if lex == '*':
                s.append(a1 * a2)
            if lex =='/':
                s.append(a1 / a2)
    return s.pop()            
 
while(True):
    a = input("Input: ")
    print("Answer: ")
    print(rpn(a))
    print(rpn_calc(rpn(a)))

