# CrewAI News Generation Pipeline
## Overview:

This project implements a robust news generation pipeline using the Crew AI framework and Google's powerful language models. The pipeline leverages the strengths of both to create high-quality news articles on various topics.

## Components:

- **Agents**:
News Researcher: Responsible for gathering relevant information, data, and insights on a given topic.
News Writer: Utilizes the research findings to craft compelling and informative news articles.

- **Research Task**: Involves data collection, analysis, and synthesis of information from various sources.
- **Write Task**: Focuses on crafting well-structured, grammatically correct, and engaging articles based on the research findings.
- **Crew**: Coordinates the agents and tasks, ensuring efficient execution of the pipeline.

## Workflow:

 1. **Topic Input**: The pipeline receives a topic as input.

 2. **Research Task**: The News Researcher agent is assigned the Research Task.
- The agent uses web scraping, API calls, or other relevant techniques to gather information from various sources.
- Data is cleaned, analyzed, and synthesized to extract key insights.

3. **Research Findings**: The News Researcher agent provides the research findings to the News Writer agent.

4. **Write Task**: The News Writer agent is assigned the Write Task.
The agent uses the research findings to craft a well-structured and informative article.
The article is formatted, edited, and proofread for clarity and coherence.

5. **Output**: The final news article is generated and made available.

## Technical Details:

- **Language Model**: Google's Gemini 1.5 Flash model is used for natural language generation and understanding.

- **Custom Tools**: The pipeline can be extended with custom tools for specific tasks, such as interacting with databases, APIs, or specialized data sources.

- **Crew AI Framework**: Provides a structured approach for managing agents, tasks, and their interactions.

- **Python**: The pipeline is implemented using Python, leveraging its versatility and extensive libraries.
