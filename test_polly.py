import unittest

from polly import Parrot, ParrotType


class TestPolly(unittest.TestCase):

    def test_speed_of_european_parrot(self):
        polly = Parrot(ParrotType.EUROPEAN, 0, 0, False)
        self.assertEqual(polly.get_speed(), 12.0)

    def test_speed_of_african_parrot(self):
        polly = Parrot(ParrotType.AFRICAN, 1, 0, False)
        self.assertEqual(polly.get_speed(), 3.0)

    def test_speed_of_african_parrot_with_two_coconuts(self):
        polly = Parrot(ParrotType.AFRICAN, 2, 0, False)
        self.assertEqual(polly.get_speed(), 0.0)

    def test_speed_of_african_parrot_with_no_coconuts(self):
        polly = Parrot(ParrotType.AFRICAN, 0, 0, False)
        self.assertEqual(polly.get_speed(), 12.0)

    def test_speed_of_nailed_norwegian_blue_parrot(self):
        polly = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 0, True)
        self.assertEqual(polly.get_speed(), 0.0)

    def test_speed_of_not_nailed_charged_norwegian_blue_parrot(self):
        polly = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 1.5, False)
        self.assertEqual(polly.get_speed(), 18.0)

    def test_speed_of_not_nailed_supercharged_norwegian_blue_parrot(self):
        polly = Parrot(ParrotType.NORWEGIAN_BLUE, 0, 4, False)
        self.assertEqual(polly.get_speed(), 24.0)


if __name__ == '__main__':
    unittest.main()
