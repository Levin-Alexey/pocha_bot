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
    button8 = types.InlineKeyboardButton(text="Люберцы", callback_data="balashiha")
    keyboardmain.add(button8)
    button9 = types.InlineKeyboardButton(text="Мытищи", callback_data="balashiha")
    keyboardmain.add(button9)
    button10 = types.InlineKeyboardButton(text="Наро - Фоминск", callback_data="balashiha")
    keyboardmain.add(button10)
    button11 = types.InlineKeyboardButton(text="Одинцово", callback_data="balashiha")
    keyboardmain.add(button11)
    button12 = types.InlineKeyboardButton(text="Орехово-Зуево", callback_data="balashiha")
    keyboardmain.add(button12)
    button13 = types.InlineKeyboardButton(text="Подольск", callback_data="balashiha")
    keyboardmain.add(button13)
    button14 = types.InlineKeyboardButton(text="Пушкинский", callback_data="balashiha")
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
        button8 = types.InlineKeyboardButton(text="Люберцы", callback_data="balashiha")
        keyboardmain.add(button8)
        button9 = types.InlineKeyboardButton(text="Мытищи", callback_data="balashiha")
        keyboardmain.add(button9)
        button10 = types.InlineKeyboardButton(text="Наро - Фоминск", callback_data="balashiha")
        keyboardmain.add(button10)
        button11 = types.InlineKeyboardButton(text="Одинцово", callback_data="balashiha")
        keyboardmain.add(button11)
        button12 = types.InlineKeyboardButton(text="Орехово-Зуево", callback_data="balashiha")
        keyboardmain.add(button12)
        button13 = types.InlineKeyboardButton(text="Подольск", callback_data="balashiha")
        keyboardmain.add(button13)
        button14 = types.InlineKeyboardButton(text="Пушкинский", callback_data="balashiha")
        keyboardmain.add(button14)
        button15 = types.InlineKeyboardButton(text="Химки", callback_data="balashiha")
        keyboardmain.add(button15)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберете Ваш почтамт",reply_markup=keyboardmain)



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
