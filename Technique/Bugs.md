Hàm strncat() sẽ copy chuỗi name vào chuỗi bullet.name, sau đó sẽ thêm 1 ký tự NULL vào cuối chuỗi. => có thể dẫn đến off-by-one => thay đổi size dẫn đến check size bị sai kết quả. 
