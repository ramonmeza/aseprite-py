from dataclasses import dataclass
from typing import List, Optional

from .types import BYTE, BYTES_LIST, DWORD, SHORT, WORD
from .types import to_byte, to_bytes_list, to_dword, to_short, to_word


@dataclass
class Header:
    """
    A 128-byte header (same as FLC/FLI header, but with other magic number)
    """

    file_size: DWORD
    """File size"""

    magic_number: WORD
    """Magic number (0xA5E0)"""

    frames: WORD
    """Frames"""

    width: WORD
    """Width in pixels"""

    height: WORD
    """Height in pixels"""

    color_depth: WORD
    """
    Color depth (bits per pixel)
        - 32 bpp = RGBA
        - 16 bpp = Grayscale
        - 8 bpp = Indexed
    """

    flags: DWORD
    """
    Flags:
        - 1 = Layer opacity has valid value
    """

    speed: WORD
    """
    Speed (milliseconds between frame, like in FLC files).

    DEPRECATED: You should use the frame duration field from each frame header
    """

    zero1: DWORD
    """Set be 0"""

    zero2: DWORD
    """Set be 0"""

    pallette_entry: BYTE
    """
    Palette entry (index) which represent transparent color in all
    non-background layers (only for Indexed sprites).
    """

    ignore: Optional[BYTES_LIST]
    """Ignore these bytes (3 bytes)"""

    num_of_colors: WORD
    """Number of colors (0 means 256 for old sprites)"""

    pixel_width: BYTE
    """
    Pixel width (pixel ratio is "pixel width/pixel height"). If this or pixel
    height field is zero, pixel ratio is 1:1
    """

    pixel_height: BYTE
    """Pixel height"""

    x: SHORT
    """X position of the grid"""

    y: SHORT
    """Y position of the grid"""

    grid_width: WORD
    """
    Grid width (zero if there is no grid, grid size is 16x16 on Aseprite by
    default)
    """

    grid_length: WORD
    """Grid height (zero if there is no grid)"""

    future: Optional[BYTES_LIST]
    """For future (set to zero) (84 bytes)"""

    @staticmethod
    def size() -> int:
        """The header has 128 bytes"""
        return 128

    @staticmethod
    def from_bytes(b: bytes) -> 'Header':
        if len(b) < Header.size():
            raise IndexError(
                'Not enough bytes for header.\n' +
                f'EXPECTED AT LEAST {Header.size()} bytes\n' +
                f'GIVEN {len(b)} bytes')

        # parse elements
        return Header(
            to_dword(b, 0),
            to_word(b, 4),
            to_word(b, 6),
            to_word(b, 8),
            to_word(b, 10),
            to_word(b, 12),
            to_dword(b, 14),
            to_word(b, 18),
            to_dword(b, 20),
            to_dword(b, 24),
            to_byte(b, 28),
            to_bytes_list(b, 29, 3),
            to_word(b, 33),
            to_byte(b, 35),
            to_byte(b, 36),
            to_short(b, 37),
            to_short(b, 39),
            to_word(b, 41),
            to_word(b, 43),
            to_bytes_list(b, 44, 84))


@dataclass
class NoneHeader(Header):

    file_size: DWORD = DWORD(0)
    magic_number: WORD = WORD(0)
    frames: WORD = WORD(0)
    width: WORD = WORD(0)
    height: WORD = WORD(0)
    color_depth: WORD = WORD(0)
    flags: DWORD = DWORD(0)
    speed: WORD = WORD(0)
    zero1: DWORD = DWORD(0)
    zero2: DWORD = DWORD(0)
    pallette_entry: BYTE = BYTE(0)
    ignore: Optional[BYTES_LIST] = None
    num_of_colors: WORD = WORD(0)
    pixel_width: BYTE = BYTE(0)
    pixel_height: BYTE = BYTE(0)
    x: SHORT = SHORT(0)
    y: SHORT = SHORT(0)
    grid_width: WORD = WORD(0)
    grid_length: WORD = WORD(0)
    future: Optional[BYTES_LIST] = None

    def __init__(self) -> None:
        self.ignore = to_bytes_list(bytes(3))
        self.future = to_bytes_list(bytes(84))
