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

# Load environment variables from .env file
load_dotenv(override=True)

from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
client = AsyncOpenAI(base_url="http://localhost:11434/v1")
model_name = "gpt-oss"
model = OpenAIChatCompletionsModel(model = model_name,openai_client= client)


# Define the main asynchronous function
async def main():
    # Create an MCP server connection using streamable HTTP protocol
    # Give the server a name and specify the URL where the MCP server is running
    # Specify additional parameters like timeout and SSE read timeout
    # We created the MCP server with server object "server"
    async with MCPServerStreamableHttp(
        name = "Calculator MCP Server", 
        params={
            "url": "http://localhost:8083/mcp",
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
            #model = "gpt-4.1-mini"
            model = model
        )
        # Call the agent using the Runner to ask a question
        result = await Runner.run(
                agent,
                "what is 5 plus 6?",
            )
        print("Result:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
