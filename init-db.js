db = db.getSiblingDB("form_db");
db.form_tb.drop();

db.form_tb.insertMany([
    {
        "name": "MyForm1",
        "main_email": "email",
        "main_phone": "phone"
    },
    {
        "name": "MyForm2",
        "expiration_date": "date",
        "manager_name": "text"
    },
    {
        "name": "OrderForm1",
        "work_email": "email",
        "description": "text",
        "work_phone": "phone"
    },
    {
        "name": "SurveyForm",
        "user_name": "text",
        "phone_number": "phone"
    },
    {
        "name": "ContactForm",
        "work_email": "email",
        "main_phone": "phone",
        "first_name": "text"
    },
    {
        "name": "FeedbackForm",
        "reg_email": "email",
        "date_of_birth": "date",
        "password": "text"
    },
    {
        "name": "RegistrationForm",
        "reg_email": "email",
        "first_name": "text",
        "last_name": "text"
    },
    {
        "name": "InquiryForm",
        "work_phone": "phone",
        "last_name": "text"
    },
    {
        "name": "JobApplicationForm",
        "field_name_1": "email",
        "field_name_2": "text",
        "field_name_3": "date"
    },
    {
        "name": "SurveyForm2",
        "employee_name": "text",
        "date_of_birth": "date",
        "contact_phone": "phone"
    }
]);