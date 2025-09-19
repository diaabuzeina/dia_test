from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    # إرسال الملف index.html مباشرة من نفس مسار app.py
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
