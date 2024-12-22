from langchain_community.tools import TavilySearchResults


def get_profile_url_tavily(topic: str) -> str:
    search = TavilySearchResults()
    res = search.run(f"{topic}")
    return res
