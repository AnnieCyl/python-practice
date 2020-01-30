def fun_sum(x):
    result = 0
    for r in range(1, x + 1):
        result = result + 1/r
    return result


def fun_get_str(x):
    str1 = 1
    for r in range(2, x + 1):
        str1 = "%s + 1/%s" %(str1, r)
    return str1


nStr = input("Input n:")
n = int(nStr)
print("%s = %.2f" %(fun_get_str(n), fun_sum(n)))

