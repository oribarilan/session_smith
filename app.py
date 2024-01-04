import gradio as gr

from abstract_tab.abstract_type import create_abstract_tab
from bio_tab.bio_tab import BioTab

app = gr.TabbedInterface(
    interface_list=[
        create_abstract_tab(),
        BioTab(
            title="Bio",
            description="This is a simple Gradio app to build speaker bios. Currently, it just echoes the inputs back."
        ).create()
    ],
    tab_names=["Abstract", "Bio"]
)

app.title = "SessionSmith: Abstract Builder"
app.description = "This is a simple Gradio app to build session abstracts. Currently, it just echoes the inputs back."

app.launch()
