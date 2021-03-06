# -*- coding: utf-8 -*-
"""
    __init__

    Collect all tests here

"""
import unittest

from .test_banner import TestBanner, TestGetHtml
from .test_cms import TestCMS
from .test_menuitem import TestMenuItem


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestBanner),
        unittest.TestLoader().loadTestsFromTestCase(TestGetHtml),
        unittest.TestLoader().loadTestsFromTestCase(TestCMS),
        unittest.TestLoader().loadTestsFromTestCase(TestMenuItem),
    ])
    return test_suite
