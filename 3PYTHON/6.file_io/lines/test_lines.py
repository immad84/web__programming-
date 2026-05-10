from lines import is_valid_file, main, get_line_count
import pytest
import sys


def test_main_no_args(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py"])
    with pytest.raises(SystemExit) as e:
        main()
    assert str(e.value) == "Too few command-line arguments"


def test_main_many_args(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "foo", "bar"])
    with pytest.raises(SystemExit) as e:
        main()
    assert str(e.value) == "Too many command-line arguments"


def test_main_is_file_exist(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ["lines.py", "non-existent.py"])
    with pytest.raises(SystemExit) as e:
        main()
    assert str(e.value) == "File does not exist"


def test_main(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "test.py"])
    main()
    captured = capsys.readouterr()
    assert captured.out == "5\n"


def test_is_valid():
    assert is_valid_file(["lines.py", "foo.py"]) == "foo.py"
    with pytest.raises(ValueError) as e:
        is_valid_file(["lines.py", "foo"])
    assert str(e.value) == "Not a Python file"


def test_get_line_count(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "test.py"])
    file = sys.argv[1]
    with open(file) as file:
        assert get_line_count(file) == 5
