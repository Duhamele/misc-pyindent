from pyindent import IndentWriter

def test_write_level():
    writer = IndentWriter("__output__.txt")

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
