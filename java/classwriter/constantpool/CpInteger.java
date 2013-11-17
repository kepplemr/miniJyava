package javacode.classwriter.constantpool;

import java.io.*;

public class CpInteger extends CpInfo {

    private int value;

    public CpInteger(int i) {
        tag = 3;
        value = i;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeInt(getValue());
    }

    /**
     * @return the value
     */
    public int getValue() {
        return value;
    }

    @Override
    public int hashCode() {
        int hash = 5;
        hash = 47 * hash + this.value;
        return hash;
    }


    @Override
    public boolean equals(Object o) {
        if(o.getClass() == this.getClass()) {
            CpInteger i = (CpInteger) o;
            if(i.getValue() == value) {
                return true;
            }
        }

        return false;
    }
}
