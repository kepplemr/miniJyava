public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        int[] test = Test2.callMe("cba");
    }
}

class Test2
{
    public Test2() {}

    public static int[] callMe(String s1)
    {
        int[] arr = new int[2];
        arr[0] = 13;
        arr[1] = 34;
        return arr;
    }
}
