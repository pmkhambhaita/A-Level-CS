import groq
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
from pathlib import Path
import time

# API Configuration
GROQ_API_KEY = "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"

class VoiceAssistant:
    def __init__(self):
        """Initialize the voice assistant"""
        print("Initializing TTS engine...")
        self.tts = TTS("tts_models/en/vctk/vits")
        self.speaker = "p226"  # British male voice
        self.speech_speed = 0.75  # Slower speech rate
        
        print("Connecting to Groq...")
        self.client = groq.Groq(api_key=GROQ_API_KEY)
        
        self.temp_dir = Path("temp_audio")
        self.temp_dir.mkdir(exist_ok=True)

    def speak_response(self, text: str) -> None:
        """Convert text to speech and play it"""
        try:
            temp_file = self.temp_dir / "response.wav"
            
            # Generate speech for entire response
            self.tts.tts_to_file(
                text=text,
                speaker=self.speaker,
                file_path=str(temp_file),
                speed=self.speech_speed
            )
            
            # Play the complete response
            data, samplerate = sf.read(str(temp_file))
            sd.play(data, samplerate)
            sd.wait()
            
        except Exception as e:
            print(f"Error in speech generation: {str(e)}")
    
    def ask_question(self, question: str) -> str:
        """Get response from Groq API"""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Answer questions clearly and concisely."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                model="mixtral-8x7b-32768",
                temperature=0.7,
                max_tokens=150
            )
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

if __name__ == "__main__":
    # Create assistant
    assistant = VoiceAssistant()
    
    print("\nVoice Assistant Ready (Press Ctrl+C to exit)")
    print("Ask your question:")
    
    try:
        while True:
            question = input("\nYou: ")
            if question.lower() in ['exit', 'quit', 'bye']:
                break
                
            print("Thinking...")
            response = assistant.ask_question(question)
            print(f"Assistant: {response}")
            assistant.speak_response(response)
            
    except KeyboardInterrupt:
        print("\nGoodbye!")