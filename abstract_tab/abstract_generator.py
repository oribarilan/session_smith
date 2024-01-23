from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI

from llm.generative_engine import GenerativeEngine


class AbstractGenerator:
    def __init__(self, llm_chat: AzureChatOpenAI):
        self.GUIDELINES = '\n'.join([
            "The abstract should refer to all terms given by the user",
            "The tone should be professional but not stuck up or tedious",
            "The abstract should be concise and to the point",
            "The abstract should start with a hook that grabs the reader's attention",
            "The abstract should end with a call to action that encourages the reader "
            " to attend the session",
            "The abstract length should somewhat correlate with the session duration length",
        ])
        self.UNKNOWN_RESPONSE = ("I don't understand. Please try again. Multiple unexpected "
                                 "attempts will ban you from the app, to avoid abuse.")
        self.engine = GenerativeEngine(
            llm_chat=llm_chat,
            sys_msg=(
                "You are an experienced technical speaker that generates great abstracts for "
                "technical conferences based on a several <properties> of the session.\n"
                
                "If any of the properties is not as expected please return "
                f"'{self.UNKNOWN_RESPONSE}'\n"
                
                "You abstract should follow the <guidelines>\n"
                "<guidelines>\n"
                f"{self.GUIDELINES}\n"
                "</guidelines>\n"
            )
        )

    def generate(self, topic: str, length: int, description: str, terms: str) -> str:
        return self.engine.generate(
            msg=(
                "Please suggest an abstract (no title) based on the following <properties>:\n"
                f"<properties>\n"
                f"Session topic is: {topic}\n"
                f"Session length: {length}\n"
                f"Description: {description}\n"
                f"Terms: {terms}\n"
                f"</properties>\n"
            )
        )
