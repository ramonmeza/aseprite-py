import os

from src.aseprite_py.ase_file import AseFile
from src.aseprite_py.header import Header, NoneHeader


TEST_FILE: str = 'tests/data/test.aseprite'


@given('the Aseprite object is loaded')  # type: ignore # noqa: F821
def step_impl(context) -> None:  # noqa: F811
    context.aseprite = AseFile(TEST_FILE)


@when('we access the header attributes')  # type: ignore # noqa: F821
def step_impl(context) -> None:  # noqa: F811
    assert context.aseprite.header is not None

    # if the header has all the attributes in the Header class,
    # we know we can accessed all of them
    for attr in Header.__annotations__.keys():
        assert hasattr(context.aseprite.header, attr)


@then('the header attributes are loaded')  # type: ignore # noqa: F821
def step_impl(context) -> None:  # noqa: F811
    header = context.aseprite.header

    # ensure TEST_FILE is loaded
    assert header is not NoneHeader

    # confirm values match what we expect
    expected_file_size = os.stat(TEST_FILE).st_size
    assert header.file_size.value == expected_file_size
    assert header.magic_number.value == 0xA5E0
