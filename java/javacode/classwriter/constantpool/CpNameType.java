package javacode.classwriter.constantpool;

import java.io.*;

public class CpNameType extends CpInfo {

    int nameIndex;
    int typeIndex;

    public CpNameType(int n, int t) {
        tag = 12;
        nameIndex = n;
        typeIndex = t;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeShort(nameIndex);
        outputFile.writeShort(typeIndex);
    }

    @Override
    public boolean equals(Object o) {
        if (o.getClass() == this.getClass()) {
            CpNameType n = (CpNameType) o;
            if (n.typeIndex == this.typeIndex &&
                    n.nameIndex == this.nameIndex) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 29 * hash + this.nameIndex;
        hash = 29 * hash + this.typeIndex;
        return hash;
    }
}
