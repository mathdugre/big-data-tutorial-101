"""Minimal test to demonstrate pytest."""
import pytest

from greeting import greet


def test_greet() -> None:
    assert greet("Alice") == "Hello Alice!"
    assert greet("Bob") == "Hello Bob!"
    if greet() != "Hello World!":
        pytest.fail()
