import main
import sys

def test_get_python_version():
    assert main.get_python_version() == sys.version
