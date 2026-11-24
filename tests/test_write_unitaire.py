import pytest

from pyindent import IndentWriter

def test_write_level_indent():
    writer = IndentWriter(".generated/__output__.txt")

    assert writer.get_indent()==0
    writer.dedent()
    assert writer.get_indent()==0
    writer.indent()
    assert writer.get_indent()==1
    writer.dedent()
    assert writer.get_indent()==0
    writer.indent(4)
    assert writer.get_indent()==4
    writer.dedent(3)
    assert writer.get_indent()==1
    writer.dedent()
    assert writer.get_indent()==0
    writer.indent(-4)
    assert writer.get_indent()==0
    writer.dedent(-3)
    assert writer.get_indent()==3

def test_write_level_indent_2():
    writer = IndentWriter(".generated/__output2__.txt")
    assert writer.get_indent()==0
    writer.set_indent(4)
    assert writer.get_indent()==4
    writer.dedent()
    assert writer.get_indent()==3
    with pytest.raises(ValueError):
        writer.set_indent(-4)
    with pytest.raises(ValueError):
        writer.set_indent(-1)
def test_indentwriter_mode_fake():
    for mode_fake in ["fe","e","o","b","bt","hjg"]:
        with pytest.raises(ValueError):
            IndentWriter(".generated/__output_error__.txt",mode_fake)
