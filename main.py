from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# صفحة رئيسية
@app.route("/")
def home():
    return render_template("index.html")

# API بسيط للبوت
@app.route("/bot", methods=["POST"])
def bot_response():
    user_msg = request.json.get("message", "")
    reply = "شكراً لتواصلك معنا!"

    if "موعد" in user_msg:
        reply = "لحجز موعد، يرجى الاتصال على الرقم 123456."
    elif "قسم" in user_msg:
        reply = "لدينا أقسام: الطوارئ، الأطفال، والباطنية."
    elif "دواء" in user_msg:
        reply = "يرجى مراجعة الصيدلية الخاصة بالمستشفى."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
