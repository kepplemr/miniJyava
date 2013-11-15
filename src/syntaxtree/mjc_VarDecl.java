/*
 * Generated by classgen, version 1.5
 * 11/14/13 12:53 PM
 */
package javacode.syntaxtree;

public class mjc_VarDecl implements SyntaxNode {

  private SyntaxNode parent;
  public mjc_Type t;
  public mjc_Identifier i;

  public mjc_VarDecl (mjc_Type t, mjc_Identifier i) {
    this.t = t;
    if (t != null) t.setParent(this);
    this.i = i;
    if (i != null) i.setParent(this);
  }

  public SyntaxNode getParent() {
    return parent;
  }

  public void setParent(SyntaxNode parent) {
    this.parent = parent;
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (t != null) t.accept(visitor);
    if (i != null) i.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (t != null) t.traverseTopDown(visitor);
    if (i != null) i.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (t != null) t.traverseBottomUp(visitor);
    if (i != null) i.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString() {
    return toString("");
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_VarDecl(\n");
      if (t != null)
        buffer.append(t.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (i != null)
        buffer.append(i.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_VarDecl]");
    return buffer.toString();
  }
}
