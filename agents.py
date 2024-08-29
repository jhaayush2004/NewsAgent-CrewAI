from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import os

#calling the gemini models
llm = ChatGoogleGenerativeAI(
                            model = "gemini-1.5-flash",
                            verbose = True,
                            temperature = 0.4,
                            google_api_key = os.getenv("GOOGLE_API_KEY")
                            )

# creating a senior research agent with memory and verbose mode

news_researcher = Agent(
    role = "Senior Researcher",
    goal = "uncover ground breaking technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = ("Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."),
    tools = [tool],
    llm = llm,
    allow_delegation =True
)

## creating a write agent with custom tools responsible in writing news blog
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False# it wil not interact with other agents
)
# now for every agents we need to create some tasks, so lets move to task.
