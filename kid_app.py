import google.generativeai as genai
import os

# 1. Setup your API Key
# Replace 'YOUR_GEMINI_KEY' with your actual API key
GEMINI_API_KEY = "YOUR_GEMINI_KEY"
genai.configure(api_key=GEMINI_API_KEY)

# 2. Define the "Kid" Persona
# This tells the AI exactly how to behave before the user even speaks.
KID_PROMPT = (
    "You are a 7-year-old child named Leo. You are curious, energetic, and "
    "sometimes use silly words. You explain things simply, use emojis, and "
    "talk about things like toys, candy, or dinosaurs. Keep your answers "
    "short and very friendly!"
)

# 3. Initialize the Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=KID_PROMPT
)

def ask_kid_app():
    print("👦 KidBot: Hi! I'm Leo! Ask me anything!! (Type 'bye' to stop)")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("👦 KidBot: Aww, okay! Race ya later! 🦖💨")
            break
        
        try:
            # Generate the response
            response = model.generate_content(user_input)
            
            print(f"\n👦 KidBot: {response.text}")
            
        except Exception as e:
            print(f"Oops! My brain got a knot: {e}")

if __name__ == "__main__":
    ask_kid_app()
