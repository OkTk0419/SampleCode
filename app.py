from flask import Flask, render_template, request, jsonify, url_for
import datetime as dt
import calendar as cl


app = Flask(__name__)


def generate_calendar(y1, m1):
    cal = [""] * 42
    for i in range(len(cal)):
        cal[i] = ""
    date = dt.date(y1, m1, 1)
    weekday = wd1
    if weekday > 5:
        weekday = weekday - 7
    cal_max = cl.monthrange(y1, m1)[1]
    for i in range(cal_max):
        str1 = str(i + 1)
        index = i + weekday + 1
        cal[index] = str1
    return cal

@app.route('/')
def index():
    global y1 
    global m1
    year = y1
    month = m1
    day = d1
    weekday = wd1
    y1=year
    m1=month
    cal = generate_calendar(year, month)
    return render_template('calendar.html', y1=year, m1=month, cal=cal, weekday=wd1)

@app.route('/prev_month')
def prev_month():
    global y1 
    global m1 
    year = y1
    month = m1 - 1
    if month < 1:
        year -= 1
        month = 12
    cal = generate_calendar(year, month)
    y1=year
    m1=month
    print(y1)
    print(m1)
    return render_template('calendar.html', y1=year, m1=month, cal=cal)

@app.route('/next_month')
def next_month():
    global y1 
    global m1 
    year = y1
    month = m1 + 1
    if month > 12:
        year += 1
        month = 1
    cal = generate_calendar(year, month)
    
    y1=year
    m1=month
    print(y1)
    print(m1)
    return render_template('calendar.html', y1=year, m1=month, cal=cal)

@app.route('/view_diary/<int:year>/<int:month>/<int:day>', methods=['GET', 'POST'])
def view_diary(year, month, day):
    if request.method == 'POST':
        # クライアントから送信されたデータを取得
        diary_data = request.get_json()
        
        # diary_dataを処理して必要な作業を行う（例：データベースに保存）
        # ...
        
        return jsonify({'status': 'success'})
    
    return render_template('view_diary.html', year=year, month=month, day=day)


if __name__ == '__main__':
    global nuw1,y1,m1,d1,wd1
    now1 = dt.datetime.now() 
    y1 = now1.year 
    m1 = now1.month 
    d1 = now1.day 
    wd1 = 0
    print("halloWorld")
    print(m1)
    
    app.run(debug=True)

