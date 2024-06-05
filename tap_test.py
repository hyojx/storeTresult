"""import gradio as gr
# 기본건강/다이어트/미용 탭으로 입력창 만들기

hello_world = gr.Interface(lambda name: "Hello " + name, "text", "text")
bye_world = gr.Interface(lambda name: "Bye " + name, "text", "text")

demo = gr.TabbedInterface([hello_world, bye_world], ["Hello World", "Bye World"])

if __name__ == "__main__":
    demo.launch() """

import gradio as gr
def update(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("Start typing below and then click **Run** to see the output.")
    with gr.Row():
        inp = gr.Textbox(placeholder="What is your name?")
        out = gr.Textbox()
    btn = gr.Button("Run")
    btn.click(fn=update, inputs=inp, outputs=out)

demo.launch()