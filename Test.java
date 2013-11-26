public class Test
{
    public static void main(String [] args)
    {
        int i1;
        int i2;
        String s1;
        String s2;
        i1 = 7;
        s1 = "abc";

        i2 = i1;
        s2 = s1;

        System.out.println(i2);
        System.out.println(s2);
    }
}

class Test2
{
    public Test2() {}

    public int callMe(String s1)
    {
        System.out.println(s1);
        return 42;
    }
}
