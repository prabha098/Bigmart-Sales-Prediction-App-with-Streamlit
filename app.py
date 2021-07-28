import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import streamlit.components.v1 as stc 


from Prediction import run_ml
from Prediction_Explore import run_prediction



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



html_temp = """
        <div style="background-color:#3872fb;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">Bigmart Sales Prediction App</h1>
        <h4 style="color:white;text-align:center;">Great Stores Great Choices</h4>
        </div>
        """



def main():
	stc.html(html_temp)

	menu = ["Home","SignUp","Login"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		from PIL import Image
		img=Image.open("bigmart.jpg")
		st.image(img, width=700)
		pass

	elif choice == "Login":
		st.subheader("Login Section")
		

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				Menu = st.selectbox("Menu",["","Prediction(Data wise)","Prediction(Category wise)","About"])
				if Menu == "Prediction(Data wise)":
					run_prediction()
					

				elif Menu == "Prediction(Category wise)":
					run_ml()
				elif Menu=="About":
					st.subheader("About")
					st.info("Built with Streamlit")
					st.text("By")
					st.text("Prabha Adsul")
					st.text("Pranita Dharmadhikari")
					st.text("Aditi Gawande")


				elif Menu == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")




 

if __name__ == '__main__':
	main()