import gradio as gr
from TTS.api import TTS

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

def text_to_speech(text: str, speaker_wav, language: str):
    tts.tts_to_file(text, speaker_wav=speaker_wav, language=language, file_path="output.wav")
    return 'output.wav'

inputs = [gr.Textbox(label="Input", value="Hello!", max_lines=3),
          gr.Audio(Lable="Speaker Wav", source="microphone", type="filepath"), 
            gr.Radio(label="Language", choices=tts.languages, value="en")]
outputs = gr.Audio(label="Output")

demo = gr.Interface(fn=text_to_speech, inputs=inputs, outputs=outputs)

demo.launch(debug=True)
