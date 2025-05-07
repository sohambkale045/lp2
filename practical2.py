from flask import Flask, request, render_template_string

app = Flask(__name__)

# Calculator functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    else:
        return n1 / n2

# HTML template for the web page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form method="POST">
        <label for="n1">Enter first number:</label>
        <input type="number" id="n1" name="n1" required><br><br>

        <label for="n2">Enter second number:</label>
        <input type="number" id="n2" name="n2" required><br><br>

        <label for="operation">Select operation:</label>
        <select id="operation" name="operation">
            <option value="add">Add</option>
            <option value="sub">Subtract</option>
            <option value="mul">Multiply</option>
            <option value="div">Divide</option>
        </select><br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

# Route for the calculator
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        try:
            n1 = int(request.form['n1'])
            n2 = int(request.form['n2'])
            operation = request.form['operation']

            if operation == 'add':
                result = add(n1, n2)
            elif operation == 'sub':
                result = sub(n1, n2)
            elif operation == 'mul':
                result = mul(n1, n2)
            elif operation == 'div':
                result = div(n1, n2)
        except ValueError:
            result = "Invalid input! Please enter valid numbers."

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
