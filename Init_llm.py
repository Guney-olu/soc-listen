"""
LLM initalization for summary and report generation 
"""

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

# Initialize the model
n_gpu_layers = -1
n_batch = 512
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

model = LlamaCpp(
    model_path="./models/zephyr-7b-beta.Q2_K.gguf.1",
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    temperature=0.75,
    max_tokens=100,
    top_p=1,
    n_ctx=35000,
    callback_manager=callback_manager,
    verbose=True,
)

# Define the prompt template
prompt_template = PromptTemplate(
    template="""
    Analyze the following text and provide a summary in the format below:
    
    Top Problems:
    - Identify and list the main problems mentioned in the text.

    Top Pros:
    - Identify and list the main advantages mentioned in the text.

    Companies:
    - Identify and list any companies mentioned in the text.
    
    Text:
    {text}
    """,
    input_variables=["text"]
)

def generate_categorized_summary(input_text):
    formatted_prompt = prompt_template.format(text=input_text)
    response = model(formatted_prompt)
    return response


# THE INPUT WILL BE EXTRACTED FROM VECTOR DB
""""
results = vector_store.similarity_search(
    "the toothbrush is verybad",
    k=2,
    filter={"metatag": "feedback"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")
"""


# Example from the datajson
input_text = """
Just in case you’re concerned you won’t be able to get a $200+ smart toothbrush, you will soon to be able to get a $400 AI powered toothbrush.
Meanwhile, Oral-B is pushing its latest toothbrush to capitalize on the latest AI tech trend. Without real detail, Oral-B claims its new $400 toothbrush has "A.I. position detection that tracks where you brush across all 3 surfaces of your teeth.” Like many, I'm skeptical about the toothbrush’s incorporation of actual AI; notably, P&G declined to comment to The Washington Post on what, exactly, makes the toothbrush "AI."
This is the future we dreamed about as children manifesting before our very own eyes!
What, exactly, makes the toothbrush "AI." The brush is so sharp and hard, you'll scream "AÏ!" when you use it.
OMG this is like the days when manufactures wanted to say their machines they produced like toasters and refrigerators were internet connected as a marketing point rather than a truly practical use.
Yeah I never thought “I wish my toothbrush had an app, imagine all the cool stuff my toothbrush could do if I could control it via app using WiFi!” Imagine being an app developer and your job was to build out a platform for a toothbrush. I would quiet quit so hard on that shit lol.
I have a toothbrush with built-in WiFi. It connects to an app supposedly, but WTF would I need to track, much less let the world track, how and when I brush my teeth?
2026: Mr Observe. I'm afraid your dental insurance will not cover your claim for dentures since you only brushed below average frequency and were inconsistent.
"""

# summary = generate_categorized_summary(input_text)
# print("Summary:", summary)

