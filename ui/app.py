import streamlit as st
import sys
import os
import time
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.crew import build_realestate_crew


def stream_text(text, placeholder, delay=0.005):
    """Simulate typing effect for better UX"""
    output = ""
    for char in text:
        output += char
        placeholder.markdown(output)
        time.sleep(delay)


def parse_report_sections(text):
    """Parse the report into sections for better display"""
    sections = {
        "executive_summary": "",
        "market_overview": "",
        "location_insights": "",
        "financial_analysis": "",
        "risk_assessment": "",
        "recommendations": "",
        "full_report": text
    }
    
    # Try to extract sections based on common headers
    if "EXECUTIVE SUMMARY" in text.upper():
        parts = text.upper().split("EXECUTIVE SUMMARY")
        if len(parts) > 1:
            sections["executive_summary"] = parts[1].split("MARKET OVERVIEW")[0] if "MARKET OVERVIEW" in parts[1] else parts[1][:500]
    
    if "RECOMMENDATIONS" in text.upper():
        parts = text.upper().split("RECOMMENDATIONS")
        if len(parts) > 1:
            sections["recommendations"] = parts[1].split("CONCLUSION")[0] if "CONCLUSION" in parts[1] else parts[1][:1000]
    
    return sections


# Page Configuration
st.set_page_config(
    page_title="Real Estate Market Research AI",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🏘️ Real Estate Market Research AI</h1>
        <p>Market Analysis → Property Research → Comprehensive Report</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")
st.sidebar.markdown("---")

# Model Selection
model_option = st.sidebar.selectbox(
    "🤖 AI Model",
    ["Groq (Fast)", "OpenAI (Recommended)", "Ollama (Local)"],
    help="Select the AI model for analysis"
)

# Research Type
research_type = st.sidebar.selectbox(
    "🔍 Research Type",
    ["Residential", "Commercial", "Investment", "Rental Market", "Custom"],
    help="Type of real estate research"
)

# Additional Options
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Report Options")
include_charts = st.sidebar.checkbox("Include Data Visualizations", value=False)
detailed_mode = st.sidebar.checkbox("Detailed Analysis Mode", value=True)
export_format = st.sidebar.selectbox("Export Format", ["Markdown", "PDF", "JSON"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Example Queries")
st.sidebar.code("Analyze residential real estate market in Austin, Texas")
st.sidebar.code("Investment opportunities in Miami commercial properties")
st.sidebar.code("Rental market trends in San Francisco Bay Area")

# Main Input Area
st.subheader("📝 Enter Your Market Research Query")

col1, col2 = st.columns([3, 1])

with col1:
    research_query = st.text_area(
        "Market Research Request",
        placeholder="Example: Analyze the residential real estate market in Seattle, Washington focusing on 2-3 bedroom homes under $800k",
        height=100,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button("🚀 Run Analysis", type="primary", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    clear_button = st.button("🗑️ Clear", use_container_width=True)

if clear_button:
    st.rerun()

# Run Analysis
if run_button:
    if not research_query.strip():
        st.warning("⚠️ Please enter a market research query")
        st.stop()
    
    # Progress tracking
    st.markdown("---")
    st.subheader("⚙️ AI Agents Working...")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Agent execution placeholders
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Market Analyst")
        market_status = st.empty()
        market_status.info("🔄 Analyzing market data...")
    
    with col2:
        st.markdown("### 🏠 Property Researcher")
        property_status = st.empty()
        property_status.info("⏳ Waiting...")
    
    with col3:
        st.markdown("### 📝 Report Generator")
        report_status = st.empty()
        report_status.info("⏳ Waiting...")
    
    # Execute the crew
    try:
        progress_bar.progress(10)
        status_text.text("Initializing AI agents...")
        
        crew = build_realestate_crew(research_query)
        
        progress_bar.progress(30)
        status_text.text("Agents analyzing market data...")
        property_status.info("🔄 Researching properties...")
        
        progress_bar.progress(50)
        result = crew.kickoff()
        
        progress_bar.progress(80)
        status_text.text("Generating final report...")
        report_status.info("🔄 Compiling report...")
        
        progress_bar.progress(100)
        status_text.text("✅ Analysis complete!")
        
        # Update status boxes
        market_status.success("✅ Market analysis complete")
        property_status.success("✅ Property research complete")
        report_status.success("✅ Report generated")
        
        time.sleep(1)
        
        # Get the output
        output_text = result.raw
        sections = parse_report_sections(output_text)
        
        # Display Results
        st.markdown("---")
        st.markdown("## 📊 Research Results")
        
        # Create tabs for different views
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📋 Executive Summary",
            "📈 Full Report",
            "💡 Key Insights",
            "📊 Raw Data",
            "💾 Export"
        ])
        
        # Executive Summary Tab
        with tab1:
            st.markdown("### 🎯 Executive Summary")
            summary_placeholder = st.empty()
            
            if sections["executive_summary"]:
                stream_text(sections["executive_summary"], summary_placeholder, delay=0.003)
            else:
                # Extract first few paragraphs as summary
                preview = output_text[:1000] + "..." if len(output_text) > 1000 else output_text
                stream_text(preview, summary_placeholder, delay=0.003)
            
            st.markdown("---")
            st.markdown("### 🎯 Key Recommendations")
            rec_placeholder = st.empty()
            
            if sections["recommendations"]:
                stream_text(sections["recommendations"], rec_placeholder, delay=0.003)
        
        # Full Report Tab
        with tab2:
            st.markdown("### 📄 Complete Market Research Report")
            report_placeholder = st.empty()
            stream_text(output_text, report_placeholder, delay=0.002)
        
        # Key Insights Tab
        with tab3:
            st.markdown("### 💡 Key Market Insights")
            
            # Create insight cards
            col1, col2 = st.columns(2)
            
            with col1:
                st.info("**🎯 Market Strength**\n\nAnalysis based on current trends and indicators")
                st.success("**📈 Growth Potential**\n\nProjected appreciation and development")
            
            with col2:
                st.warning("**⚠️ Risk Factors**\n\nPotential challenges and considerations")
                st.info("**💰 Investment Score**\n\nOverall viability assessment")
            
            st.markdown("---")
            st.markdown("#### 📊 Detailed Insights")
            st.markdown(output_text)
        
        # Raw Data Tab
        with tab4:
            st.markdown("### 🔍 Raw Analysis Output")
            st.code(output_text, language="markdown")
            
            # Show agent execution details
            with st.expander("🤖 View Agent Execution Details"):
                st.json({
                    "query": research_query,
                    "research_type": research_type,
                    "model": model_option,
                    "agents_used": ["Market Analyst", "Property Researcher", "Report Generator"],
                    "output_length": len(output_text),
                    "detailed_mode": detailed_mode
                })
        
        # Export Tab
        with tab5:
            st.markdown("### 💾 Export Report")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.download_button(
                    label="📥 Download as Markdown",
                    data=output_text,
                    file_name=f"realestate_report_{time.strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown"
                )
            
            with col2:
                st.download_button(
                    label="📥 Download as Text",
                    data=output_text,
                    file_name=f"realestate_report_{time.strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            with col3:
                # Export as JSON
                json_data = json.dumps({
                    "query": research_query,
                    "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                    "report": output_text,
                    "metadata": {
                        "research_type": research_type,
                        "model": model_option
                    }
                }, indent=2)
                
                st.download_button(
                    label="📥 Download as JSON",
                    data=json_data,
                    file_name=f"realestate_report_{time.strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
            
            st.markdown("---")
            st.info("💡 Tip: Markdown format is recommended for best formatting and readability")
        
        # Success message
        st.success("✅ Market research analysis completed successfully!")
        
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.exception(e)
        progress_bar.progress(0)
        status_text.text("❌ Analysis failed")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 2rem;'>
        <p>🏘️ Real Estate Market Research AI powered by CrewAI</p>
        <p style='font-size: 0.8rem;'>Three specialized AI agents working together: Market Analyst, Property Researcher, and Report Generator</p>
    </div>
""", unsafe_allow_html=True)
