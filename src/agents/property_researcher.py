from crewai import Agent
from src.config import get_llm


def get_property_researcher():
    return Agent(
        role="Property Research Specialist",
        goal="Research properties, neighborhoods, and location-specific insights",
        backstory=(
            "Seasoned property researcher with deep knowledge of local markets, "
            "zoning regulations, infrastructure development, and neighborhood dynamics. "
            "Specializes in discovering hidden gems and evaluating location potential. "
            "You have expertise in analyzing school districts, crime rates, amenities, "
            "transportation access, and future development plans that impact property values."
        ),
        allow_delegation=False,
        llm=get_llm(),
        verbose=True,
    )
