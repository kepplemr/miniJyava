package javacode.symbol;

import javacode.syntaxtree.*;

public class FieldEntry extends Entry {
    String name;
    mjc_Type type;
    int location;

    public FieldEntry(String n, mjc_Type t) { 
	name = n;
	type = t;
    }
    
    public void setLocation(int location)
    {
    	this.location = location;
    }

    public String toString()
    {
        return type + " " + name;
    }
}
