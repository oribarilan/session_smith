import gradio as gr


def create_abstract(topic_title: str, length: int, description: str):
    # This is a placeholder function that just returns the inputs for now.
    echo = f"{topic_title=}\n{length=}\n{description=}"
    prompt = create_prompt(topic_title, length, description)
    return echo, prompt

def create_prompt(topic_title: str, length: int, description: str):
    return f"""Please suggest a {length}-minute-long technical session abstract called '{topic_title}'.\n\n
    Session description: {description}\n\n
    """

# Sample JSON object with predefined inputs
predefined_inputs = {
    "example1": {
        "title": "Understanding AI",
        "length": 45,
        "description": "A deep dive into the workings of artificial intelligence algorithms."
    }
    # You can add more sets of predefined inputs here as "example2", "example3", etc.
}

def populate_random():
    # Currently, this function retrieves the predefined inputs for "example1".
    # You can add logic to randomly select an example if you have multiple.
    example = predefined_inputs["example1"]
    return example["title"], example["length"], example["description"]

def create_abstract_tab():
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
                prompt = gr.Textbox(lines=10, label="Session Prompt", interactive=False)
                abstract = gr.Textbox(lines=10, label="Session Abstract", interactive=False)


        generate_btn.click(create_abstract, inputs=[title, length, desc], outputs=[abstract, prompt])
        lucky_btn.click(populate_random, outputs=[title, length, desc])
    return abstract_tab