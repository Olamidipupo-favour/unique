from firebase import firebase
firebase = firebase.FirebaseApplication('https://ubrowseliteyear-default-rtdb.firebaseio.com/', None)
@app.route("/")
def home():
  result = firebase.get('/restaurants', None)
  return str(result)
