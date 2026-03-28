from crewai import Task


def create_property_research_task(agent, market_analysis_output):
    return Task(
        description=f"""
        ### PROPERTY RESEARCH ###
        
        Based on the market analysis provided below, conduct detailed property and location research:
        
        {market_analysis_output}
        
        Your research should cover:
        1. **Location Analysis**: Neighborhood characteristics, demographics
        2. **Infrastructure**: Transportation, schools, hospitals, shopping centers
        3. **Development Plans**: Upcoming projects, zoning changes
        4. **Property Types**: Most popular property types and their characteristics
        5. **Amenities**: Parks, recreational facilities, local attractions
        6. **Safety & Crime**: Crime statistics and safety ratings
        7. **School Districts**: Quality of schools and education facilities
        8. **Future Growth**: Area development potential and growth indicators
        
        Focus on location-specific insights that affect property desirability and value.
        """,
        agent=agent,
        expected_output="Comprehensive property and location research with neighborhood insights",
        context=[market_analysis_output] if hasattr(market_analysis_output, 'output') else None,
    )
