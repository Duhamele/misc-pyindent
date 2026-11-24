import filecmp

import pytest

from pyindent import IndentWriter

def test_write():
    with IndentWriter(".generated/__test__.txt",level_indent=1,mode='w') as writer:
        writer.write("test")
        writer.indent()
        writer.write("test")
        writer.dedent()
        writer.write("Test")
        writer.set_indent(4)
        writer.write("Test")
    assert filecmp.cmp(".generated/__test__.txt","tests/data/test.txt",shallow=False)
def test_write_close():
    write=IndentWriter(".generated/__empty__.txt",level_indent=1,mode='w')
    write.close()
    with pytest.raises(ValueError):
        write.write("test")
    write.destroy()
    with pytest.raises(ValueError):
        write.write("test")
