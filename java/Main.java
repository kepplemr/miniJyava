package javacode;
import java.io.*;
import javacode.syntaxtree.*;
import javacode.symbol.*;
import org.python.core.imp;
import org.python.core.PySystemState;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;
import java.util.Properties;
import org.python.core.Py;
import org.python.core.PyException;
import org.python.core.PyFile;
import org.python.util.JLineConsole;
import org.python.util.InteractiveConsole;
import org.python.util.InteractiveInterpreter;

public class Main 
{
	public static void main(String argv[]) throws java.io.IOException,
			java.lang.Exception 
	{
		Lexer scanner = null;
		try 
		{
			scanner = new Lexer(new java.io.FileReader(argv[0]));
		} 
		catch (java.io.FileNotFoundException e) 
		{
			System.out.println("File not found : \"" + argv[0] + "\"");
			System.exit(1);
		} 
		catch (java.io.IOException e) 
		{
			System.out.println("Error opening file \"" + argv[0] + "\"");
			System.exit(1);
		} 
		catch (ArrayIndexOutOfBoundsException e) 
		{
			System.out.println("Usage : java Main <inputfile>");
			System.exit(1);
		}
		try 
		{
			Parser p = new Parser(scanner, true); // debug printfs: true/false
			p.parse();			
			PythonInterpreter interpreter = new PythonInterpreter();
		    ByteArrayOutputStream out = new ByteArrayOutputStream();
		    interpreter.setOut(out);
		    interpreter.setErr(out);
			interpreter.exec("import sys");
			//interpreter.exec("print(sys.path)");
			interpreter.exec("from jythonLib.CodeGenVisitor import CodeGenVisitor");
			//interpreter.exec("print(sys.modules.keys())");
			PyObject genCode = interpreter.get("CodeGenVisitor");
			PyObject codeGen = genCode.__call__();
			Visitor pyVis = (Visitor) codeGen.__tojava__(Visitor.class);
			p.parsetreeRoot.accept(pyVis);
			System.out.println(out.toString());
			System.out.println("endCat");
		} 
		catch (Exception e) 
		{
		}
	}
}
