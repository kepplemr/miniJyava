package javacode.classwriter;
import javacode.classwriter.constantpool.CpClass;
import javacode.classwriter.constantpool.CpUtf8;
import javacode.classwriter.constantpool.CpInfo;
import java.util.*;
import java.io.*;

public class ClassFile {
    int magicNumber;
    int majorVersion;
    int minorVersion;
    int cpCount;
    ArrayList<CpInfo> constantPool;
    int accessFlags;
    int thisClassIndex;
    int superClassIndex;
    int interfaceCount;
    ArrayList<Object> interfaces;
    int fieldCount;
    ArrayList<FieldInfo> fields;
    int methodCount;
    ArrayList<MethodInfo> methods;
    int attributeCount;
    ArrayList<Object> attributes;

    public ClassFile(int me, int parent, ArrayList<CpInfo> cp, ArrayList<FieldInfo> f, ArrayList<MethodInfo> m) {
	magicNumber = 0xcafebabe;
	majorVersion = 51;    
	minorVersion = 0;
	cpCount = cp.size();  // extra cpInfo at [0] already there, but won't be written
	constantPool = cp;
	accessFlags = 0x0020;
	thisClassIndex = me;
	superClassIndex = parent;
	interfaceCount = 0; // not possible in MiniJava
	interfaces = null;
	fieldCount = f.size();
	fields = f;
	methodCount = m.size();
	methods = m;
	attributeCount = 0;   // you might want the SourceFile attribute?
	attributes = null;
    }
    public void writeFile() 
	throws java.io.IOException, Exception
    {
	String fileName;
	CpClass c = (CpClass)constantPool.get(thisClassIndex);
	CpUtf8 u = (CpUtf8)constantPool.get(c.getNameIndex());
	fileName = u.getValue();
	fileName += ".class";
	System.out.println("Writing to "+fileName);
	DataOutputStream outputFile = new DataOutputStream(new FileOutputStream(fileName));

	outputFile.writeInt(magicNumber);
	outputFile.writeShort(minorVersion);
	outputFile.writeShort(majorVersion);
	outputFile.writeShort(cpCount);
	writeConstantPool(outputFile);
	outputFile.writeShort(accessFlags);
	outputFile.writeShort(thisClassIndex);
	outputFile.writeShort(superClassIndex);
	outputFile.writeShort(interfaceCount);
	// no interfaces expected
	outputFile.writeShort(fieldCount);
	writeFields(outputFile);
	outputFile.writeShort(methodCount);
	writeMethods(outputFile);
	outputFile.writeShort(attributeCount);
	// no attributes expected

	outputFile.close();
    }
    
    public void writeConstantPool(DataOutputStream outputFile) 
	throws java.io.IOException, Exception
    {
	if (constantPool == null) return;

	for (int i=1; i < constantPool.size(); i++) {
	    CpInfo cpInfo = constantPool.get(i);
	    cpInfo.writeFile(outputFile);
	}
    }

    public void writeFields(DataOutputStream outputFile) 
	throws java.io.IOException
    {
	if (fields == null) return;

	for (int i=0; i < fields.size(); i++) {
	    FieldInfo f = fields.get(i);
	    f.writeFile(outputFile);
	}
    }

    public void writeMethods(DataOutputStream outputFile) 
	throws java.io.IOException
    {
	if (methods == null) return;

	for (int i=0; i < methods.size(); i++) {
	    MethodInfo m =  methods.get(i);
	    m.writeFile(outputFile);
	}
    }
}
