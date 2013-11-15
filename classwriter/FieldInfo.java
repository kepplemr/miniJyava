package classwriter;

import java.io.*;

public class FieldInfo {
    int accessFlags;
    int nameIndex;
    int typeIndex;
    int attributeCount;

    public FieldInfo(int a, int n, int t) {
	accessFlags = a;
	nameIndex = n;
	typeIndex = t;
	attributeCount = 0;
    }
    public void writeFile(DataOutputStream outputFile) 
	throws java.io.IOException
    {
	outputFile.writeShort(accessFlags);
	outputFile.writeShort(nameIndex);
	outputFile.writeShort(typeIndex);
	outputFile.writeShort(attributeCount);
    }
}
