from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует функцию и ее результат в файл и на консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if filename:
                    func(*args, **kwargs)
                    log_message = "my_function ok \n"
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                        print(log_message)
                else:
                    print("my_function ok \n")
            except Exception as e:
                error_mess = f"my_function error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(error_mess)
                    print(error_mess)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """Функция, которая делает сложения."""
    return x + y


my_function(1, 2)
