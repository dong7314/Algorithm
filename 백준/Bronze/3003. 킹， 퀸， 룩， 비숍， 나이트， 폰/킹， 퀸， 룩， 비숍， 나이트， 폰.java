import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] chess = {1, 1, 2, 2, 2, 8};
		int[] piece = new int[6];
		for(int i = 0; i < 6; i++) {
			piece[i] = sc.nextInt();
		}
		
		for(int i = 0; i < 6; i++) {
			System.out.print(chess[i] - piece[i]);
			System.out.print(' ');
		}

		sc.close();
	}

}
