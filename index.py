from flask import Flask, render_template_string, request
from quotes import Quotes
import time

app = Flask(__name__)


def get_random_quote():
    q = Quotes()
    data = q.random()
    return data


@app.route("/")
def index():
    user = request.args.get("user") or None
    time.sleep(3)  # Adding 1.5-second delay
    if user:
        quote = get_random_quote()
        template = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Quote Generator</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
            <style>
              body {
                  font-family: 'Roboto', sans-serif;
                  text-align: center;
                  margin: 0;
                  padding: 0;
                  background: linear-gradient(to right, #0093E9, #80D0C7);
                  color: #333;
              }
              h1 {
                  margin-top: 50px;
                  color: #fff;
                  font-size: 2.5em;
                  font-weight: 700;
              }
              .container {
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  height: 80vh;
              }
              .quote-card {
                  background: #fff;
                  border-radius: 15px;
                  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                  padding: 40px;
                  max-width: 600px;
                  margin: 0 20px;
                  position: relative;
                  overflow: hidden;
              }
              .quote {
                  font-size: 1.6em;
                  line-height: 1.6;
                  margin-bottom: 20px;
                  color: #333;
              }
              .author {
                  font-size: 1.2em;
                  color: #555;
                  margin-bottom: 20px;
              }
              button {
                  background-color: #0093E9;
                  border: none;
                  color: white;
                  padding: 15px 30px;
                  font-size: 1.1em;
                  border-radius: 25px;
                  cursor: pointer;
                  transition: background-color 0.3s, transform 0.3s;
                  display: inline-flex;
                  align-items: center;
              }
              button:hover {
                  background-color: #007bb5;
                  transform: scale(1.05);
              }
              button i {
                  margin-right: 8px;
              }
            </style>
          </head>
            """
        data = """
        <body>
           <h1>Random Quote Generator</h1>
           <div class="container">
             <div class="quote-card">
               <div class="user"> Hi {user} this is a quote for youu.</div>
               </br>
               <div class="quote">{quote}</div>
               <div class="author">{author}</div>
             </div>
           </div>
         </body>
       </html>
        """.format(
            user=user, author=quote[0], quote=quote[1]
        )
        template = template + data
        return render_template_string(template)
    template = """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Quote Generator</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
            <style>
              body {
                  font-family: 'Roboto', sans-serif;
                  text-align: center;
                  margin: 0;
                  padding: 0;
                  background: linear-gradient(to right, #0093E9, #80D0C7);
                  color: #333;
              }
              h1 {
                  margin-top: 50px;
                  color: #fff;
                  font-size: 2.5em;
                  font-weight: 700;
              }
              .container {
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  height: 80vh;
              }
              .quote-card {
                  background: #fff;
                  border-radius: 15px;
                  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                  padding: 40px;
                  max-width: 600px;
                  margin: 0 20px;
                  position: relative;
                  overflow: hidden;
              }
              .quote {
                  font-size: 1.6em;
                  line-height: 1.6;
                  margin-bottom: 20px;
                  color: #333;
              }
              .author {
                  font-size: 1.2em;
                  color: #555;
                  margin-bottom: 20px;
              }
              button {
                  background-color: #0093E9;
                  border: none;
                  color: white;
                  padding: 15px 30px;
                  font-size: 1.1em;
                  border-radius: 25px;
                  cursor: pointer;
                  transition: background-color 0.3s, transform 0.3s;
                  display: inline-flex;
                  align-items: center;
              }
              button:hover {
                  background-color: #007bb5;
                  transform: scale(1.05);
              }
              button i {
                  margin-right: 8px;
              }
            </style>
          </head>
          <body>
            <h1>Random Quote Generator</h1>
            <div class="container">
              <div class="quote-card">
                <div class="author">Hi there, try to type ur name as user params and see the secret heehhehe</div>
              </div>
            </div>
          </body>
        </html>
        """
    return render_template_string(template)


if __name__ == "__main__":
    app.run(debug=True)
