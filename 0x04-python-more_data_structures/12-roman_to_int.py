#!/usr/bin/python3


def convert_roman(ch):
    """
    converts a roman numeral character into the respective integer
    """
    ret = -1
    if ch == 'i' or ch == 'I':
        ret = 1
    elif ch == 'v' or ch == 'V':
        ret = 5
    elif ch == 'x' or ch == 'X':
        ret = 10
    elif ch == 'l' or ch == 'L':
        ret = 50
    elif ch == 'c' or ch == 'C':
        ret = 100
    elif ch == 'd' or ch == 'D':
        ret = 500
    elif ch == 'm' or ch == 'M':
        ret = 1000
    return ret


def roman_to_int(roman_string):
    """
    converts any string of roman numerals to decimal
    """
    cur_max = -1
    cur = conv = 0
    holder = []

    if roman_string is None or type(roman_string) is not str:
        return 0
    for c in roman_string:
        cur = convert_roman(c)
        if len(holder) == 0:
            if cur == cur_max or cur_max == -1:
                cur_max = cur
                conv += cur
            elif cur < cur_max:
                holder.append(cur)
            else:  # only happens if smaller is starting number
                # for example: IIX, VXC
                cur -= conv
                conv = cur
        else:
            if cur > holder[-1]:
                cur_max = cur
                cur -= sum(holder)
                conv += cur
                holder.clear()
            else:
                holder.append(cur)

    if len(holder) != 0:
        conv += sum(holder)
    return conv
