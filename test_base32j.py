import unittest
import base32j


class TestBase32j(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(base32j.encode(b''), '')
        self.assertEqual(base32j.decode(''), b'')

    def test_simple(self):
        self.assertEqual(base32j.encode(b'\0'), '00')
        self.assertEqual(base32j.decode('00'), b'\0')

    def test_complex(self):
        b = b'\xfc?\xf9\x8e\x8cj\r0\x87\xd5\x15\xc0G?\x86w'
        s = base32j.encode(b)
        self.assertEqual(s, 'zgzzm3ncd86m11yp2r04efw6ew')
        d = base32j.decode(s)
        self.assertEqual(d, b)

    def test_full(self):
        for i in range(255):
            for j in range(32):
                b = bytes([(i + j + k) % 255 for k in range(j)])
                s = base32j.encode(b)
                d = base32j.decode(s)
                self.assertEqual(d, b)


if __name__ == '__main__':
    unittest.main()
