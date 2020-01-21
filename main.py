from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '********'
app.config['MAIL_PASSWORD'] = '********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send_mail/')
def send_mail():
    mes = open('mes.txt', 'r').read()
    r = '*********'
    r = r.split(', ')
    recipients = list()
    for element in r:
        temp = list()
        temp.append(element)
        recipients.append(temp)

    for element in recipients:
        msg = Message('Noesis 6.0', sender='visionmanitbhoapl@gmail.com', recipients=element)
        msg.body = render_template("mail.html", message=mes)
        mail.send(msg)

    return render_template('mail_sent.html')


if __name__ == '__main__':
    app.run(debug=True)
