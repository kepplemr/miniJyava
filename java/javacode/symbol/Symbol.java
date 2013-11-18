package javacode.symbol;

import java.beans.*;

/**
 * Object for maintaining a collection of symbols.
 * <p>
 * Get implementation from 
 * <a href=doc-files/Symbol.java><code>Symbol.java</code></a>.<p>
 *
 * Get class file from 
 * <a href=doc-files/Symbol.class><code>Symbol.class</code></a>.
 */

public class Symbol implements java.io.Serializable {
  private String name;
  private static java.util.Hashtable dict = new java.util.Hashtable();

  private Symbol(String n) {
	name=n;
  }      
  /** 
   * Make return the unique symbol associated with a string.
   * Repeated calls to <tt>symbol("abc")</tt> will return the same Symbol.
   * @param n The name of the symbol.
   * @return The symbol for the name specified.
   */
  public static Symbol symbol(String n) {
	String u = n.intern();
	Symbol s = (Symbol)dict.get(u);
	if (s==null) {
		s = new Symbol(u);
		dict.put(u,s);
	}
	return s;
  }

  /**
   * Gets the name of the symbol.
   * @return The name of this symbol.
   */
  public String toString() {
	return name;
  }      

  
  /** 
   *  For serializable support of static members.
   */
  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
      out.defaultWriteObject();
      out.writeObject(dict);

  }

  /** 
   *  For serializable support of static members.
   */
  private void readObject(java.io.ObjectInputStream in)
                        throws java.lang.ClassNotFoundException,
                               java.io.IOException {
      in.defaultReadObject();
      dict = (java.util.Hashtable)in.readObject();
  }
}
