hoten = input("Nhập họ và tên của mình: ")
print("Họ và tên:", hoten)
def thuannghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;


n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", thuannghich(n));
m = int(input("Nhập số nguyên dương m = "));
print("Tổng các chữ số của", m, "là", thuannghich(m));

