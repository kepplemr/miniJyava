package javacode.symbol;

import javacode.syntaxtree.*;

public class FieldEntry extends Entry {
    String name;
    mjc_Type type;
    int location;

    public String getName() { return name; }
    public mjc_Type getType() { return type; }

    public FieldEntry(String n, mjc_Type t) { 
	name = n;
	type = t;
    }
    
    public void setLocation(int location)
    {
    	this.location = location;
    }
    
    public int getLocation()
    {
    	return this.location;
    }

    public String toString()
    {
        return type + " " + name;
    }
}
