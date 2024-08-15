def calculate_average(numbs):
    total = sum(numbs)
    count = len(numbs)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
