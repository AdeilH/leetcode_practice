test1 = [1,2,3,1]
test2 = [1,2,3,4]
test3 = [1,1,1,3,3,4,3,2,4,2]

def contains_duplicate(numbers) -> bool:
    duplicate = False
    length_numbers = len(numbers)
    j = length_numbers - 1
    count_of_numbers = []
    if length_numbers == 1:
        return False
    for i in range (length_numbers):
        if i >= j:
            break
        if numbers[i] == numbers[j]:
            return True
        if numbers[i] in count_of_numbers or numbers[j] in count_of_numbers:
            return True
        else:
            count_of_numbers.append(numbers[i])
            count_of_numbers.append(numbers[j])
        j -= 1
    return duplicate

print(contains_duplicate(test1))
print(contains_duplicate(test2))
print(contains_duplicate(test3))