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
	throws IllegalArgumentException
	{
		try
		{
			return getClass(classKey).getField(fieldName);
		}
		catch (Exception ex)
		{
			throw new IllegalArgumentException();
		}
	}

	public FieldEntry getMethodParam(Symbol classKey, Symbol methodName, Symbol paramName)
	throws IllegalArgumentException
	{
		try
		{
			return getClass(classKey).getMethod(methodName).getParam(paramName);
		}
		catch (Exception ex)
		{
			throw new IllegalArgumentException();
		}
	}

	public FieldEntry getMethodLocal(Symbol classKey, Symbol methodName, Symbol localName)
	throws IllegalArgumentException
	{
		try
		{
			FieldEntry fe = getClass(classKey).getMethod(methodName).getLocal(localName);
			return fe;
		}
		catch (Exception ex)
		{
			throw new IllegalArgumentException();
		}
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
