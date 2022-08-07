public class Sort{
    public static void Main(){
        // ランダムに並べられた重複のない整数の配列
        var array = new int[] { 5, 4, 6, 2, 1, 9, 8, 3, 7, 10 };
        // ソート実行
        var sortedArray = new SortLogic().SortArray(array);
        // 結果出力
        foreach (int i in sortedArray)
        {
            System.Console.WriteLine(i);
        }
    }
}
