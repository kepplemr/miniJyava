public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        X.callMe(37, 42, 140);
    }
}

class Test2
{
    public Test2() {}

    public int callMe(int i1, int i2, int i3)
    {
        System.out.println(i1);
        System.out.println(i2);
        System.out.println(i3);
        return 42;
    }
}
