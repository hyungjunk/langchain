import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from tools.index import get_profile_url_tavily

load_dotenv()


def lookup(name: str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        google_api_key=os.environ["GOOGLE_API_KEY"]
    )
    template = """
    Given the full name of {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your answer should contain only a URL.
    """
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl google 4 LinkedIn page",
            func=get_profile_url_tavily,
            description="useful for when you need get the LinkedIn profile page",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    return result['output']


lookup("MIRAN SEO")
