package javacode;
import javacode.syntaxtree.*;

public class ClassVisitor extends VisitorAdaptor 
{
    private int classDeclCount;

    public ClassVisitor() 
    {
        this.classDeclCount = 0;
    }

    public void visit(mjc_ClassDeclSimple c) 
    {
        this.classDeclCount++;
    }

    public void visit(mjc_ClassDeclExtends c) 
    {
        this.classDeclCount++;
    }

    public void visit(mjc_ClassDeclList cl) 
    {
	for (int i=0; i < cl.size(); i++)
	    cl.elementAt(i).accept(this);
    }

    public String toString()
    {
        return "Class Definition Count -> " + classDeclCount;
    }
}
