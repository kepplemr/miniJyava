public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        Test Y = new Test();
        int test = Test2.callMe(Y);
    }
}

class Test2
{
    public Test2() {}

    public static int callMe(Test x)
    {
        return 4;
    }
}
