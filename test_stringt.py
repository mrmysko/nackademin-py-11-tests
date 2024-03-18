import unittest

from stringt import stringt


class Test_Stringt(unittest.TestCase):

    # All parameters set correctly.
    def test_base_case(self):
        self.assertEqual(
            stringt("Det", "här", "är", "en", "sträng", end="1.", sep="-"),
            "Det-här-är-en-sträng1.",
        )


if __name__ == "__main__":
    unittest.main()
