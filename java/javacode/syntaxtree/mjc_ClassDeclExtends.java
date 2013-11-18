/*
 * Generated by classgen, version 1.5
 * 11/18/13 11:57 AM
 */
package javacode.syntaxtree;

public class mjc_ClassDeclExtends extends mjc_ClassDecl {

  public mjc_Identifier i;
  public mjc_Identifier j;
  public mjc_VarDeclList vl;
  public mjc_MethodDeclList ml;

  public mjc_ClassDeclExtends (mjc_Identifier i, mjc_Identifier j, mjc_VarDeclList vl, mjc_MethodDeclList ml) {
    this.i = i;
    if (i != null) i.setParent(this);
    this.j = j;
    if (j != null) j.setParent(this);
    this.vl = vl;
    if (vl != null) vl.setParent(this);
    this.ml = ml;
    if (ml != null) ml.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (i != null) i.accept(visitor);
    if (j != null) j.accept(visitor);
    if (vl != null) vl.accept(visitor);
    if (ml != null) ml.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (i != null) i.traverseTopDown(visitor);
    if (j != null) j.traverseTopDown(visitor);
    if (vl != null) vl.traverseTopDown(visitor);
    if (ml != null) ml.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (i != null) i.traverseBottomUp(visitor);
    if (j != null) j.traverseBottomUp(visitor);
    if (vl != null) vl.traverseBottomUp(visitor);
    if (ml != null) ml.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_ClassDeclExtends(\n");
      if (i != null)
        buffer.append(i.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (j != null)
        buffer.append(j.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (vl != null)
        buffer.append(vl.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (ml != null)
        buffer.append(ml.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_ClassDeclExtends]");
    return buffer.toString();
  }
}
