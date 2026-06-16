#สูตรคำนวณ BMI
def calculate_bmi(weight, height):
    bmi = weight / (height **2)
    return bmi
#ป้อนข้อมูลน้ำหนักและส่วนสูง
weight = float(input("น้ำหนัก : "))
height = float(input("ส่วนสูง : "))
#ค่าBMIของคุณ
result = calculate_bmi(weight, height)
print("BMIของคุณ เท่ากับ :",result)
#การแปลผลค่าBMI
if result < 18.5 :
    print("คุณมีค่าBMI ต่ำกว่าเกณฑ์")
elif 18.5 <= result <= 22.9 :
    print("คุณมีค่าBMI ปกติ สมส่วน")
elif 23 <= result <=24.9 :
    print("คุณมีค่าBMI น้ำหนักเกิน")
elif 25 <= result <=29.9 :
    print("คุณมีค่าBMI อ้วนระดับ1")
else :
    print("คุณมีค่าBMI อ้วนอันตราย(ระวังโรคอ้วนนะจ๊ะ)")
print("------")
print("รักสุขภาพวันนี้ ดี่กว่าเป็นโรคในวันหน้า")
