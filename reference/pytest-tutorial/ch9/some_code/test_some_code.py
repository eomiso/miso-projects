import bar_module
import foo_module


def test_foo():
    assert foo_module.foo() == "foo"


def test_bar():
    assert bar_module.bar() == "bar"
