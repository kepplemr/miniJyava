/*
 * Generated by classgen, version 1.5
 * 11/14/13 12:53 PM
 */
package javacode.syntaxtree;

public class mjc_Null extends mjc_Exp {


  public mjc_Null () {
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
    buffer.append("mjc_Null(\n");
    buffer.append(tab);
    buffer.append(") [mjc_Null]");
    return buffer.toString();
  }
}
