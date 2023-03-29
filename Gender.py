from tkinter import *

# tkinter message box t odisplay errors
from tkinter.messagebox import showerror

# the requests will be used for making requests to the API
import requests, json

def predict_gender():
    # executes when code has no errors
    try:
        # getting the input from entry
        entered_name = name_entry.get()
        entered_country=country_entry.get()
        # making a request to the API, the user's entered name is injected in the url
        response = requests.get(f'https://api.genderize.io/?name={entered_name}&country_id={entered_country}').json()
        # getting name from the response
        name = response['name']
        # getting gender from the response  
        gender = response['gender']
        # getting probability from the response 
        probability = 100 * response['probability']
        # adding name to the label that was empty, the name is being uppercased
        name_label.config(text='The Name is ' + name.upper())
        # adding gender to the label that was empty, the gender is being uppercased  
        gender_label.config(text='The Gender is ' + gender.upper())
        # adding probability to the label that was empty
        probability_label.config(text='I Am ' + str(probability) + '%' + ' accurate')
    # executes when errors are caught
    # KeyError, ConnectionTimeoutError   
    except:
        showerror(title='error', message='An error occurred!! Make sure you have internet connection or you have entered the correct data')


#colors for the Application
gold = '#ffffff'
brown = '#000000'



#creating the main window
window = Tk()
window.geometry('425x500+350+150') #350+200 center the window

window.title("Gender Game")

#make the window unresizable
#window.resizable(height=FALSE, width=FALSE)  

#now inside the window, create two frames, the top frame and the bottom frame.
top_frame = Frame(window, bg="#e6ecff", width=430, height=90)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(window, bg="#0040ff", width=430, height=450)
bottom_frame.grid(row=1, column=0)

#inside top frame, create two labels
first_label = Label(top_frame, text="Gender Game", bg="#e6ecff", fg="#000000", pady=25, padx=70, justify=CENTER, font=('Poppins 22 bold'))
first_label.grid(row=0, column=0)

second_label = Label(top_frame, text='Give me any name and i will predict its Gender', bg="#e6ecff", fg="#000000", font=('Poppins 13 bold'))
second_label.grid(row=1, column=0)

#widgets inside the bottom_frame
#the name label
label = Label(bottom_frame, bg="#0040ff", fg="#ffffff", text="Name: ", font=('Poppins 16 bold'), justify=LEFT)
label.place(x=14, y=10)

#input field for name label
name_entry = Entry(bottom_frame, bg="#ccd9ff", fg="#000000", width=24, font=("verdana 17 bold"))
name_entry.place(x=14, y=40)
name_entry.focus_set()

#the country label
label2 = Label(bottom_frame, bg="#0040ff", fg="#ffffff", text="Country: ", font=('Poppins 15 bold'), justify=LEFT)
label2.place(x=14, y=90)

#country field for name label
country_entry = Entry(bottom_frame, bg="#ccd9ff", fg="#000d33", width=24, font=("Georgia 17 bold"))
country_entry.place(x=14, y=120)


#Empty place for name label, to display name
name_label = Label(bottom_frame, text="", bg="#0040ff", font=('verdana 13 bold'), )
name_label.place(x=14, y=199)

#Empty gender name label, it will be used to display the name
gender_label = Label(bottom_frame, text='', bg="#0040ff", font=('Poppins 12 bold'), )
gender_label.place(x=14, y=230)

# the empty probability label, it will be used to display the gender probalility
probability_label = Label(bottom_frame, text='', bg="#0040ff", font=('Poppins 12 bold'))
probability_label.place(x=14, y=260)



#the predict button
predict_button = Button(bottom_frame, width=20, height=2, text="PREDICT", bg="#000d33", fg="#ffffff", font=('Poppins 13 bold'), command=predict_gender)
predict_button.place(x=14,y=310)





window.mainloop()