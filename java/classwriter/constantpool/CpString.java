package javacode.classwriter.constantpool;

import java.io.*;

public class CpString extends CpInfo {

    private int utfIndex;

    public CpString(int n) {
        tag = 8;
        utfIndex = n;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeShort(getUtfIndex());
    }

    /**
     * @return the utfIndex
     */
    public int getUtfIndex() {
        return utfIndex;
    }

    @Override
    public boolean equals(Object o) {
        if (o.getClass() == this.getClass()) {
            CpString c = (CpString) o;
            if (c.getUtfIndex() == this.getUtfIndex()) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 13 * hash + this.utfIndex;
        return hash;
    }
}
