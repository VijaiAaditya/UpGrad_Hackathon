from crewai import Agent
from src.config import get_llm


def get_market_analyst():
    return Agent(
        role="Real Estate Market Analyst",
        goal="Analyze real estate market trends, pricing patterns, and investment opportunities",
        backstory=(
            "Expert real estate analyst with 15+ years of experience in market research, "
            "property valuation, and investment analysis. Skilled at identifying emerging "
            "markets, analyzing demographics, and forecasting property values. You have "
            "a deep understanding of economic indicators, supply-demand dynamics, and "
            "market cycles that affect real estate prices."
        ),
        allow_delegation=False,
        llm=get_llm(),
        verbose=True,
    )
