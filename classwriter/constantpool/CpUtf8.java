package classwriter.constantpool;

import java.io.*;

public class CpUtf8 extends CpInfo {

    private String value;

    public CpUtf8(String s) {
        tag = 1;
        value = s;
    }

    public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException {
        outputFile.writeByte(tag);
        outputFile.writeUTF(getValue());
    }

    /**
     * @return the value
     */
    public String getValue() {
        return value;
    }

    @Override
    public boolean equals(Object o) {
        if (o.getClass() == this.getClass()) {
            CpUtf8 u = (CpUtf8) o;
            if (u.getValue().equals(this.value)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public int hashCode() {
        int hash = 3;
        hash = 83 * hash + (this.value != null ? this.value.hashCode() : 0);
        return hash;
    }
}
