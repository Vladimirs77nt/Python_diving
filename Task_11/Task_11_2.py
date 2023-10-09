# Задание №2

# - Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# - При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
#    в пару списков-архивов
# - List-архивы также являются свойствами экземпляра

import copy


class Archive:
    archive_list = []
    
    def __init__(self,  num: int, text: str):
        self.num = num
        self.text = text
        self.archive = copy.deepcopy(Archive.archive_list)
        Archive.archive_list.append ([num, text])
    

a1 = Archive (10, "Вова")
a2 = Archive (20, "Люба")
a3 = Archive (25, "Анжелика")
print (a1.num, a1.text, a1.archive)
print (a2.num, a2.text, a2.archive)
print (a3.num, a3.text, a3.archive)