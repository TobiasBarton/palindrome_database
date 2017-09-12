import unittest
import time
import json

from palindrome import Palindrome
import functions as func
from app import app


PALINDROME_STRINGS_UNCLEAN = [
'AL.ULA', ' CI!VIC', 'A"NANA', 'DEK,ED', 'DE[LED', 'DE}RED',
'DEW_ED', 'KA-IAK', 'KA?YAK', 'LEME!L', 'LEV>EL', 'MAD<AM', 
'MA   LAM', 'MIN:IM', 'RA;DAR', 'REF"E"R', 'R!OTOR', 'S  AGAS'
]

PALINDROME_STRINGS = [
'ALULA', 'CIVIC', 'ANANA', 'DEKED', 'DELED', 'DERED',
'DEWED', 'KAIAK', 'KAYAK', 'LEMEL', 'LEVEL', 'MADAM', 
'MALAM', 'MINIM', 'RADAR', 'REFER', 'ROTOR', 'SAGAS'
]

PALINDROME_OBJECTS = [Palindrome(item).serialize() for item in PALINDROME_STRINGS]


class FlaskTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_status_code(self):
        result = self.app.get('/palindromes')
        self.assertEqual(result.status_code, 200)

    def test_post_method_valid_string(self):
        result = self.app.post('/palindromes?string=alula')
        self.assertIn(b'true', result.data)

    def test_post_method_invalid_string(self):
        result = self.app.post('/palindromes?string=hello')
        self.assertIn(b'false', result.data)

    def test_get_method_data(self):
        self.app.post('palindromes?string=alula')
        result = self.app.get('/palindromes')
        self.assertIn(b'alula', result.data)


class FunctionTests(unittest.TestCase):

    def test_clean_string(self):
        check_list = []
        for item in PALINDROME_STRINGS_UNCLEAN:
            check_list.append(func.clean_string(item))
        self.assertEqual(check_list, PALINDROME_STRINGS)

    def test_get_last_pal(self):
        last_ten = func.last_palindromes(PALINDROME_OBJECTS, limit=10, duration=600)
        self.assertEqual(last_ten, PALINDROME_STRINGS[::-1][:10])


unittest.main()
