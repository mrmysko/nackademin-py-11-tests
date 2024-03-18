import unittest

from stringt import stringt


class Test_Stringt(unittest.TestCase):

    # All parameters set correctly.
    def test_base_case(self):
        self.assertEqual(
            stringt("Det", "här", "är", "en", "sträng", end="1.", sep="-"),
            "Det-här-är-en-sträng1.",
        )

    def test_list_to_string(self):
        self.assertIsInstance(stringt(["Good", "to", "be", "bad"]), str)

    def test_not_a_list(self):
        self.assertTrue(stringt("Det ballar ur"))

    def test_int_in_optional(self):
        # ...så det här testet går igenom för att ett error blir raised. Det ser ju ut som att allt funkar då, men det ska ju inte funka.
        # Ska man börja koda så att testet fallerar nu elr?
        # with self.assertRaises(TypeError):
        #    stringt(["Test", "sträng"], sep="_", end=1)
        stringt(["Test", "sträng"], sep="_", end=1)

        # with self.assertRaises(AttributeError):
        stringt(["Test", "sträng"], sep=1, end="_")


if __name__ == "__main__":
    unittest.main()
