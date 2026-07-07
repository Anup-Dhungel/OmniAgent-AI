import sys
from dotenv import load_dotenv

# Load environment variables from .env file FIRST
load_dotenv()

from agent import setup_agent

def main():
    try:
        agent_executor = setup_agent()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please set the GROQ_API_KEY and TAVILY_API_KEY environment variables.")
        sys.exit(1)

    print("==================================================")
    print("🤖 Autonomous AI Agent Initialized!")
    print("Capabilities: Web Search (Tavily), Code Execution (Python REPL), File I/O.")
    print("Type 'exit' or 'quit' to stop.")
    print("==================================================")

    # We use a fixed thread_id for this session to maintain memory
    # You could make this dynamic to support multiple distinct conversations
    config = {"configurable": {"thread_id": "cli_session_1"}}

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            # Stream the events from the agent
            events = agent_executor.stream(
                {"messages": [("user", user_input)]},
                config=config,
                stream_mode="values"
            )

            for event in events:
                # The event dictionary contains the 'messages' key
                if "messages" in event:
                    # Get the last message
                    latest_message = event["messages"][-1]
                    
                    # We only want to print AI messages or Tool outputs to the user, not echo their own input
                    # For simplicity, we just print the final content of the AI
                    pass
            
            # The last event in stream_mode="values" will contain the final state
            # Let's just print the content of the last message which should be the AI's response
            if "messages" in event:
                 latest_message = event["messages"][-1]
                 print(f"\nAgent: {latest_message.content}")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        except Exception as e:
             print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
