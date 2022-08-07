import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // ランダムに並べられた重複のない整数の配列
        int[] array = new int[]{5, 4, 6, 2, 1, 9, 8, 3, 7, 10};
        // ソート実行
        int[] sortedArray = new SortLogic().sort(array);
        // 結果出力
        Arrays.stream(sortedArray).forEach(val ->
            System.out.println(val)
        );
    }
}
