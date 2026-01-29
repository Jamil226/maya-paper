from typing import TypedDict, Annotated
from langgraph.graph import add_messages, StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from llms import llm
from tools import tools
from datetime import datetime
import json

memory = MemorySaver()

class BasicChatBot(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: BasicChatBot):
    # Get current date context
    timestamp = datetime.now().strftime("%A, %d %B %Y, %H:%M")
    
    prompt = f"""
    You are Maya, an intelligent and empathetic hospital receptionist at Kocaeli University Research and Application Hospital.
    Current Time: {timestamp}

    ### YOUR MISSION
    Your goal is to assist visitors efficiently and accurately. You handle:
    1.  **General Inquiries**: Departments, facilities, visiting hours, location (Use `ask_hospital_info`).
    2.  **Doctors & Scheduling**: Finding doctors, checking availability, and booking appointments (Use `ask_database` and `book_appointment`).

    ### RULES OF ENGAGEMENT
    - **Be Proactive**: If a user wants an appointment, GUIDE them through the process. Ask for missing details one by one (Doctor, Date, Time, Patient Name, DOB, Contact).
    - **Be Accurate**: Only book if you have ALL required fields.
    - **Be Helpful**: If a doctor isn't available, suggest checking the database for others in the same department.
    
    Do not make up information. Use your tools.
    """

    # Add system message to history
    messages_payload = [SystemMessage(content=prompt)] + state["messages"]
    
    # Use native tool binding (Llama 3 supports this!)
    print(f"--- Calling LLM with {len(messages_payload)} messages ---")
    llm_with_tools = llm.bind_tools(tools=tools)
    
    ai_message = llm_with_tools.invoke(messages_payload)
    print(f"--- LLM Output: {ai_message.content} (Tool Calls: {ai_message.tool_calls}) ---")
    
    return {
        "messages": [ai_message]
    }

def tools_router(state: BasicChatBot):
    print("--- Entering tools_router ---")
    last_message = state["messages"][-1]
    
    if (hasattr(last_message, "tool_calls") and len(last_message.tool_calls) > 0):
        print(f"--- Decided to call tool: {last_message.tool_calls} ---")
        return "tool_node"
    else:
        print("--- Decided to END ---")
        return END


tool_node = ToolNode(tools=tools)

graph = StateGraph(BasicChatBot)

graph.add_node("chatbot", chatbot)
graph.add_node("tool_node", tool_node)
graph.set_entry_point("chatbot")

graph.add_conditional_edges("chatbot", tools_router)
graph.add_edge("tool_node", "chatbot")

Maya = graph.compile(checkpointer=memory)

config = {"configurable": {
    "thread_id": "chat-thread-1"
}}

if __name__ == "__main__":
    while True:
        user_input = input("User: ")

        result = Maya.invoke({
            "messages": [HumanMessage(content=user_input)]
        }, config=config)

        print("Maya:", result["messages"][-1].content)