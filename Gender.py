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
        name_label.config(text='The name is ' + name.upper())
        # adding gender to the label that was empty, the gender is being uppercased  
        gender_label.config(text='The gender is ' + gender.upper())
        # adding probability to the label that was empty
        probability_label.config(text='Am ' + str(probability) + '%' + ' accurate')
    # executes when errors are caught
    # KeyError, ConnectionTimeoutError   
    except:
        showerror(title='error', message='An error occurred!! Make sure you have internet connection or you have entered the correct data')


#colors for the Application
gold = '#ffffff'
brown = '#000000'

#creating the main window
window = Tk()
window.geometry('325x300+500+200') #500+200 center the window

window.title("Gender Game")

#make the window unresizable
window.resizable(height=FALSE, width=FALSE)  

#now inside the window, create two frames, the top frame and the bottom frame.
top_frame = Frame(window, bg=brown, width=325, height=80)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(window, bg="#000080", width=300, height=250)
bottom_frame.grid(row=1, column=0)

#inside top frame, create two labels
first_label = Label(top_frame, text="Gender Game", bg=brown, fg=gold, pady=10, padx=20, justify=CENTER, font=('Poppins 20 bold'))
first_label.grid(row=0, column=0)

second_label = Label(top_frame, text='Give me any name and i will predict its gender', bg=brown, fg=gold, font=('Poppins 10'))
second_label.grid(row=1, column=0)

#widgets inside the bottom_frame
#the name label
label = Label(bottom_frame, text="Name: ", font=('Poppins 10 bold'), justify=LEFT)
label.place(x=4, y=5)

#input field for name label
name_entry = Entry(bottom_frame, width=25, font=("Poppins 15 bold"))
name_entry.place(x=4, y=30)


#Empty place for name label, to display name
name_label = Label(bottom_frame, text="",bg="#000080")
name_label.place(x=5, y=70)

#Empty gender name label, it will be used to display the name
gender_label = Label(bottom_frame, text='',bg="#000080", font=('Poppins 10 bold'))
gender_label.place(x=5, y=90)

# the empty probability label, it will be used to display the gender probalility
probability_label = Label(bottom_frame, text='', bg="#000080", font=('Poppins 10 bold'))
probability_label.place(x=5, y=110)



#the predict button
predict_button = Button(bottom_frame, text="PREDICT", bg=gold, fg=brown, font=('Poppins 10 bold'), command=predict_gender)
predict_button.place(x=10,y=140)

#the country label
label2 = Label(bottom_frame, text="Country: ", font=('Poppins 10 bold'), justify=LEFT)
label2.place(x=4, y=170)

#country field for name label
country_entry = Entry(bottom_frame, width=25, font=("Poppins 15 bold"))
country_entry.place(x=4, y=190)



window.mainloop()