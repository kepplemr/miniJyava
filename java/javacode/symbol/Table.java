package javacode.symbol;

import java.util.ArrayList;
import javacode.syntaxtree.mjc_BooleanType;
import javacode.syntaxtree.mjc_IntegerType;

public class Table 
{
	private static java.util.Hashtable<Symbol, ClassEntry> dict;
	private static Table instance = new Table();

	private Table() 
	{
		dict = new java.util.Hashtable<Symbol, ClassEntry>();
	}
	
	public void clearTable()
	{
		dict = new java.util.Hashtable<Symbol, ClassEntry>();
	}

	public static Table getInstance() 
	{
		return instance;
	}

	public ClassEntry getClass(Symbol classKey) 
	{
		return dict.get(classKey);
	}

	public MethodEntry getMethod(Symbol classKey, Symbol methodName)
	{
		return getClass(classKey).getMethod(methodName);
	}

	public FieldEntry getField(Symbol classKey, Symbol fieldName)
	{
		return getClass(classKey).getField(fieldName);
	}

	public FieldEntry getMethodParam(Symbol classKey, Symbol methodName, Symbol paramName)
	{
		return getClass(classKey).getMethod(methodName).getParam(paramName);
	}

	public FieldEntry getMethodLocal(Symbol classKey, Symbol methodName, Symbol localName)
	{
		return getClass(classKey).getMethod(methodName).getLocal(localName);
	}

	/**
	 * Returns an enumeration of the Table's symbols.
	*/
	public java.util.Enumeration keys() 
	{
		return dict.keys();
	}

	/**
	 * Puts the specified value into the Table, bound to the specified Symbol.
	*/
	public void put(Symbol key, ClassEntry value) 
	{
		dict.put(key, value);
	}

	public String toString() 
	{
		String s = "";
		for (java.util.Enumeration e = keys(); e.hasMoreElements();) 
		{
			s += getClass((Symbol) e.nextElement());
		}
		return s;
	}

	public static void main(String[] args) 
	{
	}
}
