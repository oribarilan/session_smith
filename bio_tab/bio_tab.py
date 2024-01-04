import gradio as gr

from base_tab import BaseTab


class BioTab(BaseTab):
    def create_inner_tab(self) -> gr.Blocks:
        with gr.Blocks() as tab:
            with gr.Row():
                with gr.Column():
                    name = gr.Textbox(lines=2, placeholder="Name", label="Speaker Name")
                    title = gr.Textbox(lines=2, placeholder="Tagline", label="Speaker Title")
                    company = gr.Textbox(lines=2, placeholder="Company", label="Speaker Company")
                    role = gr.Textbox(lines=2, placeholder="Role", label="Speaker Company")
                    generate_btn = gr.Button("Generate")

                with gr.Column():
                    bio = gr.Textbox(lines=10, label="Bio", interactive=False)

            generate_btn.click(self._create_bio, inputs=[name, title, company, role], outputs=[bio])

        return tab

    def _create_bio(self, name, title, company, role):
        return f"{name=}\n{title=}\n{company=}\n{role=}"
