from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

from llm.generative_engine import GenerativeEngine


class TitleGenerator:
    def __init__(self, llm_chat: AzureChatOpenAI):
        self.GUIDELINES = '\n'.join([
            "Titles should be no more than 20 words long",
            "Titles should be concise and to the point",
            "Titles should be catchy and grab the reader's attention",
            "Titles should be not be tedious or stuck up",
            "Titles should vary in sentiment and style"
        ])
        self.UNKNOWN_RESPONSE = ("I don't understand. Please try again. Multiple unexpected "
                                 "attempts will ban you from the app, to avoid abuse.")
        self.engine = GenerativeEngine(
            llm_chat=llm_chat,
            sys_msg=(
                "You are an experienced technical speaker that is great for creating great titles for abstracts.\n"
                
                "If a given abstract is not as expected please return "
                f"'{self.UNKNOWN_RESPONSE}'\n"
                
                "Your suggested titles should follow the <guidelines>\n"
                "<guidelines>\n"
                f"{self.GUIDELINES}\n"
                "</guidelines>\n"
            )
        )

    def generate(self, abstract: str) -> str:
        return self.engine.generate(
            msg=(
                "Please suggest 10 different abstract titles based on the following <abstract>:\n"
                f"<abstract>\n"
                f"{abstract}\n"
                f"</abstract>\n"
            )
        )
