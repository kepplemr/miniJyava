package javacode.symbol;
import javacode.syntaxtree.*;
import java.util.*;

public class MethodEntry extends Entry {
    String name;
    mjc_MethodType result;
    boolean staticMethod;
    Hashtable<Symbol, FieldEntry> params;	// String name is key and FieldEntry is the value
    Hashtable<Symbol, FieldEntry> locals;	// String name is key and FieldEntry is the value

    public Hashtable<Symbol, FieldEntry> getParams() 
    {
    	return params; 
    }
    public Hashtable<Symbol, FieldEntry> getLocals() { return locals; }
    public String getName() { return name; }
    public mjc_MethodType getResult() { return result; }
    

    public MethodEntry(String n, boolean isStatic, mjc_MethodType r, Hashtable<Symbol, FieldEntry> p, 
    				   Hashtable<Symbol, FieldEntry> l) {
		name = n;
		result = r;
		params = p;
		locals = l;
		staticMethod = isStatic;
    }
    
    public MethodEntry(String n, boolean isStatic, mjc_MethodType r, ArrayList<FieldEntry> p, 
    				   ArrayList<FieldEntry> l) {
		name = n;
		result = r;
		params = new Hashtable<Symbol, FieldEntry>();
		for (int i = 0; i < p.size(); i++)
			params.put(Symbol.symbol(p.get(i).name), p.get(i));
		locals = new Hashtable<Symbol, FieldEntry>();
		for (int i = 0; i < l.size(); i++)
			locals.put(Symbol.symbol(l.get(i).name), l.get(i));
		staticMethod = isStatic;
    }
    
    public FieldEntry getParam(Symbol name)
    {
    	return (params.containsKey(name))? params.get(name) : null;
    }
    
    public FieldEntry getLocal(Symbol name)
    {
    	return (locals.containsKey(name))? locals.get(name) : null;
    }
    
    public FieldEntry getParam(String name)
    {
    	return (params.containsKey(Symbol.symbol(name)))? params.get(Symbol.symbol(name)) : null;
    }
    
    public FieldEntry getLocal(String name)
    {
    	return (locals.containsKey(Symbol.symbol(name)))? locals.get(Symbol.symbol(name)) : null;
    }

    public String toString()
    {
        String s = "";
	if (staticMethod == true) s += "static ";
        s += "\tName: " + name + "\n\t\tType: ";
        s += (result != null)? result : "void";
        s += "\n\t\tParams:\n";
        if (params != null)
        {
        	Set keys = params.keySet();
        	Iterator it = keys.iterator();
            while(it.hasNext())
                s += "\t\t\t" + params.get(it.next()) + "\n";
        }
        s += "\t\tLocals:\n";
        if (locals != null)
        {
        	Set keys = locals.keySet();
        	Iterator it = keys.iterator();
            while(it.hasNext())
                s += "\t\t\t" + locals.get(it.next()) + "\n";
        }
        return s;
    }
}
