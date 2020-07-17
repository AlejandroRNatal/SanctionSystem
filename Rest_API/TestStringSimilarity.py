# import sys, os.path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# sys.path.insert(1,BASE_DIR)



import unittest
from unittest import TestCase



# from . import SanctionSystem
from Sanction import is_sanctioned,str_similarity

import hypothesis
from hypothesis import given
from hypothesis.strategies import text


class StringSimilarityMethods(TestCase):
    
    sanctioned_names = ['Jake Long', 'Kristopher Doe']
    sanctioned_organizations = ['Not Disney','Royal Arctic Line']
    sanctioned_countries = ['USA', 'Iceland']
    
    def test_sanctioned(self):

        sanctioned_names = ['Jake Long', 'Kristopher Doe']
        sanctioned_organizations = ['Not Disney','Royal Arctic Line']
        sanctioned_countries = ['USA', 'Iceland']

        # True cases
        #names
        self.assertTrue(is_sanctioned('Jake Long', sanctioned_names)[0])
        self.assertTrue(is_sanctioned('Kristopher Doe', sanctioned_names)[0])
        
        #countries
        self.assertTrue(is_sanctioned('USA', sanctioned_countries)[0])
        self.assertTrue(is_sanctioned('Iceland', sanctioned_countries)[0])
        
        #organizations
        self.assertTrue(is_sanctioned('Not Disney', sanctioned_organizations)[0])
        self.assertTrue(is_sanctioned('Royal Arctic Line', sanctioned_organizations)[0])
        

        return

    def test_not_sanctioned(self):

        sanctioned_names = ['Jake Long', 'Kristopher Doe']
        sanctioned_organizations = ['Not Disney','Royal Arctic Line']
        sanctioned_countries = ['USA', 'Iceland']


        #false cases
        #names
        self.assertFalse(is_sanctioned('Patricia', sanctioned_names)[0])
        self.assertFalse(is_sanctioned('Some Random Guy', sanctioned_names)[0])
        
        #countries
        self.assertFalse(is_sanctioned('Norway', sanctioned_countries)[0])
        self.assertFalse(is_sanctioned('China', sanctioned_countries)[0])
        
        #organizations
        self.assertFalse(is_sanctioned('JPMC', sanctioned_organizations)[0])
        self.assertFalse(is_sanctioned('Polaroid', sanctioned_organizations)[0])
        return

    
    @given(s=text())
    
    def test_first_arg_none(self,s):

        with self.assertRaises(ValueError):

            str_similarity(s_a=None, s_b=s)
    
    @given(s=text())
    
    def test_second_arg_none(self,s):

        with self.assertRaises(ValueError):

            str_similarity(s_a=s, s_b=None)

    @given(s=text())
    
    def test_first_equal_second(self,s):
        if s =='' or s == None:
            pass
        else:
            self.assertEqual(str_similarity(s,s), 1.0)
    
    @given(s=text())
    
    def test_first_non_empty_second_empty(self,s):
        if s == '':
            pass
        else:
            self.assertEqual(str_similarity(s,''), 0.0)

    @given(s=text())
    
    def test_first_empty_second_non_empty(self,s):
        if s == '':
            pass
        else:
            self.assertEqual(str_similarity('',s), 0.0)
    
    def test_first_empty_second_empty(self):
        self.assertEqual(str_similarity('',''), 1.0)

if __name__ == "__main__":
    unittest.main()