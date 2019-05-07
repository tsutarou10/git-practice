#coding:utf-8

import unittest
import print_hello_world
import sys
from io import StringIO
from test.support import captured_stdout

class PrintHelloWorldTest(unittest.TestCase):
    def setUp(self):
        # sys.stdoutを退避し、StringIO()で上書きする
        self.capture = StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        # 退避していたsys.stdoutを戻す
        sys.stdout = sys.__stdout__

    def test_print_hello(self):
        test1 = 'Tokyo'
        test2 = 'tOkyo'
        test3 = 'Kanagawa'
        test4 = 'kanagawa'
        test5 = 'Osaka'

        with captured_stdout() as stdout:
            print_hello_world.print_hello(test1)
            print_hello_world.print_hello(test2)
            print_hello_world.print_hello(test3)
            print_hello_world.print_hello(test4)
            print_hello_world.print_hello(test5)

            lines = stdout.getvalue().splitlines()

        self.assertEqual(lines[0], 'hello tokyo')
        self.assertEqual(lines[1], 'hello tokyo')
        self.assertEqual(lines[2], 'hello kanagawa')
        self.assertEqual(lines[3], 'hello kanagawa')
        self.assertEqual(lines[4], 'hello world')

if __name__ == '__main__':
    unittest.main()
