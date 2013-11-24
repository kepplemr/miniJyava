class Test
{
    public static void main(String [] args)
    {
        int arr[] = new int[10];
        arr[0] = 7;
        int test = arr[0];
        String strArr[] = new String[10];
        strArr[6] = "hey there";
        String testStr = strArr[6];
    }

    public String test()
    {
        return "testing";
    }

    public int testInt()
    {
        return 7;
    }
}
