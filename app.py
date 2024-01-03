import gradio as gr


def create_abstract(topic_title: str, length: int, description: str):
    # This is a placeholder function that just returns the inputs for now.
    echo = f"Title: {topic_title}\nTags: {tags}\nLength: {length} minutes\nDescription: {description}"
    prompt = create_prompt(topic_title, tags, length, description)
    return echo, prompt

def create_prompt(topic_title: str, tags: str, length: int, description: str):
    return f"""Please suggest a {length}-minute-long technical session abstract called '{topic_title}'.\n\n
    Session description: {description}\n\n
    Tags: {tags}\n\n
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


with gr.Blocks() as app:
    with gr.Row():
        app.title = "SessionSmith: Abstract Builder"
    with gr.Row():
        app.description = "This is a simple Gradio app to build session abstracts. Currently, it just echoes the inputs back."
    with gr.Row():
        title = gr.Textbox(lines=2, placeholder="Enter Topic Title", label="Topic Title")
    with gr.Row():
        length = gr.Slider(label="Session Length (minutes)", minimum=5, maximum=60, step=5,
                           value=30)
    with gr.Row():
        desc = gr.Textbox(lines=5, placeholder="Enter a brief description of the session",
                          label="Description")
    with gr.Row():
        generate_btn = gr.Button("Generate")
        lucky_btn = gr.Button("I'm Feeling Lucky")
    with gr.Column(scale=1):
        abstract = gr.Textbox(lines=10, label="Session Abstract", interactive=False)
    with gr.Column(scale=1):
        prompt = gr.Textbox(lines=10, label="Session Prompt", interactive=False)

    generate_btn.click(create_abstract, inputs=[title, length, desc], outputs=[abstract, prompt])
    lucky_btn.click(populate_random, outputs=[title, length, desc])

app.launch()
