import gradio as gr

from abstract_tab.abstract_example_factory import AbstractExampleFactory


class AbstractTab:
    def __init__(self):
        self.example_factory = AbstractExampleFactory()

    def _create_abstract(self, topic_title: str, length: int, description: str, terms: str):
        # This is a placeholder function that just returns the inputs for now.
        terms_lst = terms.split(",")
        echo = f"{topic_title=}\n{length=}\n{description=}'n{terms_lst=}"
        return echo

    def _populate_random(self):
        topic, length, description = self.example_factory.generate()
        return topic.title, length, description, topic.terms

    def create(self):
        with gr.Blocks() as abstract_tab:
            gr.Markdown("""
            # SessionSmith: Abstract Builder
            This is a simple Gradio app to build session abstracts. Currently, it just echoes the inputs back.
            """)
            with gr.Row():
                with gr.Column():
                    title = gr.Textbox(lines=1, placeholder="Enter Topic Title", label="Topic Title")
                    length = gr.Slider(label="Session Length (minutes)", minimum=5, maximum=60, step=5,value=30)
                    desc = gr.Textbox(lines=5, placeholder="Enter a brief description of the session", label="Description")
                    terms = gr.Textbox(lines=1, label="Terms (comma-separated)", placeholder="Kubernetes, Docker, Containers, Image, Isolation, Environment, Virtualization, Pod, Cluster, Node, Service, Deployment")
                    generate_btn = gr.Button("Generate")
                    with gr.Row():
                        lucky_btn = gr.Button("I'm Feeling Lucky")
                        clear = gr.ClearButton([title, length, desc, terms], value="Clear All")

                with gr.Column():
                    abstract = gr.Textbox(label="Session Abstract")

            generate_btn.click(self._create_abstract, inputs=[title, length, desc, terms], outputs=[abstract])
            lucky_btn.click(self._populate_random, outputs=[title, length, desc, terms])

        return abstract_tab