import io
import textwrap
import unittest
from logging.config import fileConfig


class TestLoggingConfig(unittest.TestCase):
    config = textwrap.dedent(
        """
        [loggers]
        keys=root
        [logger_root]
        level=INFO
        handlers=console
        [handlers]
        keys=console
        [handler_console]
        class=logging.StreamHandler
        formatter=console
        args=(sys.stdout,)
        [formatters]
        keys=console
        [formatter_console]
        format=CONSOLE: %(asctime)s %(levelname)s %(message)s
        class=%CLASS%
        """
    )

    def file_config(self, cls, **kwargs):
        f = io.StringIO(self.config.replace("%CLASS%", cls))
        fileConfig(f, **kwargs)

    def test_case0(self):
        self.file_config("logging.Formatter")

    def test_case1(self):
        self.file_config("foo.logging.FooBarFormatter")

    def test_case2(self):
        self.file_config("bar.logging.FooBarFormatter")

    def test_case3(self):
        self.file_config("baz.logging.FooBarFormatter")


if __name__ == "__main__":
    unittest.main()
