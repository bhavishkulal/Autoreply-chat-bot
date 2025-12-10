import google.generativeai as genai

genai.configure(api_key="AIzaSyAxlg-tn7CzkZ2lAoIGLXHlDBLJTrVRz-4")

models = genai.list_models()

for m in models:
    print(m.name, "  |  supports generate_content:", "generateContent" in m.supported_generation_methods)
