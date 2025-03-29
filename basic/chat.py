from dotenv import load_dotenv

from langchain.schema import AIMessage, HumanMessage, SystemMessage # Gemini would not have system message, but we will keep the import in case for model changes
# from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.chat_models import init_chat_model


# load api key
load_dotenv()

# Init chat model
# model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Init chat history
chat_history = [] # a list to store history of chat

# SystemMessage is use for the system wide instruct, however we cannot use it for Gemini model.
# HumanMessage is to encapsulate the message sent by user into the messages list.
# messages = [
#     # SystemMessage(content="Solve the following math problems.") # We will keep here for model changes
#     HumanMessage(content="What is 81 divided by 9?")
# ]

# We can keep this here to make a system message when suitable model is used
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    # Append the message into chat history
    chat_history.append(HumanMessage(content=query))

    # Get AI response based on the chat history
    result = model.invoke(chat_history)
    # Append to chat history and display the response
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)

# result = model.invoke(messages)
# print(f"Answer from AI: {result.content}")

# # Invoke the model with a message
# result = model.invoke("What is 81 divided by 9?")
# print("Full result:")
# print(result)
# print("Content only:")
# print(result.content)