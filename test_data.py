CENSOR_DATA = [
    ("Mój numer telefonu to 213 731 299", "Mój numer telefonu to *** *** ***"),
    ("2137", "****"),
    ("Napis bez cyfr.", "Napis bez cyfr."),
]


ENVELOPE_DATA = [
    (1,
"""\
***
***
***
"""),
    (2,
"""\
*****
** **
* * *
** **
*****
"""),
    (5,
"""\
***********
**       **
* *     * *
*  *   *  *
*   * *   *
*    *    *
*   * *   *
*  *   *  *
* *     * *
**       **
***********
"""),
]


IS_PRIME_DATA = [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (11, True),
    (19, True),
    (53, True),
    (71, True),
    (89, True),
    (97, True),
    (98, False),
    (99, False),
    (100, False),
    (2137, True),
]


IS_DIABOLIC_DATA = [
    (0, False),
    (6, False),
    (2137, False),
    (666, True),
    (6666, True),
    (66566, False),
    (663466623, True),
]


CIPHER_DATA = [
    ("Alfa i Omega", 13, "Nysn v Bzrtn"),
    ("Nysn v Bzrtn", 13, "Alfa i Omega"),
    ("imperator", 3, "lpshudwru"),
    ("Imperator", 3, "Lpshudwru"),
]


DECIPHER_DATA = [
    ("Alfa i Omega", 13, "Nysn v Bzrtn"),
    ("Nysn v Bzrtn", 13, "Alfa i Omega"),
    ("lpshudwru", 3, "imperator"),
    ("Lpshudwru", 3, "Imperator"),
]
