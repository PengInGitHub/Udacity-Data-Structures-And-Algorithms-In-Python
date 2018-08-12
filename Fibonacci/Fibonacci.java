public class Fibonacci{

    public static long get_fib(int n){
        if (n <= 1) return n;
        else return get_fib(n-1) + get_fib(n-2);
    }

    public static void main(String[] args){
        int n = 10; 
        for (int i = 0; i <= n; i++)
        System.out.println(i + ": " + get_fib(i));
    }
}
