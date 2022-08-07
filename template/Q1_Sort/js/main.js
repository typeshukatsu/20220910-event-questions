'use strict';

const Logic = require("./logic.js");

const main = () => {

    // ランダムに並べられた重複のない整数の配列
    const array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10];

    const logic = new Logic();

    // ソート実行
    const result = logic.sort(array);

    // 結果出力
    console.log(result);
};

main();
