package javacode;
import java.io.*;
import syntaxtree.*;
public class Main 
{
 /**
   * Runs the parser on an input file.
   *
   *
   * @param argv   the command line, argv[0] is the filename to run
   *               the parser on.
   */
  public static void main(String argv[]) 
    throws java.io.IOException, java.lang.Exception
 {
    Lexer scanner = null;
    try {
      scanner = new Lexer( new java.io.FileReader(argv[0]) );
    }
    catch (java.io.FileNotFoundException e) {
      System.out.println("File not found : \""+argv[0]+"\"");
      System.exit(1);
    }
    catch (java.io.IOException e) {
      System.out.println("Error opening file \""+argv[0]+"\"");
      System.exit(1);
    }
    catch (ArrayIndexOutOfBoundsException e) {
      System.out.println("Usage : java Main <inputfile>");
      System.exit(1);
    }

    try {
	Parser p = new Parser(scanner, true); // debug printfs: true/false
      p.parse();
      mjc_ClassDeclList cdl = p.parsetreeRoot;
      System.out.println(cdl);
      AssignVisitor av = new AssignVisitor();
      p.parsetreeRoot.accept(av);
      System.out.println(av);
      ClassVisitor cv = new ClassVisitor();
      p.parsetreeRoot.accept(cv);
      System.out.println(cv);
    }
    catch (Exception e) {
    }
  }
}




