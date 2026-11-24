


class IndentWriter:
    def __init__(self, filename, mode: str = "a", indent_char: str = "\t", level_indent: int = 0):

        match mode:
            case "a" | "w" | "x":
                pass
            case _:
                raise ValueError("Invalid mode")
        if level_indent < 0:
            raise ValueError("Invalid level indent")
        if indent_char == "":
            raise ValueError("Invalid indent_char")
        self._file = open(filename, mode)
        self._indent_char = indent_char
        self._level_indent = level_indent
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()

    def __repr__(self) -> str:
        raise NotImplementedError
        return f"{self.__class__.__name__}({self._file}, {self._level_indent})"

    __str__=None
    __eq__ =None
    __hash__ = None
    __ge__ = None
    __ne__ = None
    __gt__ = None
    __lt__ = None
    __le__ = None

    def close(self):
        if not self._closed:
            self._file.close()
            self._closed = True
            self._file = None

    def destroy(self):
        self.close()
        self._file = None


    def indent(self, value: int = 1):
        self._level_indent = max(0, self._level_indent + value)

    def dedent(self, value: int = 1):
        self._level_indent = max(0, self._level_indent - value)

    def set_indent(self, value: int):
        if value < 0:
            raise ValueError("Invalid level indent")
        self._level_indent = value

    def get_indent(self) -> int:
        return self._level_indent

    def write(self, s: str):
        if self._closed:
            raise ValueError("Cannot write to closed file")
        self._file.write(f"{self._indent_char*self._level_indent}{s}\n")

    def flush(self):
        if not self._closed:
            self._file.flush()