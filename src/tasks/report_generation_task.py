from crewai import Task


def create_report_generation_task(agent, market_output, property_output):
    return Task(
        description=f"""
        ### FINAL REPORT GENERATION ###
        
        Synthesize the market analysis and property research into a comprehensive, professional report.
        
        Market Analysis Data:
        {market_output}
        
        Property Research Data:
        {property_output}
        
        Create a well-structured report with the following sections:
        
        1. **EXECUTIVE SUMMARY**
           - Key findings and main takeaways
           - Quick decision guide for investors/buyers
        
        2. **MARKET OVERVIEW**
           - Current market conditions
           - Trend analysis and forecasts
        
        3. **LOCATION INSIGHTS**
           - Neighborhood characteristics
           - Infrastructure and amenities
           - Growth potential
        
        4. **FINANCIAL ANALYSIS**
           - Pricing trends and comparisons
           - Investment potential and ROI
           - Rental yield estimates (if applicable)
        
        5. **RISK ASSESSMENT**
           - Market risks
           - Location-specific concerns
           - Mitigation strategies
        
        6. **RECOMMENDATIONS**
           - Actionable investment strategies
           - Best property types to target
           - Timing recommendations
        
        7. **CONCLUSION**
           - Final verdict and key advice
        
        Format the report professionally with clear headings, bullet points, and data-backed insights.
        Make it actionable and easy to understand for decision-makers.
        """,
        agent=agent,
        expected_output="Professional market research report with executive summary and actionable recommendations",
        context=[market_output, property_output] if hasattr(market_output, 'output') else None,
    )
