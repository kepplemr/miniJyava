/*
 * Generated by classgen, version 1.5
 * 11/14/13 12:53 PM
 */
package javacode.syntaxtree;

public class mjc_StringType extends mjc_Type {


  public mjc_StringType () {
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_StringType(\n");
    buffer.append(tab);
    buffer.append(") [mjc_StringType]");
    return buffer.toString();
  }
}
