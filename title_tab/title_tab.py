import gradio as gr
from langchain_openai import AzureChatOpenAI

from title_tab.title_generator import TitleGenerator


class TitleTab:
    def __init__(self, llm_chat: AzureChatOpenAI):
        self.title_generator = TitleGenerator(llm_chat=llm_chat)

    def _create_titles(self, abstract: str) -> str:
        return self.title_generator.generate(
            abstract=abstract
        )

    def create(self):
        with gr.Blocks() as title_tab:
            gr.Markdown("""
            # SessionSmith: Title Recommender
            This tool helps you generate a title for your session's abstract.
            """)
            with gr.Row():
                with gr.Column():
                    desc = gr.Textbox(lines=10, placeholder="In this session....", label="Abstract")
                    generate_btn = gr.Button("Generate")
                    with gr.Row():
                        clear = gr.ClearButton([desc], value="Clear")

                with gr.Column():
                    titles = gr.Textbox(label="Suggested Titles")

            generate_btn.click(self._create_titles, inputs=[desc], outputs=[titles])

        return title_tab
