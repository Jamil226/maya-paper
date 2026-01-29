from langchain_core.messages import HumanMessage
from maya_agent import Maya
import uuid
import sys

def run_test_chat():
    print("--- Starting Console Test ---")
    
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    
    # Test query
    user_input = "Hello, can you help me?"
    print(f"User Input: {user_input}")
    
    try:
        print("Maya is thinking...")
        result = Maya.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=config
        )
        
        ai_response = result["messages"][-1].content
        print(f"\n--- Maya Response ---\n{ai_response}")
        print("\n--- End of Test ---")
        
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_test_chat()
