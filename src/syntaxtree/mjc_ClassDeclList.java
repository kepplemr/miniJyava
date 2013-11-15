/*
 * Generated by classgen, version 1.5
 * 11/14/13 12:53 PM
 */
package javacode.syntaxtree;

import java.util.Vector;
import java.util.Enumeration;

public class mjc_ClassDeclList implements SyntaxNode {

  private Vector items;
  private SyntaxNode parent;

  public mjc_ClassDeclList() {
    items = new Vector();
  }

  public mjc_ClassDeclList(mjc_ClassDecl anItem) {
    this();
    append(anItem);
  }

  public mjc_ClassDeclList append(mjc_ClassDecl anItem) {
    if (anItem == null) return this;
    anItem.setParent(this);
    items.addElement(anItem);
    return this;
  }

  public Enumeration elements() {
    return items.elements();
  }

  public mjc_ClassDecl elementAt(int index) {
    return (mjc_ClassDecl) items.elementAt(index);
  }

  public void setElementAt(mjc_ClassDecl item, int index) {
    item.setParent(this);
    items.setElementAt(item, index);
  }

  public void insertElementAt(mjc_ClassDecl item, int index) {
    item.setParent(this);
    items.insertElementAt(item, index);
  }

  public void removeElementAt(int index) {
    items.removeElementAt(index);
  }

  public int size() { return items.size(); }

  public boolean isEmpty() { return items.isEmpty(); }

  public boolean contains(mjc_ClassDecl item) {
    int size = items.size();
    for (int i = 0; i < size; i++)
      if ( item.equals(items.elementAt(i)) ) return true;
    return false;
  }

  public int indexOf(mjc_ClassDecl item) {
    return items.indexOf(item);
  }

  public String toString() {
    return toString("");
  }

  public String toString(String tab) {
    StringBuffer buffer = new StringBuffer();
    buffer.append(tab);
    buffer.append("mjc_ClassDeclList (\n");
    int size = items.size();
    for (int i = 0; i < size; i++) {
      buffer.append(((mjc_ClassDecl) items.elementAt(i)).toString("  "+tab));
      buffer.append("\n");
    }
    buffer.append(tab);
    buffer.append(") [mjc_ClassDeclList]");
    return buffer.toString();
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
    for (int i = 0; i < size(); i++)
      if (elementAt(i) != null) elementAt(i).accept(visitor);
  }

  public void traverseTopDown(Visitor visitor) {
    this.accept(visitor);
    for (int i = 0; i < size(); i++)
      if (elementAt(i) != null) elementAt(i).traverseTopDown(visitor);
  }

  public void traverseBottomUp(Visitor visitor) {
    for (int i = 0; i < size(); i++)
      if (elementAt(i) != null) elementAt(i).traverseBottomUp(visitor);
    this.accept(visitor);
  }

}
