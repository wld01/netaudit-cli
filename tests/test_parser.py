"""Unit tests for netaudit.parser."""

import os
import tempfile
import unittest

from netaudit.parser import read_config


class TestReadConfig(unittest.TestCase):
    def test_read_config_returns_content(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".cfg", delete=False
        ) as tmp:
            tmp.write("hostname router1\ninterface gi0/0\n")
            path = tmp.name
        try:
            self.assertEqual(
                read_config(path), "hostname router1\ninterface gi0/0\n"
            )
        finally:
            os.unlink(path)

    def test_read_config_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            read_config("/nonexistent/path/to/config.cfg")


if __name__ == "__main__":
    unittest.main()
