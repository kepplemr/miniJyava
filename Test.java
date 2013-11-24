public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        X.callMe("a", "b", 1, 2);
    }
}

class Test2
{
    public Test2() {}

    public int callMe(String s1, String s2, int i1, int i2)
    {
        return 42;
    }
}
