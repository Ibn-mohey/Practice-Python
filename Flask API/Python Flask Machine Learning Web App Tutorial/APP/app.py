from flask import Flask , render_template, request
import numpy as np
from joblib import load
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import uuid


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello_world():
    request_type_str = request.method
    if request_type_str == "GET":
        return render_template('index.html', href = 'static/base_pic.svg' )
    else:
        text = floats_string_to_input_arr(request.form['text'])
        
        random_str = uuid.uuid4().hex
        path = f'static/{random_str}.svg'
        model = load(filename='model.joblib')
        make_picture('AgesAndHeights.pkl',model, text, output_file=path)

        return render_template('index.html', href = path )
    # test_np = np.array([[1], [2],[3],[17]])
    # model = load(filename='model.joblib')
    # model.predict(test_np)



def make_picture(training_data_filename, model, new_input_arr, output_file):
    
    # Plot training data with model
    data = pd.read_pickle(training_data_filename)
    ages = data['Age']
    data = data[ages > 0]
    ages = data['Age']
    heights = data['Height']
    #draw a line
    x_new = np.array(list(range(19))).reshape(19, 1)
    preds = model.predict(x_new)
    fig = px.scatter(x=ages, y=heights, title="Height vs Age of People", labels={'x': 'Age (years)',
                                                                                    'y': 'Height (inches)'})
    fig.add_trace(go.Scatter(x=x_new.reshape(19), y=preds, mode='lines', name='Model'))
    # new_preds = model.predict(new_inp_np_arr)
    # fig.add_trace(go.Scatter(x=new_inp_np_arr.reshape(len(new_inp_np_arr))
    #                                 , y=new_preds, name='New Outputs', mode='markers'
    #                                 , marker=dict(color='purple', size=20, line=dict(color='purple', width=2))))

    if new_input_arr is not False:
        # Plot new predictions
        fig.add_trace(
        go.Scatter(x=new_input_arr.reshape(new_input_arr.shape[0])
        , y=model.predict(new_input_arr)
        , name='New Outputs', mode='markers', marker=dict(
                color='purple',
                size=20,
                line=dict(
                    color='purple',
                    width=2
                ))))
    
    fig.write_image(output_file, width=800,engine = 'kaleido')
    return fig




def floats_string_to_input_arr(floats_str):
    
    def is_float(x):
        try:
            float(x)
            return True
        except:
            return False
    floats = [float(x.strip()) for x in floats_str.split(',') if is_float(x)]
    as_np_arr = np.array(floats).reshape(len(floats), 1)
    return as_np_arr