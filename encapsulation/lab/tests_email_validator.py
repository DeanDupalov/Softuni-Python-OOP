import unittest
from encapsulation.lab.email_validator_02 import EmailValidator

class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_name("abc"), False)
        self.assertEqual(ev._EmailValidator__validate_name("abcdef"), True)

    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_mail("me"), True)
        self.assertEqual(ev._EmailValidator__validate_mail("you"), False)

    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_domain("he"), True)
        self.assertEqual(ev._EmailValidator__validate_domain("she"), False)

    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)


if __name__ == "__main__":
    unittest.main()