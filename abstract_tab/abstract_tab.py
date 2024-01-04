import gradio as gr

from abstract_tab.abstract_example_factory import AbstractExampleFactory


class AbstractTab:
    def __init__(self):
        self.example_factory = AbstractExampleFactory()

    def _create_abstract(self, topic_title: str, length: int, description: str):
        # This is a placeholder function that just returns the inputs for now.
        echo = f"{topic_title=}\n{length=}\n{description=}"
        return echo

    def _populate_random(self):
        # Currently, this function retrieves the predefined inputs for "example1".
        return self.example_factory.generate()

    def create(self):
        with gr.Blocks() as abstract_tab:
            gr.Markdown("""
            # SessionSmith: Abstract Builder
            This is a simple Gradio app to build session abstracts. Currently, it just echoes the inputs back.
            """)
            with gr.Row():
                with gr.Column():
                    title = gr.Textbox(lines=2, placeholder="Enter Topic Title", label="Topic Title")
                    length = gr.Slider(label="Session Length (minutes)", minimum=5, maximum=60, step=5,
                                           value=30)
                    desc = gr.Textbox(lines=5, placeholder="Enter a brief description of the session",
                                          label="Description")
                    generate_btn = gr.Button("Generate")
                    lucky_btn = gr.Button("I'm Feeling Lucky")

                with gr.Column():
                    abstract = gr.Textbox(lines=10, label="Session Abstract", interactive=False)

            generate_btn.click(self._create_abstract, inputs=[title, length, desc], outputs=[abstract])
            lucky_btn.click(self._populate_random, outputs=[title, length, desc])
        return abstract_tab