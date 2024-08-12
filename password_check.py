print('---------------------------------------------\n '
      'ПРАВИЛА НАДЕЖНОГО ПАРОЛЯ\n '
      '---------------------------------------------')

print('1) Длинна пароля должна быть не менее - 15\n'
      '2) Количество заглавных букв должно быть не менее - 5\n'
      '3) Количество чилес должно быть не менее - 5\n'
      '4) Количество повторяющихся букв не должно превышать - 5\n'
      '5) Сумма повторений букв не далжна превышать - 5\n')

password = input('Напишите пароль - ')
upperCount = 0
numberCount = 0
letter_count = {}

for letter in password:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

repeating_letters = {key: value for key, value in letter_count.items() if value > 1}
sum_repeated_letters = sum(count - 1 for count in letter_count.values() if count > 1)

for letter in password:
    if letter.isupper():
        upperCount += 1

for number in password:
    if number.isdigit():
        numberCount += 1

if (len(password) >= 15 and upperCount >= 5 and numberCount >= 5 and len(repeating_letters) <= 5 and sum_repeated_letters <= 5):
    print('\nПароль надежный\n')
else:
    print('\nПароль ненадженый, напишите снова\n')

print(f'Длинна пароля - {len(password)}')
print(f'Количество заглавных букв - {upperCount}')
print(f'Количество чисел - {numberCount}')
print(f'Сколько раз повторяеться буква - {repeating_letters}')
print(f'Количество повторяющихся букв - {len(repeating_letters)}')
print(f'Сумма повторений букв - {sum_repeated_letters}')
