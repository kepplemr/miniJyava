/*
 * Generated by classgen, version 1.5
 * 11/19/13 9:29 PM
 */
package javacode.syntaxtree;

public class mjc_This extends mjc_Exp {

  public mjc_Identifier i;

  public mjc_This (mjc_Identifier i) {
    this.i = i;
    if (i != null) i.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (i != null) i.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (i != null) i.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (i != null) i.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_This(\n");
      if (i != null)
        buffer.append(i.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_This]");
    return buffer.toString();
  }
}
