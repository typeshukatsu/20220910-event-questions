package main

import "fmt"

func main() {

	// ランダムに並べられた重複のない整数の配列
	array := []int{5, 4, 6, 2, 1, 9, 8, 3, 7, 10}

	// ソート実行
	result := sort(array)

	// 結果出力
	fmt.Println(result)
}
