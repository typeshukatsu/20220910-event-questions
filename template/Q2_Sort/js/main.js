'use strict';

const Logic = require("./logic.js");

const main = () => {

    // ランダムに並べられた重複のない最大5桁の整数の配列
    const array = [5, 4, 6, 2, 1, 100, 12000, 11111, 2222, 2213, 333, 44, 43, 9, 8, 3, 7, 10];

    // 桁数の最大値
    const MAX_DIGITS = 5;

    const logic = new Logic();

    // ソート実行
    const result = logic.sort(array, MAX_DIGITS);

    // 結果出力
    console.log(result);

};

main();
