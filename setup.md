## Softwares
- Visual studio code
- Python - preferably 3.12.3 or latest one
- Claude Desktop - AI assistant

## Install UV
Go to https://docs.astral.sh/uv/getting-started/installation/#installation-methods

Follow the instructions 

Use either curl or pip based approach

## Create a virtual environment
```sh
# Open terminal, go to any folder and run the following commands to create a virtual environment
mkdir my_project
cd my_project
python -m venv .venv
```

## Activate virtual environment
```sh
# Activate the virtual env
source .venv/bin/activate  

# On Windows use `.venv\Scripts\activate`
```

## Install python dependencies for OpenAI SDK Agent for building agents
```sh
# Install common python packages
uv pip install python-dotenv  requests bs4 

# Install openai sdk agents
uv pip install openai openai-agents 

# Install gradio for building custom chat interface
uv pip install gradio 
```

## OpenAI API key
Since we will be using OPENAI SDK agent in few use cases for building agents

1. Go to OPENAI platform https://auth.openai.com/log-in
2. Sign up
3. Create api key . https://platform.openai.com/api-keys
4. Copy this somewhere
5. Create .env file in your working directory and add your key as below
OPENAI_API_KEY="mykey"

## Install packages for building MCP servers
2 different packages can be used for building MCP. But FastMCP is better. so we will use FastMCP

1. mcp[cli] (https://modelcontextprotocol.io/docs/develop/build-server)
2. fastmcp (https://gofastmcp.com/getting-started/installation)

```sh
uv pip install mcp[cli] httpx
uv pip install fastmcp
```

## Install node js
Most of the mcp server are built using either node js or python. Also some remote mcp connection requires some packages that are built on node js. so exploring full capacity of mcp, install node js

Go to https://nodejs.org/en/download and install
After installation check node -v and npm -v. 

#### Windows
```sh
# Restart power shell after each
# You may have to run as admin

# Download and install Chocolatey:
powershell -c "irm https://community.chocolatey.org/install.ps1|iex"
# Download and install Node.js:
choco install nodejs --version="24.13.0"
# Verify the Node.js version:
node -v # Should print "v24.13.0".
# Verify npm version:
npm -v # Should print "11.6.2".
```

#### Linux
```sh
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"
# Download and install Node.js:
nvm install 24
# Verify the Node.js version:
node -v # Should print "v24.13.0".
# Verify npm version:
npm -v # Should print "11.6.2".
```

## Install Claude Desktop (AI Assistant)
Download and install claude desktop
Create a account. You may go for free tier. 

For more exploration, can go for paid plan. The content of this course can be finished within free tier. 

https://claude.com/download

Enable developer mode. 
Go to help -> enable developer mode


