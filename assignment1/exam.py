

# #4# Read input
# N = int(input())
# numbers = list(map(int, input().split()))

# # Function to count the number of operations
# def count_operations(arr):
#     operations = 0
#     while all(num % 2 == 0 for num in arr):
#         arr = [num // 2 for num in arr]
#         operations += 1
#     return operations

# # Count the operations and print the result
# operations = count_operations(numbers)
# print(operations)



# 2 with directory # Read input
# N = int(input())
# sequence = list(map(int, input().split()))
# print(sequence)
# # Count occurrences of each number
# count = {}
# for num in sequence:
#     count[num] = count.get(num, 0) + 1

# # Calculate the minimum number of elements to be removed
# removals = 0
# range=count.items()
# for num, freq in range:
#     if freq > num:
#         removals += freq - num
#     elif freq < num:
#         removals += freq

# # Print the result
# print(removals)


# 2 with list
# n = int(input())
# store = list(map(int, input().split()))

# # Creating a list 
# count = [0] * (max(store) + 1)

# # Counting occurrence of every numbedr
# for num in store:
#     count[num] += 1

# # Calculating  minimum number of elements to remove that
# rem_cnt = 0
# iterator =enumerate(count);
# for index, value in len:
#     #print(index," ",value)
#     if value > index:
#         rem_cnt += value - index
#     elif value < index:
#         rem_cnt += value

# print(rem_cnt)



# #done
# #taking input
# input_L_and_R = input()

# # Initialization
# balanced_str = []
# curr_str = ""
# balance_cnt = 0

# # counting and storing
# for c in input_L_and_R:
#     curr_str =curr_str+ c
#     if c == 'R':
#         balance_cnt =balance_cnt+ 1
#     else:
#         balance_cnt =balance_cnt- 1
    
#     # when we get same to same we append
#     if balance_cnt == 0:
#         balanced_str.append(curr_str)
#         curr_str = ""

# # Output
# print(len(balanced_str))
# for str in balanced_str:
#     print(str)
