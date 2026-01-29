# Load libraries
# We need MCPServerStreamableHttp from agents.mcp to connect to our MCP server over streamable HTTP protocol
from agents.mcp import MCPServerStreamableHttp

# We need these libraries to create an Agent that uses OpenAI models
from agents import Agent, Runner

# Load environment variables from a .env file
# Make sure your .env file has the OPENAI_API_KEY variable
# and .env is in the same directory where you run this script
from dotenv import load_dotenv

# We need asyncio to run our main function asynchronously
import asyncio

# We need gradio to create a web-based chat interface
import gradio as gr

# Load environment variables from .env file
load_dotenv(override=True)

# Define the chat function to handle user messages. It has to be asynchronous.
async def chat(message, history):
    # Create an MCP server connection using streamable HTTP protocol
    # Give the server a name and specify the URL where the MCP server is running
    # Specify additional parameters like timeout and SSE read timeout
    # We created the MCP server with server object "server"
    async with MCPServerStreamableHttp(
        name = "Calculator MCP Server", 
        params={
            "url": "http://localhost:8000/mcp",
            # Allow more time for remote tool responses.
            "timeout": 15,
            "sse_read_timeout": 300
            },
            # Retry slow/unstable remote calls a couple of times.
        max_retry_attempts=2,
        retry_backoff_seconds_base=2.0,
        client_session_timeout_seconds=15,
            ) as server:
        # Create an Agent that uses the MCP server we just created. 
        # Pass the server object in a list to the mcp_servers parameter.
        # Specify the LLM model to use for the Agent.
        agent = Agent(
            name="Calculator Assistant",
            instructions="Use the tools to respond to user requests.",
            mcp_servers=[server],
            model = "gpt-4.1-mini"
        )
        # Call the agent using the Runner to process the user message
        result = await Runner.run(
                agent,
                message,
            )
        return result.final_output

# Define the main asynchronous function to launch the Gradio chat interface
async def main():
    # Create a Gradio chat interface
    # The chat function defined above will handle user messages
    gr.ChatInterface(
    chat,
    title="Calculator MCP Chatbot",
    description="Chat with the Calculator Assistant"
    ).launch()

# Run the main function when the script is executed
if __name__ == "__main__":
    asyncio.run(main())
