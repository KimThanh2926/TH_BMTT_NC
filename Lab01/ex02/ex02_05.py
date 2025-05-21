sogiolam = float(input("Nhập số giờ làm: "))
luonggio = float(input("Nhập thù lao trên mỗi giờ tiêu chuẩn: "))
giotieuchuan= 44
giovuotchuan = max(0,sogiolam - giotieuchuan )
thuclinh= giotieuchuan*luonggio + giovuotchuan*luonggio*1.5 #tinhs tong thu nhap
print(f"Số tiền thực lĩnh của nhân viên: {thuclinh}")