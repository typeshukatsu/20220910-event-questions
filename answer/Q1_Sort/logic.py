class Logic:
    def sort(self, array):
        # 要素が1つの場合は並び替える必要がないため返却
        if len(array) <= 1:
            return array

        # 中央で分割
        mid_index = len(array) // 2
        left = array[:mid_index]
        right = array[mid_index:]

        # 再帰的に並び替えを繰り返す
        left = self.sort(left)
        right = self.sort(right)

        # 左右の要素を結合して返却
        return self.join(left, right)

    @staticmethod
    def join(left, right):
        # 結合結果を格納する変数
        joined = []

        left_index, right_index = 0, 0

        # ソート済み配列を結合するため配列の先頭同士を比較
        # どちらかの配列の末端要素にたどり着くまで繰り返す
        while left_index < len(left) and right_index < len(right):  # 末端要素に達すれば終了
            if left[left_index] <= right[right_index]:  # 左右の先頭を比較して、小さい方を結合
                joined.append(left[left_index])
                left_index += 1
            else:
                joined.append(right[right_index])
                right_index += 1

        # 末端要素に達しなかった方の配列の残った要素を末端に結合する
        if left_index < len(left):
            joined.extend(left[left_index:])
        elif right_index < len(right):
            joined.extend(right[right_index:])
        return joined
