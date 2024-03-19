import unittest

from stringt import stringt


class Test_Stringt(unittest.TestCase):

    def test_base_case(self):
        # All parameters set correctly.
        self.assertEqual(
            stringt("Det", "här", "är", "en", "sträng", end="1.", sep="-"),
            "Det-här-är-en-sträng1.",
        )

    def test_list_to_string(self):
        # This tests that the return value is a string.
        self.assertIsInstance(stringt(["Good", "to", "be", "bad"]), str)

    def test_not_a_list(self):
        # Tests if input is not a list.
        self.assertTrue(stringt(False))

    def test_int_in_optional_paramters(self):
        # Tests if parameters were not strings.
        stringt(["Test", "sträng"], sep="_", end=1)

        stringt(["Test", "sträng"], sep=1, end="_")

        stringt(["Test", "sträng"], sep=False, end=False)


if __name__ == "__main__":
    unittest.main()
