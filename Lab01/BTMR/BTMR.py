def cau1():
    import itertools
    my_list = [1, 2, 3]
    permutations = list(itertools.permutations(my_list))
    print(f"Các hoán vị của {my_list} là:")
    for p in permutations:
        print(p)

def cau2():
    import re
    input_string = input("Nhập chuỗi: ")
    numbers_str = re.findall(r'-?\d+', input_string)
    positive_sum = 0
    negative_sum = 0
    for num_str in numbers_str:
        num = int(num_str)
        if num >= 0:
            positive_sum += num
        else:
            negative_sum += num
    print(f"Chuỗi ban đầu là: \"{input_string}\"")
    print(f"Giá trị dương: {positive_sum}")
    print(f"Giá trị âm: {negative_sum}")

# Vòng lặp menu
while True:
    choice = input("\nChọn câu (1, 2) hoặc 't' để thoát: ").strip()

    match choice:
        case "1":
            cau1()
        case "2":
            cau2()
        case "t" | "T":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ!")