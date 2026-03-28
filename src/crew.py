from crewai import Crew

from src.agents.market_analyst import get_market_analyst
from src.agents.property_researcher import get_property_researcher
from src.agents.report_generator import get_report_generator

from src.tasks.market_analysis_task import create_market_analysis_task
from src.tasks.property_research_task import create_property_research_task
from src.tasks.report_generation_task import create_report_generation_task


def build_realestate_crew(research_query: str):
    """
    Build a crew of real estate research agents
    
    Args:
        research_query: The market research query (e.g., "Analyze residential real estate market in Austin, Texas")
    
    Returns:
        Crew: Configured CrewAI crew with agents and tasks
    """
    
    # Initialize agents
    market_analyst = get_market_analyst()
    property_researcher = get_property_researcher()
    report_generator = get_report_generator()
    
    # Create tasks with sequential dependencies
    market_analysis_task = create_market_analysis_task(
        market_analyst, 
        research_query
    )
    
    property_research_task = create_property_research_task(
        property_researcher,
        "{market_analysis_task}"
    )
    
    report_generation_task = create_report_generation_task(
        report_generator,
        "{market_analysis_task}",
        "{property_research_task}"
    )
    
    # Build the crew with sequential task execution
    return Crew(
        agents=[market_analyst, property_researcher, report_generator],
        tasks=[market_analysis_task, property_research_task, report_generation_task],
        verbose=True,
        memory=False,
    )
