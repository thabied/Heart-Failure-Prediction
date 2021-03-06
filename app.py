import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd

model = load_model('model')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('header.jpg')

    st.image(image,use_column_width=True)

    add_selectbox = st.sidebar.selectbox(
    "Would you like to predict for a single patient or multiple patients by uploading a .csv?",
    ("Single Patient", "Multiple"))

    st.sidebar.info('Using a Machine Learning model to predict Heart Failure in patients')
    st.sidebar.info('These results are not meant to be treated as a medical diagnosis but simply a research tool of experimentation')
    st.sidebar.info('Please refer to the GitHub repo to view the Weather Mapping for the "Weather Condition" input')
    st.sidebar.success('https://tmplayground.com')
    st.sidebar.success('https://github.com/thabied')
    st.sidebar.image('https://media.giphy.com/media/xULW8GKlriYjiarBK0/giphy.gif',use_column_width=True)

    st.title("Solar Power Prediction Application")

    if add_selectbox == 'Single Patient':

        age = st.number_input('Age', min_value=10, max_value=150, value=45)
        ejection_fraction = st.input('Percentage of blood leaving the heart at each contraction (percentage)', min_value=1, max_value=100, value=20)
        serum_creatinine = st.number_input('Level of serum creatinine in the blood (mg/dL)', min_value=0, max_value=50, value=2)

        output=""

        input_dict = {'age' : age, 'ejection_fraction' : ejection_fraction, 'serum_creatinine' : serum_creatinine}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):

            output = predict(model=model, input_df=input_df)
            if output == 1:
                answer = 'Patient will experience heart failure'
            else:
                answer = 'No indication of heart failure'

        st.success('Classification {}'.format(answer))

    if add_selectbox == 'Upload .csv':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
