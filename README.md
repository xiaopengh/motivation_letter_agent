## Personalized Motivation Letter Writer Agent

### Intelligent Career Assistant with Multi-Layer Quality Control

**Transforming the motivation letter writing process through AI-powered personalization and validation**

This project contains a sophisticated multi-agent system designed to help users create compelling, personalized motivation letters for jobs, scholarships, graduate programs, and other competitive opportunities. The agent leverages Google's Agent Development Kit (ADK) to orchestrate specialized sub-agents, each contributing to different stages of the letter creation process with built-in validators and quality checkers ensuring professional-grade output.

---

## Original Project - Agent Shutton

NOTE: This project was adapted from a **sample submission** for the [Kaggle Agents Intensive Capstone project](https://www.kaggle.com/competitions/agents-intensive-course-capstone-2025/). The original sample was inspired by the [ADK-Samples](https://github.com/google/adk-samples/tree/main/python/agents/blog-writer) repository.

The original Agent Shutton was a multi-agent system designed to assist users in creating various types of blog posts. This project has been transformed into a motivation letter writing assistant.


### Problem Statement

Writing motivation letters is a time-consuming and stressful process that requires significant effort in self-reflection, research, personalization, and persuasive writing. Job seekers, students, and professionals often struggle to effectively communicate their unique value proposition while tailoring each letter to specific opportunities. The process becomes particularly challenging when applying to multiple positions, as each letter requires customization to match different job requirements, company cultures, and selection criteria. Many applicants struggle with common pitfalls such as generic statements, clichés, poor structure, or failure to demonstrate genuine interest and research about the organization. Quality control is difficult without expert feedback, and hiring professional writers is expensive and not scalable.

### Solution Statement

An AI-powered multi-agent system can transform motivation letter writing by automatically analyzing user profiles, researching target organizations, and generating personalized, compelling letters tailored to specific opportunities. The system employs specialized agents that work in sequence: a planner to structure the letter strategically, a writer to craft engaging content, a validator to check for quality issues and common mistakes, and an editor to polish the final output. This multi-layer approach ensures professional-grade letters that stand out from generic applications. By automating the research, drafting, and quality control processes, users can focus on providing their unique insights and experiences while the system handles the heavy lifting of persuasive writing, proper formatting, and alignment with best practices.

### Architecture

The core of this system is the `motivation_letter_agent` -- a sophisticated multi-agent system that orchestrates the entire motivation letter creation process. It's not a monolithic application but an ecosystem of specialized agents, each contributing expertise to different stages of the writing workflow. This modular approach, powered by Google's Agent Development Kit (ADK), enables a robust, quality-controlled letter writing process. The central orchestrator is the `motivation_letter_agent`.


The `motivation_letter_agent` is constructed using the `Agent` class from the Google ADK. Its definition includes key parameters: the `name`, the `model` it uses for reasoning, and detailed `description` and `instruction` sets that govern its behavior. Crucially, it defines the `sub_agents` it can delegate tasks to and the `tools` at its disposal for analyzing user profiles and managing letter output.

The system's power lies in its team of specialized sub-agents working in a sequential, quality-controlled workflow:

**Letter Strategist: `robust_letter_planner`**

This agent creates a personalized, strategic outline for the motivation letter based on the user's profile and the specific opportunity requirements. It researches the target organization, identifies key talking points from the user's experience, and structures the letter for maximum impact. Implemented as a `LoopAgent` with a `LetterOutlineValidationChecker`, it ensures the outline meets quality standards before proceeding.

**Letter Writer: `robust_letter_writer`**

Once the outline is approved, this expert writer crafts a compelling first draft. It transforms the outline into a persuasive, personalized letter using specific examples from the user's profile and demonstrating genuine interest in the opportunity. The agent employs professional writing techniques, active voice, and industry-appropriate terminology. A `LetterDraftValidationChecker` ensures the draft is complete before moving to quality control.

**First Quality Checker: `robust_letter_validator`**

This validator performs the first quality control pass, checking for critical issues such as generic statements, clichés, grammatical errors, inconsistent tone, and misalignment with opportunity requirements. It verifies that the letter includes specific examples, demonstrates research, and maintains an authentic voice. The `LetterQualityValidationChecker` ensures standards are met before escalating to the final review stage.

**Second Checker/Editor: `letter_editor`**

The final agent provides a senior-level editorial review, polishing the validated letter and incorporating user feedback. This editor focuses on sentence variety, word choice precision, transition smoothness, and overall persuasiveness. It ensures the letter stands out from typical applications while maintaining professional quality and coherence.

### Essential Tools and Utilities

The `motivation_letter_agent` and its sub-agents are equipped with specialized tools to perform their tasks effectively.

**Profile Analysis (`analyze_user_profile`)**

This tool analyzes the user's CV/resume or profile document to extract relevant information about their background, experience, skills, and achievements. It reads the profile file (supporting multiple encodings) and makes the content available to all sub-agents through the session state, enabling personalized letter generation.

**Opportunity Information Loading (`load_opportunity_info`)**

This tool loads and processes information about the target opportunity (job posting, scholarship description, program details, etc.). It extracts key requirements, organizational values, and selection criteria that the letter must address, ensuring the final output is tailored and relevant.

**Letter Saving (`save_motivation_letter`)**

A robust file-saving utility that exports the final motivation letter to a file. It includes error handling to ensure the letter is safely saved and provides status feedback to the user.

**Validation Checkers (`LetterOutlineValidationChecker`, `LetterDraftValidationChecker`, `LetterQualityValidationChecker`)**

These custom `BaseAgent` implementations form the quality control backbone of the system. They verify that each stage produces valid output before proceeding:
- `LetterOutlineValidationChecker`: Ensures the outline is created and stored in session state
- `LetterDraftValidationChecker`: Verifies the draft is complete
- `LetterQualityValidationChecker`: Validates the letter meets quality standards (length, content quality, etc.)

If validation fails, the `LoopAgent` retries the operation (up to 3 attempts). If validation succeeds, they escalate with `EventActions(escalate=True)`, signaling the workflow can proceed to the next stage. This multi-layer validation ensures professional-grade output.

### Conclusion

The elegance of the `motivation_letter_agent` lies in its sequential, quality-controlled workflow with built-in validation at every stage. The agent acts as an intelligent project manager, coordinating specialized sub-agents and ensuring each phase meets quality standards before proceeding. It gathers user input, delegates to expert agents, performs multi-layer quality checks, and iteratively refines the output based on feedback. This multi-agent orchestration, powered by Google ADK, creates a system that is modular, reliable, and produces professional-grade results.

The `motivation_letter_agent` demonstrates how multi-agent systems can tackle complex, high-stakes writing tasks that traditionally required human expertise. By decomposing the letter writing process into specialized stages (planning, writing, validation, editing) and assigning each to dedicated agents with specific quality checkers, the system delivers personalized, compelling letters that help users stand out in competitive application processes.

### Value Statement

The Motivation Letter Writer Agent significantly reduces the time and stress associated with crafting compelling application letters. What traditionally takes 3-5 hours per letter (including research, drafting, and multiple revisions) is streamlined to under 30 minutes of active user input, with the AI handling research, writing, and quality control. The multi-layer validation system catches common mistakes that often lead to rejection: generic statements, poor structure, grammatical errors, and lack of personalization.

Users benefit from professional-grade letters that demonstrate thorough research and genuine interest in each opportunity, increasing their chances of success in competitive application processes. The system scales effortlessly, allowing users to apply to multiple opportunities without sacrificing letter quality or personalization.

**Future Enhancements:**
- Integration with LinkedIn API to automatically extract user profile information
- Company/institution research agent that automatically gathers intelligence from multiple sources
- A/B testing agent that generates multiple letter variants optimized for different strategies
- Analytics agent that learns from user feedback to improve future letter generation 

## Installation

This project requires Python 3.11 and uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

1. **Install uv** (if not already installed):
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Ensure Python 3.11 is available:**
   ```bash
   python --version  # Should show Python 3.11.x
   ```

### Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd agent-xpeng
   ```

2. **Sync dependencies** (creates virtual environment and installs all dependencies):
   ```bash
   uv sync
   ```

3. **Activate the virtual environment** (optional, uv commands work without activation):
   ```bash
   # On macOS/Linux
   source .venv/bin/activate

   # On Windows
   .venv\Scripts\activate
   ```

### Running the Agent

**Launch the agent in ADK Web mode:**
```bash
uv run adk web
```

Or if you've activated the virtual environment:
```bash
adk web
```

**Run the integration tests:**
```bash
uv run pytest
```

Or with the virtual environment activated:
```bash
pytest
```

### Development

**Add new dependencies:**
```bash
uv add <package-name>
```

**Add development dependencies:**
```bash
uv add --dev <package-name>
```

**Update dependencies:**
```bash
uv sync --upgrade
```

## Project Structure

The project is organized as follows:

*   `blogger_agent/`: The main Python package for the motivation letter agent system.
    *   `agent.py`: Defines the main `motivation_letter_agent` orchestrator.
    *   `sub_agents/`: Contains the specialized sub-agents, each responsible for a specific task.
        *   `letter_planner.py`: Generates personalized letter outlines based on user profile and opportunity.
        *   `letter_writer.py`: Writes compelling first drafts of motivation letters.
        *   `letter_validator.py`: First quality checker - validates for common issues and quality standards.
        *   `letter_editor.py`: Second checker - performs final editorial review and polish.
    *   `validation_checkers.py`: Defines custom validation checkers for quality control.
    *   `tools.py`: Defines the custom tools used by the agents (profile analysis, opportunity info loading, letter saving).
    *   `config.py`: Contains the configuration for the agents, such as the models to use.
    *   `agent_utils.py`: Utility functions for agent operations.
*   `tests/`: Contains integration tests for the agent system.
    *   `test_agent.py`: Test suite for agent functionality.



## Workflow

The `motivation_letter_agent` follows this quality-controlled workflow:

1.  **Gather Information:** The agent asks the user to provide:
    - Their CV/resume or profile information (file path or direct input)
    - Details about the target opportunity (job posting, scholarship description, etc.)
    - Any specific requirements or preferences

2.  **Analyze Profile:** Using the `analyze_user_profile` tool, the agent processes the user's background, extracting relevant experience, skills, and achievements.

3.  **Load Opportunity Info:** Using the `load_opportunity_info` tool, the agent processes the opportunity details to understand requirements and selection criteria.

4.  **Plan:** The agent delegates outline creation to the `robust_letter_planner`, which:
    - Researches the target organization
    - Identifies key talking points from the user's profile
    - Creates a strategic structure tailored to the opportunity
    - Validates the outline through `LetterOutlineValidationChecker` (retries up to 3 times if needed)

5.  **Refine Outline:** The user reviews the outline and provides feedback. The agent refines until approved.

6.  **Write First Draft:** Once approved, the `robust_letter_writer`:
    - Transforms the outline into a compelling letter
    - Incorporates specific examples from the user's profile
    - Demonstrates genuine interest and research
    - Validates the draft through `LetterDraftValidationChecker` (retries up to 3 times if needed)

7.  **First Quality Check:** The `robust_letter_validator` automatically:
    - Checks for generic statements, clichés, and grammatical errors
    - Verifies alignment with opportunity requirements
    - Ensures quality standards are met (appropriate length, specific examples, authentic voice)
    - Validates through `LetterQualityValidationChecker` (retries up to 3 times if needed)

8.  **Second Review & Edit:** The `letter_editor` provides final polish:
    - Reviews sentence variety and word choice
    - Smooths transitions and enhances flow
    - Strengthens persuasiveness and impact
    - Incorporates any user feedback

9.  **Iterate:** The user reviews the final letter and can request additional changes. The `letter_editor` refines based on feedback until the user is satisfied.

10. **Export:** When approved, the agent uses the `save_motivation_letter` tool to save the final letter to a file with the user's preferred filename.

