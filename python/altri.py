#list
lst = ['1',3,5,2,'9']
len(lst)

print(lst[0])
# // 2 divisione intera
print(lst[int(len(lst) / 2)])

mixed_data_types = ["Chris","22","190","Single","Genova"]
print(len(mixed_data_types))
for val in mixed_data_types:
    print(f"Generalità: {val}")

print("#; ".join(mixed_data_types))

import sys
print(sys.argv[0], sys.argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[0], sys.argv[1]))