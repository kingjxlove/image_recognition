const fs = require("fs"),
    PNG = require("pngjs").PNG;

    
let index = 6;

// fs.createReadStream(index + ".png")
//     .pipe(
//         new PNG()
//     )
//     .on("parsed", function () {
//         for (let y = 0; y < this.height; y++) {
//             for (let x = 0; x < this.width; x++) {
//                 const idx = (this.width * y + x) << 2;
//                 // 线性变换
//                 // var Gray = lineChange((this.data[idx] + this.data[idx + 1] + this.data[idx + 2]) / 3)
//                 var Gray = (this.data[idx] + this.data[idx + 1] + this.data[idx + 2]) / 3
//                 this.data[idx] = Gray;
//                 this.data[idx + 1] = Gray;
//                 this.data[idx + 2] = Gray;

//             }
//         }

//         this.pack().pipe(fs.createWriteStream(index+ "2.png"));
//     });


// // 线性变换
// function lineChange(data) {
//     return Math.round(255 - data);
// }




fs.createReadStream(index + "2.png")
    .pipe(
        new PNG()
    )
    .on("parsed", function () {

        // 灰度直方图
        const his = [];

        for (let y = 0; y < 256; y++) {
            his[y] = 0;
        }
        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                const idx = (this.width * y + x) << 2;
                his[this.data[idx]]++;
                his[this.data[idx + 1]]++;
                his[this.data[idx + 2]]++;

            }
        }


        // 计算新的灰度级
        const cons = 256 / (this.width * this.height * 4)
        const newGray = [];
        for (let y = 0; y < 256; y++) {
            newGray[y] = Math.round(cons * leiJia(his, y));
        }
        console.log(cons)
        console.log(JSON.stringify(his))
        console.log(JSON.stringify(newGray))

        // 替换灰度直方图
        for (let y = 0; y < this.height; y++) {
            for (let x = 0; x < this.width; x++) {
                const idx = (this.width * y + x) << 2;
                const gray = (newGray[this.data[idx]] + newGray[this.data[idx + 1]] + newGray[this.data[idx + 2]]) / 3
                this.data[idx] = gray;
                this.data[idx + 1] = gray;
                this.data[idx + 2] = gray;

            }
        }

        this.pack().pipe(fs.createWriteStream(index + "23.png"));
    });


// 累加
function leiJia(his, n) {
    let t = 0;
    for (let i = 0; i <= n; i++) {
        t += his[i]
    }
    return t;
}

/**
 *
 * https://echarts.apache.org/examples/zh/editor.html?c=line-smooth
 * 旧:
 * option = {
    xAxis: {
        type: 'category',
        data: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255]
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [0,0,0,0,0,0,4,123,396,649,806,679,623,812,642,561,562,589,754,783,872,945,936,906,807,812,824,907,1065,1010,902,938,902,878,923,893,883,867,887,980,968,891,893,851,877,870,913,798,918,937,1037,947,1039,1020,1047,992,1011,1138,1157,1155,1049,953,904,915,942,888,943,989,991,1000,1021,1035,1071,1074,1085,1134,1162,1223,1120,1161,1162,1210,1097,1133,1150,1352,1362,1463,1501,1553,1631,1836,1611,1639,1609,1718,1736,1862,1973,2067,2221,2117,1895,1843,1618,1531,1560,1549,1570,1653,1531,1359,1265,1226,1134,1057,900,846,757,634,553,514,412,436,424,381,367,403,401,438,396,424,433,460,555,553,611,713,755,880,882,954,999,1183,1297,1522,1612,1769,1941,2130,2288,2506,2701,2620,2488,2312,2223,2118,1917,1929,1696,1628,1455,1458,1302,1152,1036,930,849,783,778,773,661,710,645,579,602,649,534,500,481,465,465,456,416,394,341,342,347,345,373,379,377,341,394,392,382,408,407,431,489,433,514,526,500,484,516,600,613,628,629,666,687,760,654,720,656,562,596,576,598,493,570,512,465,465,551,438,419,416,421,436,443,421,417,392,424,439,322,323,295,305,296,271,280,249,208,238,236,293,333,324,391,499,381,517],
        type: 'line',
        smooth: true
    }]
};
 */