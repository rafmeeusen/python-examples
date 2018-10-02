import unittest
from mymodule import is_workingday


class TestMyMmodule (unittest.TestCase):

    ''' TRUE week days '''
    def test_is_workingday_monday(self):
        self.assertTrue(is_workingday('2018-10-1'))
    def test_is_workingday_friday(self):
        self.assertTrue(is_workingday('2018-9-28'))
    def test_is_workingday_thursday_leapyear(self):
        self.assertTrue(is_workingday('1996-2-29'))
    def test_is_workingday_zeropadded_month(self):
        self.assertTrue(is_workingday('2018-09-28'))

    ''' FALSE weekend days '''
    def test_is_workingday_saturday(self):
        self.assertFalse(is_workingday('2018-9-29'))
    def test_is_workingday_sunday(self):
        self.assertFalse(is_workingday('2018-9-30'))
    def test_is_workingday_sunday2(self):
        self.assertFalse(is_workingday('1999-2-28'))

    ''' TypeError if argument is invalid type: '''
    def test_is_workingday_badtype_none(self):
        self.assertRaises(TypeError, is_workingday, None)

    ''' ValueError if right type but bad value '''
    def test_is_workingday_badformat_year_not_number(self):
        self.assertRaises(Exception, is_workingday, 'yyyy-10-23')
    def test_is_workingday_badformat_month_not_number(self):
        self.assertRaises(Exception, is_workingday, '2018-ab-23')
    def test_is_workingday_badformat_day_not_number(self):
        self.assertRaises(Exception, is_workingday, '2018-10-d1')
    def test_is_workingday_badformat_too_many_elements(self):
        self.assertRaises(ValueError, is_workingday, '1999-12-3-4')
    def test_is_workingday_badformat_reverse_format(self):
        self.assertRaises(ValueError, is_workingday, '1-10-1999')

    ''' ValueError, msg containing word 'exist', for non-existing dates '''
    def test_is_workingday_nonexisting_day(self):
        self.assertRaisesRegex(ValueError, "exist", is_workingday, '2018-9-31')
    def test_is_workingday_nonexisting_month(self):
        self.assertRaisesRegex(ValueError, 'exist', is_workingday, '2018-13-1')



