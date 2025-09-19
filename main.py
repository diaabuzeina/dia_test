from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # رابط HTML موجود في مجلد templates

@app.route("/bot", methods=["POST"])
def bot():
    data = request.get_json()
    user_msg = data.get("message","").lower()
    reply = "شكراً لتواصلك معنا!"
    if "موعد" in user_msg:
        reply = "لحجز موعد، يرجى الاتصال على الرقم 123456."
    elif "قسم" in user_msg:
        reply = "لدينا أقسام: الطوارئ، الأطفال، والباطنية."
    elif "دواء" in user_msg:
        reply = "يرجى مراجعة الصيدلية الخاصة بالمستشفى."
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
