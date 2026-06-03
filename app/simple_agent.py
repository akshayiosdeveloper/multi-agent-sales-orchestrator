import ollama


class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

    def run(self, user_input):
        prompt = f"""
{self.instructions}

Write a cold sales email for:
{user_input}
"""
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']

    def run_streamed(self, user_input):
        prompt = f"""
{self.instructions}

Write a cold sales email for:
{user_input}
"""
        stream = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            yield chunk['message']['content']
