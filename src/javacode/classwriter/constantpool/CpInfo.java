package javacode.classwriter.constantpool;

import java.io.*;

public abstract class CpInfo {

    int tag;

    abstract public void writeFile(DataOutputStream outputFile)
            throws java.io.IOException, Exception;
}
