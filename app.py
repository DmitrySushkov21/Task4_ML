import pickle
import streamlit as st

pickled = open('model/IrisClassifier.pkl', 'rb')
iris_model = pickle.load(pickled)

layout = 'centered'
page_title = 'Iris Classification App'
page_icon = ':rose:'

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(f'{page_icon} {page_title}')

# html reset
html_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
"""
st.markdown(html_style, unsafe_allow_html=True)
with st.sidebar:
    st.markdown('## Iris Classification App')

with st.container():
    with st.form(key='my_form'):
        st.text('Enter details bellow')
        sep_len = st.text_input(label='Sepal Length')
        sep_wid = st.text_input(label='Sepal Width')
        pet_len = st.text_input(label='Petal Length')
        pet_wid = st.text_input(label='Petal Width')
        submit = st.form_submit_button(label='Predict')

    if submit:
        data = [[int(sep_len), int(sep_wid), int(pet_len), int(pet_wid)]]
        flower = iris_model.predict(data)
        st.text(flower[0])
        match flower[0]:
            case 'Setosa':
                st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/413px-Irissetosa1.jpg')
            case 'Virginica':
                st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/800px-Iris_versicolor_3.jpg')
            case 'Versicolor':
                st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/330px-Iris_virginica_2.jpg')