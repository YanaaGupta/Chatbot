from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryMemory
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

# Step 1: LLM + Memory
llm = ChatOllama(model="llama3")
memory = ConversationSummaryMemory(llm=llm)

# Step 2: Prompt Template
template = """
Use the conversation history and respond accordingly.
Conversation Summary:
{history}
User: {input}
Bot:"""
prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Step 3: Combining memory + prompt + LLM into a RunnableSequence; RunnableLambda to fetch memory
def get_inputs(input: str):
    return {"input": input, "history": memory.load_memory_variables({})["history"]}
chain = (
    RunnableLambda(get_inputs)
    | prompt
    | llm
)

# Step 4: Chat Loop
print('''               !!! CHATBOT READY !!! 
Type 'quit' or 'exit' to end the conversation.
BOT: Hi, How can I help you?''')
while True:
    user_input = input("YOU: ")
    if user_input.lower() in ["exit", "quit"]:
        print("!!! CHATBOT SIGNING OFF !!!")
        break

    # Running chain and updating memory
    response = chain.invoke(user_input)
    memory.save_context({"input": user_input}, {"output": response.content})
    print(" BOT:", response.content)