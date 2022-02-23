from .header import Header, NoneHeader


class AseFile:

    header: Header

    def __init__(self, path: str) -> None:
        try:
            with open(path, 'rb') as file:
                header_bytes: bytes = file.read(Header.size())
                self.header = Header.from_bytes(header_bytes)

        except FileNotFoundError as e:
            print(repr(e))
            self.header = NoneHeader()
