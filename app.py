from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Registration.html')
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    student_id = request.form['student_id']
    email = request.form['email']
    year = request.form['year']
    return render_template('Success.html', name=name, year=year)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)



    