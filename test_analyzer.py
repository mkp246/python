import os
import unittest

def analyze_text(filename):
    with open(filename, 'r') as f:
        return sum_tuple((1, len(line)) for line in f)

def sum_tuple(iter):
    sumx = (0, 0)
    for x in iter:
        sumx = x[0] + sumx[0], sumx[1] + x[1]
    return sumx

class TextAnalysisTests(unittest.TestCase):
    """"Test for analyze text function"""

    def setUp(self): # fixture runs b4 each test
        """"create file for test case usage"""
        self.filename = 'text_analysis_text_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged to great civil war.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure')

    def tearDown(self):
        """"Fixture to delete the file"""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self): # self_ required to be detected as test
        """"Basic smoke test"""
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 128)

    def test_no_such_file(self):
        with self.assertRaises(IOError):
            analyze_text("foo_bar")

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    unittest.main()
