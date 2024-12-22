import os

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Running langchain")
    response = scrape_linkedin_profile('')
    summary = """
    Given the LinkedIn information {given_information} about a person from I want you to create
    1. a short summary
    2. Two interesting facts about them.
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["given_information"], template=summary
    )
    # llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.2")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=os.environ["GOOGLE_API_KEY"])

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"given_information": response})
    print(res)
