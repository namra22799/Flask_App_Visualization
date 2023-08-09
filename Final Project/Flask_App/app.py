from flask import Flask, render_template
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
db = client['xyz_database']  # Replace with your database name
collection = db['car_collection']
#data_file = 'ca-dealers-used.csv'
# df = pd.read_csv(data_file)
df = pd.DataFrame(list(collection.find()))
df = df.drop('_id', axis = 1)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html', data = df.to_dict(orient='records'))

@app.route('/aboutUs')
def aboutUs():
    return render_template('about us.html')

if __name__ == '__main__':
    app.run(debug=True)
