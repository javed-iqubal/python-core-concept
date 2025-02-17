
phone_number = {
    'Alec': 12345,
    'Marry': 67890,
    'Tom': 13579
}

print(phone_number)

for i in phone_number:
    print(phone_number[i])

print(f" First key: {list(phone_number)[0]} ")

print(f"first Value: {phone_number.get(list(phone_number)[0])}")

# phone_number2 = phone_number.copy()
#
# phone_number2['Marry'] = 556600
#
# phone_number3 = phone_number
#
# phone_number['Tom'] = "101010101"
#
#
# print(f"phone_number: {phone_number.items()}")
# print(f"phone_number2: {phone_number2.items()}")
# print(f"phone_number3: {phone_number3.items()}")
