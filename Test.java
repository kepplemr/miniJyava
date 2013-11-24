public class Test
{
    public static void main(String [] args)
    {
        Test2 X = new Test2();
        X.callMe();
    }
}

class Test2
{
    public Test2() {}

    public void callMe()
    {
        System.out.println("Hey");
    }
}
