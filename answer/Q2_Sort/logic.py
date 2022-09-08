class Logic:

    # 基数ソート
    def sort(self, array, max_digits):
        # 基数
        RADIX = 10

        # 桁数回のループでバケツソート
        for digit_index in range(max_digits):

            # 2次元配列のバケツを初期化
            nested_bucket = self.init_nested_bucket(RADIX)

            # 配列をループして、桁毎の数字をkeyにnested_bucketへ追加していく
            for value in array:
                # ソート対象桁の値(key)
                target_digit_number = self.get_target_digit_number(value, digit_index, RADIX)

                # ソート対象桁の値をkeyとして、バケツに追加
                nested_bucket[target_digit_number].append(value)

            # バケツの前から順にarrayへ詰め直し
            array = []
            for values in nested_bucket:
                for value in values:
                    array.append(value)

            # ここで対象桁digit_indexのソートが完了しているので、次の桁へループする

        # ソートした配列を返却
        return array

    # 2次元配列のバケツを初期化
    @staticmethod
    def init_nested_bucket(radix):
        # 2次元配列のバケツを用意
        #   各桁は`0~9`までの`10`個の数値を取り得るため、radix = `10`個のバケツを内包
        nested_bucket = [[] for _ in range(radix)]
        return nested_bucket

    # ソート対象桁の値を取得
    @staticmethod
    def get_target_digit_number(value, digit_index, radix):
        # ソート対象桁の値
        #    = ソート対象桁以上の値(value // radix**(digit_index))
        #        を基数(radix)で割った`余り`
        upper_target_digit_number = value // radix**(digit_index)
        return upper_target_digit_number % radix
