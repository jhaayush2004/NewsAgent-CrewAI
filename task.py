from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)
'''
The async_execution parameter in the task configuration determines whether the task should be performed synchronously or asynchronously. Here’s a more detailed explanation:

Synchronous Execution (async_execution=False)
Synchronous Execution means that the task will be performed in a sequential manner, blocking further execution until the task is completed. When async_execution is set to False, the system will wait for the task to finish before moving on to the next task or returning control to the user. This approach ensures that the task is completed before any subsequent operations are performed.

Example Scenario:

You want to generate an article on the latest trends in AI.
The task is configured to be synchronous (async_execution=False).
The system will start the article generation process.
It will not perform any other tasks or return control until the article is fully generated and saved to new-blog-post.md.
Asynchronous Execution (async_execution=True)
Asynchronous Execution allows the task to run in the background, enabling other tasks to be performed concurrently. When async_execution is set to True, the system initiates the task and immediately returns control, allowing for other operations to be carried out while the task is still running.

Example Scenario:

You want to generate an article on the latest trends in AI.
The task is configured to be asynchronous (async_execution=True).
The system will start the article generation process.
It will immediately return control, allowing you to perform other tasks (like handling user input or starting another task) while the article generation continues in the background.
When to Use Synchronous vs. Asynchronous Execution
Use Synchronous Execution (async_execution=False) when:

You need to ensure that the task is completed before proceeding.
The task result is required for subsequent operations.
Blocking behavior is acceptable or necessary.
Use Asynchronous Execution (async_execution=True) when:

You want to improve efficiency by performing other tasks concurrently.
The task might take a long time, and you don't want to block the system.
The result is not immediately needed for subsequent operations.
Applying to Your Task
In your case, the task to be performed is generating an insightful article on a given topic. By setting async_execution to False, you are instructing the system to:

Begin the article generation process.
Wait until the article is fully written and saved to the specified output file (new-blog-post.md) before performing any other tasks or returning control.
'''
