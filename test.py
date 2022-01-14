# Here we will set up our tests.

import lab1
import pytest


class TestAdd:
    def test_1(self):
        assert lab1.add(5,6) == 11

    def test_2(self):
        assert lab1.add(7,8) == 15

    def test_3(self):
        assert lab1.add('a',7) == ValueError, "Remember to consider non-numeric inputs!"

class TestSubtract:
    def test_1(self):
        assert lab1.sub(5,6) == -1

    def test_2(self):
        assert lab1.sub(12,8) == 4

    def test_3(self):
        assert lab1.sub('a',7) == ValueError, "Remember to consider non-numeric inputs!"