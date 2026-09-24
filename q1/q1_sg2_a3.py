"Lyndon John F. Nicolas"
"9-Samat"
"August 15 2026"

Z_sign =[ 
    "Rat (鼠 / Shǔ)",
"Ox (牛 / Niú)",
" Tiger (虎 / Hǔ)",
 "Rabbit (兔 / Tù)",
"Dragon (龙 / Lóng)",
 "Snake (蛇 / Shé)",
 "Horse (马 / Mǎ)",
"Goat (羊 / Yáng)",
 "Monkey (猴 / Hóu)",
"Rooster (鸡 / Jī)",
 "Dog (狗 / Gǒu)",
 "Pig (猪 / Zhū)"]

birth = int(input("Enter your birth year: "))

if birth < 1900:
    print  ("Invalid year, it should not be earlier than 1900")

else:
    x = (birth - 1900)
    zodiac = x%12
    print("Your Chinese Zodiac Sign is  :" , Z_sign[zodiac])
