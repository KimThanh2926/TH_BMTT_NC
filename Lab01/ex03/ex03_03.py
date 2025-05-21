def tao_tuple_tu_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List:",numbers)
print("Tuple tu list:", my_tuple)