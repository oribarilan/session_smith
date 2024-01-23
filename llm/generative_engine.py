from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI


class GenerativeEngine:
    def __init__(self, llm_chat: AzureChatOpenAI, sys_msg: str):
        self.llm_chat = llm_chat
        self.sys_msg = sys_msg

    def generate(self, msg: str) -> str:
        chat_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=self.sys_msg),
                HumanMessage(content=msg),
            ]
        )

        chain = chat_template | self.llm_chat

        return chain.invoke({}).content
