def cypher(msg: str):
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
        print(k, omega, omega_k, end="   ")
        if omega_k in asd:
            omega = omega_k
            print('-')
        else:
            lox = asd.index(omega)
            print(lox)
            res = res + str(lox)
            asd.append(omega_k)
            omega = k
    return res


# def decypher(msg: str, asd: list) -> str:
#     i = 0
#     k = msg[0]
#     omega = msg[0]
#
#     k = msg[i]
#     if k in range(asd):
#         print(asd[k])
#         asd.append(str(asd[k] + "?"))