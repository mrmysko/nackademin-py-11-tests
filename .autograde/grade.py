import pytest
import doctest
import os


def test_smoke_stringt():
    import stringt

    stringt = getattr(stringt, "stringt")
    assert stringt("a", "b") == "a b\n"


def test_smoke_palindromish():
    import palindromish

    palindromish = getattr(palindromish, "palindromish")
    assert palindromish("kajak")


def test_smoke_treecoords():
    import treecoords

    treecoords = getattr(treecoords, "treecoords")
    assert treecoords({"a": {"b": {"c": 1}}}) == ((("a", "b", "c"), 1),)


def test_requirements_file():
    assert os.path.isfile("requirements.txt"), "requirements.txt file does not exist"
    assert os.path.getsize("requirements.txt") > 0, "requirements.txt file is empty"


def test_palindromish_doctest():

    import palindromish

    doctest_results = doctest.testmod(palindromish)

    assert doctest_results.attempted >= 3, "Expected at least three doctests"

    assert doctest_results.failed == 0, "Doctests failed"


def test_stringt_unittest():
    import test_stringt
    import unittest

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_stringt)

    assert suite.countTestCases() >= 3, "Expected at least three test cases"

    test_result = suite.run(unittest.TestResult())

    assert not test_result.failures


def test_treecoords_pytest():
    import test_treecoords

    with open(test_treecoords.__file__) as f:
        content = f.read()

    assert content.count("def test_") >= 3, "Expected at least three tests"

    result = pytest.main([test_treecoords.__file__])

    assert result == 0, "Tests failed"


def test_requirements_in_venv():

    import tempfile
    import subprocess

    with tempfile.TemporaryDirectory() as tmpdirname:
        subprocess.run(["python3", "-m", "venv", tmpdirname], check=True)
        subprocess.run(
            [f"{tmpdirname}/bin/pip", "install", "-r", "requirements.txt"], check=True
        )
        subprocess.run([f"{tmpdirname}/bin/pip", "show", "pytest"], check=True)
