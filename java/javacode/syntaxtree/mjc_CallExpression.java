/*
 * Generated by classgen, version 1.5
 * 11/18/13 11:57 AM
 */
package javacode.syntaxtree;

public class mjc_CallExpression extends mjc_Exp {

  public mjc_Exp e;
  public mjc_Identifier i;
  public mjc_ExpList el;

  public mjc_CallExpression (mjc_Exp e, mjc_Identifier i, mjc_ExpList el) {
    this.e = e;
    if (e != null) e.setParent(this);
    this.i = i;
    if (i != null) i.setParent(this);
    this.el = el;
    if (el != null) el.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (e != null) e.accept(visitor);
    if (i != null) i.accept(visitor);
    if (el != null) el.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (e != null) e.traverseTopDown(visitor);
    if (i != null) i.traverseTopDown(visitor);
    if (el != null) el.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (e != null) e.traverseBottomUp(visitor);
    if (i != null) i.traverseBottomUp(visitor);
    if (el != null) el.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_CallExpression(\n");
      if (e != null)
        buffer.append(e.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (i != null)
        buffer.append(i.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (el != null)
        buffer.append(el.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_CallExpression]");
    return buffer.toString();
  }
}
