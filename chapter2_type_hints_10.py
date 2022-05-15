from typing import Any, cast

def f(x: Any) -> Any:
    return x

a = f("a") # type(a) is Any
a = cast(str, f("a")) # forced type to be "str"
