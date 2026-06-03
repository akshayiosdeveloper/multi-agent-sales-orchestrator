from app.tools import (
    professional_email_tool,
    engaging_email_tool,
    concise_email_tool,
    send_email
)
from app.agents import sales_manager_agent


class SalesManager:

    def run(self, message):

        print("\n=== Generating Professional Draft ===")
        draft1 = professional_email_tool(message)
        print(draft1[:500])

        print("\n=== Generating Engaging Draft ===")
        draft2 = engaging_email_tool(message)
        print(draft2[:500])

        print("\n=== Generating Concise Draft ===")
        draft3 = concise_email_tool(message)
        print(draft3[:500])

        evaluation_prompt = f"""
        EMAIL 1
        {draft1}

        EMAIL 2
        {draft2}

        EMAIL 3
        {draft3}

        Choose the single best email.

        Return only the winning email.
        """

        best_draft = sales_manager_agent.run(evaluation_prompt)
        print("\n=== RAW MANAGER RESPONSE ===\n")
        print(best_draft)
        print("\n=== AI SELECTED EMAIL ===\n")
        print(best_draft[:500])

        send_email(best_draft)

        return best_draft
