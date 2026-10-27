
from pathlib import Path
import unittest

class ContactFormTests(unittest.TestCase):
    def test_required_form_fields(self):
        html = Path("index.html").read_text(encoding="utf-8")

        self.assertIn('id="contactForm"', html)
        self.assertIn('name="name"', html)
        self.assertIn('type="email"', html)
        self.assertIn('name="contact"', html)
        self.assertIn('type="submit"', html)

if __name__ == "__main__":
    unittest.main()
