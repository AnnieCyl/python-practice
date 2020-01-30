def fun_sum(x):
    result = 0;
    if x == 0:
        return 0

    for n in range(1, x + 1):
        result = result + n;
    return result;


def fun_get_str(x):
    str1 = "1"
    for n in range(2, x + 1):
        str1 = "%s + %d" %(str1, n)
    return str1


nStr = input("Input n: ")
n = int(nStr)
print("%s = %d" % (fun_get_str(n), fun_sum(n)))