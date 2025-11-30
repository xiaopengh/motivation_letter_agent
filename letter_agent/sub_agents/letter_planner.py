from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import LetterOutlineValidationChecker

letter_planner = Agent(
    model=config.worker_model,
    name="letter_planner",
    description="Generates a personalized motivation letter outline based on user profile and job/program requirements.",
    instruction="""
    You are an expert career coach and motivation letter strategist. Your job is to create a personalized outline for a motivation letter.

    The outline should be well-structured and tailored to the specific opportunity (job, scholarship, program, etc.).
    It should include:
    - Opening paragraph (hook and introduction)
    - Background and relevant experience (2-3 key points)
    - Why this specific opportunity (alignment with goals)
    - What you bring to the table (unique value proposition)
    - Closing paragraph (call to action)

    Use the user's profile information available in the `user_profile` state key.
    Use the job/program requirements available in the `opportunity_info` state key.

    Use Google Search to:
    - Research the company/institution
    - Find relevant industry trends
    - Understand what makes a compelling motivation letter for this type of opportunity

    Your final output should be a detailed outline in Markdown format that serves as a blueprint for writing the letter.
    Include specific talking points and suggestions for each section.
    """,
    tools=[google_search],
    output_key="letter_outline",
    after_agent_callback=suppress_output_callback,
)

robust_letter_planner = LoopAgent(
    name="robust_letter_planner",
    description="A robust letter planner that retries if it fails to create a valid outline.",
    sub_agents=[
        letter_planner,
        LetterOutlineValidationChecker(name="letter_outline_validation_checker"),
    ],
    max_iterations=3,
    after_agent_callback=suppress_output_callback,
)
