if __name__ == "__main__":
    from functions import cipher, decipher


# Вот это менять
msg = "студент седьмой учебной группы ботников дмитрий александрович"

dct = sorted(list(set(msg)))
# dct = ["a", "b", "c", "d", "e"]
# encoded_msg = "01235245"

if __name__ == "__main__":
    print("""
--- Cipher ---
        """)
    encoded_msg = cipher(msg, True)
    print(encoded_msg)

    print("""
--- Decipher ---
    """)

    print(decipher(encoded_msg.split(), dct, True))
