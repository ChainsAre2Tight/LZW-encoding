def cipher(msg: str, debug=False):
    asd = sorted(list(set(msg)))
    i = 1
    omega = msg[0]
    res = ''
    printout = '-'
    while i <= len(msg):
        if i < len(msg):
            k = msg[i]
        omega_k = str(omega + k)

        if omega_k in asd:
            omega = omega_k
        else:
            lox = asd.index(omega)
            printout = lox
            res = res + " " + str(lox)
            asd.append(omega_k)
            omega = k
        i += 1
        if debug:
            print(k, omega, omega_k, printout)
    return res


def decipher(msg: str, asd: list, debug=False) -> str:
    i = 0
    k = msg[0]
    omega = msg[0]
    res = ""
    flag = 0
    buffer = ""

    while i < len(msg):
        polnaya_zapis = '-'
        k = int(msg[i])
        if k < len(asd):

            letter = asd[k]
            if flag != 0:
                polnaya_zapis = str(buffer + letter)
                asd.append(polnaya_zapis)
            res = res + letter
            buffer = letter
            if debug:
                print(k, letter, polnaya_zapis, buffer + "?")
            flag = 1
        i += 1

    return res
