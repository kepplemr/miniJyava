package javacode.classwriter.constantpool;
import java.io.*;

public class CpClass extends CpInfo {

    private int nameIndex;

    public CpClass(int n) {
        tag = 7;
        nameIndex = n;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeShort(getNameIndex());
    }

    /**
     * @return the nameIndex
     */
    public int getNameIndex() {
        return nameIndex;
    }

    @Override
    public boolean equals(Object o) {
        if (o.getClass() == this.getClass()) {
            CpClass c = (CpClass) o;
            if (c.getNameIndex() == this.getNameIndex()) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 13 * hash + this.nameIndex;
        return hash;
    }
}
