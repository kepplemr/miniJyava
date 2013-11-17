package javacode.classwriter;
import javacode.classwriter.constantpool.CpClass;
import javacode.classwriter.constantpool.CpString;
import javacode.classwriter.constantpool.CpFieldInfo;
import javacode.classwriter.constantpool.CpInfo;
import javacode.classwriter.constantpool.CpInteger;
import javacode.classwriter.constantpool.CpMethodInfo;
import javacode.classwriter.constantpool.CpNameType;
import javacode.classwriter.constantpool.CpUtf8;
import javacode.classwriter.constantpool.CpNull;
import java.util.ArrayList;


/*
This class automatically keeps track of ConstantPool indexes.

To use: call the get* methods.  These return an index into the
constant pool to an entry that fits the passed in parameters.
*/
public class ConstantPoolIndexer {

    private ArrayList<CpInfo> pool = new ArrayList<CpInfo>();

    public ConstantPoolIndexer() {
        pool.add(new CpNull());
    }

    public void clearConstantPool() {
        pool.clear();
        pool.add(new CpNull());  //0
    }

    public void createBasicConstantPool() {
        getUtf8("java/lang/Object");  
        getClass("java/lang/Object"); // 2
        getUtf8("<init>");
        getUtf8("()V");
        getNameAndType("<init>", "()V");
        getMethodInfo("java/lang/Object", "<init>", "()V");
        getUtf8("Code"); // 7
    }

    public void createPrintLineEntries() {
        createBasicConstantPool();
        getUtf8("java/lang/System");
        getUtf8("out");
        getUtf8("Ljava/io/PrintStream;");
        getNameAndType("out", "Ljava/io/PrintStream;");
        getClass("java/lang/System");
        getFieldInfo("java/lang/System", "out", "Ljava/io/PrintStream;");
        getUtf8("java/io/PrintStream");
        getUtf8("println");
        getUtf8("(I)V");
        getNameAndType("println", "(I)V");
        getClass("java/io/PrintStream");
        getMethodInfo("java/io/PrintStream", "println", "(I)V");  // 19
        getMethodInfo("java/io/PrintStream", "println", "(Z)V");  // 22
        getMethodInfo("java/io/PrintStream", "println", 
		                       "(Ljava/lang/String;)V");  // 25
    }

    public ArrayList<CpInfo> getCPClone() {
        return new ArrayList<CpInfo>(pool);
    }

    public int getUtf8(String s) {
        CpUtf8 temp = new CpUtf8(s);
        return getIndex(temp);
    }

    public int getClass(String s) {
        int utf8_index = getUtf8(s);
        CpClass temp = new CpClass(utf8_index);

        return getIndex(temp);
    }

    public int getString(String s) {
        int utf8_index = getUtf8(s);
        CpString temp = new CpString(utf8_index);

        return getIndex(temp);
    }

    public int getNameAndType(String name, String type) {
        int name_i = getUtf8(name);
        int type_i = getUtf8(type);

        CpNameType temp = new CpNameType(name_i, type_i);

        return getIndex(temp);
    }

    public int getMethodInfo(String class_name, String name, String type) {
        int class_i = getClass(class_name);
        int nt_i = getNameAndType(name, type);

        CpMethodInfo temp = new CpMethodInfo(class_i, nt_i);

        return getIndex(temp);
    }

    public int getFieldInfo(String class_name, String name, String type) {
        int class_i = getClass(class_name);
        int nt_i = getNameAndType(name, type);

        CpFieldInfo temp = new CpFieldInfo(class_i, nt_i);

        return getIndex(temp);
    }

    public int getInteger(int i) {
        CpInteger temp = new CpInteger(i);

        return getIndex(temp);
    }

    private int getIndex(CpInfo c) {
        if (!pool.contains(c)) {
            pool.add(c);
        }

        return pool.indexOf(c);
    }
}
