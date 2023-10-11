def cipher(msg: str, debug=False):
    asd = sorted(list(set(msg)))
    i = 0
    omega = msg[0]
    res = ''
    while i < len(msg):
        i += 1
        if i == len(msg):
            # print(asd.index(omega))
            pass
        else:
            k = msg[i]
        omega_k = str(omega + k)
        if debug:
            print(k, omega, omega_k, end="   ")
        if omega_k in asd:
            omega = omega_k
            if debug:
                print('-')
        else:
            lox = asd.index(omega)
            if debug:
                print(lox)
            res = res + str(lox)
            asd.append(omega_k)
            omega = k
    return res


def decipher(msg: str, asd: list, debug=False) -> str:
    i = 0
    k = msg[0]
    omega = msg[0]
    res = ""
    flag = 0
    buffer = ""

    while i < len(msg):
        k = int(msg[i])
        if k < len(asd):

            letter = asd[k]
            if debug:
                print(k, letter, end=" ")
            if flag != 0:
                polnaya_zapis = str(buffer + letter)
                if debug:
                    print(polnaya_zapis, end=' ')
                asd.append(polnaya_zapis)
            res = res + letter
            buffer = letter
            if debug:
                print(buffer + "?")
            flag = 1
        i += 1

    return res
