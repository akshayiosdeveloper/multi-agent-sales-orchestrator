import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from app.config import SENDGRID_API_KEY


def send_test_email(body):
    if not SENDGRID_API_KEY:
        raise ValueError("SENDGRID_API_KEY not found in environment variables")

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    from_email = Email("akshay_099@outlook.com")
    to_email = To("akshay.iosdeveloper@gmail.com")

    content = Content("text/plain", body)

    mail = Mail(from_email, to_email,
                "Test Email from AI Agent", content).get()

    response = sg.client.mail.send.post(request_body=mail)

    print("Status Code:", response.status_code)
