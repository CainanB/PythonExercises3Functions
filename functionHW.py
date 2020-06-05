# # Exercise 1
# def madlib(name, subject):
#     print(f"""
#     {name}'s favorite subject is {subject}
#     """)

# madlib("Cainan", "Math")

# # Exercise 2

# def c_to_f(temp_c):
#     temp_f = (temp_c * 9/5) + 32
#     return temp_f

# converted_ctemp = c_to_f(100)

# # Exercise 3

# def f_to_c(temp_f):
#     temp_c = (temp_f - 32) * 5/9
#     return temp_c

# converted_ftemp = f_to_c(100)

# # Exercise 4

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# # Exercise 5
# def is_odd(num):
#     answer = is_even(num)
#     return not answer

# print(is_odd(5))

# # Exercise 6
# def only_evens(num_list):
#     even_nums_list = []
#     for num in num_list:
#         if is_even(num):
#             even_nums_list.append(num)
#     return even_nums_list

# print(only_evens([11, 20, 42, 97, 23, 10]))

# # Exercise 7
# def only_odds(num_list):
#     odds_num_list = []
#     for num in num_list:
#         if is_odd(num):
#             odds_num_list.append(num)
#     return odds_num_list
# print(only_odds([11, 20, 42, 97, 23, 10]))

# Medium #1

# def smallest(num_list):
#     current_small = num_list[0]
#     for num in num_list:
#         if num < current_small:
#             current_small = num
#     return current_small
# #print(smallest([3,7,9,24,6,7,-8]))

# # Medium #1 Option 2

# def smallest_2(num_list):
#     num_list.sort()
#     return num_list[0]

# print(smallest_2([3,7,9,24,6,7,-8]))
# # Medium # 2


# def largest(num_list):
#     current_large = num_list[0]
#     for num in num_list:
#         if num > current_large:
#             current_large = num
#     return current_large
# #print(largest([3,7,9,24,6,7,-8]))

# # Medium # 2 option 2

# def largest_2(num_list):
#     num_list.sort()
#     return num_list[len(num_list)-1]

# print(largest_2([3,7,9,24,6,7,-8]))
# Medium # 3

def shortest_string(string_list):
    current_shortest_str = string_list[0]
    current_shortest_str_len = len(string_list[0])

    for current_str in string_list:
        if len(current_str) < current_shortest_str_len:
            current_shortest_str = current_str
            current_shortest_str_len = len(current_str)
    return current_shortest_str
print(shortest_string(["Cainan", "Dog", "Table", "Airplane"]))

# Medium #3 Option 2


# Medium # 4

def longest_string(string_list):
    current_longest_str = string_list[0]
    current_longest_str_len = len(string_list[0])

    for current_str in string_list:
        if len(current_str) > current_longest_str_len:
            current_longest_str = current_str
            current_longest_str_len = len(current_str)
    return current_longest_str
print(longest_string(["Cainan", "Dog", "Table", "Airplane"]))







