/*
 * Generated by classgen, version 1.5
 * 11/18/13 11:57 AM
 */
package javacode.syntaxtree;

public class mjc_MethodVoidType extends mjc_MethodType {


  public mjc_MethodVoidType () {
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
    buffer.append("mjc_MethodVoidType(\n");
    buffer.append(tab);
    buffer.append(") [mjc_MethodVoidType]");
    return buffer.toString();
  }
}
