/*
 * Generated by classgen, version 1.5
 * 11/14/13 12:53 PM
 */
package javacode.syntaxtree;

public class mjc_MethodDeclSimple extends mjc_MethodDecl {

  public mjc_MethodType t;
  public mjc_Identifier i;
  public mjc_FormalList fl;
  public mjc_VarDeclList vl;
  public mjc_StatementList sl;
  public mjc_Exp e;

  public mjc_MethodDeclSimple (mjc_MethodType t, mjc_Identifier i, mjc_FormalList fl, mjc_VarDeclList vl, mjc_StatementList sl, mjc_Exp e) {
    this.t = t;
    if (t != null) t.setParent(this);
    this.i = i;
    if (i != null) i.setParent(this);
    this.fl = fl;
    if (fl != null) fl.setParent(this);
    this.vl = vl;
    if (vl != null) vl.setParent(this);
    this.sl = sl;
    if (sl != null) sl.setParent(this);
    this.e = e;
    if (e != null) e.setParent(this);
  }

  public void accept(Visitor visitor) {
    visitor.visit(this);
  }

  public void childrenAccept(Visitor visitor) {
    if (t != null) t.accept(visitor);
    if (i != null) i.accept(visitor);
    if (fl != null) fl.accept(visitor);
    if (vl != null) vl.accept(visitor);
    if (sl != null) sl.accept(visitor);
    if (e != null) e.accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    accept(visitor);
    if (t != null) t.traverseTopDown(visitor);
    if (i != null) i.traverseTopDown(visitor);
    if (fl != null) fl.traverseTopDown(visitor);
    if (vl != null) vl.traverseTopDown(visitor);
    if (sl != null) sl.traverseTopDown(visitor);
    if (e != null) e.traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    if (t != null) t.traverseBottomUp(visitor);
    if (i != null) i.traverseBottomUp(visitor);
    if (fl != null) fl.traverseBottomUp(visitor);
    if (vl != null) vl.traverseBottomUp(visitor);
    if (sl != null) sl.traverseBottomUp(visitor);
    if (e != null) e.traverseBottomUp(visitor);
    accept(visitor);
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_MethodDeclSimple(\n");
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
      if (fl != null)
        buffer.append(fl.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (vl != null)
        buffer.append(vl.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (sl != null)
        buffer.append(sl.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
      if (e != null)
        buffer.append(e.toString("  "+tab));
      else
        buffer.append(tab+"  null");
    buffer.append("\n");
    buffer.append(tab);
    buffer.append(") [mjc_MethodDeclSimple]");
    return buffer.toString();
  }
}
