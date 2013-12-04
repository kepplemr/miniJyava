package javacode.symbol;
import javacode.syntaxtree.*;
import java.util.*;

public class ClassEntry extends Entry {
    String name;
    String parent;
    Hashtable<Symbol, FieldEntry> fields;
    Hashtable<Symbol, MethodEntry> methods;

    public String getName() { return name; }
    public String getParent() { return parent; }
    public Hashtable<Symbol, FieldEntry> getFields() { return fields; }
    public Hashtable<Symbol, MethodEntry> getMethods() { return methods; }

    public ClassEntry(String n, String p, Hashtable<Symbol, FieldEntry> f, 
    				  Hashtable<Symbol, MethodEntry> m) {
		name = n;
		parent = p;
		fields = f;
		methods = m;
    }
    public ClassEntry(String n, Hashtable<Symbol, FieldEntry> f, 
			  		  Hashtable<Symbol, MethodEntry> m) {
		name = n;
		parent = null;
		fields = f;
		methods = m;
    }
    
    public ClassEntry(String n, String p, ArrayList<FieldEntry> f, 
			  		  ArrayList<MethodEntry> m) {
		name = n;
		parent = p;
		fields = new Hashtable<Symbol, FieldEntry>();
		for (int i = 0; i < f.size(); i++)
			fields.put(Symbol.symbol(f.get(i).name), f.get(i));
		methods = new Hashtable<Symbol, MethodEntry>();
		for (int i = 0; i < m.size(); i++)
			methods.put(Symbol.symbol(m.get(i).name), m.get(i));
	}
    
    public ClassEntry(String n, ArrayList<FieldEntry> f, 
	  		  		  ArrayList<MethodEntry> m) {
		name = n;
		parent = null;
		fields = new Hashtable<Symbol, FieldEntry>();
		for (int i = 0; i < f.size(); i++)
			fields.put(Symbol.symbol(f.get(i).name), f.get(i));
		methods = new Hashtable<Symbol, MethodEntry>();
		for (int i = 0; i < m.size(); i++)
			methods.put(Symbol.symbol(m.get(i).name), m.get(i));
	}
    
    public FieldEntry getField(String name)
    {
    	return (fields.containsKey(Symbol.symbol(name)))? fields.get(Symbol.symbol(name)) : null;
    }
    
    public MethodEntry getMethod(String name)
    {
    	return (methods.containsKey(Symbol.symbol(name)))? methods.get(Symbol.symbol(name)) : null;
    }
    
    public FieldEntry getField(Symbol name)
    {
    	return (fields.containsKey(name))? fields.get(name) : null;
    }
    
    public MethodEntry getMethod(Symbol name)
    {
    	return (methods.containsKey(name))? methods.get(name) : null;
    }

    public String toString2(){ return "Class entry: " + name + "\n"; }

    public String toString()
    {
        String s = "\nClassEntry: " + name;
        s += (parent != null)? " Extends: " + parent : "";
        s += "\nHas Fields:\n";
        if (fields != null)
        {
        	Set keys = fields.keySet();
        	Iterator it = keys.iterator();
            while(it.hasNext())
                s += "\t\t" + fields.get(it.next()) + "\n";
        }
        s += "\nHas Methods:\n";
        if (methods != null)
        {
        	Set keys = methods.keySet();
        	Iterator it = keys.iterator();
            while(it.hasNext())
                s += "" + methods.get(it.next()) + "\n";
        }
        return s + "\n";
    }
}
