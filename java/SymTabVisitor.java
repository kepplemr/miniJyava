package javacode;
import javacode.syntaxtree.*;
import javacode.symbol.*;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Set;

/**
 * SymTabVisitor - visitor implementation that constructs a symbol table of 
 *     parsed MiniJyava code.
 * 
 * @author  michael
 * @version 1.1
 * @since   12 Nov 2013
 */
public class SymTabVisitor extends VisitorAdaptor
{
    private Table table = Table.getInstance();
    private ArrayList<ClassEntry> classes;
    private ArrayList<FieldEntry> fields;
    private ArrayList<MethodEntry> methods;

    public SymTabVisitor()
    {
        this.classes = new ArrayList<ClassEntry>();
    }

    // ClassDeclList handler
    @Override
    public void visit(mjc_ClassDeclList cl)
    {
        for (int i = 0; i < cl.size(); i++)
            cl.elementAt(i).accept(this);
        for (int i = 0; i < classes.size(); i++)
        {
            table.put(Symbol.symbol(classes.get(i).getName()), classes.get(i));
        }
    }

    // ClassDeclSimple handler
    @Override
    public void visit(mjc_ClassDeclSimple c)
    {
        // Clear out global ArrayList's
        fields = new ArrayList<FieldEntry>();
        methods = new ArrayList<MethodEntry>();
        // Handle class fields
        for (int i = 0; i < c.vl.size(); i++)
            c.vl.elementAt(i).accept(this);
        ArrayList<FieldEntry> classFields = new ArrayList<FieldEntry>(fields);
        // Handle class methods
        for (int i = 0; i < c.ml.size(); i++)
        {
            mjc_MethodDecl md = (mjc_MethodDecl) c.ml.elementAt(i);
            md.accept(this);
        }
        ClassEntry ce = new ClassEntry(c.i.s, "", classFields, methods);
        classes.add(ce);
    }

    // ClassDeclExtends handler
    @Override
    public void visit(mjc_ClassDeclExtends c)
    {
        // Clear out global ArrayList's
        fields = new ArrayList<FieldEntry>();
        methods = new ArrayList<MethodEntry>();
        // Handle class fields
        for (int i = 0; i < c.vl.size(); i++)
            c.vl.elementAt(i).accept(this);
        ArrayList<FieldEntry> classFields = new ArrayList<FieldEntry>(fields);
        // Handle class methods
        for (int i = 0; i < c.ml.size(); i++)
        {
            mjc_MethodDecl md = (mjc_MethodDecl) c.ml.elementAt(i);
            md.accept(this);
        }
        ClassEntry ce = new ClassEntry(c.i.s, c.j.s, classFields, methods);
        classes.add(ce);
    }


    // MethodDeclSimple handler
    @Override
    public void visit(mjc_MethodDeclSimple md)
    {
        fields = new ArrayList<FieldEntry>();
        int location = 1;
        // Handle parameters
        for (int i = 0; i < md.fl.size(); i++)
        {
            md.fl.elementAt(i).accept(this);
            // Local zero gets object reference
        	fields.get(i).setLocation(i+1);
        }
        ArrayList<FieldEntry> params = new ArrayList<FieldEntry>(fields);
        fields = new ArrayList<FieldEntry>();
        // Handle locals
        for (int i = 0; i < md.vl.size(); i++)
        {
            md.vl.elementAt(i).accept(this);
            fields.get(i).setLocation(location + i);
        }
        ArrayList<FieldEntry> locals = new ArrayList<FieldEntry>(fields);
        MethodEntry me = new MethodEntry(md.i.toString(), false, md.t, params, locals);
        methods.add(me);
    }

    // MethodDeclStatic heandler
    @Override
    public void visit(mjc_MethodDeclStatic md)
    {
        fields = new ArrayList<FieldEntry>();
        int location = 1;
        // Handle parameters
        for (int i = 0; i < md.fl.size(); i++)
        {
            md.fl.elementAt(i).accept(this);
            fields.get(i).setLocation(i+1);
            location++;
        }
        ArrayList<FieldEntry> params = new ArrayList<FieldEntry>(fields);
        fields = new ArrayList<FieldEntry>();
        // Handle locals
        for (int i = 0; i < md.vl.size(); i++)
        {
            md.vl.elementAt(i).accept(this);
            fields.get(i).setLocation(location + i);
        }
        ArrayList<FieldEntry> locals = new ArrayList<FieldEntry>(fields);
        MethodEntry me = new MethodEntry(md.i.toString(), false, md.t, params, locals);
        methods.add(me);
    }

    // Formal handler
    @Override
    public void visit(mjc_Formal f)
    {
        FieldEntry fe = new FieldEntry(f.i.toString(), f.t);
        fields.add(fe);
    }

    // VarDecl handler
    @Override
    public void visit(mjc_VarDecl vd)
    {
        FieldEntry fe = new FieldEntry(vd.i.toString(), vd.t);
        fields.add(fe);
    }

    @Override
    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        for (ClassEntry ce : classes)
        {
            sb.append("\nCLASS -> " + ce.getName() + " extends -> " + ce.getParent());
            Enumeration en = ce.getFields().elements();
            while (en.hasMoreElements())
            {
                FieldEntry fe = (FieldEntry) en.nextElement();
                sb.append("\n\tCLASS FIELD -> " + fe.toString());
            }
            en = ce.getMethods().elements();
            while (en.hasMoreElements())
            {
                MethodEntry me = (MethodEntry) en.nextElement();
                sb.append("\n\tMETHOD -> " + me.getName());
                Enumeration methodEn = me.getParams().elements();
                while (methodEn.hasMoreElements())
                {
                    FieldEntry fn = (FieldEntry) methodEn.nextElement();
                    sb.append("\n\t\tMETHOD PARAM -> " + fn.toString());
                }
                methodEn = me.getLocals().elements();
                while (methodEn.hasMoreElements())
                {
                    FieldEntry fn = (FieldEntry) methodEn.nextElement();
                    sb.append("\n\t\tMETHOD LOCAL -> " + fn.toString());
                }
            }
        }
        return sb.toString();

    }
}
