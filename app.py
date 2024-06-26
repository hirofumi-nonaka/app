from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3


db = sqlite3.connect(
    "./tax.db",              #ファイル名
    isolation_level=None,
)

#フィールド作成用SQL文
sql = """
    create table if not exists TAX (
      id integer primary key autoincrement,
      price integer
    )
"""

db.execute(sql)     #sql文を実行
db.close()          #データベースを閉じる


app = Flask(__name__)

app.config["SECRET_KEY"] = 'secret_key'

 

@app.route('/', methods=['GET', 'POST'])

def index():

    if request.method == 'POST':

      session['eat'] = request.form['eat']

      price=float(request.form['price'])

      eat_in = int(session['eat'])

      if eat_in==1:

         price = price*1.1

         #session['cost'] = price

   

      else:

         price = price*1.08

         #session['cost'] = price
      table_name="TAX"
      con = sqlite3.connect("./tax.db") # コネクト
      cur=con.cursor()
      data=(int(price),)
      #print("data:",data)
      sql = f"insert into {table_name} (price) values (?)"
      cur.execute(sql, data) # SQL実行
      con.commit()
      con.close()

      con = sqlite3.connect('./tax.db')
      cur = con.cursor()
      cur.execute("SELECT * FROM TAX")
      rows = cur.fetchall()
      print("ROWS",rows)
      for row in rows:
          #print(str(row[0]) + "," + str(row[1]))
          #print("ROW",row)
          session['cost'] = row[1] #最後のデータだけsession['cost']に保存
          print(row[1])
          print(session['cost'])
      con.close()

 

      return redirect(url_for('registerd'))

    return render_template('register.html')

 

@app.route('/registered')

def registerd():

  return render_template('registered.html')

 

 

if __name__ == '__main__':

  app.run(debug=True,port=8000)

