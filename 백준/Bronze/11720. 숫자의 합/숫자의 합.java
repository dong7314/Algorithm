import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String s = sc.next();
        String[] arr = s.split("");

        int num = 0;
        for (int i = 0; i < arr.length; i++) {
            num += Integer.parseInt(arr[i]);
        }

        System.out.println(num);
    }
}