from flask import Flask, make_response, jsonify

from flask import request

import hyperlpr
import cv2
import os
import time

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))


@app.route('/', methods=['POST'])
def hello_world():
    t1 = time.time()
    upload_file = request.files['file']
    file_name = upload_file.filename
    file_path = './pictures/'
    save_path = file_path + str(int(time.time())) + '_' + file_name
    upload_file.save(save_path)
    img = cv2.imread(save_path)
    result = {'resultList': hyperlpr.HyperLPR_plate_recognition(img)}
    response = make_response(jsonify(result))
    os.remove(save_path)
    # 设置响应请求头
    response.headers["Access-Control-Allow-Origin"] = '*'  # 允许使用响应数据的域。也可以利用请求header中的host字段做一个过滤器。
    response.headers["Access-Control-Allow-Methods"] = 'POST'  # 允许的请求方法
    response.headers["Access-Control-Allow-Headers"] = "x-requested-with,content-type"
    app.logger.info(time.time() - t1)
    return response


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5001, host="0.0.0.0")
