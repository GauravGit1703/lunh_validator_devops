from flask import Flask, render_template, request

app = Flask(__name__)

def is_luhn_valid(number: str) -> bool:
    total = 0
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        if not digit.isdigit():
            return False  # invalid if contains non-digit
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    number = ""
    if request.method == "POST":
        number = request.form.get("number", "")
        result = is_luhn_valid(number)
    return render_template("index.html", result=result, number=number)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
