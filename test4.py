import pymysql
import datetime
import sys
from datetime import datetime

sys.path.append(r'D:\anaconda3\Lib\site-packages')
import face_recognition
import os
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='70582829',
    db='oldweb',
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8'
)


def imgg(imgpath):
    all = "D:/web1/imag/faces/old_people/106/"
    count = 0
    unknown_picture = face_recognition.load_image_file(imgpath)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    for path, dir, filelist in os.walk(all):
        for filename in filelist:
            if filename.endswith('jpg'):
                filename = "D:/web1/imag/faces/old_people/106/" + filename
                picture_of_me = face_recognition.load_image_file(filename)
                my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

                results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

                if results[0] == True:
                    count = count + 1
                    print("It's a picture of me!")

    if count != 0:
        cur = con.cursor()
        sql = 'insert into event_info(descrip) values({})'.format("有陌生人进入")
        cur.execute(sql)
        con.commit()


def imgg1(time):
    model_path = './fall_detection.hdf5'
    img = cv2.imread('static/facedata'+time+'.jpg')
    img = cv2.flip(img, 1)
    # 全局常量
    TARGET_WIDTH = 64
    TARGET_HEIGHT = 64
    roi = cv2.resize(img, (TARGET_WIDTH, TARGET_HEIGHT))
    roi = roi.astype("float") / 255.0
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    model = load_model(model_path)
    (fall, normal) = model.predict(roi)[0]
    label = "Fall" if fall > normal else "Normal"
    if label == "Fall":
        cur = con.cursor()
        sql = 'insert into event_info(descrip) values({})'.format("有老人摔倒")
        cur.execute(sql)
        con.commit()


def imgg2(time, time1):
    emotion_dict = {'生气': 0, '悲伤': 5, '中性': 4, '厌恶': 1, '惊讶': 6, '恐惧': 2, '高兴': 3}
    image = face_recognition.load_image_file('static/facedata/' + time + '.jpg')
    # 载入图像
    face_locations = face_recognition.face_locations(image)
    # 寻找脸部
    top, right, bottom, left = face_locations[0]
    # 将脸部框起来

    face_image = image[top:bottom, left:right]
    face_image = cv2.resize(face_image, (48, 48))
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
    face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
    # 调整到可以进入该模型输入的大小

    model = load_model("./model_v6_23.hdf5")
    # 载入模型

    predicted_class = np.argmax(model.predict(face_image))
    # 分类情绪
    label_map = dict((v, k) for k, v in emotion_dict.items())
    predicted_label = label_map[predicted_class]
    s = "有老人" + str(predicted_label)
    u=datetime.now()
    cur = con.cursor()
    sql = 'insert into event_info(descrip) values({})'.format("'"+s+"'")
    cur.execute(sql)
    con.commit()
