from flask import Flask, request
from flask_cors import CORS, cross_origin
import database as db

app = Flask(__name__)
cors = CORS(app, )
app.config['CORS_HEADERS'] = 'Content-Type'

def latest_data(n):
    values =db.retrieve_latest_entries(n)
    color = db.retrieve_latest_color()
    return {'data':values ,
            'color': color}


@app.route("/charts/n=<n>",methods =['GET','POST','DELETE','OPTIONS'])
@cross_origin()
def charts_backend(n):
    n=int(n)
    if request.method =='GET':
        return latest_data(n)

    elif request.method =='POST':
        vals = db.create_entries(n)
        color = db.create_color_entry()
        return {'data': vals,
                'color': color}

    elif request.method =='DELETE':
        db.delete_latest_entries(n)
        db.delete_latest_color_entry()
        return latest_data(n)

    else:
        return{}




if __name__ == '__main__':
    app.run(debug=True)


