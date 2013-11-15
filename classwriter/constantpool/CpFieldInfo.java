package classwriter.constantpool;

import java.io.*;

public class CpFieldInfo extends CpInfo {

    int classIndex;
    int nametypeIndex;

    public CpFieldInfo(int c, int nt) {
        tag = 9;
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
            CpFieldInfo f = (CpFieldInfo) o;
            if(f.classIndex == this.classIndex &&
                    f.nametypeIndex == this.nametypeIndex) {
                return true;
            }
        }

        return false;
    }

    @Override
    public int hashCode() {
        int hash = 5;
        hash = 13 * hash + this.classIndex;
        hash = 13 * hash + this.nametypeIndex;
        return hash;
    }
}

