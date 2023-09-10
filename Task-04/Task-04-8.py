# Задание №8

# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». 
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
#    (кроме переменной из одной буквы s) на None. 
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def func ():
    globals_temp ={}
    for i in globals():
        if not i.startswith("__"):
            if i.endswith("s") and len(i)>1:
                globals_temp[i[:-1]] = globals()[i]
                globals_temp[i] = None
    globals().update(globals_temp)
            
start = 100
s = "Letter"
apples = 8734
codes = 1010100100010
func()
print([item for item in globals().items() if not item[0].startswith("__")])

print(apple)
print(code)