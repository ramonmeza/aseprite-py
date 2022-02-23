from ctypes import c_uint8, c_uint16, c_uint32, c_int16, c_int32, c_double
from ctypes import sizeof
from typing import List


BYTE = c_uint8
"""An 8-bit unsigned integer value"""

WORD = c_uint16
"""A 16-bit unsigned integer value"""

SHORT = c_int16
"""A 16-bit signed integer value"""

DWORD = c_uint32
"""A 32-bit unsigned integer value"""

LONG = c_int32
"""A 32-bit signed integer value"""

FIXED = c_double
"""A 32-bit fixed point (16.16) value"""

BYTES_LIST = List[BYTE]
"""List of bytes."""


def to_byte(b: bytes, offset: int = 0) -> BYTE:
    return BYTE(b[offset])


def to_word(b: bytes, offset: int = 0) -> WORD:
    return WORD(
        int.from_bytes(
            b[offset:offset + sizeof(WORD)],
            'little',
            signed=False))


def to_short(b: bytes, offset: int = 0) -> SHORT:
    return SHORT(
        int.from_bytes(
            b[offset:offset + sizeof(SHORT)],
            'little',
            signed=True))


def to_dword(b: bytes, offset: int = 0) -> DWORD:
    return DWORD(
        int.from_bytes(
            b[offset:offset + sizeof(DWORD)],
            'little',
            signed=False))


def to_long(b: bytes, offset: int = 0) -> LONG:
    return LONG(
        int.from_bytes(
            b[offset:offset + sizeof(LONG)],
            'little',
            signed=True))


def to_fixed(b: bytes, offset: int = 0) -> FIXED:
    return FIXED(
        float.fromhex(
            b[offset:offset + sizeof(FIXED)].hex()))


def to_bytes_list(b: bytes, index: int = 0, count: int = 1) -> BYTES_LIST:
    return list([BYTE(i) for i in b[index:index + count]])
