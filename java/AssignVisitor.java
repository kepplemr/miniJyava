package javacode;
import javacode.syntaxtree.*;

public class AssignVisitor extends VisitorAdaptor 
{
    private int assignCount;

    public AssignVisitor() 
    {
        this.assignCount = 0;
    }

    @Override
    public void visit(mjc_Assign c) 
    {
        assignCount++;
    }

    @Override
    public void visit(mjc_ArrayAssign a)
    {
        assignCount++;
    }

    @Override
    public void visit(mjc_MethodDeclSimple m)
    {
        for (int i = 0; i < m.sl.size(); i++)
            m.sl.elementAt(i).accept(this);
    }

    @Override
    public void visit(mjc_MethodDeclStatic m)
    {
        for (int i = 0; i < m.sl.size(); i++)
            m.sl.elementAt(i).accept(this);
    }

    @Override
    public void visit(mjc_ClassDeclSimple c)
    {
        for (int i = 0; i < c.ml.size(); i++)
            c.ml.elementAt(i).accept(this);
    }

    @Override
    public void visit(mjc_ClassDeclExtends c)
    {
        for (int i = 0; i < c.ml.size(); i++)
            c.ml.elementAt(i).accept(this);
    }

    @Override
    public void visit(mjc_ClassDeclList cl)
    {
        for (int i = 0; i< cl.size(); i++)
            cl.elementAt(i).accept(this);
    }

    public String toString()
    {
        return "Assign Count -> " + assignCount;
    }
}

