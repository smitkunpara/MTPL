# File Processing and Emailing Summary

This project is a Django web application that allows users to upload a CSV or Excel file. The application processes the file to generate a summary and then sends that summary to a specified email address.

## Approach

1. **File Upload**: The user uploads a CSV or Excel file through the web interface. The file is then sent to the server as part of a POST request.

2. **Data Processing**: The server reads the file into a pandas DataFrame. It then groups the data by 'Cust State' and 'DPD' columns and counts the number of occurrences to generate a summary.

3. **Emailing Summary**: The server gets the email address from the request. It then creates an email with the subject 'Summary of the data' and the DataFrame attached as an Excel file. The email is sent to the specified address using SMTP.

## Libraries Used

- Django: For the web framework.
- pandas: For data processing.
- smtplib: For sending emails.
- io and email.message.EmailMessage: For creating the email with the attached file.
- environ: To get environment variables.