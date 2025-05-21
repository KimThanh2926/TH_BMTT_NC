def so_chia_het_cho_5(so_nhi_phan):
    return int(so_nhi_phan, 2) % 5 == 0

lst = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ").split(',')
kq = [so for so in lst if so_chia_het_cho_5(so)]

print(f"Số nhị phân chia hết cho 5 là: {','.join(kq)}" if kq else "Không có giá trị nào chia hết cho 5 trong chuỗi đã nhập.")
