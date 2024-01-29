from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import tensorflow as tf
from PIL import Image
import numpy as np
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure the database connection
app.secret_key = 'Muskan@2002'
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Muskan@2002'
app.config['MYSQL_DB'] = 'GreenVision'


mysql = MySQL(app)

model_target_sizes = {
    'Banana': (224, 224),
    'Blackgram': (224, 224),
    'Capsicum': (150, 150),
    'Coffee': (150, 150),
    'Corn': (224, 224),
    'Cotton': (150, 150),
    'Grape': (224, 224),
    'Paddy': (224, 224),
    'Potato': (224, 224),
    'Sugarcane': (224, 224),
    'Sunflower': (224, 224),
    'Tomato': (224, 224),
   
}

@app.route('/')
def home():
   
    available_models = [
        {'id': 'Banana', 'name': 'Banana'},
        {'id': 'Blackgram', 'name': 'Blackgram'},
        {'id': 'Capsicum', 'name': 'Capsicum'},
        {'id': 'Coffee', 'name': 'Coffee'},
        {'id': 'Corn', 'name': 'Corn'},
        {'id': 'Cotton', 'name': 'Cotton'},
        {'id': 'Grape', 'name': 'Grape'},
        {'id': 'Paddy', 'name': 'Paddy'},
        {'id': 'Potato', 'name': 'Potato'},
        {'id': 'Sugarcane', 'name': 'Sugarcane'},
        {'id': 'Sunflower', 'name': 'Sunflower'},
        {'id': 'Tomato', 'name': 'Tomato'},
      
    ]
    return render_template('index.html', available_models=available_models)


@app.route('/contactus')
def contact_us():
    return render_template('contactus.html')

@app.route('/banana')
def banana():
    return render_template('Banana.html')

@app.route('/blackgram')
def blackgram():
    return render_template('Blackgram.html')

@app.route('/capsicum')
def capsicum():
    return render_template('Capsicum.html')

@app.route('/coffee')
def coffee():
    return render_template('Coffee.html')

@app.route('/corn')
def corn():
    return render_template('Corn.html')

@app.route('/cotton')
def cotton():
    return render_template('Cotton.html')

@app.route('/grape')
def grape():
    return render_template('Grape.html')

@app.route('/paddy')
def paddy():
    return render_template('Paddy.html')

@app.route('/potato')
def potato():
    return render_template('Potato.html')

@app.route('/sugarcane')
def sugarcane():
    return render_template('Sugarcane.html')

@app.route('/sunflower')
def sunflower():
    return render_template('Sunflower.html')

@app.route('/tomato')
def tomato():
    return render_template('Tomato.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
        else:
            msg = 'Incorrect email or password!'
    return render_template('index.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if not email or not password or not confirm_password:
            msg = 'Please fill out the form!'
        elif password != confirm_password:
            msg = 'Passwords do not match!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO accounts (email, password) VALUES (%s, %s)', (email, password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    return render_template('index.html', msg=msg)  # You can redirect to a different page after registration if needed


@app.route('/predict/<model_id>', methods=['POST'])
def predict(model_id):
    error = None
    result = None

    if request.method == 'POST':
        # to check if a file was uploaded
        if 'image' not in request.files:
            error = 'No file uploaded'
        else:
            # to get the uploaded file
            uploaded_file = request.files['image']

            # to check if the file has a valid extension (optional)
            if uploaded_file.filename == '':
                error = 'No selected file'
            elif not allowed_file(uploaded_file.filename):
                error = 'Invalid file format'
            else:
                try:
                    # to process the uploaded image
                    img = Image.open(uploaded_file.stream)
                    
                    
                    # to check if the image size matches the target size for the model
                    target_size = model_target_sizes.get(model_id)
                    
                    if target_size is None:
                        error = 'Invalid model ID'
            #         else:
            # # Resize the image to the target size
            #             img = img.resize(target_size)

            #             img_array = np.array(img, dtype=np.float32)  # Convert to float32
            #             img_array /= 255.0 
                    # elif img.size != target_size:
                    else:
                        print("Code execution reached here")
                        print(f"Resizing image to {target_size}")
                        img = img.resize(target_size)
                    
                        img_array = np.array(img, dtype=np.float32)  # Convert to float32
                        img_array /= 255.0  # Normalize the image data

                        # to load the specific model
                        model_path = f'models/{model_id}.h5'
                        model = tf.keras.models.load_model(model_path)

                        # to load class labels for the specific model
                        labels_path = f'class_labels/{model_id}.json'
                        with open(labels_path, 'r') as labels_file:
                            class_labels = json.load(labels_file)

                        # to use the loaded model to make predictions
                        predictions = model.predict(np.expand_dims(img_array, axis=0))

                        # to get the predicted class index
                        predicted_class_index = np.argmax(predictions[0])

                        # to check if the index is within the valid range
                        if 0 <= predicted_class_index < len(class_labels):
                            predicted_class = class_labels[predicted_class_index]
                        else:
                            predicted_class = "Unknown"

                        result = f"Disease: {predicted_class}, Confidence: {max(predictions[0])*100:.2f}%"
                except Exception as e:
                    print(f"Error processing the image: {str(e)}")
                    error = f"Error processing the image: {str(e)}"

    return render_template('model.html', result=result, error=error)

def allowed_file(filename):
    
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

if __name__ == '__main__':
    app.run(debug=True)
