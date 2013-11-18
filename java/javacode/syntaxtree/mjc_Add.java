/*
 * Generated by classgen, version 1.5
 * 11/18/13 11:57 AM
 */
package javacode.syntaxtree;

public class mjc_Add extends mjc_Exp {

  public mjc_Exp e1;
  public mjc_Exp e2;

  public mjc_Add (mjc_Exp e1, mjc_Exp e2) {
    this.e1 = e1;
    if (e1 != null) e1.setParent(this);
    this.e2 = e2;
    if (e2 != null) e2.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (e1 != null) e1.accept(visitor);
    if (e2 != null) e2.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (e1 != null) e1.traverseTopDown(visitor);
    if (e2 != null) e2.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (e1 != null) e1.traverseBottomUp(visitor);
    if (e2 != null) e2.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_Add(\n");
      if (e1 != null)
        buffer.append(e1.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (e2 != null)
        buffer.append(e2.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_Add]");
    return buffer.toString();
  }
}
