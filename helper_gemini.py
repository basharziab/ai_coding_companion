
import google.generativeai as genai
import google.ai.generativelanguage as glm


def gemini_text(prompt, entered_api_key):
    print(f"gemini entered_api_key : {entered_api_key}")
    genai.configure(api_key=entered_api_key)
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(
        f"You are a helpful programmer. You communicate using markdown. You only respond if the prompt is relevent to programming.  \n  Prompt: {prompt}.")
    # print(f"RESPONSE GEMINI : {response}")
    # print(f"RESPONSE TEXT GEMINI : {response.text}")

    return response.text
