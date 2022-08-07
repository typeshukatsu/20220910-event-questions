package main

import "fmt"

func main() {

	// ランダムに並べられた重複のない最大5桁の整数の配列
	array := []int{5, 4, 6, 2, 1, 100, 12000, 11111, 2222, 2213, 333, 44, 43, 9, 8, 3, 7, 10}

	// 桁数の最大値
	const MAX_DIGITS = 5

	// ソート実行
	result := sort(array, MAX_DIGITS)

	// 結果出力
	fmt.Println(result)
}
