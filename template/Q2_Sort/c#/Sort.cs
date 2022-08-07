public class Sort{
    public static void Main(){
        // ランダムに並べられた重複のない整数の配列
        var array = new int[] { 5, 4, 6, 2, 1, 100, 12000, 11111, 2222, 2213, 333, 44, 43, 9, 8, 3, 7, 10 };
        // 桁数の最大値
        var MAX_DIGITS = 5;
        // ソート実行
        var sortedArray = new SortLogic().SortArray(array, MAX_DIGITS);
        // 結果出力
        foreach (int i in sortedArray)
        {
            System.Console.WriteLine(i);
        }
    }
}
