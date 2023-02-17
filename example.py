#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import mylib  # noqa (i.e ignore cette erreur)


def foo(bar: str):
    print("foo {}".format(bar))


def ratio_example_for_mypy(numerator: int, denominator: int):
    result = numerator / denominator
    return result


ratio_1 = ratio_example_for_mypy(6, 2)
print(ratio_1)
