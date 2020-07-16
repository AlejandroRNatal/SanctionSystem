import unittest as ut
from ut import TestCase

import Sanction

import hypothesis as hp
from hp import given
from hp.strategies import text, example


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
        self.assertTrue(Sanction.is_sanctioned('Jake Long', sanctioned_names)[0])
        self.assertTrue(Sanction.is_sanctioned('Kristopher Doe', sanctioned_names)[0])
        
        #countries
        self.assertTrue(Sanction.is_sanctioned('USA', sanctioned_countries)[0])
        self.assertTrue(Sanction.is_sanctioned('Iceland', sanctioned_countries)[0])
        
        #organizations
        self.assertTrue(Sanction.is_sanctioned('Not Disney', sanctioned_organizations)[0])
        self.assertTrue(Sanction.is_sanctioned('Royal Arctic Line', sanctioned_organizations)[0])
        

        return

    def test_not_sanctioned(self, s):

        sanctioned_names = ['Jake Long', 'Kristopher Doe']
        sanctioned_organizations = ['Not Disney','Royal Arctic Line']
        sanctioned_countries = ['USA', 'Iceland']


        #false cases
        #names
        self.assertFalse(Sanction.is_sanctioned('Patricia', sanctioned_names)[0])
        self.assertFalse(Sanction.is_sanctioned('Some Random Guy', sanctioned_names)[0])
        
        #countries
        self.assertFalse(Sanction.is_sanctioned('Norway', sanctioned_countries)[0])
        self.assertFalse(Sanction.is_sanctioned('China', sanctioned_countries)[0])
        
        #organizations
        self.assertFalse(Sanction.is_sanctioned('JPMC', sanctioned_organizations)[0])
        self.assertFalse(Sanction.is_sanctioned('Polaroid', sanctioned_organizations)[0])
        return

    def test_not_sanctioned_25_percent(self, s):
        '''Add the percentage logic here'''
        sanctioned_names = ['Jake Long', 'Kristopher Doe']
        sanctioned_organizations = ['Not Disney','Royal Arctic Line']
        sanctioned_countries = ['USA', 'Iceland']


        #false cases
        #names
        status, probability = Sanction.is_sanctioned('Patricia', sanctioned_names)
        self.assertFalse(status)
        self.assertEqual(probability,0.25)

        status, probability = Sanction.is_sanctioned('Some Random Guy', sanctioned_names)
        self.assertFalse(status)
        self.assertEqual(probability,0.25)
        
        #countries
        status, probability = Sanction.is_sanctioned('Norway', sanctioned_countries)
        self.assertFalse(status)
        self.assertEqual(probability, 0.25)

        status, probability = Sanction.is_sanctioned('Chaine', sanctioned_countries)
        self.assertFalse(status)
        self.assertEqual(probability,0.25)

        #organizations
        status, probability = Sanction.is_sanctioned('JPMC', sanctioned_organizations)
        self.assertFalse(status)
        self.assertEqual(probability,0.25)
        
        status, probability = Sanction.is_sanctioned('Polaroid', sanctioned_organizations)
        self.assertFalse(status)
        self.assertEqual(probability,0.25)
        return

    def test_not_sanctioned_50_percent(self, s):
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