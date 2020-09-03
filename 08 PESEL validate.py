CHECK_TABLE = [int(item) for item in ('1 3 7 9 1 3 7 9 1 3'.split(' '))]


def validate_pesel(PESEL):
    try:
        to_check = [int(item) for item in PESEL]
    except  ValueError as e: 
        return False
    result = 10 - sum([to_check[i]*CHECK_TABLE[i] for i in range(10)]) % 10
    if result ==10: result = 0
    return result == to_check[10]


if __name__ == "__main__":
    print("PESEL - 69010108851:", validate_pesel("69010108851"))
    print("PESEL - 69010108850:", validate_pesel("69010108850"))
    print("PESEL - 02321709033:", validate_pesel("02321709033"))
