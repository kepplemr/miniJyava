package symbol;

import java.util.ArrayList;

import syntaxtree.mjc_BooleanType;
import syntaxtree.mjc_IntegerType;

/**
 * The Table class is similar to java.util.Dictionary, except that
 * each key must be a Symbol and there is a scope mechanism. 
 */
public class Table {

	  /**
	   * The dictionary collection for the symbol table.
	   */
	// Singleton pattern
	private static java.util.Hashtable<Symbol, ClassEntry> dict;
	private static Table instance = new Table();
	private Table() {
	dict = new java.util.Hashtable<Symbol, ClassEntry>();
	}      
	public static Table getInstance() {
	return instance;
	}
	// end Singleton pattern
	
	
	 /**
	  * Drilling method to easily get a ClassEntry for a specific class
          * @param classKey	Symbol for the desired class
          * @return		Class Entry, null if class entry does not exist
	  */
	  public ClassEntry getClass(Symbol classKey) {
		return dict.get(key);
	  }      

	  //Begin Drilling stubs //
	  
	  /**
	   * Drilling method to easily get a MethodEntry for a specific class
	   * @param classKey	Symbol for the desired class
	   * @param methodName	Symbol for the desired method
	   * @return			Method Entry, null if method entry does not exist
	   * @throws UnsupportedOperationException (not sure what condition causes this)
	   */
	  public MethodEntry getMethod(Symbol classKey, Symbol methodName) throws UnsupportedOperationException
	  {
		  return null;
	  }
	  
	  /**
	   * Drilling method to easily get a FieldEntry for a specific class
	   * @param classKey	Symbol for the desired class
	   * @param fieldName	Symbol for the desired method
	   * @return			Method Entry, null if method entry does not exist
	   * @throws UnsupportedOperationException (not sure when/why)
	   */
	  public FieldEntry getField(Symbol classKey, Symbol fieldName) throws UnsupportedOperationException
	  {
		  return null;
	  }
	
	  /**
	   * Drilling method to easily get the FieldEntry for a parameter of a class method
	   * @param classKey	Symbol for the desired class
	   * @param methodName	Symbol for the desired method
	   * @param paramName	Symbol for the desired param
	   * @return			Field Entry, null if method entry does not exist
	   * @throws UnsupportedOperationException (not sure when/why)
	   */
	  public FieldEntry getMethodParam(Symbol classKey, Symbol methodName, Symbol paramName) throws UnsupportedOperationException
	  {
		  return null;
	  }
	  
	  /**
	   * Drilling method to easily get a MethodEntry for a specific class
	   * @param classKey	Symbol for the desired class
	   * @param methodName	Symbol for the desired method
	   * @param localName	Symbol for the desired local
	   * @return			Field Entry, null if method entry does not exist
	   * @throws UnsupportedOperationException (not sure when/why)
	   */
	  public FieldEntry getMethodLocal(Symbol classKey, Symbol methodName, Symbol localName) throws UnsupportedOperationException
	  {
		  return null;
	  }
	  
	  // End Drilling Stubs //
	  
	  /**
	   * Returns an enumeration of the Table's symbols.
	   */
	  public java.util.Enumeration keys() {return dict.keys();}      
	
	 /**
	  * Puts the specified value into the Table, bound to the specified Symbol.
	  */
	  public void put(Symbol key, ClassEntry value) {
		  dict.put(key, value);
	  }      

	public String toString()
	{
	    String s = "";
	    
	    for (java.util.Enumeration e = keys(); e.hasMoreElements();)
	    {
	        s += getClass((Symbol)e.nextElement());
	    }
	    return s;
	}

    /* Just for testing/learning purposes */
	public static void main(String[] args)
	{
		Table table = Table.getInstance();

		// Want to add a ClassEntry to the table, but first need some 
		// fields and methods (and methods need params and locals)
		// So the LAST thing we do is make the ClassEntry (after these other things
		// are built up)
		ArrayList<FieldEntry> params = new ArrayList<FieldEntry>();
		FieldEntry fe = new FieldEntry("x", new mjc_IntegerType());
		params.add(fe);
		ArrayList<FieldEntry> locals = new ArrayList<FieldEntry>();
		// using an "anonymous" FieldEntry object for this add!
		locals.add(new FieldEntry("y", new mjc_IntegerType()));
		MethodEntry me = new MethodEntry("method1", new mjc_IntegerType(), params, locals);
		// So, now have a single method with lists of params (only 1) and locals (1)

		ArrayList<FieldEntry> fields = new ArrayList<FieldEntry>();
		ArrayList<MethodEntry> methods = new ArrayList<MethodEntry>();
		fields.add(new FieldEntry("IamAfield", new mjc_BooleanType())); // anonymous FieldEntry
		methods.add(me);
		// So, now have lists of fields (1 entry) and methods (our me object from above!)
		
		ClassEntry ce = new ClassEntry("Class1", fields, methods);
		table.put(Symbol.symbol(ce.name), ce);
		// Ta Da!!

		// And now another one
		params = new ArrayList<FieldEntry>();
		params.add(new FieldEntry("bob", new mjc_IntegerType()));
		params.add(new FieldEntry("fred", new mjc_IntegerType()));
		locals = new ArrayList<FieldEntry>();
		locals.add(new FieldEntry("Wilma", new mjc_BooleanType()));
		methods = new ArrayList<MethodEntry>();
		methods.add(new MethodEntry("BobAndFred",new mjc_IntegerType(),params,locals));
		ce = new ClassEntry("Class2", fields, methods);
		table.put(Symbol.symbol(ce.name), ce);
		
		// Showing some uses of the table and its accessor methods.
		System.out.println(table);
		ce = table.getClass(Symbol.symbol("Class1"));
		fe = ce.getField("IamAfield");
		System.out.println(fe);
		System.out.println(ce.getMethod(Symbol.symbol("method1")));
	}
}
