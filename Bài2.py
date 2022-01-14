tendem = input("Nhập tên đệm của mình: ")
print("Tên đệm:", tendem)
def tongsonguyen(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;


n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", tongsonguyen(n));

