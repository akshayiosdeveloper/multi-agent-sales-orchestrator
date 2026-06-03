from app.simple_agent import Agent


instructions1 = """
You are a sales agent working for ComplAI.
You write professional, serious cold emails.
"""

instructions2 = """
You are a humorous, engaging sales agent.
You write witty, engaging cold emails.
"""

instructions3 = """
You are a busy sales agent.
You write concise, to the point cold emails.
"""

sales_agent1 = Agent(
    name="Professional Sales Agent",
    instructions=instructions1,
    model="llama3.1:8b-instruct-q4_K_M"
)

sales_agent2 = Agent(
    name="Engaging Sales Agent",
    instructions=instructions2,
    model="llama3.1:8b-instruct-q4_K_M"
)

sales_agent3 = Agent(
    name="Busy Sales Agent",
    instructions=instructions3,
    model="llama3.1:8b-instruct-q4_K_M"
)

sales_manager_agent = Agent(
    name="Sales Manager",
    instructions="""
You are a Sales Manager.

You will receive 3 cold sales emails.

Evaluate them carefully.

Select the single best email based on:
- professionalism
- persuasiveness
- clarity
- likelihood of getting a response

Return ONLY the winning email.

Do not explain your reasoning.
""",
    model="llama3.1:8b-instruct-q4_K_M"
)
