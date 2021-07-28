# Core Pkgs
import streamlit as st 

# Utils
import numpy as np 
import joblib
import os

import pickle
import pandas as pd
import string
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


pickle_in = open("XG_bm_sales_model_20_May.pkl","rb")
booster=pickle.load(pickle_in)






#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()




#def scale_data(x):
 #   X = scaler.fit_transform(x)
  #  return X

item_fat_content_dict={"Item_Fat_Content_0":0,"Item_Fat_Content_1":1,"Item_Fat_Content_2":2}
outlet_location_type_dict={"Outlet_Location_Type_0":0,"Outlet_Location_Type_1":1,"Outlet_Location_Type_2":2 }
outlet_size_dict={"Outlet_Size_0":0,"Outlet_Size_1":1,"Outlet_Size_2":2}
outlet_dict={"Outlet_0":0,"Outlet_1":1,"Outlet_2":2, "Outlet_3":3, "Outlet_4":4,"Outlet_Size_5":5,"Outlet_Size_6":6,"Outlet_Size_7":7, "Outlet_Size_8":8, "Outlet_Size_9":9}
new_item_type_dict={"Food":0,"Non-Consumable":1,"Drinks":2}
outlet_type_dict={"Supermarket type 1":0,"Grocery":1,"Supermarket type 3":2, "Supermarket Type2":3}
outlet_years_dict={"24":0,"22":1,"5":2,"12":3,"10":4,"7":5,"0":6,"2":7,"11":8}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value 

#load data


@st.cache


def load_model(model_file):
    pickle_in = open("XG_bm_sales_model_20_May.pkl","rb")
    booster=pickle.load(pickle_in)
    return booster





# Load ML Models
#@st.cache
#def load_model(model_file):
 #   loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
  #  return loaded_model
    


def run_ml():
    st.subheader("Bigmart Sales Predictor")
    

    outlet_location_type = st.selectbox("Outlet_Location_Type",["Outlet_Location_Type_0","Outlet_Location_Type_1","Outlet_Location_Type_2"])
    outlet_size = st.selectbox("Outlet_Size",["Outlet_Size_0","Outlet_Size_1","Outlet_Size_2"])
    item_fat_content = st.selectbox("Item_Fat_Content",["Item_Fat_Content_0","Item_Fat_Content_1","Item_Fat_Content_2"])
    outlet=st.selectbox("Outlet",["Outlet_0","Outlet_1","Outlet_2", "Outlet_3", "Outlet_4","Outlet_5","Outlet_6","Outlet_7", "Outlet_8","Outlet_9"])
    outlet_type=st.selectbox("Outlet_Type",["Supermarket type 1","Grocery","Supermarket type 3", "Supermarket Type2"])
    new_item_type=st.selectbox("New_Item_Type",["Food","Non-Consumable","Drinks"])
    outlet_years=st.selectbox("Outlet_Years",["24","22","5","12","10","7","0","2","11"])
    item_visibility=st.slider("Item_Visibility",0.0000,0.3236,0.0001)
    item_weight =st.slider("Item_Weight",4.5550,21.35,0.0001)
    item_visib_avg =st.slider("Item_Visibility_Avg",0.0000,2.0776,0.0001)
    item_MRP=st.slider("Item_MRP",31.9900,266.5884,1.000)
  

    selected_options = {'Item_Fat_Content':item_fat_content, 'Outlet_Location_Type':outlet_location_type, 'Outlet_Size':outlet_size,
       'Outlet_Type':outlet_type, 'Outlet_Years':outlet_years, 'New_Item_Type':new_item_type, 'Outlet':outlet,'Item_Visibility':item_visibility,'Item_Weight':item_weight,'Item_MRP':item_MRP}


    Outlet_Location_Type_en = get_value(outlet_location_type,outlet_location_type_dict)
    Outlet_Size_en = get_value(outlet_size,outlet_size_dict)
    Item_Fat_Content_en = get_value(item_fat_content,item_fat_content_dict)
    Outlet_en = get_value(outlet,outlet_dict)
    Outlet_Type_en = get_value(outlet_type,outlet_type_dict)
    New_Item_Type_en = get_value(new_item_type,new_item_type_dict)
    Outlet_Years_en = get_value(outlet_years,outlet_years_dict)
    Item_Visibility_en=item_visibility
    Item_Weight_en =item_weight
    item_visib_avg_en=item_visib_avg
    Item_MRP_en=item_MRP

    single_sample=[Item_MRP_en,Item_Visibility_en,Item_Weight_en,Outlet_Years_en,item_visib_avg_en,Item_Fat_Content_en,Outlet_Location_Type_en,Outlet_Size_en,New_Item_Type_en,Outlet_Type_en,Outlet_en]
    st.write(selected_options)

    if st.button("Predict"):
        # scaled_sample = scale_data(np.array(single_sample).reshape(1,-1))
        # st.write(scaled_sample)
        sample = np.array(single_sample).reshape(1,-1)
        
        

        #model = load_model("models/XG_bm_sales_model_20_May.pkl")
        prediction = booster.predict(sample)

        st.info("Predicted Sale")
        st.write("Item_Outlet_Sale:Rs{}".format(abs(prediction)))
        st.balloons()