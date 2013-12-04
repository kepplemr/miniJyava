package javacode.classwriter;

import java.util.ArrayList;

public class CodeGenerator {
    ArrayList<ClassFile> classes;
    public CodeGenerator() {
	classes = new ArrayList<ClassFile>();
    }
    public void addClass(ClassFile c) {
	classes.add(c);
    }
    public void writeFiles() 
	throws java.io.IOException, Exception
    {
	for (int i=0; i < classes.size(); i++) {
	    ClassFile cf = classes.get(i);
	    cf.writeFile();
	}
    }
}
