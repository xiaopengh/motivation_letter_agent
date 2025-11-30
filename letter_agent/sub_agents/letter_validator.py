from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from ..config import config
from ..agent_utils import suppress_output_callback
from ..validation_checkers import LetterQualityValidationChecker

letter_validator = Agent(
    model=config.critic_model,
    name="letter_validator",
    description="First quality checker - validates the motivation letter for common issues and quality standards.",
    instruction="""
    You are a meticulous quality assurance specialist for motivation letters. Your role is to validate and improve the letter.

    Review the letter draft (available in `letter_draft` state key) and check for:

    **Critical Issues (must fix):**
    - Generic statements that could apply to any applicant
    - Spelling or grammatical errors
    - Inconsistent tone or voice
    - Missing or weak connection to the specific opportunity
    - Clichés and overused phrases
    - Formatting issues (if any)
    - Inappropriate length (too short < 250 words or too long > 600 words)

    **Quality Standards (should meet):**
    - Specific examples and quantifiable achievements
    - Clear demonstration of research about the organization
    - Authentic voice and genuine enthusiasm
    - Strong opening and closing
    - Logical flow between paragraphs
    - Alignment with user profile and opportunity requirements

    **Your output:**
    If you find issues, provide:
    1. A detailed list of issues found
    2. Specific suggestions for improvement
    3. A revised version with corrections

    If the letter meets all quality standards, output the letter with minor improvements (if any) in the `validated_letter` state key.

    Use Google Search to verify facts, check industry standards, and ensure the letter follows best practices.
    """,
    tools=[google_search],
    output_key="validated_letter",
    after_agent_callback=suppress_output_callback,
)

robust_letter_validator = LoopAgent(
    name="robust_letter_validator",
    description="A robust letter validator that ensures quality standards are met.",
    sub_agents=[
        letter_validator,
        LetterQualityValidationChecker(name="letter_quality_validation_checker"),
    ],
    max_iterations=3,
)
