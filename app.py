from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
  return "Hello World from Jenkins CI/CD"  

if _name _=="_main_":
  app.run(host="0.0.0.0", port=5000)
