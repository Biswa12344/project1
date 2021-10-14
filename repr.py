# class car:
#     def __init__(self,color,number):
#         self.color= color
#         self.number=number
#     def __str__(self):
#         return 'a {self.color} car'.format(self=self)
#
# my_car=car('red',22596)
#
# #print(str(my_car))
#
# #print(my_car.color)



from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np

repr=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@repr.route("/")
def Home():
    return render_template('index.html')
@repr.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    output=round(prediction[0],2)
    return render_template('index.html',prediction_text='CO2 shoukd be {}'.format(output))
if __name__=='__main__':
    repr.run(debug=True)
