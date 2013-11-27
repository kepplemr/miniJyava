public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        String[] test = Test2.callMe("cba");
    }
}

class Test2
{
    public Test2() {}

    public static String[] callMe(String s1)
    {
        String[] arr = new String[2];
        arr[0] = "abc";
        arr[1] = "def";
        return arr;
    }
}
