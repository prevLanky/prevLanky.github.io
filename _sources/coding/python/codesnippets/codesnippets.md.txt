# Codesnippets

## Custom Classes
asd
### std::expected
```python
from typing import Generic, TypeVar, Callable, Optional

T = TypeVar("T")  # Value type
E = TypeVar("E")  # Error type
U = TypeVar("U")  # Return type for and_then/or_else

class Expected(Generic[T, E]):
    """
    Python implementation of C++ std::expected.
    Supports None as a valid value.
    Provides value(), error(), value_or(), error_or(), and_then(), or_else().
    """
    __slots__ = ("_value", "_error", "_has_value")

    def __init__(self, value: Optional[T] = None, error: Optional[E] = None, *, has_value: Optional[bool] = None):
        if has_value is None:
            has_value = error is None

        if has_value:
            if error is not None:
                raise ValueError("Cannot have error when creating a value Expected")
            self._value = value  # None is valid
            self._error = None
        else:
            if value is not None:
                raise ValueError("Cannot have value when creating an error Expected")
            self._value = None
            self._error = error

        self._has_value = has_value

    def has_value(self) -> bool:
        return self._has_value

    def value(self) -> T:
        if not self._has_value:
            raise ValueError(f"No value present. Error: {self._error!r}")
        return self._value

    def error(self) -> E:
        if self._has_value:
            raise ValueError(f"No error present. Value: {self._value!r}")
        return self._error

    def value_or(self, default: T) -> T:
        return self._value if self._has_value else default

    def error_or(self, default: E) -> E:
        return self._error if not self._has_value else default

    def and_then(self, fn: Callable[[T], "Expected[U, E]"]) -> "Expected[U, E]":
        if self._has_value:
            try:
                result = fn(self._value)
                if not isinstance(result, Expected):
                    raise TypeError("and_then function must return an Expected instance")
                return result
            except Exception as e:
                return Expected(error=e)
        return Expected(error=self._error)

    def or_else(self, fn: Callable[[E], "Expected[T, U]"]) -> "Expected[T, U]":
        if not self._has_value:
            try:
                result = fn(self._error)
                if not isinstance(result, Expected):
                    raise TypeError("or_else function must return an Expected instance")
                return result
            except Exception as e:
                return Expected(error=e)
        return Expected(value=self._value)

    def __repr__(self) -> str:
        if self._has_value:
            return f"Expected(value={self._value!r})"
        return f"Expected(error={self._error!r})"
```

### std::Expected unit test
You can add this if you want to ensure nothing changes in case the std::Expected class is changed.
```python
import pytest
import sys
import os
# Add the Python package root dynamically
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from expected import Expected

def test_value_creation():
    e = Expected(42)
    assert e.has_value
    assert e.value == 42
    with pytest.raises(ValueError):
        _ = e.error

def test_none_value_creation():
    e = Expected(None)
    assert e.has_value
    assert e.value is None
    with pytest.raises(ValueError):
        _ = e.error

def test_error_creation():
    e = Expected(error="error occurred")
    assert not e.has_value
    assert e.error == "error occurred"
    with pytest.raises(ValueError):
        _ = e.value

def test_value_or():
    e_val = Expected(10)
    e_err = Expected(error="fail")
    assert e_val.value_or(0) == 10
    assert e_err.value_or(0) == 0

def test_error_or():
    e_val = Expected(10)
    e_err = Expected(error="fail")
    assert e_val.error_or("default") == "default"
    assert e_err.error_or("default") == "fail"


def test_and_then_value():
    def next_step(x: int) -> Expected[int, str]:
        return Expected(x * 2)

    e = Expected(5)
    result = e.and_then(next_step)
    assert result.has_value
    assert result.value == 10


def test_and_then_error_propagates():
    def next_step(x: int) -> Expected[int, str]:
        return Expected(x * 2)

    e = Expected(error="fail")
    result = e.and_then(next_step)
    assert not result.has_value
    assert result.error == "fail"


def test_or_else_error():
    def recover(err: str) -> Expected[int, str]:
        return Expected(99)

    e = Expected(error="fail")
    result = e.or_else(recover)
    assert result.has_value
    assert result.value == 99


def test_or_else_value_propagates():
    def recover(err: str) -> Expected[int, str]:
        return Expected(99)

    e = Expected(42)
    result = e.or_else(recover)
    assert result.has_value
    assert result.value == 42


def test_and_then_exception_caught():
    def fail_fn(x):
        raise RuntimeError("oops")

    e = Expected(1)
    result = e.and_then(fail_fn)
    assert not result.has_value
    assert isinstance(result.error, RuntimeError)


def test_or_else_exception_caught():
    def fail_fn(err):
        raise RuntimeError("oops")

    e = Expected(error="fail")
    result = e.or_else(fail_fn)
    assert not result.has_value
    assert isinstance(result.error, RuntimeError)
```
### Logger
```python
import sys
import threading
from datetime import datetime
import traceback
import inspect

"""
TODO: Add loglevel in order to control what is printed etc.
        But how to remove the statements in production?
        I dont even want to call the functions?
        But it might not be an issue, since errors and warns does print that often?
"""
class Logger:
    _instance = None
    _lock = threading.Lock()

    COLORS = {
        "DEBUG": "\033[90m",
        "INFO":  "\033[92m",
        "WARN":  "\033[93m",
        "ERROR": "\033[91m",
        "FATAL": "\033[95m",
        "RESET": "\033[0m"
    }

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, use_colors=True, show_caller_info=True):
        if hasattr(self, "_initialized"):
            return
        self.use_colors = use_colors and sys.stdout.isatty()
        self.show_caller_info = show_caller_info
        self._write_lock = threading.Lock()
        self._initialized = True

    def _colorize(self, message, level_name):
        if not self.use_colors:
            return message
        return f"{self.COLORS[level_name]}{message}{self.COLORS['RESET']}"

    #def _get_caller_info(self):
    #    """Get file and line of the caller, without function name."""
    #    frame = inspect.stack()[3]  # skip logger internals
    #    filename = frame.filename
    #    lineno = frame.lineno
    #    return f"{filename}:{lineno}"
    
    def _get_caller_info(self):
        """Get file, line, and optionally function of the caller."""
        frame = inspect.stack()[3]  # skip logger internals
        filename = frame.filename
        lineno = frame.lineno
        funcname = frame.function
        return f"{filename}:{funcname}():{lineno}:"

    def _log(self, text, level_name, fatal_extra=True):
        #timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        caller_info = f" {self._get_caller_info()}" if self.show_caller_info else ""
        msg = f"[{level_name}]{caller_info} {text}"

        with self._write_lock:
            print(self._colorize(msg, level_name))

            if level_name == "FATAL" and fatal_extra:
                print("\n=== STACK TRACE ===")
                traceback.print_stack()
                print("==================")
                sys.exit(1)

    def debug(self, msg): self._log(msg, "DEBUG")
    def info(self, msg): self._log(msg, "INFO")
    def warn(self, msg): self._log(msg, "WARN")
    def error(self, msg): self._log(msg, "ERROR")
    def fatal(self, msg): self._log(msg, "FATAL")

log = Logger()
```
## File managment
asd
### Read Files
asd
#### CSV
a
#### txt
b
#### word
c
#### pdf
d
### Write Files
asd
#### CSV
a
