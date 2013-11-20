/*
 * Generated by classgen, version 1.5
 * 11/19/13 9:29 PM
 */
package javacode.syntaxtree;

public class mjc_MethodReturnType extends mjc_MethodType {

  public mjc_Type t;

  public mjc_MethodReturnType (mjc_Type t) {
    this.t = t;
    if (t != null) t.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (t != null) t.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (t != null) t.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (t != null) t.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_MethodReturnType(\n");
      if (t != null)
        buffer.append(t.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_MethodReturnType]");
    return buffer.toString();
  }
}
