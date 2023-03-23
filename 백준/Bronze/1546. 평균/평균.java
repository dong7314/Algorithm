import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        double maxScore = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] > maxScore) {
                maxScore = arr[i];
            }
        }

        double sumScore = 0;
        for (int i = 0; i < N; i++) {
            double newScore = (arr[i] / maxScore) * 100;
            sumScore += newScore;
        }

        System.out.println(sumScore / N);

    }
}