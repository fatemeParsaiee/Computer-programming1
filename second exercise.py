import random

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("عدد باید بزرگتر از صفر باشد!")
                continue
            return value
        except ValueError:
            print("لطفاً فقط عدد وارد کنید!")

# دریافت تعداد اعداد تصادفی از کاربر
num_entries = get_valid_input("چند عدد تصادفی می‌خواهید؟ ")

# دریافت تعداد برندگان از کاربر
num_winners = get_valid_input("چند برنده می‌خواهید انتخاب شود؟ ")

# ساخت لیست شماره‌های تلفن
phone_numbers = []  
pre = "89"  # پیش‌شماره ثابت

for i in range(num_entries):  # تولید اعداد بر اساس ورودی کاربر
    numbers = random.randint(100000000, 999999999)  # عدد ۹ رقمی تصادفی
    phone_number = f"{pre}{numbers}"  # ساخت شماره ۱۱ رقمی
    phone_numbers.append(phone_number)

# انتخاب برندگان (بدون تکرار)
if num_winners > num_entries:
    print(f"خطا: تعداد برندگان ({num_winners}) نمی‌تواند بیشتر از تعداد اعداد ({num_entries}) باشد!")
else:
    winners = random.sample(phone_numbers, num_winners)  # انتخاب تصادفی بدون تکرار

    # نمایش برندگان با بخش میانی مخفی
    print("\nنتایج قرعه کشی:")
    print(f"تعداد شرکت کنندگان: {num_entries}")
    print(f"تعداد برندگان: {num_winners}\n")
    
    print("لیست برندگان:")
    for i, winner in enumerate(winners, 1):
        hidden_number = f"{winner[:4]}*{winner[-3:]}"  # مثلا: 8912*345
        print(f"{i}. {hidden_number} (شماره کامل: {winner})")

    # نمایش تمام اعداد تولید شده (اختیاری)
    print("\nتمام شماره‌های تولید شده:")
    for num in phone_numbers:
        print(num)
