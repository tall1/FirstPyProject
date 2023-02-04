def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))


def is_prime(number):
    return True not in [number % x == 0 for x in range(2, number)]


def is_funny(string):
    return 0 not in [1 if c == 'h' or c == 'a' else 0 for c in string]


print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
print(is_prime(62))
print(is_prime(43))
print(is_funny("hahahahahaha"))
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print("".join([chr(ord(c) + 2) if 'a' <= c <= 'z' else c for c in password]))
