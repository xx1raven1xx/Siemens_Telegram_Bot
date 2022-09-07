from aiogram.types import ReplyKeyboardMarkup, \
                        KeyboardButton

# Одна кнопка
btnGroup = KeyboardButton("/Group")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnGroup)

# Много кнопок
button1 = KeyboardButton("/lica_r8_val")
button2 = KeyboardButton("/lica_r5_val")
button3 = KeyboardButton("/lica_r6_val")

btn1 = KeyboardButton("/R1_R8")
btn2 = KeyboardButton("/С1_С12")

btnR1 = KeyboardButton("/lica_r1_val")
btnR2 = KeyboardButton("/lica_r2_val")
btnR3 = KeyboardButton("/lica_r3_val")
btnR4 = KeyboardButton("/lica_r4_val")
btnR5 = KeyboardButton("/lica_r5_val")
btnR6 = KeyboardButton("/lica_r6_val")
btnR7 = KeyboardButton("/lica_r7_val")
btnR8 = KeyboardButton("/lica_r8_val")

markup1 = ReplyKeyboardMarkup().add(button1).add(button2).add(button3)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3) \
                                                .add(KeyboardButton("Средняя кнопка! 👋"))

markupGroup = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1).add(btn2)

markupR = ReplyKeyboardMarkup(resize_keyboard=True).row(btnR1, btnR2, btnR3)
markupR.add(btnR4,btnR5,btnR6)
markupR.add(btnR7,btnR8,btnGroup)
# markupR = ReplyKeyboardMarkup().row(btnR7, btnR8)

# markup3.row(KeyboardButton("4"), KeyboardButton("5"))
# markup3.insert(KeyboardButton("6"))
# markup3.add(KeyboardButton("Новая строка"))

# Кнопки отправки контакта и геолокации
markup_requests = ReplyKeyboardMarkup(resize_keyboard=True) \
  .add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(KeyboardButton('Отправить свою геолокацию', request_location=True))