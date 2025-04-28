

def cap_me(arr):
    new_arr = []
    new_name =""
    flag = 0
    for name in arr:
        for letter in name:
            if letter and flag == 0:
                new_name += letter.upper()
                flag = 1
            else:
                new_name += letter.low()
        new_arr.append(new_name)
        new_name = ""
        flag = 0

    return new_arr


if __name__ == '__main__':
    print(cap_me(["jo", "nelson", "jurie"]))