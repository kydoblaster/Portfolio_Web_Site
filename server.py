from flask import Flask, render_template, request
from forms import ContactForm
import smtplib

my_email = "kydoblaster@gmail.com"
my_password = "kydoblaster327!!!"
app = Flask(__name__)
app.secret_key = 'secretKey'



@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="kyle.yonan@gmail.com",
                msg=f"Subject: New Form Submission\n\n{name}\n{email}\n{message}\n"
            )
            connection.close()
        return render_template("contact.html", TOPPER="Message Sent!", form=form)
    return render_template("contact.html", TOPPER="Contact Me", form=form)


if __name__ == "__main__":
    app.run(debug=True)