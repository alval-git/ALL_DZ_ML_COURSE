

def find_min_max(list_of_numbers):
    if len(list_of_numbers) < 2:
        print("В списке менее двух чисел")
        return 0
    
    min = list_of_numbers[0]
    max = list_of_numbers[0]

    for i in list_of_numbers:
        if min > i:
            min = i
        if max < i:
            max = i
    
    result = (min, max)
    print(result)

    return result


find_min_max([0,25,9,7,7,2,7,0,-10,12])