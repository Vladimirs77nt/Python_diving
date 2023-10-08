# Задание

# 1. Решить задания, которые не успели решить на семинаре.
# 2. Доработаем задания 5-6. Создайте класс-фабрику:
#     Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#     Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
#     Превратите функции в методы класса, а параметры в свойства.
#     Задания должны решаться через вызов методов экземпляра.

# БАНКОМАТ... еще в работе....


def init ():
    print ()
    print ("-"*50)
    print ("       <<< ДОБРО ПОЖАЛОВТЬ В БАНКОМАТ >>>")
    print ("-"*50)
    print ()
    global cash, operation_count, operation_record, wealth_tax
    cash = 0                # сумма счета
    operation_count = 1     # счетчик операций
    operation_record = []   # журнал операций
    wealth_tax = False      # налог на богатство
    
def view_menu ():
    print (" --- МЕНЮ БАНКОМАТА ---")
    print (" >>> выберите:")
    print ("1. Пополнить счет")
    print ("2. Снять со счета")
    print ("3. Выйти")
    print ("4. Показать историю (log) операций")
    print ()
    view_cash ()

def view_cash ():
    global cash
    cash = round (cash, 2)
    print (f" >> Текущий баланс: {cash}")
    print ()
    
def controller ():
    global cash, operation_count, operation_record, wealth_tax
    view_menu ()

    while True:
        choice = input ("Выберите действие: ")
        match choice:

            # ПОПОЛНИТЬ счет
            case "1":
                print ()
                print (">> выбрано '1. Пополнить счет'")
                print ()
                cash_in = amount_selecrion ()
                print ()
                if cash_in > 0:
                    print (f" >> Счет пополнен на {cash_in}")
                    cash += cash_in
                    operation_record.append (f"{operation_count}. Пополнение счета на {cash_in}. Баланс {cash}")
                    print ()
                    operation_count += 1
                    if (operation_count-1)%3 == 0:
                        view_cash ()
                        accrual_of_money_interest (3)
                if cash_in == 0:
                    print (f" -- Операция прервана! Счет не пополнен...")
                    operation_record.append (" >> Операция прервана! Счет не пополнен...")
                    print ()
                view_menu ()

            # СНЯТЬ со счета
            case "2":
                print ()
                print (">> выбрано '2. Снять со счета'")
                print ()
                if cash < 30:
                    print (">> суммы на счете не хватает для выполнения операции!")
                    print ()
                else:
                    cash_out = amount_selecrion ()
                    print ()
                    if cash_in == 0:
                        print (f" -- Операция прервана! Со счета ничего не снято...")
                        operation_record.append (" >> Операция прервана! Со счета ничего не снято...")
                        print ()
                        operation_wealth_tax (10, 5000000)
                    elif cash_out > cash:
                        print (f" >> Введенная сумма ({cash_out}) превышает баланс счета!")
                        operation_wealth_tax (10, 5000000)
                    elif cash_out > 0:
                        # percentage_for_withdrawal_of_money - процент за снятие денег = 1,5 %
                        percentage_for_withdrawal_of_money = round (cash_out*1.5/100, 2)
                        if percentage_for_withdrawal_of_money < 30:
                            percentage_for_withdrawal_of_money = 30
                        if percentage_for_withdrawal_of_money > 600:
                            percentage_for_withdrawal_of_money = 600
                        if (cash_out + percentage_for_withdrawal_of_money) > cash:
                            print (f" >> Введенная сумма ({cash_out}), с учетом процента за снятие ({percentage_for_withdrawal_of_money}), превышает баланс счета!")
                            print (f" -- Операция прервана! Со счета ничего не снято...")
                            operation_record.append (" >> Операция прервана! Со счета ничего не снято...")
                        else:
                            print (f" >> Введена сумма {cash_out}")
                            print (f" >> Процент за снятие: {percentage_for_withdrawal_of_money}.  Итого сумма списания: {cash_out + percentage_for_withdrawal_of_money}")
                            cash -= (cash_out + percentage_for_withdrawal_of_money)
                            print (f" >> Со счета снято {cash_out} ({cash_out + percentage_for_withdrawal_of_money})")
                        operation_record.append (f"{operation_count}. Списание со счета суммы {cash_out} ({cash_out + percentage_for_withdrawal_of_money}). Баланс {cash}")
                        print ()
                        operation_count += 1
                        if (operation_count-1)%3 == 0:
                            view_cash ()
                            accrual_of_money_interest (3)
                view_menu ()

            # ВЫХОД из программы
            case "3" | "0":
                print ()
                print (">> выбрано '3. Выйти'")
                print ()
                view_cash ()
                print (">> Программа завершена...")
                print ()
                break

            # ПОКАЗАТЬ ЖУРНАЛ ОПЕРАЦИЙ СО СЧЕТОМ
            case "4":
                print ()
                operation_wealth_tax (10, 5000000)
                print ()
                view_cash ()
                print (">> выбрано '4. Показать историю (log) операций'")
                print ()
                if operation_count > 0:
                    for i in operation_record:
                        print(f" >> record:  {i}")
                    print (" >> record:      ----- конец записи -----")
                else:
                    print (" >> record:      ----- запись пустая -----")
                print ()
                view_menu ()

            case _:
                print ()
                print (">> команда не распознана! пожалуйста повторите выбор...")
                operation_wealth_tax (10, 5000000)
                print ()
                view_menu ()

# ИНТЕРФЕЙС ВЫБОРА (ВВОДА) СУММЫ
def amount_selecrion ():
    view_cash ()
    global cash
    print ("Внимание !!!")
    print (" ✔ Сумма пополнения и снятия кратны 50 у.е.")
    print (" ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.")

    while True:
        print ()
        operation_wealth_tax (10, 5_000_000)
        amount_selection = input ("Введите сумму (0 - выход): ")
        if amount_selection == "0":
            return 0
        if amount_selection.isdigit():
            if int(amount_selection)%50 == 0:
                cash_input = int(amount_selection)
                return cash_input
            else:
                print (" >>> Ошибка ввода суммы !!! ✔ Сумма пополнения и снятия кратны 50 у.е.")
                print (" ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.")
        else:
            print (" >>> Ошибка ввода !!! ✔ Введите число !")

# НАЧИСЛЕНИЕ ДЕНЕЖНЫХ ПРОЦЕНТОВ      
def accrual_of_money_interest (proc):
    global cash
    summ_proc = round (cash*proc/100, 2)
    print (f" >> НАЧИСЛЕНЫ ПРОЦЕНТЫ ( +{proc}% ) !!! => +{summ_proc}")
    cash += round(summ_proc, 2)
    operation_record.append (f" -- Начислены проценты: +{proc}% (+{summ_proc}). Баланс {cash}")
    print ()

# ОПЕРАЦИЯ СНЯТИЯ НАЛОГА НА БОГАТСТВО
def operation_wealth_tax (tax, wealth_limit):
    global cash, wealth_tax
    if cash < wealth_limit:
        wealth_tax = False
        return False
    wealth_tax = True
    summ_tax = round (cash*tax/100, 2)
    print ()
    print (f" >> СПИСАН НАЛОГ НА БОГАТСТВО ( -{tax}% ) !!! => -{summ_tax}")
    cash -= summ_tax
    operation_record.append (f" -- Списан налог на богатство: -{tax}% (-{summ_tax}). Баланс {cash}")
    return True

###########################################################
# --- ЗАПУСК

init ()
controller ()