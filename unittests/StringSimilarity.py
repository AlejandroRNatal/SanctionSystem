import unittest as ut
from ut import TestCase

import Sanction

import hypothesis as hp
from hp import given
from hp.strategies import text, example


class StringSimilarityMethods(TestCase):

    def test_sanctioned(self, s):
        return

    def test_not_sanctioned(self, s):
        return

    def test_not_sanctioned_25_percent(self, s):
        return

    def test_not_sanctioned_50_percent(selfs, s):
        return
    
    def test_sanctioned_75_percent(self, s):
        return
    
    def test_sanctioned_100_percent(self, s):
        return

    @given(s=text())
    @example(s='a')
    def test_first_arg_none(self,s):

        with self.assertRaises(ValueError):

            Sanction.str_similarity(s_a=None, s_b=s)
    
    @given(s=text())
    @example(s='a')
    def test_second_arg_none(self,s):

        with self.assertRaises(ValueError):

            Sanction.str_similarity(s_a=s, s_b=None)

    @given(s=text())
    @example(s='')
    def test_first_equal_second(self,s):
        if s =='':
            pass
        else:
            self.assertEqual(Sanction.str_similarity(s,s), 1.0)
    
    @given(s=text())
    @example(s='a')
    def test_first_non_empty_second_empty(self,s):

        self.assertEqual(Sanction.str_similarity(s,''), 1.0)

    @given(s=text())
    @example(s='a')
    def test_first_empty_second_non_empty(self,s):
        self.assertEqual(Sanction.str_similarity('',s), 1.0)
    
    def test_first_empty_second_empty(self):
        self.assertEqual(Sanction.str_similarity('',''), 1.0)

if __name__ == "__main__":
    ut.main()