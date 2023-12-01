# AWSを使用するためのライブラリを読み込む
import boto3
# iniファイルを使用するためのライブラリを読み込む
import configparser
# 認識結果を表示するためのライブラリを読み込む
# from matplotlib import pyplot as plt
from PIL import Image
import random

# client = boto3.client('rekognition', 'ap-northeast-1')

filename = "./IMG_0170.jpeg"

ini = configparser.ConfigParser()
ini.read("./config.ini", "UTF-8")

access_key = ini["AWS_KEY"]["awsaccesskeyid"]
secret_key = ini["AWS_KEY"]["awssecretkey"]

with open('./IMG_0170.jpeg', 'rb') as source_image:
    source_bytes = source_image.read()

session = boto3.Session(
    aws_access_key_id=access_key, aws_secret_access_key=secret_key
)

rekognition = session.client("rekognition",'ap-northeast-1')

response = rekognition.detect_labels(Image={'Bytes':source_bytes})

print(response)






# res = rekognition.detect_labels(Image=img)
# print(res)
