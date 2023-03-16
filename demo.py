import gradio as gr
from TTS.api import TTS

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

def text_to_speech(text: str, speaker_wav, language: str):
    tts.tts_to_file(text, speaker_wav=speaker_wav, language=language, file_path="output.wav")
    # tts.tts_to_file(text=text, speaker=tts.speakers[0], language=language, file_path="output.wav")
    return 'output.wav'

inputs = [gr.Textbox(label="Input", value="Personalized learning platform for students with learning differences: You could develop an AI-powered platform that uses adaptive learning algorithms to provide personalized learning experiences for students with learning differences such as dyslexia or ADHD. As a front-end developer, you could design and develop the user interface, while your background in psychology could inform the adaptive learning algorithms used by the platform.", max_lines=3),
          gr.Audio(Lable="Speaker Wav", source="microphone", type="filepath"), 
            gr.Radio(label="Language", choices=tts.languages, value="en")]
outputs = gr.Audio(label="Output")

demo = gr.Interface(fn=text_to_speech, inputs=inputs, outputs=outputs)

demo.launch(debug=True)
