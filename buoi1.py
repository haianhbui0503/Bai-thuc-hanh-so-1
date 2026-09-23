#Bai 1
name= "Hai Anh"
age = 18
school = "PTIT"
print(f"Xin chào, tôi là {name}, năm nay {age} tuổi, đang học tại {school}")

#Bài2
chieu_dai = float(input())
chieu_rong = float(input())
chu_vi = (chieu_dai + chieu_rong) * 2
dien_tich=  round(chieu_dai * chieu_rong, 2)
print("Chu vi bằng:", chu_vi)
print("Diện tích bằng:", dien_tich)

#Bai3
C = int(input("Nhập số: "))
F = C * 9/5 + 32
print(C, "độ C bằng", F, "độ F")

#Bai4
Toan = float(input("Điểm Toán: "))
Van = float(input("Điểm Văn: "))
Anh = float(input("Điểm Anh: "))
trung_binh= (Toan + Van + Anh) /3
print("Điểm trung bình 3 môn là:", round(trung_binh, 2))

#Bai5
ten = "Hai Anh"
tuoi = 18
print(f"Tôi tên là {ten}, tôi {tuoi} tuổi")
print(f"Sang năm tôi sẽ {tuoi + 1} tuổi")

#Bai6
x= int(input("Nhập số: "))
if x % 2 ==0:
  print ("Số chẵn")
else:
  print("Số lẻ")

#Bai7
a=input("Nhập số a: ")
b=input("Nhập số b: ")
if a==b:
  print("Hai số a, b bằng nhau")
elif a>b:
  print(a)
elif b>a:
  print(b)

#Bai8
diem_trung_binh = float(input("Nhập điểm trung bình môn: "))
if diem_trung_binh >= 8:
  print("Giỏi")
elif 6.4 <= diem_trung_binh <= 7.9:
  print("Khá")
elif 5 <= diem_trung_binh <= 6.4:
  print("Trung bình")
else:
  print("Yếu")

#Bai9
x = float(input("Nhập số kWh điện tiêu thụ: "))
if x <= 50:
  a = int(x*1800)
  print("Tổng tiền:", a, "đồng")
if 51 <= x <= 100:
  a = int(50 * 1800 + (x-50)*2000)
  print("Tổng tiền:", a, "đồng")
if x > 100:
  a = int(50*1800 + 50*2000 + (x-100)*2500)
  print("Tổng tiền:", a, "đồng")

#Bai10
a = int(input("Nhập năm: "))
if (a %4 == 0 and a %100 !=0) or a %400 ==0:
  print (a, "là năm nhuận")
else:
  print(a, " không là năm nhuận")

#Bai11
n = int (input("Nhập một số n: "))
for i in range (1, 11):
  print (n*i)

#Bai12
n = int (input("Nhập một số n: "))
for i in range (1, n):
  n += i
print("Tổng từ 1 đến n bằng:", n)

#Bai13
n = int (input("Nhập số lượng phấn tử: "))
so_chan = 0
for i in range (n):
  x = int(input(f"Nhập số thứ {i+1}: "))
  if x %2 == 0:
    so_chan += 1
print(f"Có {so_chan} số chẵn trong dãy")

#Bai14
import random
secret = random.randint(1, 10)
doan = int(input())
while doan != secret:
  if doan > secret: 
    print("Số bí mật nhỏ hơn")
    doan=int(input())
  elif doan < secret: 
    print("Số bí mật lớn hơn")
    doan= int(input())
if doan == secret:
    print("Chúc mừng bạn đã đoán đúng!!^^")

#Bai15
n = int(input("Nhập số: "))
for i in range (1, n+1):
  print ("*" * i)



  
  


