import streamlit as st
import pandas as pd
import joblib

Model=joblib.load("model.h5")
Inputs=joblib.load("input.h5")

def predict(online_order,book_table,votes,location,rest_type,cuisines,cost2people,types):
    df_test=pd.DataFrame(columns=Inputs)
    
    df_test.at[0,'online_order']=online_order
    df_test.at[0,'book_table']=book_table
    df_test.at[0,'votes']=votes
    df_test.at[0,'location']=location
    df_test.at[0,'rest_type']=rest_type
    df_test.at[0,'cuisines']=cuisines
    df_test.at[0,'cost2people']=cost2people
    df_test.at[0,'types']=types
    result=Model.predict(df_test)[0]
    return result

def main():
    st.title('Estimate of Rate  Bangalore Restaurants')
    
    online_order=st.selectbox('online_order', ['Yes', 'No'])
    
    book_table=st.selectbox('book_table', ['Yes', 'No'])
    
    votes=st.slider('votes' ,min_value=0,max_value=16900,value=25,step=1)
    
    location=st.selectbox('location' , ['Banashankari', 'Basavanagudi', 'other', 'Jayanagar', 'JP Nagar','Bannerghatta Road', 'BTM', 'Electronic City', 'HSR','Marathahalli', 'Koramangala five Block', 'Richmond Road','Koramangala seven Block', 'Koramangala four Block', 'Bellandur','Sarjapur Road', 'Whitefield', 'Old Airport Road', 'Indiranagar','Koramangala one Block', 'Frazer Town', 'MG Road', 'Brigade Road','Lavelle Road', 'Church Street', 'Ulsoor', 'Residency Road','Malleshwaram', 'Kammanahalli', 'Koramangala six  Block','Brookefield', 'Rajajinagar', 'Banaswadi', 'Kalyan Nagar','New BEL Road'])
    rest_type=st.selectbox('rest_type' , ['Casual Dining', 'Other', 'Quick Bites', 'Cafe', 'Delivery','Dessert Parlor', 'Takeaway Delivery'])
    
    cuisines=st.selectbox('cuisines', ['others', 'South Indian North Indian', 'North Indian', 'Cafe','Cafe Continental', 'Cafe Fast Food', 'Bakery Desserts', 'Pizza','Biryani', 'North Indian Chinese Fast Food', 'South Indian','Burger Fast Food', 'Pizza Fast Food', 'North Indian Chinese','Chinese Thai', 'Ice Cream Desserts', 'Desserts Beverages','Chinese', 'Bakery', 'Fast Food', 'Mithai Street Food','South Indian Chinese', 'Biryani North Indian Chinese', 'Desserts','Ice Cream', 'South Indian North Indian Chinese','South Indian Biryani', 'Beverages', 'Chinese North Indian','South Indian North Indian Chinese Street Food', 'Street Food','Desserts Ice Cream', 'North Indian Chinese Biryani','Beverages Fast Food', 'North Indian Chinese South Indian','North Indian Fast Food', 'North Indian South Indian','North Indian Biryani', 'Finger Food', 'Continental','Fast Food Beverages', 'Biryani Kebab', 'North Indian Mughlai','North Indian South Indian Chinese', 'Biryani North Indian','Chinese Momos', 'Desserts Bakery', 'Bakery Fast Food', 'Kerala'])
                          
    cost2people=st.slider('cost2people', min_value=40, max_value=6000,value=20,step=1)
                          
    types=st.selectbox('types', ['Buffet', 'Cafes', 'Delivery', 'Desserts','Dineout', 'Drinks and nightlife', 'Pubs and bars'])
    
    if st.button('predict'):
        result=predict(online_order,book_table,votes,location,rest_type,cuisines,cost2people,types)
        st.write("Rate of resturant in Bangalore will be : {}".format(result))
if __name__ == '__main__':
    main()
