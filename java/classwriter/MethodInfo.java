package javacode.classwriter;
import java.util.*;
import java.io.*;

public class MethodInfo {
    int accessFlags;
    int nameIndex;
    int typeIndex;
    int attributeCount;
    // inside Code (the only one MiniJava worried about) attribute
    int attributeNameIndex;
    int attributeLength;
    int maxStack;
    int maxLocals;
    int codeLength;
    ArrayList<Integer> code;
    int exceptionLength;
    int nestedAttributeLength;

    public MethodInfo(int a, int n, int t, int an, int al, int ms, int ml, ArrayList<Integer> c) {
	accessFlags = a;
	nameIndex = n;
	typeIndex = t;
	attributeCount = 1;
	attributeNameIndex = an;
	attributeLength = al;
	maxStack = ms;
	maxLocals = ml;
	codeLength = c.size();
	code = c;
	exceptionLength = 0;
	nestedAttributeLength = 0;
    }
    public void writeFile(DataOutputStream outputFile) 
	throws java.io.IOException
    {
	outputFile.writeShort(accessFlags);
	outputFile.writeShort(nameIndex);
	outputFile.writeShort(typeIndex);
	outputFile.writeShort(attributeCount);

	outputFile.writeShort(attributeNameIndex);
	outputFile.writeInt(attributeLength);
	outputFile.writeShort(maxStack);
	outputFile.writeShort(maxLocals);
	outputFile.writeInt(codeLength);

	for (int i=0; i < code.size(); i++) {
	    int bytecode = code.get(i).intValue();
	    outputFile.writeByte(bytecode);
	}

	outputFile.writeShort(exceptionLength);
	outputFile.writeShort(nestedAttributeLength);
	
    }
}
