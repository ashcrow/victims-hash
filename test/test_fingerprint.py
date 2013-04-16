import unittest

from victims_hash.fingerprint import fingerprint


class TestFinterprint(unittest.TestCase):
    """
    Test for the fingerprint function.
    """

    def test_input_restrictions(self):
        """
        Verify that we can not pass both file and io.
        """
        self.assertRaises(Exception, fingerprint, (True, True))
