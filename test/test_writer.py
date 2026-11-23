from pyindent import IndentWriter

with IndentWriter("output.txt","a") as writer:
    writer.write("Root")

    writer.indent()
    writer.write("Child")

    writer.indent()
    writer.write("Grandchild")