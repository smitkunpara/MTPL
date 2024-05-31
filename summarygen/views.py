from email.message import EmailMessage
from django.shortcuts import render
import pandas as pd
import smtplib
import environ
import io
env = environ.Env()

def gensummary(file):
    try:
        if file.name.endswith('.csv'):
            try:
                data = pd.read_csv(file, encoding='utf-8')
            except UnicodeDecodeError:
                data = pd.read_csv(file, encoding='ISO-8859-1')
        elif file.name.endswith('.xlsx'):
            data = pd.read_excel(file)
        else:
            print("Unsupported file format")
            return None
        new_data = data.groupby(['Cust State','DPD']).size().reset_index(name='count')
        print("new data:",new_data)
        return new_data
    except Exception as e:
        print("Error:",e)
        return None

def home(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            summary = gensummary(file)
            if summary is None:
                return render(request, 'home.html', {'message': 'Error in processing the file please check the file and try again', 'state': 'error'})
            email = request.POST.get('email')
            mailinfo = sendmail(email,summary)
            return render(request, 'home.html', mailinfo)
        else:
            return render(request, 'home.html')
    return render(request, 'home.html')

def sendmail(email, data):
    print("envemail:", env("EMAIL"))
    print("envpassword:", env("PASSWORD"))
    try:
        msg = EmailMessage()
        msg.set_content('Summary of the data')
        msg['Subject'] = 'Summary of the data'
        msg['To'] = email
        with io.BytesIO() as buffer:
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                data.to_excel(writer, index=False)
            file_data = buffer.getvalue()
        msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename='summary.xlsx')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(env("EMAIL"), env("PASSWORD"))
            smtp.send_message(msg)
            smtp.quit()
        return {"message": "Please check your email for the summary of the data", 'state': 'success'}
    except Exception as e:
        print("Error:", e)
        return {'message': "Error in sending the email", 'state': 'error'}