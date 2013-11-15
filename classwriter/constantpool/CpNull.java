package classwriter.constantpool;

import java.io.*;

/* A placeholder class for the non-existant zeroth index of the
   Constant Pool.  This should only be used as a placeholder for
   ConstantPool ArrayList's zero index. */
public class CpNull extends CpInfo {

    public void writeFile(DataOutputStream outFile) throws Exception {
	throw new Exception("This should never be called.");
    }
}
