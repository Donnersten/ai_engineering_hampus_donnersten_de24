from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

class JokeBot:
    def __init__(self):
        self.chat_agent = Agent(
            "google-gla:gemini-2.5-flash",
            system_prompt="Ref is a soccer referee. He is a real sports freak. He knews all rules. Answer in a short and fun way and use emojis! "
        )
            
        self.result = None

    def chat(self,prompt:str) -> dict:
        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history)

        return {"user": prompt, "bot": self.result.output}


if __name__ == "__main__":
    bot = JokeBot()
    result = bot.chat("Hello there!")
    result = bot.chat("Tell me a joke!")
    
    result = bot.chat("What did i ask you first")
    print(result)
    
