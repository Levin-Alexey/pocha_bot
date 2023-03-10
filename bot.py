import telebot
from telebot import types
token = "5979919901:AAFMoPDdUiKaq-9H8BeBY6qgPRzz-iASC_4"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboardmain = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Балашиха", callback_data="balashiha")
    keyboardmain.add(button1)
    button2 = types.InlineKeyboardButton(text="Воскресенск", callback_data="voskres")
    keyboardmain.add(button2)
    button3 = types.InlineKeyboardButton(text="Дмитров", callback_data="dmitrov")
    keyboardmain.add(button3)
    button4 = types.InlineKeyboardButton(text="Домодедово", callback_data="domoded")
    keyboardmain.add(button4)
    button5 = types.InlineKeyboardButton(text="Кашира", callback_data="kashira")
    keyboardmain.add(button5)
    button6 = types.InlineKeyboardButton(text="Коломна", callback_data="kolomna")
    keyboardmain.add(button6)
    button7 = types.InlineKeyboardButton(text="Красногорск", callback_data="kras")
    keyboardmain.add(button7)
    button8 = types.InlineKeyboardButton(text="Люберцы", callback_data="luber")
    keyboardmain.add(button8)
    button9 = types.InlineKeyboardButton(text="Мытищи", callback_data="mitishi")
    keyboardmain.add(button9)
    button10 = types.InlineKeyboardButton(text="Наро - Фоминск", callback_data="balashiha")
    keyboardmain.add(button10)
    button11 = types.InlineKeyboardButton(text="Одинцово", callback_data="odin")
    keyboardmain.add(button11)
    button12 = types.InlineKeyboardButton(text="Орехово-Зуево", callback_data="oreh")
    keyboardmain.add(button12)
    button13 = types.InlineKeyboardButton(text="Подольск", callback_data="podol")
    keyboardmain.add(button13)
    button14 = types.InlineKeyboardButton(text="Пушкинский", callback_data="pushki")
    keyboardmain.add(button14)
    button15 = types.InlineKeyboardButton(text="Химки", callback_data="balashiha")
    keyboardmain.add(button15)
    bot.send_message(message.chat.id, "Выберете Ваш почтамт", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=3)
        button1 = types.InlineKeyboardButton(text="Балашиха", callback_data="balashiha")
        keyboardmain.add(button1)
        button2 = types.InlineKeyboardButton(text="Воскресенск", callback_data="voskres")
        keyboardmain.add(button2)
        button3 = types.InlineKeyboardButton(text="Дмитров", callback_data="dmitrov")
        keyboardmain.add(button3)
        button4 = types.InlineKeyboardButton(text="Домодедово", callback_data="domoded")
        keyboardmain.add(button4)
        button5 = types.InlineKeyboardButton(text="Кашира", callback_data="kashira")
        keyboardmain.add(button5)
        button6 = types.InlineKeyboardButton(text="Коломна", callback_data="kolomna")
        keyboardmain.add(button6)
        button7 = types.InlineKeyboardButton(text="Красногорск", callback_data="kras")
        keyboardmain.add(button7)
        button8 = types.InlineKeyboardButton(text="Люберцы", callback_data="luber")
        keyboardmain.add(button8)
        button9 = types.InlineKeyboardButton(text="Мытищи", callback_data="mitishi")
        keyboardmain.add(button9)
        button10 = types.InlineKeyboardButton(text="Наро - Фоминск", callback_data="nara")
        keyboardmain.add(button10)
        button11 = types.InlineKeyboardButton(text="Одинцово", callback_data="odin")
        keyboardmain.add(button11)
        button12 = types.InlineKeyboardButton(text="Орехово-Зуево", callback_data="oreh")
        keyboardmain.add(button12)
        button13 = types.InlineKeyboardButton(text="Подольск", callback_data="podol")
        keyboardmain.add(button13)
        button14 = types.InlineKeyboardButton(text="Пушкинский", callback_data="pushki")
        keyboardmain.add(button14)
        button15 = types.InlineKeyboardButton(text="Химки", callback_data="himki")
        keyboardmain.add(button15)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете Ваш почтамт",reply_markup=keyboardmain)

    if call.data == "himki":
        keyboard_himki = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Химки", callback_data="himki1")
        keyboard_himki.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Солнечногорск и район", callback_data="solnech")
        keyboard_himki.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Клин и район", callback_data="klin")
        keyboard_himki.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_himki.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_himki)

    elif call.data == "klin":
        keyboard_klin = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="klin_kom")
        keyboard_klin.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="klin_kon_kom")
        keyboard_klin.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="klin")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_klin)

    elif call.data == "klin_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_klin_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="klin")
        keyboard_klin_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_klin_kom)


    elif call.data == "klin_kon_kom":
        keyboard_klin_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_klin")
        keyboard_klin_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_klin")
        keyboard_klin_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_klin")
        keyboard_klin_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="klin")
        keyboard_klin_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_klin_kon_kom)

    elif call.data == "sber_klin":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_klin = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="klin")
        keyboard_sber_klin.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 11 офисов 13 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_klin)


    elif call.data == "vtb_klin":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_klin = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="klin_kon_kom")
        keyboard3_vtb_klin.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 6 банкоматов)\n Под какой % принимают платежи  наличными в кассе.\nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_klin)

    elif call.data == "moe_solnech":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_solnech = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboard3_moe_solnech.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 3 терминала)\nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МОЕ р/сч 6635 без комиссии, МОЕ р/сч 6799-  0,99 % \nСвет - Терминал МКБ  1%  \nГаз - не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_solnech)



    elif call.data == "solnech":
        keyboard_solnech = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="solnech_kom")
        keyboard_solnech.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="solnech_kon_kom")
        keyboard_solnech.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_solnech)

    elif call.data == "solnech_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_solnech_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboard_solnech_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_solnech_kom)

    elif call.data == "solnech_kon_kom":
        keyboard_solnech_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_solnech")
        keyboard_solnech_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_solnech")
        keyboard_solnech_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_solnech")
        keyboard_solnech_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboard_solnech_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_solnech_kon_kom)


    elif call.data == "sber_solnech":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_solnech = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboard_sber_solnech.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 8 офисов 18 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_solnech)

    elif call.data == "moe_solnech":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_solnech = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="solnech")
        keyboard3_moe_solnech.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 2 терминала)\nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МОЕ р/сч 6635 без комиссии, МОЕ р/сч 6799-  0,99 % \nСвет - Терминал МКБ  1,5 %  \nГаз - не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_solnech)


    elif call.data == "vtb_solnech":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_solnech = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="solnech_kon_kom")
        keyboard3_vtb_solnech.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (5 офисов 5 банкоматов)\n Под какой % принимают платежи  наличными в кассе.\nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_solnech)


    elif call.data == "himki1":
        keyboard_himki1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="himki1_kom")
        keyboard_himki1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="himki1_kon_kom")
        keyboard_himki1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_himki1)

    elif call.data == "himki1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_himki1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboard_himki1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_himki1_kom)

    elif call.data == "himki1_kon_kom":
        keyboard_himki1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_himki1")
        keyboard_himki1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ Юбилейная 67", callback_data="moe_himki1")
        keyboard_himki1_kon_kom.add(rele2)
        rele4 = types.InlineKeyboardButton(text="МОЕ Гоголя 9", callback_data="moe9_himki1")
        keyboard_himki1_kon_kom.add(rele4)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_himki1")
        keyboard_himki1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboard_himki1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_himki1_kon_kom)

    elif call.data == "vtb_himki1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_himki1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="himki1_kon_kom")
        keyboard3_vtb_himki1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (5 офисов 5 банкоматов)\n Под какой % принимают платежи  наличными в кассе.\nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_himki1)

    elif call.data == "moe_himki1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_himki1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboard3_moe_himki1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис)\nОплата наличными: МОЕ - МОЕ р/сч 6635 без комиссии, МОЕ р/сч  6799 - 1,78%\nОплата наличными других поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МОЕ р/сч 6635 без комиссии, МОЕ р/сч  6799 - 1,78% \nСвет - Терминал МКБ  1,5 %  \nГаз - не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_himki1)


    elif call.data == "moe9_himki1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe9_himki1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboard3_moe9_himki1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис)\nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МОЕ р/сч 6635 без комиссии, МОЕ р/сч 6799-  0,99 %\nСвет - Терминал МКБ  1,5 %  \nГаз - не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe9_himki1)

    elif call.data == "sber_himki1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_himki1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="himki1")
        keyboard_sber_himki1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 13 офисов 30 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_himki1)


    elif call.data == "krasno":
        keyboard_krasno = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="krasno_kom")
        keyboard_krasno.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="krasno_kon_kom")
        keyboard_krasno.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="krasno")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_krasno)

    elif call.data == "krasno_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_krasno_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="krasno")
        keyboard_krasno_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_krasno_kom)

    elif call.data == "krasno_kon_kom":
        keyboard_krasno_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_krasno")
        keyboard_krasno_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_krasno")
        keyboard_krasno_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="krasno")
        keyboard_krasno_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_krasno_kon_kom)


    elif call.data == "moe_krasno":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_krasno = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="krasno")
        keyboard3_moe_krasno.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ \nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_krasno)


    elif call.data == "sber_krasno":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_krasno = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="krasno")
        keyboard_sber_krasno.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 13 офисов 30 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_krasno)





    elif call.data == "ivanteevka":
        keyboard_ivanteevka = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="ivanteevka_kom")
        keyboard_ivanteevka.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="ivanteevka_kon_kom")
        keyboard_ivanteevka.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ivanteevka")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_ivanteevka)

    elif call.data == "ivanteevka_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_ivanteevka_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ivanteevka")
        keyboard_ivanteevka_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_ivanteevka_kom)


    elif call.data == "ivanteevka_kon_kom":
        keyboard_ivanteevka_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_ivanteevka")
        keyboard_ivanteevka_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_ivanteevka")
        keyboard_ivanteevka_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ivanteevka")
        keyboard_ivanteevka_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_ivanteevka_kon_kom)

    elif call.data == "moe_ivanteevka":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_ivanteevka = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ivanteevka")
        keyboard3_moe_ivanteevka.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ \nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_ivanteevka)


    elif call.data == "sber_ivanteevka":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_ivanteevka = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ivanteevka")
        keyboard_sber_ivanteevka.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 13 офисов 30 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_ivanteevka)


    elif call.data == "pushkino":
        keyboard_pushkino = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="pushkino_kom")
        keyboard_pushkino.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="pushkino_kon_kom")
        keyboard_pushkino.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="pushkino")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_pushkino)

    elif call.data == "pushkino_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_pushkino_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushkino")
        keyboard_pushkino_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_pushkino_kom)

    elif call.data == "pushkino_kon_kom":
        keyboard_pushkino_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_pushkino")
        keyboard_pushkino_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_pushkino")
        keyboard_pushkino_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_pushkino")
        keyboard_pushkino_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="pushkino")
        keyboard_pushkino_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_pushkino_kon_kom)

    elif call.data == "sber_pushkino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_pushkino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushkino")
        keyboard_sber_pushkino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 13 офисов 30 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_pushkino)


    elif call.data == "vtb_pushkino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_pushkino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushkino_kon_kom")
        keyboard3_vtb_pushkino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_pushkino)

    elif call.data == "moe_pushkino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_pushkino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushkino")
        keyboard3_moe_pushkino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ \nОплата наличными поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_pushkino)



    elif call.data == "sergiev":
        keyboard_sergiev = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="sergiev_kom")
        keyboard_sergiev.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="sergiev_kon_kom")
        keyboard_sergiev.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="sergiev")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_sergiev)


    elif call.data == "sergiev_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sergiev_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="sergiev")
        keyboard_sergiev_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_sergiev_kom)

    elif call.data == "sergiev_kon_kom":
        keyboard_sergiev_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_sergiev")
        keyboard_sergiev_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_sergiev")
        keyboard_sergiev_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_sergiev")
        keyboard_sergiev_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="СППА", callback_data="sppa_sergiev")
        keyboard_sergiev_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="sergiev")
        keyboard_sergiev_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_sergiev_kon_kom)

    elif call.data == "moe_sergiev":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_sergiev = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="sergiev")
        keyboard3_moe_sergiev.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ ( 1  офис  в Сергиев - Посаде , гор Хотьково- 2 офиса, гор Пересвет- 2 кассы, МКБ терминалы 24 шт)\nМОЕ - Расчетный счет 6799-3%, Расчетный счет 6635-0%. Оплата наличными других поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_sergiev)


    elif call.data == "sber_sergiev":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_sergiev = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="sergiev")
        keyboard_sber_sergiev.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 8 офисов 24 банкомата/терминала)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_sergiev)

    elif call.data == "vtb_sergiev":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_sergiev = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="sergiev_kon_kom")
        keyboard3_vtb_sergiev.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 12 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_sergiev)

    elif call.data == "sppa_sergiev":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_sppa_sergiev = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="sergiev_kon_kom")
        keyboard3_sppa_sergiev.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (9 касс)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 0,024%\nСвет - 2,5%, min 10 руб.\nГАЗ - 3%, мin 10 руб.\nОплаты картой нет\n",reply_markup=keyboard3_sppa_sergiev)


    if call.data == "podol":
        keyboard_podol = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Подольск", callback_data="podol1")
        keyboard_podol.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Чехов и район", callback_data="cheh")
        keyboard_podol.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Серпухов и район", callback_data="serp")
        keyboard_podol.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Пущино", callback_data="pushi")
        keyboard_podol.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_podol.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_podol)

    elif call.data == "pushi":
        keyboard_pushi = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="pushi_kom")
        keyboard_pushi.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="pushi_kon_kom")
        keyboard_pushi.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="pushi")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_pushi)



    elif call.data == "pushi_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_pushi_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushi")
        keyboard_pushi_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_pushi_kom)

    elif call.data == "pushi_kon_kom":
        keyboard_pushi_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_pushi")
        keyboard_pushi_kon_kom.add(rele1)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_pushi")
        keyboard_pushi_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="pushi")
        keyboard_pushi_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_pushi_kon_kom)

    elif call.data == "sber_pushi":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_pushi = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushi")
        keyboard_sber_pushi.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк \nКомиссия при оплате наличными в кассе:\nМОЕ - Все квитанции МОЕ - 3% минимум 50 руб. мах 5000 руб\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\nМОЕ - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nСвет -  через терминал 1,2%, личный кабинет 1% , максимум 500 руб.\nГаз - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nГИБДД - 1,2 % максимум 500 руб. (по карте), счету комиссия 2%, мин. 10р., макс. 2000 руб. (сторонней картой, наличными).\nРостелеком - в окне картой  3%  картой; в терминале наличными  2,5% мин 5,00;  без %  картой в терминале.\nМобильная связь - без комиссии.\n",reply_markup=keyboard_sber_pushi)

    elif call.data == "vtb_pushi":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_pushi = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pushi_kon_kom")
        keyboard3_vtb_pushi.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_pushi)


    elif call.data == "serp":
        keyboard_serp = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="serp_kom")
        keyboard_serp.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="serp_kon_kom")
        keyboard_serp.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_serp)

    elif call.data == "serp_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_serp_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboard_serp_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_serp_kom)

    elif call.data == "serp_kon_kom":
        keyboard_serp_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_serp")
        keyboard_serp_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_serp")
        keyboard_serp_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_serp")
        keyboard_serp_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="ПАО ПСБ", callback_data="psb_serp")
        keyboard_serp_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboard_serp_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_serp_kon_kom)

    elif call.data == "moe_serp":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_serp = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboard3_moe_serp.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\n1 офис и 2 терминала. Принимают только оплату картой за МОЕ - 1,5% Свет - без комиссии.\n", reply_markup=keyboard3_moe_serp)

    elif call.data == "psb_serp":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_psb_serp = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboard_psb_serp.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\n1 офис 10 банкоматов. Оплату наличными не принимают.\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nВсе контрагенты оплачиваются без комиссии. ГИБДД - Оплата через личный кабинет он-лайн, через банкомат и терминал для владельцев карт банка 1%, мин. 30 руб. до 1000 руб.\n", reply_markup=keyboard_psb_serp)

    elif call.data == "sber_serp":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_serp = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serp")
        keyboard_sber_serp.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк \nКомиссия при оплате наличными в кассе:\nМОЕ - Все квитанции МОЕ - 3% минимум 50 руб. мах 5000 руб\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\nМОЕ - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nСвет -  через терминал 1,2%, личный кабинет 1% , максимум 500 руб.\nГаз - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nГИБДД - 1,2 % максимум 500 руб. (по карте), счету комиссия 2%, мин. 10р., макс. 2000 руб. (сторонней картой, наличными).\nРостелеком - в окне картой  3%  картой; в терминале наличными  2,5% мин 5,00;  без %  картой в терминале.\nМобильная связь - без комиссии.\n",reply_markup=keyboard_sber_serp)

    elif call.data == "vtb_serp":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_serp = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serp_kon_kom")
        keyboard3_vtb_serp.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_serp)


    elif call.data == "cheh":
        keyboard_cheh = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="cheh_kom")
        keyboard_cheh.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="cheh_kon_kom")
        keyboard_cheh.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="cheh")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_cheh)

    elif call.data == "cheh_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_cheh_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="cheh")
        keyboard_cheh_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_cheh_kom)

    elif call.data == "cheh_kon_kom":
        keyboard_cheh_kon_kom = types.InlineKeyboardMarkup()
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_cheh")
        keyboard_cheh_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_cheh")
        keyboard_cheh_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="cheh")
        keyboard_cheh_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_cheh_kon_kom)

    elif call.data == "moe_cheh":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_cheh = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="cheh")
        keyboard3_moe_cheh.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\n1 касса. Принимают без комиссии оптау наличными и картой за МОЕ, Свет, Газ. Остальных поставщиков оплатить невозможно\n", reply_markup=keyboard3_moe_cheh)

    elif call.data == "vtb_cheh":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_cheh = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="cheh_kon_kom")
        keyboard3_vtb_cheh.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_cheh)


    elif call.data == "podol1":
        keyboard_podol1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="podol1_kom")
        keyboard_podol1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="podol1_kon_kom")
        keyboard_podol1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_podol1)

    elif call.data == "podol1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_podol1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboard_podol1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_podol1_kom)


    elif call.data == "podol1_kon_kom":
        keyboard_podol1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_podol1")
        keyboard_podol1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_podol1")
        keyboard_podol1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_podol1")
        keyboard_podol1_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="ПАО ПСБ", callback_data="psb_podol1")
        keyboard_podol1_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboard_podol1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_podol1_kon_kom)

    elif call.data == "moe_podol1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_podol1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboard3_moe_podol1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\n4 офиса 2 терминала. Оплата принимается по тарифам банкоматов Сбер и ВТБ\n", reply_markup=keyboard3_moe_podol1)


    elif call.data == "sber_podol1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_podol1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboard_sber_podol1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 22 офиса 32 банкомата 47 терминала)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\nМОЕ - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nСвет -  через терминал 1,2%, личный кабинет 1% , максимум 500 руб.\nГаз - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nГИБДД - 1,2 % максимум 500 руб. (по карте), счету комиссия 2%, мин. 10р., макс. 2000 руб. (сторонней картой, наличными).\nРостелеком - в окне картой  3%  картой; в терминале наличными  2,5% мин 5,00;  без %  картой в терминале.\nМобильная связь - без комиссии.\n",reply_markup=keyboard_sber_podol1)


    elif call.data == "psb_podol1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_psb_podol1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="podol1")
        keyboard_psb_podol1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n1 офис 10 банкоматов. Оплату наличными не принимают.\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nВсе контрагенты оплачиваются без комиссии. ГИБДД - Оплата через личный кабинет он-лайн, через банкомат и терминал для владельцев карт банка 1%, мин. 30 руб. до 1000 руб.\n",reply_markup=keyboard_psb_podol1)

    elif call.data == "vtb_podol1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_podol1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="podol1_kon_kom")
        keyboard3_vtb_podol1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_podol1)





    if call.data == "oreh":
        keyboard_oreh = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Орехово - Зуево и район", callback_data="oreh1")
        keyboard_oreh.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Павлово - Посад и район", callback_data="pavel")
        keyboard_oreh.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Шатура и район", callback_data="shatura")
        keyboard_oreh.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_oreh.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_oreh)




    elif call.data == "shatura":
        keyboard_shatura = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="shatura_kom")
        keyboard_shatura.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="shatura_kon_kom")
        keyboard_shatura.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data=shatura)
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_shatura)

    elif call.data == "shatura_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_shatura_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_shatura_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_shatura_kom)


    elif call.data == "shatura_kon_kom":
        keyboard_shatura_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_shatura")
        keyboard_shatura_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_shatura")
        keyboard_shatura_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_shatura")
        keyboard_shatura_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_shatura_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_shatura_kon_kom)

    elif call.data == "sber_shatura":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_shatura = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_sber_shatura.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 5 офисов 11 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии, р/с 6635\nСвет - Без комиссии/входит в общую квитанцию\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  без комиссии\nСвет -  без комиссии\nГаз -  2,5% (картой на кассе)1,2% (картой в банкомате)\nГИБДД - 2,5% (картой на кассе)1,2% (картой в банкомате)\nРостелеком - 2 % (картой на кассе) 1,2% (картой в банкомате)\nМобильная связь - 2 % (картой на кассе) 1,2% (картой в банкомате)\n",reply_markup=keyboard_sber_shatura)

    elif call.data == "moe_shatura":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_shatura = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard3_moe_shatura.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\nОплата принимается картой. МОЕ - без комиссии\n", reply_markup=keyboard3_moe_shatura)


    elif call.data == "vtb_shatura":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_shatura = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura_kon_kom")
        keyboard3_vtb_shatura.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_shatura)




    elif call.data == "pavel":
        keyboard_pavel = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="pavel_kom")
        keyboard_pavel.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="pavel_kon_kom")
        keyboard_pavel.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data=pavel)
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_pavel)

    elif call.data == "pavel_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_pavel_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pavel")
        keyboard_pavel_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_pavel_kom)

    elif call.data == "pavel_kon_kom":
        keyboard_pavel_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_pavel")
        keyboard_pavel_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_pavel")
        keyboard_pavel_kon_kom.add(rele2)
        rele4 = types.InlineKeyboardButton(text="ЖилСервис-Посад", callback_data="gsp_pavel")
        keyboard_pavel_kon_kom.add(rele4)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_pavel")
        keyboard_pavel_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="pavel")
        keyboard_pavel_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_pavel_kon_kom)

    elif call.data == "sber_pavel":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_pavel = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pavel")
        keyboard_sber_pavel.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офисов 16 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии, р/с 6635\nСвет - Без комиссии/входит в общую квитанцию\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  без комиссии\nСвет -  без комиссии\nГаз -  2,5% (картой на кассе)1,2% (картой в банкомате)\nГИБДД - 2,5% (картой на кассе)1,2% (картой в банкомате)\nРостелеком - 2 % (картой на кассе) 1,2% (картой в банкомате)\nМобильная связь - 2 % (картой на кассе) 1,2% (картой в банкомате)\n",reply_markup=keyboard_sber_pavel)

    elif call.data == "moe_pavel":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_pavel = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pavel")
        keyboard3_moe_pavel.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\nКасса МОЕ. 4 офиса. Прием оплаты за МОЕ картой и наличными - без комиссии.\n", reply_markup=keyboard3_moe_pavel)

    elif call.data == "vtb_pavel":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_pavel = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pavel_kon_kom")
        keyboard3_vtb_pavel.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_pavel)


    elif call.data == "gsp_pavel":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_gsp_pavel = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="pavel_kon_kom")
        keyboard3_gsp_pavel.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nРКЦ ЖилСервис-Посад (12 офисов 5 терминалов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1%, 6635 без комисии\nСвет - 1.5%, мin 200, мах 3000 руб\nГаз - 1,5%\nГИБДД - не принимают.\nРостелеком - 1.5%\nСотовая связь - 1,5%.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 2% с клиента.\nСвет - 2% с клиента.\nГаз - 2% с клиента.\nГИБДД - 2% с клиента\nРостелеком - 2% с клиента\nСотовая связь - 2% с клиента\n",reply_markup=keyboard3_gsp_pavel)


    elif call.data == "oreh1":
        keyboard_oreh1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="oreh1_kom")
        keyboard_oreh1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="oreh1_kon_kom")
        keyboard_oreh1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="oreh1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_oreh1)

    elif call.data == "oreh1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_oreh1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="oreh1")
        keyboard_oreh1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_oreh1_kom)


    elif call.data == "oreh1_kon_kom":
        keyboard_oreh1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_oreh1")
        keyboard_oreh1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="ЕСГП", callback_data="esgp_oreh1")
        keyboard_oreh1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_oreh1")
        keyboard_oreh1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="oreh1")
        keyboard_oreh1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_oreh1_kon_kom)


    elif call.data == "vtb_oreh1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_oreh1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="oreh1_kon_kom")
        keyboard3_vtb_oreh1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_oreh1)


    elif call.data == "esgp_oreh1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_esgp_oreh1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="oreh1")
        keyboard3_esgp_oreh1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nЕСГП Московской области. 2 кассы \nПод какой % принимают платежи  наличными в кассе\nМОЕ - 3% не менее 50 руб.\nСвет -3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая свзяь - не принимают\n",reply_markup=keyboard3_esgp_oreh1)

    elif call.data == "sber_oreh1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_oreh1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="oreh1")
        keyboard_sber_oreh1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 5 офисов 23 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  2,5% мин.50 р (картой на кассе) 1,2% (картой в банкомате).\nСвет -  2,5% (картой на кассе) 1,2% (картой в банкомате)\nГаз -  2,5% (картой на кассе) 1,2% (картой в банкомате)\nГИБДД - 2,5% (картой на кассе) 1,2% (картой в банкомате)\nРостелеком - 2 % (картой на кассе) 1,2% (картой в банкомате)\nМобильная связь - 2 % (картой на кассе) 1,2% (картой в банкомате)\n",reply_markup=keyboard_sber_oreh1)



    if call.data == "odin":
        keyboard_odin = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Одинцово и район (Звенигород, Краснознаменск)", callback_data="odin1")
        keyboard_odin.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Руза иа район", callback_data="ruza")
        keyboard_odin.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_odin.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_odin)

    elif call.data == "ruza":
        keyboard_ruza = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="ruza_kom")
        keyboard_ruza.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="ruza_kon_kom")
        keyboard_ruza.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ruza")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_ruza)

    elif call.data == "ruza_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_ruza_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ruza")
        keyboard_ruza_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_ruza_kom)

    elif call.data == "ruza_kon_kom":
        keyboard_ruza_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_ruza")
        keyboard_ruza_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_ruza")
        keyboard_ruza_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_ruza")
        keyboard_ruza_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ruza")
        keyboard_ruza_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_ruza_kon_kom)

    elif call.data == "sber_ruza":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_ruza = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ruza")
        keyboard_sber_ruza.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 6 офисов 16 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nСвет -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГаз -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГИБДД - оплата картой1.2 %, мах 500 руб. наличными в терминале 2%, мин. 10 руб, мах 2000 руб.\nРостелеком - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.).\nМобильная связь - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.)\n",reply_markup=keyboard_sber_ruza)


    elif call.data == "moe_ruza":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_ruza = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=moga)
        keyboard3_moe_ruza.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="\n2 офиса 2 терминала. Оплата наличными не принимается.\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nКомиссия составляет 1,5% по всем поставщикам\n", reply_markup=keyboard3_moe_ruza)


    elif call.data == "vtb_ruza":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_ruza = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ruza")
        keyboard3_vtb_ruza.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 2 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nПлатежи наличными не принимаются\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСвет - 1,5 % (min 200 руб. max 3000 руб.), по карте. \nГаз - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nГИБДД - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nРостелеком - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСотовая связь - 1,5 % (min 200 руб. max 3000 руб.), по карте\n",reply_markup=keyboard3_vtb_ruza)






    elif call.data == "odin1":
        keyboard_odin1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="odin1_kom")
        keyboard_odin1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="odin1_kon_kom")
        keyboard_odin1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="odin1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_odin1)



    elif call.data == "odin1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_odin1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="odin1")
        keyboard_odin1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_odin1_kom)


    elif call.data == "odin1_kon_kom":
        keyboard_odin1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_odin1")
        keyboard_odin1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_odin1")
        keyboard_odin1_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="odin1")
        keyboard_odin1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_odin1_kon_kom)


    elif call.data == "sber_odin1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_odin1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="odin1")
        keyboard_sber_odin1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 8 офисов 21 банкомат/терминал)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nСвет -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГаз -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГИБДД - оплата картой1.2 %, мах 500 руб. наличными в терминале 2%, мин. 10 руб, мах 2000 руб.\nРостелеком - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.).\nМобильная связь - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.)\n",reply_markup=keyboard_sber_odin1)

    elif call.data == "moe_odin1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_odin1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=moga)
        keyboard3_moe_odin1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n5 офисов. Оплата наличными не принимается.\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nКомиссия составляет 1,5% по всем поставщикам\n",reply_markup=keyboard3_moe_odin1)

    if call.data == "nara":
        keyboard_nara = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Можайск и район", callback_data="moga")
        keyboard_nara.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Наро-Фоминск и район", callback_data="nara1")
        keyboard_nara.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_nara.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_nara)

    elif call.data == "nara1":
        keyboard_nara1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="nara1_kom")
        keyboard_nara1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="nara1_kon_kom")
        keyboard_nara1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="nara1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_nara1)

    elif call.data == "nara1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_nara1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="nara1")
        keyboard_nara1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n", reply_markup=keyboard_nara1_kom)

    elif call.data == "nara1_kon_kom":
        keyboard_nara1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_nara1")
        keyboard_nara1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_nara1")
        keyboard_nara1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_nara1")
        keyboard_nara1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="nara1")
        keyboard_nara1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_nara1_kon_kom)

    elif call.data == "sber_nara1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_nara1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="nara1")
        keyboard_sber_nara1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офиса 11 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ - без комиссии МОЕ (кап.ремонт)-3% мин. 50 руб, макс. 5000р.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nСвет -  через терминал 1,2%, личный кабинет 1% , максимум 500 руб.\nГаз - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nГИБДД - 1,2 % максимум 500 руб. (по карте), счету комиссия 2%, мин. 10р., макс. 2000 руб. (сторонней картой, наличными).\nРостелеком - в окне картой  3%  картой; в терминале наличными  2,5% мин 5,00;  без %  картой в терминале.\nМобильная связь - без комиссии.\n",reply_markup=keyboard_sber_nara1)

    elif call.data == "moe_nara1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_nara1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=moga)
        keyboard3_moe_nara1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОпалата налитчными: МОЕ 0,8%. Остальные поставщики не принимаются. Оплата картой: МОЕ - 1,5%. Остальные поставщики не принимаются.\n",reply_markup=keyboard3_moe_nara1)

    elif call.data == "vtb_nara1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_nara1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="moga_kon_kom")
        keyboard3_vtb_nara1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 3 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_nara1)


    elif call.data == "moga":
        keyboard_moga = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="moga_kom")
        keyboard_moga.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="moga_kon_kom")
        keyboard_moga.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="moga")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_moga)

    elif call.data == "moga_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_moga_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="moga")
        keyboard_moga_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_moga_kom)

    elif call.data == "moga_kon_kom":
        keyboard_moga_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_moga")
        keyboard_moga_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_moga")
        keyboard_moga_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_moga")
        keyboard_moga_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="moga")
        keyboard_moga_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_moga_kon_kom)

    elif call.data == "sber_moga":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_moga = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="moga")
        keyboard_sber_moga.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офиса 11 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ - без комиссии МОЕ (кап.ремонт)-3% мин. 50 руб, макс. 5000р.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nСвет -  через терминал 1,2%, личный кабинет 1% , максимум 500 руб.\nГаз - через терминал 1,2%, личный кабинет 1%, максимум 500 руб. \nГИБДД - 1,2 % максимум 500 руб. (по карте), счету комиссия 2%, мин. 10р., макс. 2000 руб. (сторонней картой, наличными).\nРостелеком - в окне картой  3%  картой; в терминале наличными  2,5% мин 5,00;  без %  картой в терминале.\nМобильная связь - без комиссии.\n",reply_markup=keyboard_sber_moga)

    elif call.data == "moe_moga":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_moga = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=moga)
        keyboard3_moe_moga.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОпалата налитчными: МОЕ 0,8%. Остальные поставщики не принимаются. Оплата картой: МОЕ - 1,5%. Остальные поставщики не принимаются.\n",reply_markup=keyboard3_moe_moga)

    elif call.data == "vtb_moga":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_moga = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="moga_kon_kom")
        keyboard3_vtb_moga.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 3 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_moga)


    if call.data == "mitishi":
        keyboard_mitishi = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Мытищи и район", callback_data="mitishi1")
        keyboard_mitishi.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Щелково и район", callback_data="shelk")
        keyboard_mitishi.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Королев", callback_data="korol")
        keyboard_mitishi.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_mitishi.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_mitishi)

    elif call.data == "korol":
        keyboard_korol = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="korol_kom")
        keyboard_korol.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="korol_kon_kom")
        keyboard_korol.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="korol")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_korol)


    elif call.data == "korol_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_korol_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="korol")
        keyboard_korol_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_korol_kom)

    elif call.data == "korol_kon_kom":
        keyboard_korol_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_korol")
        keyboard_korol_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_korol")
        keyboard_korol_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_korol")
        keyboard_korol_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="ЕСГП", callback_data="esgp_korol")
        keyboard_korol_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="korol")
        keyboard_korol_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_korol_kon_kom)

    elif call.data == "vtb_korol":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_korol = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="korol_kon_kom")
        keyboard3_vtb_korol.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (7 офисов 9 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_korol)

    elif call.data == "sber_korol":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_korol = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="korol")
        keyboard_sber_korol.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 14 офисов 30 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_korol)

    elif call.data == "moe_korol":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_korol = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=korol)
        keyboard3_moe_korol.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис, 31 терминал)\nОплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_korol)


    elif call.data == "esgp_korol":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_esgp_korol = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=korol)
        keyboard3_esgp_korol.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (80 терминалов в городе Королев)\nОплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - 1,59%\nСвет - 1,5%\nГаз- 1,5%\nГИБДД -не принимают\nРостелеком - 1%\nМобильная связь - 5%\n",reply_markup=keyboard3_esgp_korol)






    elif call.data == "shelk":
        keyboard_shelk = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="shelk_kom")
        keyboard_shelk.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="shelk_kon_kom")
        keyboard_shelk.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="shelk")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_shelk)

    elif call.data == "shelk_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_shelk_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shelk")
        keyboard_shelk_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_shelk_kom)

    elif call.data == "shelk_kon_kom":
        keyboard_shelk_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_shelk")
        keyboard_shelk_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_shelk")
        keyboard_shelk_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_shelk")
        keyboard_shelk_kon_kom.add(rele3)
        rele3 = types.InlineKeyboardButton(text="ООО КП", callback_data="kp_shelk")
        keyboard_shelk_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="shelk")
        keyboard_shelk_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_shelk_kon_kom)

    elif call.data == "vtb_shelk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_shelk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1_kon_kom")
        keyboard3_vtb_shelk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (4 офиса 19 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_shelk)

    elif call.data == "sber_shelk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_shelk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shelk")
        keyboard_sber_shelk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 16 офисов 36 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_shelk)

    elif call.data == "moe_shelk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_shelk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=shelk)
        keyboard3_moe_shelk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (4 офиса.)\nРасчетный счет 6799-1,5%, Расчетный счет 6635-0%. Оплата наличными других поставщиков не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - 1,5%\nСвет - 1%\nГаз- не принимают\nГИБДД -3% не менее 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_shelk)

    elif call.data == "kp_shelk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_kp_shelk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=shelk)
        keyboard3_kp_shelk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ООО КП (1 касса.)\nПод какой % принимают платежи  наличными в кассе\nМОЕ - 3,1%\nСвет - 3,1%\nГаз - 3,1%\n Платежи на остальных поставщиков не принимаются. Оплаты картой нет.",reply_markup=keyboard3_kp_shelk)



    elif call.data == "mitishi1":
        keyboard_mitishi1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="mitishi1_kom")
        keyboard_mitishi1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="mitishi1_kon_kom")
        keyboard_mitishi1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_mitishi1)


    elif call.data == "mitishi1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_mitishi1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1")
        keyboard_mitishi1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_mitishi1_kom)

    elif call.data == "mitishi1_kon_kom":
        keyboard_mitishi1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_mitishi1")
        keyboard_mitishi1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_mitishi1")
        keyboard_mitishi1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_mitishi1")
        keyboard_mitishi1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1")
        keyboard_mitishi1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_mitishi1_kon_kom)

    elif call.data == "vtb_mitishi1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_mitishi1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1_kon_kom")
        keyboard3_vtb_mitishi1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (3 офиса 13 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_mitishi1)


    elif call.data == "sber_mitishi1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_mitishi1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="mitishi1")
        keyboard_sber_mitishi1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 16 офисов 67 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Расчетный счет 6799-3% не менее 50 руб. и не более 2500 руб., Расчетный счет 6635-0%.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1,2%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 0,5% онлайн и мобильный банк, оплата р/с 6635 везде без %.\nСвет -  2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - Н2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nГИБДД - 2,5% (не менее 25 руб., не более 1500 руб.)на окне картой, 1%  оплата картой через банкомат, 2% (не менее 10 руб, не более 2000 руб.) наличными в банкоматах, 1% онлайн и мобильный банк.\nРостелеком - 2,5% не менее 10 руб картой на окне/ 3%  мин 10,00 нал в терминале/ без %  картой в терминале.\nМобильная связь - 2,5% наличными через терминал, без % по карте банка.\n",reply_markup=keyboard_sber_mitishi1)

    elif call.data == "moe_mitishi1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_mitishi1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data=mitishi1)
        keyboard3_moe_mitishi1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 53 терминала.)\n Оплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - Расчетный счет 6799-0,99%, Расчетный счет 6635-0%\nСвет - Наличными/карта - 1% (внешняя)\nГаз- не принимают\nГИБДД -3% не менее 30р.\nHРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_mitishi1)





    if call.data == "luber":
        keyboard_luber = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Люберцы и район", callback_data="luber1")
        keyboard_luber.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Дзержинский", callback_data="dzer")
        keyboard_luber.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Лыткарино", callback_data="litka")
        keyboard_luber.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Раменское и район", callback_data="ramen")
        keyboard_luber.add(rele4)
        rele5 = types.InlineKeyboardButton(text="Жуковский", callback_data="guk")
        keyboard_luber.add(rele5)
        rele6 = types.InlineKeyboardButton(text="Бронницы", callback_data="bron")
        keyboard_luber.add(rele6)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_luber.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_luber)

    elif call.data == "bron":
        keyboard_bron = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="bron_kom")
        keyboard_bron.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="bron_kon_kom")
        keyboard_bron.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="bron")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_bron)


    elif call.data == "bron_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_bron_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="bron")
        keyboard_bron_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_bron_kom)

    elif call.data == "bron_kon_kom":
        keyboard_bron_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_bron")
        keyboard_bron_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_bron")
        keyboard_bron_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="bron")
        keyboard_bron_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_bron_kon_kom)

    elif call.data == "moe_bron":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_bron = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard3_moe_bron.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 касса.)\n Оплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы\nСвет - Наличными/карта - 1% (внешняя)\nГаз- не принимают\nГИБДД -30р.\nHРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_bron)


    elif call.data == "sber_bron":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_bron = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="bron")
        keyboard_sber_bron.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 2 офиса 4 банкомата/терминала)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет -  Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.).\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_bron)




    elif call.data == "guk_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_guk_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard_guk_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_guk_kom)



    elif call.data == "guk":
        keyboard_guk = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="guk_kom")
        keyboard_guk.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="guk_kon_kom")
        keyboard_guk.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_guk)

    elif call.data == "guk_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_guk_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard_guk_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_guk_kom)

    elif call.data == "guk_kon_kom":
        keyboard_guk_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_guk")
        keyboard_guk_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_guk")
        keyboard_guk_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_guk")
        keyboard_guk_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard_guk_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_guk_kon_kom)

    elif call.data == "moe_guk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_guk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard3_moe_guk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис.)\n Оплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы\nСвет - Наличными/карта - 1% (внешняя)\nГаз- не принимают\nГИБДД -30р.\nHРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_guk)


    elif call.data == "vtb_guk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_guk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard3_vtb_guk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (4 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nПлатежи наличными не принимаются\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы.\nСвет - Наличными/карта - 1% (внешняя). \nГаз - не принимают.\nГИБДД - 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99% .\nСотовая связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%.\n",reply_markup=keyboard3_vtb_guk)

    elif call.data == "sber_guk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_guk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="guk")
        keyboard_sber_guk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 5 офисов 20 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет -  Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.).\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_guk)


    elif call.data == "ramen":
        keyboard_ramen = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="ramen_kom")
        keyboard_ramen.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="ramen_kon_kom")
        keyboard_ramen.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ramen")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_ramen)

    elif call.data == "ramen_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_ramen_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ramen")
        keyboard_ramen_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_ramen_kom)

    elif call.data == "ramen_kon_kom":
        keyboard_ramen_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_ramen")
        keyboard_ramen_kon_kom.add(rele1)
        rele3 = types.InlineKeyboardButton(text="Кассы УК", callback_data="vkassa_ramen")
        keyboard_ramen_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ramen")
        keyboard_ramen_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_ramen_kon_kom)

    elif call.data == "sber_ramen":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_ramen = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ramen")
        keyboard_sber_ramen.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 5 офисов 20 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет -  Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.).\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_ramen)


    elif call.data == "vkassa_ramen":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vkassa_volo_ramen = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ramen")
        keyboard3_vkassa_volo_ramen.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n7 точек приема платежей. Оплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - 1,59% терминал\nСвет - 2%\nГаз - 2%\nГИБДД - не принимают\nРостелеком - 1%\nСотовая связь -5%\n",reply_markup=keyboard3_vkassa_ramen)


    elif call.data == "luber1":
        keyboard_luber1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="luber1_kom")
        keyboard_luber1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="luber1_kon_kom")
        keyboard_luber1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="luber1")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_luber1)

    elif call.data == "luber1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_luber1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luber1")
        keyboard_luber1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_luber1_kom)

    elif call.data == "luber1_kon_kom":
        keyboard_luber1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_luber1")
        keyboard_luber1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_luber1")
        keyboard_luber1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Выездная касса", callback_data="vkassa_luber1")
        keyboard_luber1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="luber1")
        keyboard_luber1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_luber1_kon_kom)

    elif call.data == "sber_luber1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_luber1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luber1")
        keyboard_sber_luber1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 10 офисов 27 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет -  Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.).\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_luber1)


    elif call.data == "vkassa_luber1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vkassa_volo_luber1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard3_vkassa_volo_luber1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nВыездная касса 140140 и 140143. Принимают только МОЕ, наличная оплата, без комиссии\n",reply_markup=keyboard3_vkassa_luber1)


    elif call.data == "moe_luber1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_luber1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard3_moe_luber1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис, 12 дополнительных офисов, 14 терминалов.)\n Оплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы\nСвет - Наличными/карта - 1% (внешняя)\nГаз- не принимают\nГИБДД -30р.\nHРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nМобильная связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_luber1)

    elif call.data == "dzer":
        keyboard_dzer = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="dzer_kom")
        keyboard_dzer.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="dzer_kon_kom")
        keyboard_dzer.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="dzer")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_dzer)

    elif call.data == "dzer_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_dzer_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dzer")
        keyboard_dzer_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_dzer_kom)


    elif call.data == "dzer_kon_kom":
        keyboard_dzer_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_dzer")
        keyboard_dzer_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_dzer")
        keyboard_dzer_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="dzer")
        keyboard_dzer_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_dzer_kon_kom)

    elif call.data == "sber_dzer":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_dzer = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_sber_dzer.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 1 офис 13 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5%, мин 25 руб.  МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_dzer)


    elif call.data == "moe_dzer":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_dzer = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard3_moe_dzer.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (2 кассы)\nОплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы\nСвет - Наличными/карта - 1% (внешняя)\nГаз - не принимают\nГИБДД - 30р.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nСотовая связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_dzer)


    elif call.data == "litka":
        keyboard_litka = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="volo_kom")
        keyboard_litka.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="volo_kon_kom")
        keyboard_litka.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="litka")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_litka)

    elif call.data == "litka_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_litka_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="litka")
        keyboard_litka_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_litka_kom)


    elif call.data == "litka_kon_kom":
        keyboard_litka_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_litka")
        keyboard_litka_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_litka")
        keyboard_litka_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="litka")
        keyboard_litka_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_litka_kon_kom)

    elif call.data == "moe_litka":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_litka = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="litka")
        keyboard3_moe_litka.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 1 касса)\nОплата наличными не принимается\nПод какой % принимают банкоматы, терминалы/ оплата в офисе картой\nМОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы\nСвет - Наличными/карта - 1% (внешняя)\nГаз - не принимают\nГИБДД - 30р.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%\nСотовая связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%\n",reply_markup=keyboard3_moe_litka)

    elif call.data == "sber_litka":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_litka = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="litka")
        keyboard_sber_litka.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 1 офис 13 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5%, мин 25 руб.  МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_litka)




    if call.data == "kras":
        keyboard_kras = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Красногорск и район", callback_data="kras1")
        keyboard_kras.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Истра и Дедовск", callback_data="istra")
        keyboard_kras.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Волоколамск, Лотошино, Шаховская", callback_data="volo")
        keyboard_kras.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_kras.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_kras)



    elif call.data == "volo":
        keyboard_volo = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="volo_kom")
        keyboard_volo.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="volo_kon_kom")
        keyboard_volo.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboardvoloa.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_volo)

    elif call.data == "volo_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_volo_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard_volo_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_volo_kom)

    elif call.data == "volo_kon_kom":
        keyboard_volo_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_volo")
        keyboard_volo_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_volo")
        keyboard_volo_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_volo")
        keyboard_volo_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard_volo_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_volo_kon_kom)


    elif call.data == "moe_volo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_volo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard3_moe_volo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 1 касса.)\n Принимается оплата наличными МОЕ - 1,8%, по карте 1,5%. Все остальные платежи не принимаются\n",reply_markup=keyboard3_moe_volo)

    elif call.data == "vtb_volo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_volo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="volo")
        keyboard3_vtb_volo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офиса 3 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nПлатежи наличными не принимаются\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСвет - 1,5 % (min 200 руб. max 3000 руб.), по карте. \nГаз - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nГИБДД - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nРостелеком - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСотовая связь - 1,5 % (min 200 руб. max 3000 руб.), по карте\n",reply_markup=keyboard3_vtb_volo)

    elif call.data == "sber_volo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_volo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_sber_volo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 1 офис 6 банкоматов/терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nСвет -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГаз -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГИБДД - оплата картой1.2 %, мах 500 руб. наличными в терминале 2%, мин. 10 руб, мах 2000 руб.\nРостелеком - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.).\nМобильная связь - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.)\n",reply_markup=keyboard_sber_volo)


    elif call.data == "istra":
        keyboard_istra = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="istra_kom")
        keyboard_istra.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="istra_kon_kom")
        keyboard_istra.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_istra.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_istra)


    elif call.data == "istra_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_istra_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_istra_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_istra_kom)

    elif call.data == "istra_kon_kom":
        keyboard_istra_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_istra")
        keyboard_istra_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_istra")
        keyboard_istra_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_istra")
        keyboard_istra_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Юнистрим Банк", callback_data="unis_istra")
        keyboard_istra_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_istra_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете конкурента", reply_markup=keyboard_istra_kon_kom)

    elif call.data == "unis_istra":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_unis_istra = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard3_unis_istra.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 4 терминала)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 0,9 %, мин. 49 руб.\n Свет - 0,9 %, мин. 49 руб.\n Газ - 0,9 %, мин. 49 руб.\n ГИБДД - 0,9 %, мин. 49 руб.\nРостелеком - 1% мин.10 руб.\nМобильная связь - 1% мин.10 руб.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Терминалы МКБ  находится в офисе МОЕ принимают под  1, 5%.\nСвет - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%. \nГаз - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%.\nГИБДД - Терминалы МКБ  находится в офисе МОЕ принимают под 1,5%.\nРостелеком - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%.\nСотовая связь - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%.\n",reply_markup=keyboard3_unis_istra)



    elif call.data == "sber_istra":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_istra = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard_sber_istra.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 2 офисов 10 банкомата/терминала)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nСвет -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГаз -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГИБДД - оплата картой1.2 %, мах 500 руб. наличными в терминале 2%, мин. 10 руб, мах 2000 руб.\nРостелеком - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.).\nМобильная связь - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.)\n",reply_markup=keyboard_sber_istra)


    elif call.data == "vtb_istra":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_istra = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard3_vtb_istra.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офиса 10 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nПлатежи наличными не принимаются\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСвет - 1,5 % (min 200 руб. max 3000 руб.), по карте. \nГаз - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nГИБДД - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nРостелеком - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСотовая связь - 1,5 % (min 200 руб. max 3000 руб.), по карте\n",reply_markup=keyboard3_vtb_istra)

    elif call.data == "moe_istra":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_istra = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="istra")
        keyboard3_moe_istra.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 1 терминал.)\n Оплата наличными в кассе\nОплата наличными всех поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Терминалы МКБ  находится в офисе МОЕ принимают под  1, 5%.\nСВЕТ - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nГАЗ - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\n ГИБДД - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nРостелеком - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nСотовая связь - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\n",reply_markup=keyboard3_moe_istra)



    elif call.data == "kras1":
        keyboard_kras1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="kras1_kom")
        keyboard_kras1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="kras1_kon_kom")
        keyboard_kras1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard_kras1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_kras1)

    elif call.data == "kras1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_kras1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard_kras1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_kras1_kom)


    elif call.data == "kras1_kon_kom":
        keyboard_kras1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_kras1")
        keyboard_kras1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_kras1")
        keyboard_kras1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_kras1")
        keyboard_kras1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard_kras1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_kras1_kon_kom)


    elif call.data == "sber_kras1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_kras1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard_sber_kras1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 13 офисов/32 банкомата/терминала)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб. мах 5000 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь - 2,5 %  не менее 10 руб.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nСвет -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГаз -  с карты банка 1,2%,мах. 500 руб. наличными в терминале 2%(мин.10 руб. мах 2000).\nГИБДД - оплата картой1.2 %, мах 500 руб. наличными в терминале 2%, мин. 10 руб, мах 2000 руб.\nРостелеком - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.).\nМобильная связь - оплата по карте банка 1.2% мах. 500 руб. наличными в терминале 3 %(мин. 10 руб. мах 2000 руб.)\n",reply_markup=keyboard_sber_kras1)

    elif call.data == "vtb_kras1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_kras1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard3_vtb_kras1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 6 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nПлатежи наличными не принимаются\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСвет - 1,5 % (min 200 руб. max 3000 руб.), по карте. \nГаз - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nГИБДД - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nРостелеком - 1,5 % (min 200 руб. max 3000 руб.), по карте.\nСотовая связь - 1,5 % (min 200 руб. max 3000 руб.), по карте\n",reply_markup=keyboard3_vtb_kras1)

    elif call.data == "moe_kras1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_kras1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kras1")
        keyboard3_moe_kras1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (2 офиса 2 терминала.)\n Оплата наличными в кассе\nОплата наличными всех поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%.\nСВЕТ - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nГАЗ - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\n ГИБДД - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nРостелеком - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\nСотовая связь - Терминалы МКБ  находится в офисе МОЕ принимают под  1,5%\n",reply_markup=keyboard3_moe_kras1)




    if call.data == "kolomna":
        keyboard_kolomna = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Коломна и район", callback_data="kolomna1")
        keyboard_kolomna.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Луховицы и район", callback_data="luho")
        keyboard_kolomna.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Озеры и район", callback_data="ozer")
        keyboard_kolomna.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Зарайск и район", callback_data="zara")
        keyboard_kolomna.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_kolomna.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_kolomna)

    elif call.data == "ozer":
        keyboard_ozer = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="ozer_kom")
        keyboard_ozer.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="ozer_kon_kom")
        keyboard_ozer.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ozer")
        keyboard_ozer.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_ozer)

    elif call.data == "zara":
        keyboard_zara = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="zara_kom")
        keyboard_zara.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="zara_kon_kom")
        keyboard_zara.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="zara")
        keyboard_zara.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_zara)

    elif call.data == "zara_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_zara_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="zara")
        keyboard_zara_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_zara_kom)


    elif call.data == "zara_kon_kom":
        keyboard_zara_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_zara")
        keyboard_zara_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_zara")
        keyboard_zara_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="zara")
        keyboard_zara_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_zara_kon_kom)

    elif call.data == "sber_zara":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_zara = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="zara")
        keyboard_sber_zara.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 3 офиса 8 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 1,5 % от суммы.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_zara)


    elif call.data == "moe_zara":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_zara = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="zara")
        keyboard3_moe_zara.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 1 терминал.)\n Оплата наличными в кассе\nМОЕ - 1,5% внешняя\nОплата наличными всех остальных поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5%.\nСВЕТ - 1%\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_zara)



    elif call.data == "ozer_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_ozer_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ozer")
        keyboard_ozer_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_ozer_kom)


    elif call.data == "ozer_kon_kom":
        keyboard_ozer_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_ozer")
        keyboard_ozer_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_ozer")
        keyboard_ozer_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="ozer")
        keyboard_ozer_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_ozer_kon_kom)

    elif call.data == "sber_ozer":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_ozer = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ozer")
        keyboard_sber_ozer.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 3 офиса 5 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Без комиссии.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_ozer)

    elif call.data == "moe_ozer":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_ozer = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="ozer")
        keyboard3_moe_ozer.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (2 офиса 2 терминала.)\n Оплата наличными в кассе\nМОЕ - без комиссии\nОплата наличными всех остальных поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - без комиссии.\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_ozer)



    elif call.data == "luho":
        keyboard_luho = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="luho_kom")
        keyboard_luho.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="luho_kon_kom")
        keyboard_luho.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard_luho.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_luho)


    elif call.data == "luho_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_luho_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard_luho_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_luho_kom)

    elif call.data == "luho_kon_kom":
        keyboard_luho_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_luho")
        keyboard_luho_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_luho")
        keyboard_luho_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_luho")
        keyboard_luho_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard_luho_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_luho_kon_kom)

    elif call.data == "sber_luho":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_luho = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard_sber_luho.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 7 офисов 24 терминала/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Без комиссии.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_luho)


    elif call.data == "moe_luho":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_luho = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard3_moe_luho.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 2 терминала.)\n Оплата наличными в кассе\nОплата наличными всех поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1,5% от суммы.\n Свет - 1%\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_luho)

    elif call.data == "vtb_luho":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_luho = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="luho")
        keyboard3_vtb_luho.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ ( 2 офиса 14 терминалов.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nСвет - Без комиссии.\nГаз - Без комиссии.\nГИБДД - Без комиссии.\nРостелеком - Без комиссии.\nСотовая связь - Без комиссии\n",reply_markup=keyboard3_vtb_luho)


    elif call.data == "kolomna1":
        keyboard_kolomna1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="kolomna1_kom")
        keyboard_kolomna1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="kolomna1_kon_kom")
        keyboard_kolomna1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard_kolomna1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_kolomna1)

    elif call.data == "kolomna1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_kolomna1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard_kolomna1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_kolomna1_kom)


    elif call.data == "kolomna1_kon_kom":
        keyboard_kolomna1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_kolomna1")
        keyboard_kolomna1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_kolomna1")
        keyboard_kolomna1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_kolomna1")
        keyboard_kolomna1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard_kolomna1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_kolomna1_kon_kom)

    elif call.data == "sber_kolomna1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_kolomna1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard_sber_kolomna1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 11 офисов 29 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Без комиссии.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_kolomna1)


    elif call.data == "moe_kolomna1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_kolomna1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard3_moe_kolomna1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (3 офиса 5 терминалов.)\n Оплата наличными в кассе\nОплата наличными всех поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\n Свет - 1%\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_kolomna1)

    elif call.data == "vtb_kolomna1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_kolomna1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kolomna1")
        keyboard3_vtb_kolomna1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ ( 2 офиса 14 терминалов.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nСвет - Без комиссии.\nГаз - Без комиссии.\nГИБДД - Без комиссии.\nРостелеком - Без комиссии.\nСотовая связь - Без комиссии\n",reply_markup=keyboard3_vtb_kolomna1)



    if call.data == "kashira":
        keyboard_kashira = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Ступино", callback_data="stupino")
        keyboard_kashira.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Кашира", callback_data="kashira1")
        keyboard_kashira.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Серебряно-Прудский район", callback_data="serebro")
        keyboard_kashira.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_kashira.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_kashira)

    elif call.data == "serebro":
        keyboard_serebro = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="serebro_kom")
        keyboard_serebro.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="serebro_kon_kom")
        keyboard_serebro.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard_serebro.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_serebro)

    elif call.data == "serebro_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_serebro_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard_serebro_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_serebro_kom)

    elif call.data == "serebro_kon_kom":
        keyboard_serebro_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_serebro")
        keyboard_serebro_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_serebro")
        keyboard_serebro_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_serebro")
        keyboard_serebro_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard_serebro_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_serebro_kon_kom)

    elif call.data == "sber_serebro":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_serebro = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard_sber_serebro.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 6 офисов 6 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3%  не менее 50 руб.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - 1,5% от суммы.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_serebro)


    elif call.data == "vtb_serebro":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_serebro = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard3_vtb_serebro.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 2 терминала.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nСвет - Без комиссии.\nГаз - Без комиссии.\nГИБДД - Без комиссии.\nРостелеком - Без комиссии.\nСотовая связь - Без комиссии\n",reply_markup=keyboard3_vtb_serebro)



    elif call.data == "moe_serebro":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_serebro = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="serebro")
        keyboard3_moe_serebro.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 офис 3 терминала.)\n Оплата наличными в кассе\nОплата наличными всех поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\n Свет - 1%\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_serebro)

    elif call.data == "kashira1":
        keyboard_kashira1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="kashira1_kom")
        keyboard_kashira1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="kashira1_kon_kom")
        keyboard_kashira1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard_kashira1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_kashira1)

    elif call.data == "kashira1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_kashira1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard_kashira1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_kashira1_kom)

    elif call.data == "kashira1_kon_kom":
        keyboard_kashira1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_kashira1")
        keyboard_kashira1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_kashira1")
        keyboard_kashira1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_kashira1")
        keyboard_kashira1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard_kashira1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_kashira1_kon_kom)

    elif call.data == "sber_kashira1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_kashira1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard_sber_kashira1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офиса 18 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Без комиссии.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_kashira1)

    elif call.data == "vtb_kashira1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_kashira1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard3_vtb_kashira1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 10 терминалов.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nСвет - Без комиссии.\nГаз - Без комиссии.\nГИБДД - Без комиссии.\nРостелеком - Без комиссии.\nСотовая связь - Без комиссии\n",reply_markup=keyboard3_vtb_kashira1)


    elif call.data == "moe_kashira1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_kashira1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="kashira1")
        keyboard3_moe_kashira1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (3 офиса 6 терминалов.)\n Оплата наличными в кассе\nМОЕ - Без комиссии\nОплата наличными всех других поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_kashira1)



    elif call.data == "stupino":
        keyboard_stupino = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="stupino_kom")
        keyboard_stupino.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="stupino_kon_kom")
        keyboard_stupino.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard_stupino.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_stupino)

    elif call.data == "stupino_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_stupino_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard_stupino_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_stupino_kom)


    elif call.data == "stupino_kon_kom":
        keyboard_stupino_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_stupino")
        keyboard_stupino_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_stupino")
        keyboard_stupino_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_stupino")
        keyboard_stupino_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard_stupino_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_stupino_kon_kom)

    elif call.data == "sber_stupino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_stupino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard_sber_stupino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 14 офисов 33 терминалов/банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - Без комиссии.\nСвет - 3%  не менее 25 руб.\nГаз - 3%  не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - 2,5 %  не менее 10 руб.\nСотовая связь -  не принимают.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Без комиссии.\nСвет - 1%\nГаз - 1%.\nГИБДД - 1,2% макс 500 руб.\nРостелеком - 1,2%.\nМобильная связь - Без комиссии.\n",reply_markup=keyboard_sber_stupino)


    elif call.data == "moe_stupino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_stupino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard3_moe_stupino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (2 офиса 4 терминала.)\n Оплата наличными в кассе\nМОЕ - Без комиссии\nОплата наличными всех других поставщиков не принимается\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nОплата всех других поставщиков не принимается\n",reply_markup=keyboard3_moe_stupino)


    elif call.data == "vtb_stupino":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_stupino = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stupino")
        keyboard3_vtb_stupino.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (3 офиса 23 терминала.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Без комиссии.\nСвет - Без комиссии.\nГаз - Без комиссии.\nГИБДД - Без комиссии.\nРостелеком - Без комиссии.\nСотовая связь - Без комиссии\n",reply_markup=keyboard3_vtb_stupino)



    if call.data == "domoded":
        keyboard_domoded = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Ленинский район. Видное", callback_data="vidnoe")
        keyboard_domoded.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Долгопрудный", callback_data="domoded1")
        keyboard_domoded.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_domoded.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_domoded)


    elif call.data == "domoded1":
        keyboard_domoded1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="domoded1_kom")
        keyboard_domoded1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="domoded1_kon_kom")
        keyboard_domoded1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="domoded")
        keyboard_domoded1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_domoded1)

    elif call.data == "domoded1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_domoded1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="domoded1")
        keyboard_domoded1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_domoded1_kom)

    elif call.data == "domoded1_kon_kom":
        keyboard_domoded1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_domoded1")
        keyboard_domoded1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Кассы ЖЭУ", callback_data="geu_domoded1")
        keyboard_domoded1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_domoded1")
        keyboard_domoded1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="domoded1")
        keyboard_domoded1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_domoded1_kon_kom)

    elif call.data == "sber_domoded1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_domoded1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="domoded1")
        keyboard_sber_domoded1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 12 офиса/60 банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5%, мин 25 руб. МОЕ кап.ремонт то же.\nСвет - ННаличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р.\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_domoded1)


    elif call.data == "vtb_domoded1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_domoded1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="domoded1")
        keyboard3_vtb_domoded1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офиса 9 банкоматов.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nСвет - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГаз - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГИБДД - без комиссии.\nРостелеком - Наличными: 20 руб. Карта: без комиссии.\nСотовая связь - Наличными без карты: не принимают. Карта: без комиссии\n",reply_markup=keyboard3_vtb_domoded1)



    elif call.data == "geu_domoded1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_geu_domoded1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="domoded1")
        keyboard3_geu_domoded1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы касс ЖЭУ (18 касс.) МОЕ - 1,8% (внешняя) \n Свет - 1,8% (внешняя)\n Все остальные формы оплаты и поставщики отсутствуют\n",reply_markup=keyboard3_geu_domoded1)


    elif call.data == "vidnoe":
        keyboard_vidnoe = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="vidnoe_kom")
        keyboard_vidnoe.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="vidnoe_kon_kom")
        keyboard_vidnoe.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="domoded")
        keyboard_vidnoe.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_vidnoe)


    elif call.data == "vidnoe_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_vidnoe_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard_vidnoe_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_vidnoe_kom)


    elif call.data == "vidnoe_kon_kom":
        keyboard_vidnoe_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_vidnoe")
        keyboard_vidnoe_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_vidnoe")
        keyboard_vidnoe_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_vidnoe")
        keyboard_vidnoe_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="МКБ", callback_data="mkb_vidnoe")
        keyboard_vidnoe_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard_vidnoe_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_vidnoe_kon_kom)

    elif call.data == "sber_vidnoe":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_vidnoe = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard_sber_vidnoe.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 3 офиса/40 банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии, МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - Наличными: 3%  не менее 25 руб., картой: 2,5%, не менее 50 руб.\nГаз - Наличными: 3%  не менее 50 руб., Картой: 2,5, не менее 50 руб.\nГИБДД - 3%  не менее 50 руб.\nРостелеком - Наличными: 2,5 %  не менее 10 руб. Картой: 2%, не менее 10р, max 1500р\nСотовая связь - Наличными:2,5 %  не менее 10 руб. Картой: 2%, min 10р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - Наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы.\nГаз - Наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - Наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии.\n",reply_markup=keyboard_sber_vidnoe)

    elif call.data == "vtb_vidnoe":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_vidnoe = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard3_vtb_vidnoe.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 8 банкоматов.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nСвет - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГаз - Наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГИБДД - без комиссии.\nРостелеком - Наличными: 20 руб. Карта: без комиссии.\nСотовая связь - Наличными без карты: не принимают. Карта: без комиссии\n",reply_markup=keyboard3_vtb_vidnoe)

    elif call.data == "mkb_vidnoe":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_mkb_vidnoe = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard3_mkb_vidnoe.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МКБ(1 офис 17 банкоматов 41 терминал.)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 0,99 % от суммы.\nСвет - Наличными/карта - 1% (внешняя).\nГаз - не принимают.\nГИБДД - 30 руб.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -499% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%.\nСотовая связь - Наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99%.\n",reply_markup=keyboard3_mkb_vidnoe)

    elif call.data == "moe_vidnoe":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_vidnoe = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="vidnoe")
        keyboard3_moe_vidnoe.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы МОЕ (1 касса)\n Наличные платежи не принимаются \nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - 1%.\n",reply_markup=keyboard3_moe_vidnoe)


    if call.data == "dmitrov":
        keyboard_dmitrov = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Мытищинский район", callback_data="mitish")
        keyboard_dmitrov.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Долгопрудный", callback_data="dolgo")
        keyboard_dmitrov.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Лобня", callback_data="lobny")
        keyboard_dmitrov.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Дмитров", callback_data="dmitrov1")
        keyboard_dmitrov.add(rele4)
        rele5 = types.InlineKeyboardButton(text="Талдом", callback_data="taldom")
        keyboard_dmitrov.add(rele5)
        rele6 = types.InlineKeyboardButton(text="Дубна", callback_data="dubna")
        keyboard_dmitrov.add(rele6)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_dmitrov.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_dmitrov)



    elif call.data == "dubna":
        keyboard_dubna = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="dubna_kom")
        keyboard_dubna.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="dubna_kon_kom")
        keyboard_dubna.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_dubna.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_dubna)


    elif call.data == "dubna_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_dubna_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dubna")
        keyboard_dubna_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_dubna_kom)


    elif call.data == "dubna_kon_kom":
        keyboard_dubna_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_dubna")
        keyboard_dubna_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_dubna")
        keyboard_dubna_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_dubna")
        keyboard_dubna_kon_kom.add(rele3)
        rele4 = types.InlineKeyboardButton(text="ИРЦ Дубна", callback_data="irc_dubna")
        keyboard_dubna_kon_kom.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="taldom")
        keyboard_dubna_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_dubna_kon_kom)



    elif call.data == "moe_dubna":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_dubna = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dubna_kon_kom")
        keyboard3_moe_dubna.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n2 терминала\nПод какой % принимают платежи  наличными в кассе\nНаличные пплатежи не принимаются, нет касс.\n Оплата в банкомате, терминале/оплата в офисе картой: МОЕ - Терминал МКБ   МОЕ р/сч 6799, кап ремонт 1,5 %  .\nСвет - Терминал МКБ 1%.\nГаз - не принимают.\nГИБДД - не принимают.\nРостелеком до 99 руб-4,99 руб. от 100 руб -4,99%.\nСотовая связь - до 10 руб. -5 руб. //от 11 до 99 руб -5,99 руб. //от 100 руб.-5,99%\n",reply_markup=keyboard3_moe_dubna)



    elif call.data == "sber_dubna":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_dubna = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dubna")
        keyboard_sber_dubna.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офиса/ 4 терминалов и 10 банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3% мин 50 рублей.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - МОЕ ,МОЕ кап ремонт 2,5% на окне картой мин 25 руб, нал в терминале 2%, картой 1,2%.\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_dubna)


    elif call.data == "vtb_dubna":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_dubna = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dubna")
        keyboard3_vtb_dubna.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 7 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_dubna)


    elif call.data == "irc_dubna":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_irc_dubna = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dubna")
        keyboard3_irc_dubna.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nНе принимают",reply_markup=keyboard3_irc_dubna)



    elif call.data == "taldom":
        keyboard_taldom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="taldom_kom")
        keyboard_taldom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="taldom_kon_kom")
        keyboard_taldom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_taldom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_taldom)


    elif call.data == "taldom_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_taldom_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="taldom")
        keyboard_taldom_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_taldom_kom)

    elif call.data == "taldom_kon_kom":
        keyboard_taldom_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_taldom")
        keyboard_taldom_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_taldom")
        keyboard_taldom_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_taldom")
        keyboard_taldom_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="taldom")
        keyboard_taldom_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_taldom_kon_kom)

    elif call.data == "moe_taldom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_taldom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="taldom_kon_kom")
        keyboard3_moe_taldom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n2 терминала\nПод какой % принимают платежи  наличными в кассе\nНаличные пплатежи не принимаются, нет касс.\n Оплата в банкомате, терминале/оплата в офисе картой: МОЕ - Терминал МКБ  МОЕ р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 1,5 %.\nСвет - Терминал МКБ 1%.\nГаз - не принимают.\nГИБДД - не принимают.\nдо 99 руб-4,99 руб. от 100 руб -4,99%.\nСотовая связь - до 10 руб. -5 руб. //от 11 до 99 руб -5,99 руб. //от 100 руб.-5,99%\n",reply_markup=keyboard3_moe_taldom)



    elif call.data == "vtb_taldom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_taldom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1_kon_kom")
        keyboard3_vtb_taldom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 3 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_taldom)


    elif call.data == "sber_taldom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_taldom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1")
        keyboard_sber_taldom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 12 офис/ 20 терминалов и банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - 3% мин 50 рублей.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - МОЕ Талдом ,МОЕ кап ремонт 2,5% на окне картой мин 25 руб, нал в терминале 2%, картой 1,2%.\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_taldom)



    elif call.data == "dmitrov1":
        keyboard_dmitrov1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="dmitrov1_kom")
        keyboard_dmitrov1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="dmitrov1_kon_kom")
        keyboard_dmitrov1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_dmitrov1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_dmitrov1)

    elif call.data == "dmitrov1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_dmitrov1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1")
        keyboard_dmitrov1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_dmitrov1_kom)

    elif call.data == "dmitrov1_kon_kom":
        keyboard_dmitrov1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_dmitrov1")
        keyboard_dmitrov1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_dmitrov1")
        keyboard_dmitrov1_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_dmitrov1")
        keyboard_dmitrov1_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1")
        keyboard_dmitrov1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_dmitrov1_kon_kom)

    elif call.data == "moe_dmitrov1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_dmitrov1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1_kon_kom")
        keyboard3_moe_dmitrov1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n1 офис 5 терминалов\nПод какой % принимают платежи  наличными в кассе\nНаличные пплатежи не принимаются, нет касс.\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - Терминал МКБ  МОЕ р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 1,5 %.\nСвет - Терминал МКБ 1%.\nГаз - не принимают.\nГИБДД - 3% не менее 30 рублей.\nдо 99 руб-4,99 руб. от 100 руб -4,99%.\nСотовая связь - до 10 руб. -5 руб. //от 11 до 99 руб -5,99 руб. //от 100 руб.-5,99%\n",reply_markup=keyboard3_moe_dmitrov1)

    elif call.data == "vtb_dmitrov1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_dmitrov1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1_kon_kom")
        keyboard3_vtb_dmitrov1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офиса 4 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой сторонего банка 2% мин 20 руб.\nСвет - терминал без %, картой сторонего банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_dmitrov1)


    elif call.data == "sber_dmitrov1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_dmitrov1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dmitrov1")
        keyboard_sber_dmitrov1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 12 офис/ 20 терминалов и банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ р/сч 6799  3% мин 50 руб., кап.ремонт 3% мин 50 руб.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - МОЕ без комиссии; МОЕ кап ремонт/ МОЕ р/сч 2,5% на окне картой мин 25 руб., нал в терминале 2%, картой 1,2%\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_dmitrov1)



    elif call.data == "lobny":
        keyboard_lobny = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="lobny_kom")
        keyboard_lobny.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="lobny_kon_kom")
        keyboard_lobny.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_lobny.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_lobny)

    elif call.data == "lobny_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_lobny_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="lobny")
        keyboard_lobny_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_lobny_kom)

    elif call.data == "lobny_kon_kom":
        keyboard_lobny_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_lobny")
        keyboard_lobny_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_lobny")
        keyboard_lobny_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_lobny")
        keyboard_lobny_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="lobny")
        keyboard_lobny_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_lobny_kon_kom)

    elif call.data == "moe_lobny":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_lobny = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="lobny_kon_kom")
        keyboard3_moe_lobny.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\n1 офис, 2 кассы + терминалы\nПод какой % принимают платежи  наличными в кассе\nМОЕ - 1,77%. Все остальные поставщищи отсутствуют.\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - 1,77% картой.\nСвет - Терминал МКБ 1%.\nГаз - не принимают.\nГИБДД - 3% не менее 30 рублей.\nдо 99 руб-4,99 руб. от 100 руб -4,99%.\nСотовая связь - до 10 руб. -5 руб. //от 11 до 99 руб -5,99 руб. //от 100 руб.-5,99%\n",reply_markup=keyboard3_moe_lobny)

    elif call.data == "vtb_lobny":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_lobny = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="lobny_kon_kom")
        keyboard3_vtb_lobny.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (1 офис 4 банкомата.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая связь - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой ст банка 2% мин 20 руб.\nСвет - терминал без %, картой ст банка 2% мин 20 руб. \nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой сторонего банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_lobny)

    elif call.data == "sber_lobny":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_lobny = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="lobny")
        keyboard_sber_lobny.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офис/ 14 терминалов и банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ р/сч 6799  3% мин 50 руб., кап.ремонт 3% мин 50 руб.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 2,5% на окне картой мин 25 руб, нал в терминале 2%, картой 1,2%.\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_lobny)



    elif call.data == "dolgo":
        keyboard_dolgo = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="dolgo_kom")
        keyboard_dolgo.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="dolgo_kon_kom")
        keyboard_dolgo.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_dolgo.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_dolgo)

    elif call.data == "dolgo_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_dolgo_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dolgo")
        keyboard_dolgo_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_dolgo_kom)

    elif call.data == "dolgo_kon_kom":
        keyboard_dolgo_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_dolgo")
        keyboard_dolgo_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="МОЕ", callback_data="moe_dolgo")
        keyboard_dolgo_kon_kom.add(rele2)
        rele3 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_dolgo")
        keyboard_dolgo_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="dolgo")
        keyboard_dolgo_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_dolgo_kon_kom)

    elif call.data == "sber_dolgo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_dolgo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dolgo")
        keyboard_sber_dolgo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офис/4 терминал 13 банкоматов)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ р/сч 6799  3% мин 50 руб., кап.ремонт 3% мин 50 руб.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 2,5% на окне картой мин 25 руб, нал в терминале 2%, картой 1,2%.\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_dolgo)

    elif call.data == "moe_dolgo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_dolgo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dolgo_kon_kom")
        keyboard3_moe_dolgo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ отсутсвуют. 2 терминала.)\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - Терминал МКБ  МОЕ р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 1,5 %.\nСвет - Терминал МКБ 1%.\nГаз - не принимают.\nГИБДД - 3% не менее 30 рублей.\nдо 99 руб-4,99 руб. от 100 руб -4,99%.\nСотовая связь - до 10 руб. -5 руб. //от 11 до 99 руб -5,99 руб. //от 100 руб.-5,99%\n",reply_markup=keyboard3_moe_dolgo)


    elif call.data == "vtb_dolgo":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_dolgo = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="dolgo_kon_kom")
        keyboard3_vtb_dolgo.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (2 офис 8 банкоматов.)\n Под какой % принимают платежи  наличными в кассе. \nМОЕ - 1.5%, мin 200, мах 3000 руб.\nСвет - 1.5%, мin 200, мах 3000 руб\nГИБДД - 2% мин 75 руб.\nРостелеком - 1.5%, мin 200, мах 3000 руб\nСотовая свяхи - не принимается.\nОплата в банкомате, терминале/оплата в офисе картой: МОЕ - терминал без %, картой ст банка 2% мин 20 руб.\nСвет терминал без %, картой ст банка 2% мин 20 руб.\nГаз - терминал без %, картой ст банка 2% мин 20 руб.\nГИБДД - 4% наличными в терминале, картой банка без %.\nРостелеком - терминал без %, картой ст банка 2% мин 20 руб.\nСотовая связь - без %\n",reply_markup=keyboard3_vtb_dolgo)

    elif call.data == "mitish":
        keyboard_mitish = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="mitish_kom")
        keyboard_mitish.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="mitish_kon_kom")
        keyboard_mitish.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mitish")
        keyboard_mitish.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_mitish)

    elif call.data == "mitish_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_mitish_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="mitish")
        keyboard_mitish_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_mitish_kom)

    elif call.data == "mitish_kon_kom":
        keyboard_mitish_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_mitish")
        keyboard_mitish_kon_kom.add(rele1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mitish")
        keyboard_mitish_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_mitish_kon_kom)

    elif call.data == "sber_mitish":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_mitish = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_sber_mitish.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 1 офис/1 терминал)\nКомиссия при оплате наличными в кассе:\nМОЕ - МОЕ р/сч 6799  3% мин 50 руб., кап.ремонт 3% мин 50 руб.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - р/сч 6635 без комиссии; МОЕ р/сч 6799, кап ремонт 2,5% на окне картой мин 25 руб, нал в терминале 2%, картой 1,2%.\nСвет - 2,5% на окне картой мин 25 руб.// 1,5%  мин 10 руб. налич в терминале// 1,0 % картой в терминале.\nГаз - 2,5% на окне картой мин 25 руб// 2%  мин 10 руб. нал в терминале// 1,2% картой в терминале.\nГИБДД - 2,5% на окне картой// 2 % мин 10,00 нал в терминале// 1,2%  картой в терминале.\nРостелеком - 2,5% не менее 10 руб картой на окне/// 3%  мин 10,00 нал в терминале//  без %  картой в терминале.\nМобильная связь - терминал наличными 2,5% мин 5 руб ,картой без %.\n",reply_markup=keyboard_sber_mitish)



    if call.data == "voskres":
        keyboard_voskres = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Воскресенск", callback_data="voskres1")
        keyboard_voskres.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Егорьевск", callback_data="egor")
        keyboard_voskres.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Раменский район", callback_data="rama")
        keyboard_voskres.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Шатурский район", callback_data="shatura")
        keyboard_voskres.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_voskres.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboard_voskres)


    elif call.data == "shatura":
        keyboard_shatura = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="shatura_kom")
        keyboard_shatura.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="shatura_kon_kom")
        keyboard_shatura.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_shatura.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_shatura)

    elif call.data == "shatura_kon_kom":
        keyboard_shatura_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_shatura")
        keyboard_shatura_kon_kom.add(rele1)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_shatura_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_shatura_kon_kom)

    elif call.data == "sber_shatura":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_shatura = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_sber_shatura.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 4 офиса/1 терминал)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии,МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы\nГаз - наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии\n",reply_markup=keyboard_sber_shatura)

    elif call.data == "shatura_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_shatura_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="shatura")
        keyboard_shatura_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_shatura_kom)



    elif call.data == "rama":
        keyboard_rama = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="rama_kom")
        keyboard_rama.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="rama_kon_kom")
        keyboard_rama.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="voskres")
        keyboard_rama.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_rama)

    elif call.data == "rama_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_rama_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="rama")
        keyboard_rama_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_rama_kom)

    elif call.data == "rama_kon_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_rama = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="rama")
        keyboard3_moe_rama.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nАльтернативы нет\n",reply_markup=keyboard3_moe_rama)


    elif call.data == "egor":
        keyboard_egor = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="egor_kom")
        keyboard_egor.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="egor_kon_kom")
        keyboard_egor.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="voskres")
        keyboard_egor.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_egor)

    elif call.data == "egor_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_egor_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="egor")
        keyboard_egor_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_egor_kom)

    elif call.data == "egor_kon_kom":
        keyboard_egor_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Кассы МОЕ", callback_data="moe_egor")
        keyboard_egor_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_egor")
        keyboard_egor_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="egor")
        keyboard_egor_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_egor_kon_kom)
    elif call.data == "moe_egor":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_egor = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="egor_kon_kom")
        keyboard3_moe_egor.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ (оплата наличными в кассе не принимают. МКБ 1 офис, 2 терминала. Кассы МОЕ - 1.)\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - МКБ: терминал (наличными/картой) - МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - (внешняя) 1,5% от суммы.\nСвет наличные и карта - 1%.\nГаз - не принимают.\nГИБДД - 30 рублей.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -4,99% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%.\nСотовая связь - наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99% \n",reply_markup=keyboard3_moe_egor)


    elif call.data == "vtb_egor":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_vtb_egor = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="egor_kon_kom")
        keyboard3_vtb_egor.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nОтделения и терминлы ВТБ (оплата наличными в кассе не принимают. 1 офис 5 банкоматов.)\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nСвет наличные и карта - наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГаз - наличными: не принимаются. Карта ВТБ: без взимании комиссии.\nГИБДД - 0р.\nРостелеком - Наличными: 20 руб. Карта: без комиссии.\nСотовая связь - наличными без карты: не принимают. Карта: без комиссии\n",reply_markup=keyboard3_vtb_egor)

    elif call.data == "voskres1":
        keyboard_voskres1 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="voskres1_kom")
        keyboard_voskres1.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="voskres1_kon_kom")
        keyboard_voskres1.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="voskres")
        keyboard_voskres1.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard_voskres1)

    elif call.data == "voskres1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_voskres1_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="voskres")
        keyboard_voskres1_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_voskres1_kom)


    elif call.data == "voskres1_kon_kom":
        keyboard_voskres1_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Кассы МОЕ", callback_data="moe_voskres1")
        keyboard_voskres1_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_voskres1")
        keyboard_voskres1_kon_kom.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="voskres1")
        keyboard_voskres1_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_voskres1_kon_kom)

    elif call.data == "moe_voskres1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_voskres1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="voskres1_kon_kom")
        keyboard3_moe_voskres1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ (оплата наличными в кассе не принимают. МКБ 1 офис, 4 терминала. Кассы МОЕ - 3.)\n Оплата в банкомате, терпиналей/оплата в офисе картой: МОЕ - терминал МКБ, наличные и картой - 1,5%.\nСвет наличные и карта - 1%.\nГаз - не принимают.\nГИБДД - 30 рублей.\nРостелеком - до 99 руб. - 4,99 руб., от 100 руб -4,99% Мобильный Ростелеком: до 99 руб. - 4,99 руб., от 100 руб. - 4,99%.\nСотовая связь - наличными и картой: до 10 руб. - 5 руб., от 11 до 99 руб. - 5,99 руб., от 100 руб. - 5,99% \n",reply_markup=keyboard3_moe_voskres1)

    elif call.data == "sber_voskres1":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_voskres1 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="voskres1")
        keyboard_sber_voskres1.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 10 офисов/31 банкомат)\nКомиссия при оплате наличными в кассе:\nМОЕ - МосОблЕИРЦ (р/с …635) - без комиссии,МосОблЕИРЦ (р/с …799) внешняя -  наличка 3% от суммы,мин 50 руб., карта 2,5% мин 25руб. МОЕ кап.ремонт то же.\nСвет - 3% не менее 25р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5 %  не менее 10 рублей.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n МОЕ - Банкомат: МОЕ (р/с …635) - без комиссии, МОЕ (р/с…799) - внешняя 2% от суммы, карта 1,2%.\nСвет - наличными: 1,5% от суммы min 10 руб., max 2000 руб. Карта: 1% от суммы\nГаз - наличными 2% от суммы, min 10 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nГИБДД - наличными: 3% от суммы, min 20 руб., max 2000 руб.\nРостелеком - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: 1,2% от суммы, max 500 руб.\nМобильная связь - Наличными: 2% от суммы, min 5 руб., max 2000 руб. Карта: без комиссии\n",reply_markup=keyboard_sber_voskres1)


    if call.data == "balashiha":
        keyboardb = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Балашиха", callback_data="balashiha1")
        keyboardb.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Реутов", callback_data="reutov2")
        keyboardb.add(rele2)
        rele3 = types.InlineKeyboardButton(text="Ногинск", callback_data="noginsk")
        keyboardb.add(rele3)
        rele4 = types.InlineKeyboardButton(text="Электросталь", callback_data="stal")
        keyboardb.add(rele4)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboardb.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете район",reply_markup=keyboardb)

    elif call.data == "stal":
        keyboardstal = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="stal_kom")
        keyboardstal.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="stal_kon_kom")
        keyboardstal.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="balashiha")
        keyboardstal.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboardstal)

    elif call.data == "stal_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_stal_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="noginsk")
        keyboard_stal_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р. Комиссия за кап ремонт 1,68% мин 30р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_stal_kom)

    elif call.data == "stal_kon_kom":
        keyboard_stal_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Кассы МОЕ", callback_data="moe_stal")
        keyboard_stal_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_stal")
        keyboard_stal_kon_kom.add(rele2)
        rele2 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_stal")
        keyboard_stal_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="stal")
        keyboard_stal_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_stal_kon_kom)
    elif call.data == "moe_stal":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_stal = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stal_kon_kom")
        keyboard3_moe_stal.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ (оплата наличными в кассе и картой. 9 офисов):\nМОЕ - 1,2%. Всё остальное не принимают.\nСвет - 2,5% мин. 30р.\nГаз - 2,5% мин. 30р.\nРостелеком - 2,5% min 30р.\nСотовая связь - не принимают\n",reply_markup=keyboard3_moe_stal)
    elif call.data == "sber_stal":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_stal = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="stal")
        keyboard_sber_stal.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 7 офисов/20 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-3% не менее 50р.\nСвет - 3% не менее 50р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - не принимают\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2,5% мин.50 р (картой на кассе) 1,2% (картой в банкомате). Ростелеком и сотовая связь - 2% картой на кассе 1,2% картой в банкомате\nКассы",reply_markup=keyboard_sber_stal)
    elif call.data == "vtb_stal":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_vtb_stal = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_vtb_stal.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО ВТБ (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 2 офисов/5 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-1,5% не менее 200р. и не более 3000р.\nСвет - 1,5% не менее 200р. и не более 3000р.\nГаз - 1,5% не менее 200р. и не более 3000р.\nГИБДД - 2% не менее 75р.\nРостелеком - 1,5% не менее 200р. и не более 3000р.\nСотовая связь - 1,5% не менее 200р. и не более 3000р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2% мин.20р. + наличный расчет.",reply_markup=keyboard_vtb_stal)

    elif call.data == "noginsk":
        keyboardnoginsk = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="noginsk_kom")
        keyboardnoginsk.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="noginsk_kon_kom")
        keyboardnoginsk.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="balashiha")
        keyboardnoginsk.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboardnoginsk)

    elif call.data == "noginsk_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_noginsk_kom = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="noginsk")
        keyboard_noginsk_kom.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 25р. Комиссия за кап ремонт 1,68% мин 30р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,54 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_noginsk_kom)

    elif call.data == "noginsk_kon_kom":
        keyboard_noginsk_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Кассы МОЕ", callback_data="moe_noginsk")
        keyboard_noginsk_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_noginsk")
        keyboard_noginsk_kon_kom.add(rele2)
        rele2 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_noginsk")
        keyboard_noginsk_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="noginsk")
        keyboard_noginsk_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_noginsk_kon_kom)
    elif call.data == "moe_noginsk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_noginsk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="noginsk_kon_kom")
        keyboard3_moe_noginsk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ (оплата только наличными в кассе. 10 офисов):\nМОЕ - без комиссии. Всё остальное не принимают.\nСвет - 2,5% мин. 30р.\nГаз - 2,5% мин. 30р.\nРостелеком - 2,5% min 30р.\nСотовая связь - не принимают\n",reply_markup=keyboard3_moe_noginsk)
    elif call.data == "sber_noginsk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_noginsk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="noginsk")
        keyboard_sber_noginsk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 6 офисов/27 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-3% не менее 50р.\nСвет - 3% не менее 50р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - не принимают\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2,5% мин.50 р (картой на кассе) 1,2% (картой в банкомате). Ростелеком и сотовая связь - 2% картой на кассе 1,2% картой в банкомате\nКассы",reply_markup=keyboard_sber_noginsk)
    elif call.data == "vtb_noginsk":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_vtb_noginsk = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_vtb_noginsk.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО ВТБ (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 2 офисов/8 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-1,5% не менее 200р. и не более 3000р.\nСвет - 1,5% не менее 200р. и не более 3000р.\nГаз - 1,5% не менее 200р. и не более 3000р.\nГИБДД - 2% не менее 75р.\nРостелеком - 1,5% не менее 200р. и не более 3000р.\nСотовая связь - 1,5% не менее 200р. и не более 3000р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2% мин.20р. + наличный расчет.",reply_markup=keyboard_vtb_noginsk)

    elif call.data == "reutov2":
        keyboardreutov2 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="reutov2_kom")
        keyboardreutov2.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="reutov2_kon_kom")
        keyboardreutov2.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="balashiha")
        keyboardreutov2.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboardreutov2)

    elif call.data == "reutov2_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_reutov = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_reutov.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 30р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,54 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard_reutov)

    elif call.data == "reutov2_kon_kom":
        keyboard_reutov_kon_kom = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Кассы МОЕ", callback_data="moe_reutov2")
        keyboard_reutov_kon_kom.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_reutov2")
        keyboard_reutov_kon_kom.add(rele2)
        rele2 = types.InlineKeyboardButton(text="ВТБ", callback_data="vtb_reutov")
        keyboard_reutov_kon_kom.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_reutov_kon_kom.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard_reutov_kon_kom)
    elif call.data == "moe_reutov2":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3_moe_reutov2 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="keyboard_reutov_kon_kom")
        keyboard3_moe_reutov2.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nКассы МОЕ (оплата только наличными в кассе. 1 офис):\nМОЕ - 2%\nСвет - 2,5% мин. 30р.\nГаз - 2,5% мин. 30р.\nРостелеком - 2,5% min 30р.\nСотовая связь - не принимают\n",reply_markup=keyboard3_moe_reutov2)
    elif call.data == "sber_reutov2":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_sber_reutov2 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_sber_reutov2.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 7 офисов/97 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-3% не менее 50р.\nСвет - 3% не менее 50р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - 2,5% не менее 10р\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2,5% мин.50 р (картой на кассе) 1,2% (картой в банкомате). Ростелеком и сотовая связь - 2% картой на кассе 1,2% картой в банкомате\nКассы",reply_markup=keyboard_sber_reutov2)
    elif call.data == "vtb_reutov":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard_vtb_reutov = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="reutov2")
        keyboard_vtb_reutov.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО ВТБ (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 2 офисов/8 терминалов)\nКомиссия при оплате наличными в кассе:\nМОЕ-1,5% не менее 200р. и не более 3000р.\nСвет - 1,5% не менее 200р. и не более 3000р.\nГаз - 1,5% не менее 200р. и не более 3000р.\nГИБДД - 2% не менее 75р.\nРостелеком - 1,5% не менее 200р. и не более 3000р.\nСотовая связь - 1,5% не менее 200р. и не более 3000р.\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2% мин.20р. + наличный расчет.",reply_markup=keyboard_vtb_reutov)

    elif call.data == "balashiha1":
        keyboard2 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Комиссия почты", callback_data="balashiha1_kom")
        keyboard2.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Комиссия конкурентов", callback_data="balashiha1_kon_kom")
        keyboard2.add(rele2)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="balashiha")
        keyboard2.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете поставщика",reply_markup=keyboard2)
    elif call.data == "balashiha1_kom":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="balashiha1")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="МОЕ: - 1,68% мин 30р.\nАО Мосэнергосбыт - 2,44% мин 25 руб (внешняя)\nАО Мособлгаз - 2,5 % мин 25 руб (внешняя)\nГИБДД - 2,54% (внешняя), мин 25 руб.\nРостелеком - ГОПС 2,5 % мин. 10 руб. (внешняя), СОПС 4,1 % (внутренняя)\nСотовая связь - 6,4% (внешняя ) мин 10 руб. Прием в ФСГ и на МПКТ\n",reply_markup=keyboard3)
    elif call.data == "balashiha1_kon_kom":
        keyboard4 = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="Менада", callback_data="madana")
        keyboard4.add(rele1)
        rele2 = types.InlineKeyboardButton(text="Сбербанк", callback_data="sber_bal")
        keyboard4.add(rele2)
        rele2 = types.InlineKeyboardButton(text="Кассы БРЦ", callback_data="brc")
        keyboard4.add(rele3)
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="keyboard2")
        keyboard4.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете конкурента",reply_markup=keyboard2)
    elif call.data == "madana":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="keyboard4")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nМенада (оплата только наличными в кассе. 13 офисов):\nМОЕ - 2,5 %, min 30 р.\nСвет - 1,7%\nГаз - 2%\nРостелеком - 2,0% min 15 р.\nСотовая связь - 1,9%\n",reply_markup=keyboard3)
    elif call.data == "sber_bal":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="keyboard4")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="\nПАО Сбербанк (Оплату принимают и наличными в кассе, в банкоматах и терминалах. 29 офисов)\nКомиссия при оплате наличными в кассе:\nМОЕ-3% не менее 50р.\nСвет - 3% не менее 50р.\nГаз - 3% не менее 50р.\nГИБДД - 3% не менее 50р.\nРостелеком - 2,5% не менее 10р\nСотовая связь - не принимают\nКомиссия при оплате в терминале, банкомате картой и на кассе:\n Все КА - 2,5% мин.50 р (картой на кассе) 1,2% (картой в банкомате)\nКассы",reply_markup=keyboard3)
    elif call.data == "brc":
        bot.answer_callback_query(callback_query_id=call.id)
        keyboard3 = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Назад", callback_data="keyboard4")
        keyboard3.add(button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=")\nКассы БРЦ - принимают только наличными платежи МОЕ - 0,85 % с клиента, мин.5 руб.",reply_markup=keyboard3)

    elif call.data == "second":
        keyboards = types.InlineKeyboardMarkup()
        rele1 = types.InlineKeyboardButton(text="", callback_data="gg")
        backbutton = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboards.add(rele1, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboards)
    #if _name_ == "__main__":
    #   bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0) 
