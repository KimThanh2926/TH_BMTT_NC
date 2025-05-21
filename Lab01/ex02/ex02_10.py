def dao_so_nguoc(chuoi):
    return chuoi[::-1]

input_string= input("Nhập vào chuỗi cần đổi ngược:")
print("Chuỗi cần đảo ngược là", dao_so_nguoc(input_string))