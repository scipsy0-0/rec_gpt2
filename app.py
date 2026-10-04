import gradio as gr
from justrun import generate

start = "meow meow meow"
num_samples = 1
max_new_tokens = 128
temperature = 0.9
top_k = 50
seed = 1337

def func(start = "meow meow", num_samples = 1, max_new_tokens = 128, temperature = 0.9, top_k = 50, seed = 1337):
    ans = generate(start, num_samples, max_new_tokens, temperature, top_k, seed)
    result = ""
    for i in ans:
        result += i
        result += '\n-------------------------------\n'
    return result

demo = gr.Interface(fn=func, 
                    inputs=["text", gr.Slider(minimum=1, maximum=100, value=1, step=1), gr.Slider(minimum=1, maximum=1000, value=128, step=4), gr.Slider(minimum=0, maximum=1, value=0.95, step=0.01), gr.Slider(minimum=1, maximum=100, value=50, step=1), gr.Number(value=1337)], 
                    outputs="text"
                    )
demo.launch()   