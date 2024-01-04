import gradio as gr

from abstract_tab.abstract_tab import AbstractTab
from bio_tab.bio_tab import BioTab

app = gr.TabbedInterface(
    interface_list=[
        AbstractTab().create(),
        BioTab().create()
    ],
    tab_names=["Abstract", "Bio"]
)

app.title = "SessionSmith: Your buddy for crafting technical sessions"
app.description = "Use this app to create a professional bio, compelling abstract, and more!"

app.launch()
