import tkinter as tk
import tkinter.ttk as ttk
from datetime import date,datetime,time,timedelta
import calendar

#these are zodiac features
zodiacsd = {

         "Aries" : "  Unpredictable, Stubborn, Destructive, Immature",
         "Taurus" : "  Shy, Lazy, Irrational, Materialistic",
         "Gemini" : "  Manipulative, Complicated, Materialistic, Duality",
         "Cancer" :  "  Clingy, Sensitive, Closed-off, Emotional",
         "Leo" : "  Arrogant, Sensitive, Impatient, Easily Angered",
         "Virgo" : "  Judgmental, Controlling, Skeptical,Critical" ,
         "Libra" : "  Dramatic, Unreliable,Two-Faced, Unpredictable",
         "Scorpio" : "  Jealous, Malicious, Argumentative, Domineering",
         "Saggittarius" : "  Impatient, Unpredictibale, Factles, Know it all" ,
         "Capricorn" : "  Arrogant, Selfish, Stubborn, Materialistic",
         "Aquarius": "  Stubborn, Rebelious, Impulsive, Cold",
         "Pisces" : "  Timid, Codependent, Gullible, Laziness"

}


#create window
window = tk.Tk()
window.title("Know your Stars")
window.geometry("450x300")

frameInput = tk.LabelFrame(master = window, height = 100)
frameInput['bg'] = '#FFAEC9'
frameInput.pack( fill = tk.BOTH)

frameOutput = tk.LabelFrame(master = window, height = 350)
frameOutput['bg'] = '#99D9EA'
frameOutput.pack(fill = tk.BOTH)

#create widgets
lbl1 = tk.Label(master = frameInput, text = 'Enter your DOB:', bg = '#FFAEC9', font = 'Times')

ent_day = tk.Entry(master= frameOutput, width = 20)
ent_age = tk.Entry(master = frameOutput, width = 20)
ent_zodiac = tk.Entry(master = frameOutput, width = 20)

ent_char = tk.Entry(master = frameOutput, width = 48)

ent_day['state'] = 'disabled'
ent_age['state'] = 'disabled'
ent_zodiac['state'] = 'disabled'
ent_char['state'] = 'disabled'


ent_day.place(x = 230, y = 11)
ent_age.place(x = 230, y = 41)
ent_zodiac.place(x = 230, y = 71)
ent_char.place(x = 90, y = 110)


#Place your widgets
lbl1.place(x = 10, y = 30)
dates = [1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21,22,23,24,25,26,27,28,29,30,31]
current = tk.StringVar()
current.set('DD')

dateInput = ttk.Combobox(master=frameInput,values=dates, state='readonly', width = 4, textvariable = current)
dateInput.place(x = 160, y = 32)
date1= current.get()

months= ['January', 'February', 'March', 'April', 'May', 'June', 'July' , 'August', 'September', 'October', 'November', 'December']

currentm = tk.StringVar()
currentm.set('Month')

monthInput = ttk.Combobox(master=frameInput,values=months, state='readonly', width =10, textvariable = currentm)
monthInput.place(x = 210, y = 32)

year= tk.Entry(master = frameInput, text = 'YY', width = 8)

year.place(x= 295, y = 32)

def show():
    result = year.get()
    global yob
    yob = result

    print(dob, mob, yob)
    return yob, mob, dob
bttn_dob = tk.Button(master= frameInput, text= 'Confirm', command = show)
bttn_dob.place(x =380,y=32)

def selectiondate(x):
    global dob
    dob = current.get()
    return dob
dateInput.bind('<<ComboboxSelected>>', selectiondate)

def selectionmonth(x):
    global mob
    mob = currentm.get()
    return mob
monthInput.bind('<<ComboboxSelected>>', selectionmonth)

def dayOfBirth():
    k = (months.index(mob)) + 1
    day = calendar.weekday(int(yob), k, int(dob))
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Day of birth: ', week[day])
    txt =  week[day]
    ent_day['state'] = 'normal'
    ent_day.delete(0, tk.END)
    ent_day.insert(5, txt)
    #ent_day['state'] = 'disabled'

bttn_day = tk.Button(master= frameOutput, text= 'Day of Birth: ', command = dayOfBirth, width = 12, bg = 'yellow')
bttn_day.place(x= 110, y = 10)

def presentAge():
    k = (months.index(mob)) + 1
    dt = datetime.now()
    dt2 = datetime(int(yob), k, int(dob), 0, 0)
    delta = dt - dt2
    y = (int(delta.days) // 365)
    #m = (abs((dt2.month - k))) + 1
    #leap = 0
    #for i in range(int(yob), date.today().year):
    #    if i%4 == 0:
    #        leap+= 1
    #print(leap)
    #str(m) + " months " + str(d) + " days "
    #d = (int(delta.days) % 365) - leap
    print("Present Age is "+ str(y) + " years " )
    txt = "Present Age is "+ str(y) + " years "
    ent_age['state'] = 'normal'
    ent_age.delete(0, tk.END)
    ent_age.insert(5, txt)
    #ent_age['state'] = 'disabled'

age_bttn = tk.Button(master= frameOutput, text= 'Current Age: ', command = presentAge, width = 12, bg = 'yellow')
age_bttn.place(x= 110, y = 40)


def zodiac():
    if mob == "January":
        if 20<=int(dob)<=31:
            z = "Aquarius"
        elif 1<=int(dob)<=19:
            z = "Capricorn"

    elif mob == "February":
        if 1<=int(dob)<=18:
            z = "Aquarius"
        elif 19<=int(dob)<=29:
            z = "Pisces"

    elif mob == "March":
        if 1 <= int(dob) <= 20:
            z = "Pisces"
        elif 21 <= int(dob) <= 31:
            z = "Aries"

    elif mob == "April":
        if 1 <= int(dob) <= 19:
            z = "Aries"
        elif 20 <= int(dob) <= 30:
            z = "Taurus"

    elif mob == "May":
        if 1 <= int(dob) <= 20:
            z = "Taurus"
        elif 21 <= int(dob) <= 31:
            z = "Gemini"

    elif mob == "June":
        if 1 <= int(dob) <= 20:
            z = "Gemini"
        elif 21 <= int(dob) <= 30:
            z = "Cancer"

    elif mob == "July":
        if 1 <= int(dob) <= 22:
            z = "Cancer"
        elif 23 <= int(dob) <= 31:
            z = "Leo"

    elif mob == "August":
        if 1 <= int(dob) <= 22:
            z = "Leo"
        elif 23 <= int(dob) <= 30:
            z = "Virgo"

    elif mob == "September":
        if 1 <= int(dob) <= 22:
            z = "Virgo"
        elif 23 <= int(dob) <= 31:
            z = "Libra"

    elif mob == "October":
        if 1 <= int(dob) <= 22:
            z = "Libra"
        elif 23 <= int(dob) <= 30:
            z = "Scorpio"

    elif mob == "November":
        if 1 <= int(dob) <= 21:
            z = "Scorpio"
        elif 22 <= int(dob) <= 31:
            z = "Sagittarius"

    elif mob == "December":
        if 1 <= int(dob) <= 21:
            z = "Sagittarius"
        elif 22 <= int(dob) <= 30:
            z = "Capricorn"

    print(z)
    print(zodiacsd.get(z))

    txt =  z
    ent_zodiac['state'] = 'normal'
    ent_zodiac.delete(0, tk.END)
    ent_zodiac.insert(5, txt)
    #ent_zodiac['state'] = 'disabled'

    txt2 = zodiacsd.get(z)
    ent_char['state'] = 'normal'
    ent_char.delete(0, tk.END)
    ent_char.insert(5, txt2)
    #ent_char['state'] = 'disabled'

zod_bttn = tk.Button(master= frameOutput, text= 'Your Zodiac: ', command = zodiac, width = 12, bg = 'yellow')
zod_bttn.place(x= 110, y = 70)
window.mainloop()
