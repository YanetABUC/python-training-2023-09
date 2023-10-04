#exercise average of list of numbers
def calculate_average(list_numbers_to_calculate_average):
    if len(list_numbers_to_calculate_average) == 0:
        return "List of numbers is empty"

    result_average = sum(list_numbers_to_calculate_average)   
    result_average = round(result_average/len(list_numbers_to_calculate_average), 2)
    return result_average

list_numbers_by_user = input("Enter a list of integers separated by a comma (Ex: 2,1.2,3): ").split(",")
list_numbers = []

for str_num in list_numbers_by_user:
    list_numbers.append(int(str_num))

average = calculate_average(list_numbers)

print(f"The average is: {average}")