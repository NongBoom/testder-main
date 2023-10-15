from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from predict import predict
from datetimePost import now
# from textprocess import text_process

# save comment and prediction
feed_comments = [] 

app = Flask(__name__)
@app.route("/")
def index(): #โมดูลรับค่าจากไฟล์ index.html โดยการส่งค่าในรูปแบบ POST
    return render_template('index.html', feed_comments = feed_comments)

@app.route('/save', methods=['POST'])
def save(): #โมดูลแสดงข้อมูล
    textinput = request.form.get('textarea') # รับข้อความจาก form หน้า index.html
    # print(textinput)
    p = predict(textinput) # ทำนายข้อความ
    dictlabel = {'pos': 'positive', 'neu': 'neutral', 'neg': 'negative'}
    label = dictlabel[p[0]]
    cid = len(feed_comments)
    feed_comments.append({"id": cid, "content": textinput, "predict": label,"time": now()}) # save id ข้อความ ประเภทข้อความ เวลา
    return redirect(url_for('index'))

@app.route('/feed_summary')
def feed_summary():
    # Calculate the summary data for the pie chart
    content_summary = {}
    for item in feed_comments:
        content = item['predict']
        content_summary[content] = content_summary.get(content, 0) + 1

    # Prepare the data for the pie chart
    labels = list(content_summary.keys())
    values = list(content_summary.values())

    return jsonify(labels=labels, values=values)

@app.route('/clear_feed', methods=['POST'])
def clear_feed():
    feed_comments.clear()  # Clear the list of feed comments
    return redirect(url_for('index'))

app.run(debug=True)