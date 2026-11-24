


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
        self.file = open(filename, mode)
        self.indent_char = indent_char
        self.level_indent = level_indent
        self.separators = "\n"
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()

    def __repr__(self) -> str:
        raise NotImplementedError
        return f"{self.__class__.__name__}({self.file}, {self.level_indent})"

    def __str__(self) -> str:
        raise TypeError("String conversion is disabled")

    __eq__ =None
    __hash__ = None
    __ge__ = None
    __ne__ = None
    __gt__ = None
    __lt__ = None
    __le__ = None

    def close(self):
        if not self.closed:
            self.file.close()
            self.closed = True
            self.file = None

    def destroy(self):
        self.close()
        self.file = None


    def indent(self, value: int = 1):
        self.level_indent = max(0, self.level_indent + value)

    def dedent(self, value: int = 1):
        self.level_indent = max(0, self.level_indent - value)

    def set_indent(self, value: int):
        if value < 0:
            raise ValueError("Invalid level indent")
        self.level_indent = value

    def get_indent(self) -> int:
        return self.level_indent

    def write(self, s: str,end: str = "\n"):
        if self.closed:
            raise ValueError("Cannot write to closed file")
        self.file.write(self.indent_char*self.level_indent+s+end)

    def flush(self):
        if not self.closed:
            self.file.flush()

