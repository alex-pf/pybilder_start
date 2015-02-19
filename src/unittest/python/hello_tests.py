__author__ = 'pf'
#from mockito import mock, when, any, unstub, verify
import unittest
import sys

import hello_world

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message (self):
        h = hello_world.hello_world_class()
        self.assertEqual(h.sayHello(),'Hello user')

if __name__ == '__main__':
    unittest.main()