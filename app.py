import os

import gradio as gr

from abstract_tab.abstract_tab import AbstractTab
from bio_tab.bio_tab import BioTab
from langchain_openai import AzureChatOpenAI

from title_tab.title_tab import TitleTab

os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_KEY")

llm_chat = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="ss_gpt-35-turbo",
)

app = gr.TabbedInterface(
    interface_list=[
        AbstractTab(llm_chat=llm_chat).create(),
        TitleTab(llm_chat=llm_chat).create(),
        BioTab().create()
    ],
    tab_names=["Abstract", "Title", "Bio"]
)

app.title = "SessionSmith: Your buddy for crafting technical sessions"
app.description = "Use this app to create a professional bio, compelling abstract, and more!"

app.launch()
