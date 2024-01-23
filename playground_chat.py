import os

from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import AzureChatOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_KEY")

chat = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="ss_gpt-35-turbo",
)

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are a technical assistant that helps people write "
                "technical abstracts for conferences."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
chain = chat_template | chat
messages = chain.invoke({'text': 'Intro to k8s'})
abstract = messages.content