package javacode.classwriter.constantpool;

import java.io.*;

public class CpMethodInfo extends CpInfo {

    int classIndex;
    int nametypeIndex;

    public CpMethodInfo(int c, int nt) {
        tag = 10;
        classIndex = c;
        nametypeIndex = nt;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeShort(classIndex);
        outputFile.writeShort(nametypeIndex);
    }

    @Override
    public boolean equals(Object o) {
        if(o.getClass() == this.getClass()) {
            CpMethodInfo m = (CpMethodInfo) o;
            if(m.classIndex == this.classIndex &&
                    m.nametypeIndex == this.nametypeIndex) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 53 * hash + this.classIndex;
        hash = 53 * hash + this.nametypeIndex;
        return hash;
    }
}
