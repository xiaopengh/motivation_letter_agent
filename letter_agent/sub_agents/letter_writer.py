from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import LetterDraftValidationChecker

letter_writer = Agent(
    model=config.critic_model,
    name="letter_writer",
    description="Writes a personalized motivation letter based on the approved outline.",
    instruction="""
    You are an expert motivation letter writer with years of experience helping candidates secure jobs, scholarships, and admission to competitive programs.

    Your task is to write a compelling, personalized motivation letter based on:
    - The approved outline (available in `letter_outline` state key)
    - User profile information (available in `user_profile` state key)
    - Opportunity details (available in `opportunity_info` state key)

    Writing guidelines:
    - Write in a professional yet engaging tone
    - Use specific examples and achievements from the user's profile
    - Demonstrate genuine enthusiasm and cultural fit
    - Keep paragraphs concise (3-5 sentences each)
    - Use active voice and strong action verbs
    - Avoid clichés and generic statements
    - Tailor every sentence to the specific opportunity
    - Match the tone and formality level appropriate for the opportunity type
    - Length should be 300-500 words unless specified otherwise

    Use Google Search to:
    - Find examples of successful motivation letters in the relevant field
    - Research the organization's values and culture
    - Understand industry-specific terminology

    The final output must be a complete motivation letter in plain text format (not Markdown).
    Include proper letter formatting with salutation and closing.
    """,
    tools=[google_search],
    output_key="letter_draft",
    after_agent_callback=suppress_output_callback,
)

robust_letter_writer = LoopAgent(
    name="robust_letter_writer",
    description="A robust letter writer that retries if it fails to create a valid draft.",
    sub_agents=[
        letter_writer,
        LetterDraftValidationChecker(name="letter_draft_validation_checker"),
    ],
    max_iterations=3,
)
