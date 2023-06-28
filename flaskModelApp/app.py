from flask import Flask, request, jsonify, render_template  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import tensorflow as tf
import sklearn
import numpy as np
import joblib

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.


@app.route("/")  # 홈 화면
def hello():
    return render_template('home.html')


@app.route("/model", methods=['POST'])  # POST 요청 받기
def model():
    if request.method == 'POST':
        data = {"data": request.form["data"]}  # 데이터 받기

        model = joblib.load(
            'C:/HSM/Workspace/pythonTest/flaskModelApp/saved_model_clf.pkl')  # 모델 불러오기 -> 현재 결정 트리 모델로 구성을 했다
        arr = np.array([request.form["data"].split(',')])  # 받은 인자값 ,로 구분해 넘파이 배열로 변환

        prediction = model.predict(arr)  # 모델 예측값
        result = prediction  # 모델 예측값 결과값에 저장
        print("result : ", result)  # 출력
        print("predict_proba : ", model.predict_proba(arr))  # 클래스별 예측값 출력 -> 현재는 딱히 구분 안됨
        # result = {"test" : "test1234"}
    return jsonify(result.tolist(), model.predict_proba(arr).tolist()), 200  # 결괏값 리턴


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
