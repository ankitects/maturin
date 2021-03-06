#!/usr/bin/env python3

import cffi_pure


def test_range():
    point = cffi_pure.lib.get_origin()
    point.x = 10
    point.y = 10

    assert not cffi_pure.lib.is_in_range(point, 14)
    assert cffi_pure.lib.is_in_range(point, 15)


def test_ffi():
    point = cffi_pure.ffi.new("Point *", (10, 20))
    assert point.x == 10
    assert point.y == 20
