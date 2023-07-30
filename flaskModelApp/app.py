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
import matplotlib.pyplot as plt
from skimage import feature
import cv2
import base64



app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app)


@app.route("/")  # 홈 화면
def hello():
    
    return render_template('home.html')
    

@app.route("/Imagefiles", methods=["POST"])
def files():
    print("1-------------------------------------------------")
    #file = request.files["files"]  # 클라이언트로부터 전송된 파일 받기
    data = request.form["base64String"]
        # 파일 처리 로직 작성
        # 예를 들어, 파일 저장을 원한다면:
    #print(data)
    model = joblib.load(
        '/Users/hongseongmin/Documents/GitHub/notice-board/pythonTest/flaskModelApp/parkinsons_spiral_model_Rf.pkl')
    test_prediction(model,data)
    print("-------------------------------------------------")
    return jsonify({"message": "파일 업로드 성공"})


def quantify_image(image):
    features = feature.hog(image, orientations=9,
                           pixels_per_cell=(10, 10), cells_per_block=(2, 2),
                           transform_sqrt=True, block_norm="L1")
    return features

def test_prediction(model, base64_image_data):
    # get the list of images
    
    # base64 디코드하여 이미지 데이터로 변환
    image_data = base64.b64decode(base64_image_data)
    nparr = np.frombuffer(image_data, np.uint8)
    output_images = []
    # pick 15 images at random
    # NumPy 배열을 이미지로 읽어들이기
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    output = image.copy()
    cv2.imwrite("file_image.png", image)
    output = cv2.resize(output, (128, 128))
    # pre-process the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (200, 200))
    image = cv2.threshold(image, 0, 255,
                            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # quantify the image and make predictions based on the extracted features
    features = quantify_image(image)
    preds = model.predict([features])
    print(preds)
    predict_proba = model.predict_proba([features])
    print(predict_proba)
    label = "Parkinsons" if preds[0] else "Healthy"

    # draw the colored class label on the output image and add it to
    # the set of output images
    color = (0, 255, 0) if label == "Healthy" else (0, 0, 255)
    cv2.putText(output, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                color, 2)
    output_images.append(output)
    cv2.imwrite("file_name.png", output)
    print("ok")


@app.route("/model", methods=['POST'])  # POST 요청 받기
def model():
    if request.method == 'POST':
        data = request.form.get('age')
        print(data)
        #data = {"data": request.form["data"]}  # 데이터 받기

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
