# Задание №5

# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.

# Напишите 3-7 тестов unittest для данного класса.


import unittest
from Rectangle import Rectangle

class TestCaseName(unittest.TestCase):

    def setUp(self) -> None:
        self.rect1 = Rectangle (4, 5)
        self.rect2 = Rectangle (2, 10)
        self.rect3 = Rectangle (3, 3)
        self.rect4 = self.rect1 + self.rect3
    
    def test_method_1 (self):
        self.assertEqual(self.rect1, self.rect2)

    def test_method_2 (self):
        self.assertNotEqual(self.rect1, self.rect3)

    def test_method_3 (self):
        self.assertRaises (ValueError, Rectangle, 0)

    def test_method_4 (self):
        self.assertRaises (ValueError, Rectangle, 0, 3)

    def test_method_5 (self):
        self.assertRaises (TypeError, Rectangle, None)

    def test_method_6 (self):
        self.assertEqual(self.rect1.perimeter(), 18)

    def test_method_7 (self):
        self.assertEqual(self.rect1.area(), 20)

    def test_method_8 (self):
        self.assertGreater(self.rect1, self.rect3)

    def test_method_9 (self):
        self.assertEqual(self.rect3.get_type(), "Квадрат")

    def test_method_11 (self):
        self.assertEqual(self.rect1 + self.rect3, Rectangle (7, 8))

    def test_method_12 (self):
        self.assertEqual(self.rect1 - self.rect3, Rectangle (1, 2))

    def test_method_13 (self):
        self.assertEqual(self.rect1.__str__(), "Прямоугольник со сторонами 4 и 5")

    def test_method_13 (self):
        self.assertEqual(self.rect3.__str__(), "Квадрат со стороной 3")
        

unittest.main(verbosity=2)