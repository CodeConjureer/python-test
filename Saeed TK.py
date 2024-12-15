from tkinter import *
from tkinter.colorchooser import *
from tkinter import messagebox
from datetime import datetime
import time

person1=[]
person2=[]


def open_page1():
  
  page1 =Toplevel()
  page1.title     ("Person1")
  page1.geometry  ("800x790",)
  page1.resizable (False,False)
  page1.configure (background="gray")

  frame = LabelFrame(page1,
                          font=("Arial",15,),
                          bg='gray',
                          fg='black',
                          bd=5,
                          relief="groove")
  
  
  frame.place(x=35,y=30, width=730, height=730)

                  
                  
                   
  
  #lable

                                    
  
  
  first_name=Label(frame,text="First Name",font=("Arial",15),bg="gray")
  first_name.grid(row=0,column=0,pady=20)
  first_name_entry = Entry(frame,font=("Arial",15))
  first_name_entry.grid(row=0,column=2,pady=20)
  
  
  last_name=Label(frame,text="Last Name",font=("Arial",15),bg="gray")
  last_name.grid(row=1,column=0,pady=20)
  last_name_entry = Entry(frame,font=("Arial",15))
  last_name_entry.grid(row=1,column=2,pady=20)
  
  
  age=Label(frame,text="Age",font=("Arial",15),bg="gray")
  age.grid(row=2,column=0,pady=20)
  age_entry = Entry(frame,font=("Arial",15))
  age_entry.grid(row=2,column=2,pady=20)
  
  
  gender=Label(frame,text="Gender",font=("Arial",15),bg="gray")
  gender.grid(row=3,column=0)
  gender_var = StringVar(frame)
  gender1_button= Radiobutton(frame,bg="gray",text="Male",font=("Arial",15),variable=gender_var,value="yes")
  gender1_button.grid(row=3,column=1)
  gender2_button = Radiobutton(frame,bg="gray",text="Female",font=("Arial",15),variable=gender_var,value="no")
  gender2_button.grid(row=3,column=2)


  car=Label(frame,text="Car",font=("Arial",15),bg="gray")
  car.place(x=30,y=260)
  car_var = StringVar(frame)
  car1=Checkbutton(frame,text="i have a car",font=("Arial",15),bg="Gray")
  car1.place(x=100,y=265)
  car2=Checkbutton(frame,text="i dont have car ",font=("Arial",15),bg="Gray")
  car2.place(x=250,y=265)


  
  
  state=Label(frame,text="State",font=("Arial",15),bg="gray")
  state.grid(row=5,column=0,padx=20,pady=30)
  state_var = StringVar(frame)
  state_options = ["Fars","Tehran","Sistan","Balooch","Kerman","Khoozestan"]
  state_menue = OptionMenu(frame,state_var,*state_options)
  state_menue.grid(row=6,column=0)
  state_menue.configure(font=("Arial",10),bg="gray")

  language=Label(frame,text="language",font=("Arial",15),bg="gray")
  language.grid(row=5,column=1,padx=20,pady=30)
  language_var = StringVar(frame)

  language_options = ["Person","English","Chinees","German","French","African","Other"]
  language_menue = OptionMenu(frame,language_var,*language_options)
  language_menue.grid(row=6,column=1)
  language_menue.configure(font=("Arial",10),bg="gray")
  
  city=Label(frame,text="city",font=("Arial",15),bg="gray")
  city.grid(row=5,column=2,padx=20,pady=30)
  city_var = StringVar(frame)
  city_options = ["Shiraz","Esfahan","Tehran","qom","Kerman","Ahvaz","Bushehr","Mashhad","Tabriz","Other"]
  city_menue = OptionMenu(frame,city_var,*city_options)
  city_menue.grid(row=6,column=2)
  city_menue.configure(font=("Arial",10),bg="gray")
  
  color=Label(frame,text="color",font=("Arial",15),bg="gray")
  color.grid(row=5,column=3,padx=20,pady=30)
  color_var = StringVar(frame)
  color_options = ["Red","Blue","Brown","Yellow","Black","White","Pink","Green","other"]
  color_menue = OptionMenu(frame,color_var,*color_options)
  color_menue.grid(row=6,column=3)
  color_menue.configure(font=("Arial",10),bg="gray")
  
  height=Label(frame,text="height",font=("Arial",15),bg="gray")
  height.grid(row=7,column=0,padx=20,pady=30)
  #spinbox
  height_spinbox = Spinbox(frame, from_=0,to=10000,increment=0.5,font=("Arial",15),width=5,bg="gray")
  height_spinbox.grid(row=8,column=0)
  
  
  job=Label(frame,text="job",font=("Arial",15),bg="gray")
  job.grid(row=7,column=1,padx=20,pady=30)
  job_var = StringVar(frame)
  job_options = ["programmer","Doctor","Engineer","Lawer","Other"]
  job_menue = OptionMenu(frame,job_var,*job_options)
  job_menue.grid(row=8,column=1)
  job_menue.configure(font=("Arial",10),bg="gray")

  Skin=Label(frame,text="Skin Color",font=("Arial",15),bg="gray")
  Skin.grid(row=7,column=2,padx=20,pady=30)
  Skin_var = StringVar(frame)
  Skin_options = ["Wite", "Black", "Brown", "Yellow", "Red", "Other"]
  Skin_menue = OptionMenu(frame,Skin_var,*Skin_options)
  Skin_menue.grid(row=8,column=2)
  Skin_menue.configure(font=("Arial",10),bg="gray")

  food=Label(frame,text="food",font=("Arial",15),bg="gray")
  food.grid(row=7,column=3,padx=20,pady=30)
  food_var = StringVar(frame)
  food_options = ["Pizza","Burger","Rice","Bread","Hot Dog","Pasta","Other"]
  food_menue = OptionMenu(frame,food_var,*food_options)
  food_menue.grid(row=8,column=3)
  food_menue.configure(font=("Arial",10),bg="gray")
  
  activity=Label(frame,text="activity",font=("Arial",15),bg="gray")
  activity.grid(row=9,column=0,padx=20,pady=30)
  activity_var = StringVar(frame)
  activity_options = ["Watching TV","Playing games","Exercising","Cooking","Shopping","Working","Studying","Sleeping","Other"]
  activity_menue = OptionMenu(frame,activity_var,*activity_options)
  activity_menue.grid(row=10,column=0)
  activity_menue.configure(font=("Arial",10),bg="gray")
  
  weather=Label(frame,text="weather",font=("Arial",15),bg="gray")
  weather.grid(row=9,column=1,padx=20,pady=30)
  weather_var = StringVar(frame)
  
  weather_options = ["sunny","cloudy","rainy","snowy","windy","foggy","stormy","other"]
  weather_menue = OptionMenu(frame,weather_var,*weather_options)
  weather_menue.grid(row=10,column=1)
  weather_menue.configure(font=("Arial",10),bg="gray")
  
  commitment=Label(frame,text="commitment",font=("Arial",15),bg="gray")
  commitment.grid(row=9,column=2,padx=20,pady=30)
  commitment_var = StringVar(frame)
    
  commitment_options = ["Engaged","Single"]
  commitment_menue = OptionMenu(frame,commitment_var,*commitment_options)
  commitment_menue.grid(row=10,column=2)
  commitment_menue.configure(font=("Arial",10),bg="gray")
    
  income=Label(frame,text="income",font=("Arial",15),bg="gray")
  income.grid(row=9,column=3,padx=20,pady=30)
  income_var = StringVar(frame)
  income_options = ["Low","High"]
  income_menue = OptionMenu(frame,income_var,*income_options)
  income_menue.grid(row=10,column=3)
  income_menue.configure(font=("Arial",10),bg="gray")
  

  
  def save_and_close():
    person1.append(first_name_entry.get())
    person1.append(last_name_entry.get())
    person1.append(age_entry.get())
    person1.append(gender_var .get())
    person1.append(  car_var .get())
    person1.append(state_var.get())
    person1.append(language_var.get())
    person1.append(city_var.get())
    person1.append(color_var.get())
    person1.append(height_spinbox .get())
    person1.append(job_var.get())
    person1.append( Skin_var .get())
    person1.append( food_var .get())
    person1.append(activity_var.get())
    person1.append(commitment_var.get())
    person1.append(income_var.get())
    person1.append(weather_var.get())
    
    print(person1)
    return person1

  save_button = Button(frame,bg="teal",activebackground="black",text="Save",font=("Arial",15)
                       ,relief="groove",command=save_and_close)
  save_button.grid(row=4,column=3,)

def open_page2():
  
  
  
  page2 =Toplevel()
  page2.title     ("Person1")
  page2.geometry  ("800x790",)
  page2.resizable (False,False)
  page2.configure (background="gray")

  frame = LabelFrame(page2,
                          font=("Arial",15,),
                          bg='gray',
                          fg='black',
                          bd=5,
                          relief="groove")
  
  
  frame.place(x=35,y=30, width=730, height=730)
  #lable 
  first_name=Label(frame,text="First Name",font=("Arial",15),bg="gray")
  first_name.grid(row=0,column=0,pady=20)
  first_name_entry = Entry(frame,font=("Arial",15))
  first_name_entry.grid(row=0,column=2,pady=20)
  
  
  last_name=Label(frame,text="Last Name",font=("Arial",15),bg="gray")
  last_name.grid(row=1,column=0,pady=20)
  last_name_entry = Entry(frame,font=("Arial",15))
  last_name_entry.grid(row=1,column=2,pady=20)
  
  
  age=Label(frame,text="Age",font=("Arial",15),bg="gray")
  age.grid(row=2,column=0,pady=20)
  age_entry = Entry(frame,font=("Arial",15))
  age_entry.grid(row=2,column=2,pady=20)
  
  
  gender=Label(frame,text="Gender",font=("Arial",15),bg="gray")
  gender.grid(row=3,column=0)
  gender_var = StringVar(frame)

  #radiobutton
  gender1_button= Radiobutton(frame,bg="gray",text="Male",font=("Arial",15),variable=gender_var,value="yes")
  gender1_button.grid(row=3,column=1)
  gender2_button = Radiobutton(frame,bg="gray",text="Female",font=("Arial",15),variable=gender_var,value="no")
  gender2_button.grid(row=3,column=2)


  car=Label(frame,text="Car",font=("Arial",15),bg="gray")
  car.place(x=30,y=265)
  car_var = StringVar(frame)
  car1=Checkbutton(frame,text="i have a car",font=("Arial",15),bg="Gray")
  car1.place(x=100,y=265)
  car2=Checkbutton(frame,text="i dont have car ",font=("Arial",15),bg="Gray")
  car2.place(x=250,y=265)

  
  
  
  state=Label(frame,text="State",font=("Arial",15),bg="gray")
  state.grid(row=5,column=0,padx=20,pady=30)
  state_var = StringVar(frame)
 
  state_options = ["Fars","Tehran","Sistan","Balooch","Kerman","Khoozestan"]
  state_menue = OptionMenu(frame,state_var,*state_options)
  state_menue.grid(row=6,column=0)
  state_menue.configure(font=("Arial",10),bg="gray")

  language=Label(frame,text="language",font=("Arial",15),bg="gray")
  language.grid(row=5,column=1,padx=20,pady=30)
  language_var = StringVar(frame)

  language_options = ["Person","English","Chinees","German","French","African","Other"]
  language_menue = OptionMenu(frame,language_var,*language_options)
  language_menue.grid(row=6,column=1)
  language_menue.configure(font=("Arial",10),bg="gray")
  
  city=Label(frame,text="city",font=("Arial",15),bg="gray")
  city.grid(row=5,column=2,padx=20,pady=30)
  city_var = StringVar(frame)
  city_options = ["Shiraz","Esfahan","Tehran","qom","Kerman","Ahvaz","Bushehr","Mashhad","Tabriz","Other"]
  city_menue = OptionMenu(frame,city_var,*city_options)
  city_menue.grid(row=6,column=2)
  city_menue.configure(font=("Arial",10),bg="gray")
  
  color=Label(frame,text="color",font=("Arial",15),bg="gray")
  color.grid(row=5,column=3,padx=20,pady=30)
  color_var = StringVar(frame)

  color_options = ["Red","Blue","Brown","Yellow","Black","White","Pink","Green","other"]
  color_menue = OptionMenu(frame,color_var,*color_options)
  color_menue.grid(row=6,column=3)
  color_menue.configure(font=("Arial",10),bg="gray")
  
  height=Label(frame,text="height",font=("Arial",15),bg="gray")
  height.grid(row=7,column=0,padx=20,pady=30)
  height_spinbox = Spinbox(frame, from_=0,to=10000,increment=0.5,font=("Arial",15),width=5,bg="gray")
  height_spinbox.grid(row=8,column=0)
  
  
  job=Label(frame,text="job",font=("Arial",15),bg="gray")
  job.grid(row=7,column=1,padx=20,pady=30)
  job_var = StringVar(frame)

  job_options = ["programmer","Doctor","Engineer","Lawer","Other"]
  job_menue = OptionMenu(frame,job_var,*job_options)
  job_menue.grid(row=8,column=1)
  job_menue.configure(font=("Arial",10),bg="gray")

  Skin=Label(frame,text="Skin Color",font=("Arial",15),bg="gray")
  Skin.grid(row=7,column=2,padx=20,pady=30)
  Skin_var = StringVar(frame)

  Skin_options = ["Wite", "Black", "Brown", "Yellow", "Red", "Other"]
  Skin_menue = OptionMenu(frame,Skin_var,*Skin_options)
  Skin_menue.grid(row=8,column=2)
  Skin_menue.configure(font=("Arial",10),bg="gray")

  food=Label(frame,text="food",font=("Arial",15),bg="gray")
  food.grid(row=7,column=3,padx=20,pady=30)
  food_var = StringVar(frame)

  food_options = ["Pizza","Burger","Rice","Bread","Hot Dog","Pasta","Other"]
  food_menue = OptionMenu(frame,food_var,*food_options)
  food_menue.grid(row=8,column=3)
  food_menue.configure(font=("Arial",10),bg="gray")
  
  activity=Label(frame,text="activity",font=("Arial",15),bg="gray")
  activity.grid(row=9,column=0,padx=20,pady=30)
  activity_var = StringVar(frame)

  activity_options = ["Watching TV","Playing games","Exercising","Cooking","Shopping","Working","Studying","Sleeping","Other"]
  activity_menue = OptionMenu(frame,activity_var,*activity_options)
  activity_menue.grid(row=10,column=0)
  activity_menue.configure(font=("Arial",10),bg="gray")
  weather=Label(frame,text="weather",font=("Arial",15),bg="gray")
  weather.grid(row=9,column=1,padx=20,pady=30)
  weather_var = StringVar(frame)
  weather_options = ["sunny","cloudy","rainy","snowy","windy","foggy","stormy","other"]
  weather_menue = OptionMenu(frame,weather_var,*weather_options)
  weather_menue.grid(row=10,column=1)
  weather_menue.configure(font=("Arial",10),bg="gray")
  
  commitment=Label(frame,text="commitment",font=("Arial",15),bg="gray")
  commitment.grid(row=9,column=2,padx=20,pady=30)
  commitment_var = StringVar(frame)
  commitment_options = ["Engaged","Single"]
  commitment_menue = OptionMenu(frame,commitment_var,*commitment_options)
  commitment_menue.grid(row=10,column=2)
  commitment_menue.configure(font=("Arial",10),bg="gray")
    
  income=Label(frame,text="income",font=("Arial",15),bg="gray")
  income.grid(row=9,column=3,padx=20,pady=30)
  income_var = StringVar(frame)
  income_options = ["Low","High"]
  income_menue = OptionMenu(frame,income_var,*income_options)
  income_menue.grid(row=10,column=3)
  income_menue.configure(font=("Arial",10),bg="gray")
  
  
  def save_and_close():
    person2.append(first_name_entry.get())
    person2.append(last_name_entry.get())
    person2.append(age_entry.get())
    person2.append(gender_var .get())
    person2.append(  car_var .get())
    person2.append(state_var.get())
    person2.append(language_var.get())
    person2.append(city_var.get())
    person2.append(color_var.get())
    person2.append(height_spinbox .get())
    person2.append(job_var.get())
    person2.append( Skin_var .get())
    person2.append( food_var .get())
    person2.append(activity_var.get())
    person2.append(commitment_var.get())
    person2.append(income_var.get())
    person2.append(weather_var.get())
    
    print(person2)
    return person2
        

  save_button = Button(frame,bg="teal",activebackground="black",text="Save",font=("Arial",15)
                       ,relief="groove",command=save_and_close)
  save_button.grid(row=4,column=3)
  
def compare(person1, person2):
    person1_filtered = list(filter(lambda x: x and x != 0, person1))
    person2_filtered = list(filter(lambda x: x and x != 0, person2))

    common_features = sum(p1 == p2 for p1, p2 in zip(person1_filtered, person2_filtered))
    total_features = max(len(person1_filtered), len(person2_filtered))

    similarity_score = round(common_features / total_features * 100, 2)

    return similarity_score

def Result():
    new_window = Toplevel(window)
    new_window.title("Ranks")
    new_window.geometry("300x300")
    new_window.resizable(False, False)
    new_window.configure(background="Gray")  
    score = compare(person1,person2)
    re = Label(new_window, bg="gray", fg="black", font=("Arial", 15), relief="sunken", text=f"Score: {score}%")
    re.pack(side="top")
    

    
    if score >= 80:
        messagebox.showinfo("Ranking", "The users have a high  Rak")
    elif score >= 60:
        messagebox.showinfo("Ranking", "The users have a moderate rank.")
    else:
        messagebox.showinfo("Ranking", "The users have a low rank.")


# def update_time(window):
#     current_time = time.strftime("%H:%M:%S")
#     time_label.config(text=current_time)
#     window.after(1000, update_time)  # Update every 1 second
#     time_label = Button(window,  text="time",font=("Helvetica", 24),command=update_time)
#     time_label.place(x=200,y=100)





def window_close_message_box():
  if (messagebox.askyesno("Quit","Do you want to quit?")):
    window.destroy()

def color_chooser(window): 
  color=askcolor()
  window.configure(bg=color[1])


window=Tk()
window.protocol   ("WM_DELETE_WINDOW",window_close_message_box)
window.geometry   ("780x640")
window.title      ("Friend Ranking")
window.resizable  (False,False)
window.configure  (bg="gray")


color_button=Button(window,
                    text="Color Chooser",
                    command=lambda: color_chooser(window),
                    bg="gray",
                    relief="groove",
                    bd=5,
                    font=("Arail",20,),
                    activebackground="black",
                    activeforeground="gold")
color_button.pack(padx=12,
                  pady=150)


control_panel = LabelFrame(window,
                          text="Control Panel",
                          font=("Arail",18,),
                          bg="gray",
                          fg="black",
                          relief="groove",
                          bd=7)
control_panel.place(x=90,
                    y=400,
                    width=600,
                    height=175 )


button1=Button(control_panel,
               text="Person 1",
               font=("Arial",18,),
               bg='teal',
               fg='black',
               command=open_page1)
button1.pack(side="left",
             padx=70,
             pady=20)

button2=Button(control_panel,
               text="Person 2",
               font=("Arial",18),
               bg="teal",
               fg='black',
               command=open_page2)
button2.pack(side="right",
             padx=70,
             pady=20)

button3 = Button(control_panel,
                 text="Rank",
                 font=("Arial",18,),
                 bg="teal",
                 fg="black",
                command=Result)
button3.place(anchor="center",relx=0.5,rely=0.5,width=100,height=60)












window.mainloop()