from flask import Flask, request, jsonify, render_template  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
import tensorflow as tf
import sklearn
import numpy as np
import pandas as pd
import joblib
import os
import re
from flask_cors import CORS
app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app)


@app.route("/")  # 홈 화면
def hello():
    
    return render_template('home.html')
    

@app.route("/files", methods=["POST"])
def files():
    try:
        file = request.files["imageFile"]  # 클라이언트로부터 전송된 파일 받기
        # 파일 처리 로직 작성
        # 예를 들어, 파일 저장을 원한다면:
        file.save("uploaded_file.png")
        return jsonify({"message": "파일 업로드 성공"})
    except Exception as e:
        return jsonify({"error": str(e)})


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

@app.route("/reviewModel", methods=['POST'])
def reviewModel():
    if request.method == 'POST':
        print('테스트')
        model = joblib.load('C:/HSM/Workspace/pythonTest/flaskModelApp/best_model.h5')
        connect = cx_Oracle.connect("JSP", "JSP", "localhost:1521/xe")
        df=pd.read_sql_query(""" SELECT * FROM BBS """ , con = connect)
        connect.close()
        print(df)
        return '테스트'

def sentiment_predict(new_sentence):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
    new_sentence = mecab.morphs(new_sentence)
    new_sentence = [word for word in new_sentence if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([new_sentence])
    pad_new = pad_sequences(encoded, maxlen = max_len)

    score = float(loaded_model.predict(pad_new))
    if(score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
