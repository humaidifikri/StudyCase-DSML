import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from house_price_prediction.predict_regression import reg_predict
# st.set_page_config(page_title="Demo Regresi Linear")

def regression():       
    df = pd.read_csv('.\house_price_prediction\data\housing_price.csv')
    st.markdown('## Dashboard Harga Properti')

    number_of_bedrooms = df.groupby('bedrooms')['price'].agg(
        min='min',
        max='max',
        mean= 'mean'
    )

    number_of_bathrooms = df.groupby('bathrooms')['price'].agg(
        min='min',
        max='max',
        mean= 'mean'
    )

    number_of_stories = df.groupby('stories')['price'].agg(
        min='min',
        max='max',
        mean= 'mean'
    )

    number_of_parking = df.groupby('parking',)['price'].agg(
        min='min',
        max='max',
        mean= 'mean'
    )

    furnishedStatus = df.groupby('furnishingstatus',)['price'].agg(
        min='min',
        max='max',
        mean= 'mean'
    )
    
    st.markdown('Harga properti berdasarkan luas area')
    st.scatter_chart(data=df,x='area',y='price')
    
    col1,col2 = st.columns(2)
    # # st.dataframe(number_of_bedrooms)
    with col1:
        st.markdown('Harga properti berdasarkan jumlah kamar')
        st.bar_chart(number_of_bedrooms)

        st.markdown('Harga properti berdasarkan jumlah lantai')
        st.bar_chart(number_of_stories)
        
        st.markdown('Harga properti berdasarkan status furnish')
        st.bar_chart(furnishedStatus)

    with col2:
        st.markdown('Harga properti berdasarkan jumlah kamar mandi')
        st.bar_chart(number_of_bathrooms)

        st.markdown('Harga properti berdasarkan jumlah ruang parkir')
        st.bar_chart(number_of_parking)

        yes_no_list = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
        selected_feature = st.selectbox("Pilih fitur lainnya:", yes_no_list)
        price_summary = df.groupby(selected_feature)['price'].agg(
            min='min',
            max='max',
            mean= 'mean'
        )
        st.markdown(f'#### Harga properti berdasarkan adanya {selected_feature}/tidak')
        st.bar_chart(price_summary)


    st.markdown(f'## Prediksi Harga Properti')
     
    
    col3,col4 = st.columns(2)

    with col3:
        area = int(st.number_input("Masukkan luas area (ft)",step=1000))
        bedrooms = st.slider("Pilih jumlah kamar",1,10,2)
        stories = st.slider("Pilih jumlah lantai",1,10,4)
        # st.write(yes_no_list[:3])
        mainroad, guestroom, basement = [st.radio(f"Apakah ada {kategori}",['yes','no'],key=kategori) for kategori in yes_no_list[:3]]


    with col4:
        furnishingstatus = st.selectbox("Pilih status furnish",['furnished','unfurnished','semi-furnished'])
        bathrooms = st.slider("Pilih jumlah kamar mandi",1,5,1)
        parking = st.slider("Pilih jumlah lahan parkir",0,5,1)
        hotwaterheating, airconditioning, prefarea = [st.radio(f"Apakah ada {kategori}",['yes','no'],key=kategori) for kategori in yes_no_list[3:]]
    
    data_predict = pd.DataFrame({
                            'area':[area],
                            'bedrooms':[bedrooms],
                            'bathrooms':[bathrooms],
                            'stories':[stories],
                            'parking':[parking],
                            'prefarea':[prefarea],
                            'mainroad':[mainroad],
                            'guestroom':[guestroom],
                            'basement':[basement],
                            'hotwaterheating':[hotwaterheating],
                            'airconditioning':[airconditioning],
                            'furnishingstatus':[furnishingstatus]
                            },index=[0])

    if st.button("Prediksi harga!"):
        pred = reg_predict(data_predict)        
        st.success(f'Harga rumah anda diperkirakan {pred}')
