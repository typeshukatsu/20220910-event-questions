import logic

def main():
    # ランダムに並べられた重複のない最大5桁の整数の配列
    array = [5, 4, 6, 2, 1, 100, 12000, 11111, 2222, 2213, 333, 44, 43, 9, 8, 3, 7, 10]
    # 桁数の最大値
    MAX_DIGITS = 5
    # ソート実行
    sorted_array = logic.Logic().sort(array, MAX_DIGITS)
    # 結果出力
    [print(i) for i in sorted_array]

if __name__ == '__main__':
    main()
