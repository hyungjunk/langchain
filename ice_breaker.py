from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

information = """

Pichai Sundararajan (born June 10, 1972), better known as Sundar Pichai,[a] is an Indian-born American business executive.[3][4] He is the chief executive officer of Alphabet Inc. and its subsidiary Google.[5]

Pichai began his career as a materials engineer. Following a short stint at the management consulting firm McKinsey & Co., Pichai joined Google in 2004,[6] where he led the product management and innovation efforts for a suite of Google's client software products, including Google Chrome and ChromeOS, as well as being largely responsible for Google Drive. In addition, he went on to oversee the development of other applications such as Gmail and Google Maps. In 2010, Pichai also announced the open-sourcing of the new video codec VP8 by Google and introduced the new video format, WebM. The Chromebook was released in 2012. In 2013, Pichai added Android to the list of Google products that he oversaw.

Pichai was selected to become the next CEO of Google on August 10, 2015, after previously being appointed chief product officer by then CEO Larry Page. On October 24, 2015, he stepped into the new position at the completion of the formation of Alphabet Inc., the new holding company for the Google company family. He was appointed to the Alphabet Board of Directors in 2017.[7]

"""

if __name__ == "__main__":
    print("Hello from LanguageChain")
    summary = """
    Given the information {given_information} about a person from I want you to create
    1. a short summary
    2. Two interesting facts about them.
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["given_information"], template=summary
    )
    # llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3.1:latest")

    chain= summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"given_information": information})

    print(res)