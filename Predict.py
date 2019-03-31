# load json and create model
from keras.engine.saving import model_from_json, load_model

#
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
#
# # load weights into new model
# loaded_model.load_weights("/home/sumit/PycharmProjects/Personalised-Diabetes-Assistant/model_num2.h5")
# print("Loaded model from disk")

import numpy as np

def getVector(data):
    vector = ''

    # sleep range 0-24
    sleep_count = data['sleep']
    vector += format(sleep_count, '05b')

    # glucode level range 1-1024
    glucose_count = data['glucose']
    vector += format(glucose_count, '010b')

    # weight range 1-128
    weight_count = data['weight']
    vector += format(weight_count, '07b')

    # type of excersize 0-
    exersize_count = data['excersize']
    vector += format(exersize_count, '011b')
    result = []
    for i in vector:
        if i == '1':
            result.append(1)
        else:
            result.append(0)

    return np.array(result[5:15])

def pred(x):
    json_file = open('/home/sumit/PycharmProjects/Personalised-Diabetes-Assistant/model_num2.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/home/sumit/PycharmProjects/Personalised-Diabetes-Assistant/model_num2.h5")
    print("Loaded model from disk")
    x = x.reshape(1, 10, 1)
    x = [1 if i > 0.5 else 0 for i in loaded_model.predict(x)[0]]
    x  = int("".join(str(i) for i in x), 2)
    return x
