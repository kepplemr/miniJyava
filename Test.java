public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        X.callMe(37);
    }
}

class Test2
{
    public Test2() {}

    public int callMe(int i1)
    {
        System.out.println(i1);
        return 42;
    }
}
