/*
 * Generated by classgen, version 1.5
 * 11/18/13 11:57 AM
 */
package javacode.syntaxtree;

public class mjc_If extends mjc_Statement {

  public mjc_Exp e;
  public mjc_Statement s1;
  public mjc_Statement s2;

  public mjc_If (mjc_Exp e, mjc_Statement s1, mjc_Statement s2) {
    this.e = e;
    if (e != null) e.setParent(this);
    this.s1 = s1;
    if (s1 != null) s1.setParent(this);
    this.s2 = s2;
    if (s2 != null) s2.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (e != null) e.accept(visitor);
    if (s1 != null) s1.accept(visitor);
    if (s2 != null) s2.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (e != null) e.traverseTopDown(visitor);
    if (s1 != null) s1.traverseTopDown(visitor);
    if (s2 != null) s2.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (e != null) e.traverseBottomUp(visitor);
    if (s1 != null) s1.traverseBottomUp(visitor);
    if (s2 != null) s2.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_If(\n");
      if (e != null)
        buffer.append(e.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (s1 != null)
        buffer.append(s1.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (s2 != null)
        buffer.append(s2.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_If]");
    return buffer.toString();
  }
}
