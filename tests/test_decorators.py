from src.decorators import my_function, log
from typing import Any


def test_log(capsys: Any) -> Any:
    log(filename="mylog.txt")
    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == ("my_function error: unsupported operand type(s) "
                            "for +: 'int' and 'str'. Inputs:(1, '2'), {}\n")


def test_log_for_emty(capsys: Any) -> Any:
    log(filename="")
    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == ("my_function error: unsupported operand type(s) "
                            "for +: 'int' and 'str'. Inputs:(1, '2'), {}\n")


def test_for_emty(capsys: Any) -> Any:
    log(filename="")
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok \n\n"
