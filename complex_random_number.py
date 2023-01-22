import random
import json

start = int(input("Enter starting num: "))
end = int(input("Enter ending num: "))
count = int(input("Enter count: "))
num_type = input("Enter 'i' for ints and 'f' for floats: ")
distribution = input("Enter 'u' for uniform or 'n' for normal: ")
seed = input("Enter seed or leave blank: ")
file_name = input("Enter file name or leave blank: ")

if seed:
    random.seed(int(seed))

nums = []
for i in range(count):
    if num_type == "i":
        nums.append(random.randint(start, end))
    elif num_type == "f":
        if distribution == "u":
            nums.append(random.uniform(start, end))
        elif distribution == "n":
            nums.append(random.normalvariate(start, end))
    else:
        print("Invalid input")
        break

if file_name:
    with open(file_name, "w") as f:
        json.dump(nums, f)
    print(f"Numbers saved to {file_name}")
else:
    print(nums)