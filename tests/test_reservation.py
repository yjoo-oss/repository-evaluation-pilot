import unittest
from reservation import is_active


class ReservationTests(unittest.TestCase):
    def test_before_deadline(self):
        self.assertTrue(is_active(100, 99))

    def test_after_deadline(self):
        self.assertFalse(is_active(100, 101))

    def test_exact_deadline_is_expired(self):
        self.assertFalse(is_active(100, 100))
