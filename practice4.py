def fun_sort(target_list):
    for x in range(len(target_list)):
        for y in range(len(target_list) - 1):
            if target_list[y] > target_list[y + 1]:
                temp = target_list[y]
                target_list[y] = target_list[y + 1]
                target_list[y + 1] = temp;
    return target_list


list1 = [23,18,7,64,99,12,138]
list2 = [32, 1, 5, 42, 3, 38, 4, 22, 18, 77]
list3 = [2, 3, 4, 5, 6, 7, 8]
print(fun_sort(list1))
print(fun_sort(list2))
print(fun_sort(list3))
