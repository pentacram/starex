import unittest
from unittest.mock import patch
from main import main
from request import request

class Teststarex(unittest.TestCase):

    def test_403(self):
        self.assertEqual(request('https://www.hepsiburada.com/protex-ultra-koruma-antibakteriyel-sivi-sabun-300-ml-p-SGARPFTR12954?magaza=Hepsiburada'), 
                                    'Security Alert, Permission Denied', 'OK')
    
    def test_suwen(self):
        self.assertEqual(request('https://www.suwen.com.tr/p/erkek-bambu-corap-siyah-sc1183012-2908'),
                        '19,90 TL', 'OK')

    def test_main(self):
        fake_args = [None, 'https://www.defacto.com.tr/beli-buzgulu-kapusonlu-uzun-mont-1574817']
        with patch('sys.argv', fake_args):
            self.assertEqual(main(), '159,99 TL', 'OK')

    



if __name__ == '__main__':
    unittest.main()
