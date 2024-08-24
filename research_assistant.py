from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.file import FileTools
from dotenv import load_dotenv
from prompts import description, instructions, query

load_dotenv()

assistant = Assistant(
    llm=Groq(model="llama-3.1-8b-instant"),
    description=description,
    instructions=[instructions],
    tools=[DuckDuckGo(), FileTools()],
    show_tool_calls=True,
    # debug_mode=True,
)
assistant.print_response(query, markdown=True)
