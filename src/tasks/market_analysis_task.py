from crewai import Task


def create_market_analysis_task(agent, research_query):
    return Task(
        description=f"""
        ### MARKET ANALYSIS ###
        
        Conduct a comprehensive market analysis for the following request:
        {research_query}
        
        Your analysis should include:
        1. **Market Overview**: Current market conditions and trends
        2. **Price Analysis**: Average prices, price ranges, and historical trends
        3. **Supply & Demand**: Inventory levels, days on market, absorption rates
        4. **Economic Indicators**: Employment rates, income levels, economic growth
        5. **Investment Potential**: ROI estimates, appreciation forecasts
        6. **Market Comparison**: How this market compares to similar regions
        7. **Risk Assessment**: Market risks and volatility factors
        
        Provide data-driven insights with specific numbers and percentages where possible.
        """,
        agent=agent,
        expected_output="Detailed market analysis report with trends, pricing, and investment insights",
    )
