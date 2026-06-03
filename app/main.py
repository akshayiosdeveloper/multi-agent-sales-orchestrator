from app.sales_manager import SalesManager

from app.tools import send_email
from app.email_service import send_test_email
import certifi
import os
import ollama
os.environ['SSL_CERT_FILE'] = certifi.where()


def main():

    manager = SalesManager()

    message = "Write a cold sales email addressed to Dear CEO"

    manager.run(message)


if __name__ == "__main__":
    main()


# async def run_async(agent, message):
#     print(f"Starting agent: {agent.name}")
#     loop = asyncio.get_event_loop()
#     print(f"Finished agent: {agent.name}")
#     return await loop.run_in_executor(None, agent.run, message)


# # main async function
# async def main():
#     message = "Write a cold sales email"

#     results = await asyncio.gather(
#         run_async(sales_agent1, message),
#         run_async(sales_agent2, message),
#         run_async(sales_agent3, message),
#     )

#     for output in results:
#         print("\n\n", output)

# if __name__ == "__main__":
#     asyncio.run(main())
# if __name__ == "__main__":
#     user_input = "Sell an AI compliance tool to a startup founder"

#     print("\n--- Streaming Output ---\n")

#     for token in sales_agent1.run_streamed("Write a cold sales email"):
#         print(token, end="", flush=True)
# print("\n--- Professional ---\n")
# print(sales_agent1.run(user_input))

# print("\n--- Engaging ---\n")
# print(sales_agent2.run(user_input))

# print("\n--- Concise ---\n")
# print(sales_agent3.run(user_input))
# send_test_email()
