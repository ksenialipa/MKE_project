import random
import string
rand_string_array = []

def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    # print("Alphanum Random string of length", length, "is:", rand_string)
    return rand_string

def generate_alphanum_random_string_array(length):
    for i in range(length):
        rand_string = generate_alphanum_random_string(1) + '.' + generate_alphanum_random_string(1)
        rand_string_array.append(rand_string)
    return rand_string_array

# input_data = [ '0.' , '.4' , '.3' , '1.2' , '2' , '2.45' , '2.3' , '3.0' , '3.0' , '3.0' , '3.0' , '3.6' , '', '4.g' , 'h.3' , 'r.t' , '.' , '3dfh43.r5dg3f' ]
input_data = generate_alphanum_random_string_array(1000)

right_input_data = []
bad = []
bad_arr = []
bad_str = ''

def valid():
    j = 0
    k = 0
    for coordinate in input_data:
        j += 1
        coordinate_arr = coordinate.split('.')
        try:
            for num in coordinate_arr:
                if num != '':
                    num = int(num)
        except:
            bad.append(j)
            bad_arr.append(coordinate)
    for i in bad:
        k -= 1
        input_data.pop(i + k)
    return input_data

valid()
# for i in range(len(bad_arr)-1):
#     bad_str += bad_arr[i] + ', '
# bad_str += bad_arr[-1] + '.'
# print('\nБыли удалены следующие значения: ' + str(bad_str))

def get_right():
    for coordinate in input_data:
        coordinate_arr = coordinate.split('.')
        for i in coordinate_arr:
            if i.isalpha():
                print('плохо ' + str(coordinate))
        if len(coordinate_arr) > 1 and coordinate_arr[1] == str(0) :
            coordinate_arr[1] = ''
        elif coordinate_arr[0] == '':
            coordinate_arr[0] = '0'
        if len(coordinate_arr) > 1:
            right_coordinate = coordinate_arr[0] + '.' + coordinate_arr[1]
        else:
            right_coordinate = coordinate_arr[0] + '.' + ''
        right_input_data.append(right_coordinate)
    return right_input_data

get_right()
print('\nМассив чисел правильного формата')
print(right_input_data)

if bad_arr != []:
    for i in range(len(bad_arr)-1):
        bad_str += bad_arr[i] + ', '
    bad_str += bad_arr[-1] + '.'
    print('Были удалены следующие значения: ' + str(bad_str))

newbad = []
bad_num_str = ''
proverka = False
k = 0
bad_num_arr = []

def delete_leser_number():
    i = 0
    while i < len(right_input_data):
        if float(right_input_data[i]) <= float(right_input_data[i - 1]):
            bad_num_arr.append(right_input_data[i])
            right_input_data.pop(i)
        else:
            i += 1
    return right_input_data

delete_leser_number()
# while proverka is False:
#     if k == len(right_input_data):
#         proverka = True
#     for i in range(len(right_input_data)-1, 0 , -1):
#         if float(right_input_data[i]) <= float(right_input_data[i - 1]):
#             bad_num_arr.append(right_input_data[i])
#             right_input_data.pop(i)
#     k = len(right_input_data)
# right_input_data = str(right_input_data)

print('\nМассив последовательных чисел' + str(right_input_data))
if bad_num_arr != []:
    for i in range(len(bad_num_arr)-1):
        bad_num_str += bad_num_arr[i] + ', '
    bad_num_str += bad_num_arr[-1] + '.'
    print('Были удалены следующие значения: ' + str(bad_num_str))

grid_arr = []
grid_str = []

def make_grid():
    for i in range(len(right_input_data)):
        grid_num = str(i)
        for j in range(16-len(grid_num)):
            grid_num += ' '
        grid_x_coordinate = right_input_data[i]
        for j in range(8-len(grid_x_coordinate)):
            grid_x_coordinate += ' '
        grid_str = 'GRID    ' + grid_num + grid_x_coordinate + '0.      0.'
        grid_arr.append(grid_str)
    return grid_arr

make_grid()
print('\nМассив строк GRID:')
for i in range(len(right_input_data)):
    print(str(grid_arr[i]))