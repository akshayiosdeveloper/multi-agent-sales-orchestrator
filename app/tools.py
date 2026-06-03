
from app.email_service import send_test_email
from app.agents import sales_agent1
from app.agents import sales_agent2
from app.agents import sales_agent3


def send_email(body: str):
    print("\n[TOOL] Sending email...\n")

    send_test_email(body)

    return {"status": "success"}


def professional_email_tool(message):
    print("[TOOL] Professional Agent")
    return sales_agent1.run(message)


def engaging_email_tool(message):
    print("[TOOL] Engaging Agent")
    return sales_agent2.run(message)


def concise_email_tool(message):
    print("[TOOL] Concise Agent")
    return sales_agent3.run(message)
