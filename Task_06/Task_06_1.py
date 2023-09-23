# Задание 1 

# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами (3-7 строк импорта).

from DZ_04.DZ_04_3 import view_menu as vm
from DZ_05.DZ_05_1 import func as prost

print ("--- 1 ---")
vm ()

print ("--- 2 ---")
a = prost ()
for _ in range (20):
    print (next(a))