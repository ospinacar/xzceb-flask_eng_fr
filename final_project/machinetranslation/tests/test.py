import unittest
from translator import english_french, french_english

class Testenglish_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_french('hello'),'Bonjour')
        self.assertEqual(english_french('Star'),'Étoile')
        self.assertNotEqual(english_french('hello'),'Buendia')
        

class Testfrench_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_english('bonjour'),'Hello')
        self.assertEqual(french_english('Étoile'),'Star')
        self.assertNotEqual(french_english('bonjour'),'Hola')

unittest.main()
