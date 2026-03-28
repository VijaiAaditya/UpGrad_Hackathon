# 🏘️ Real Estate Market Research AI Crew

A sophisticated multi-agent AI system powered by CrewAI for comprehensive real estate market research and analysis.

## 🎯 Features

- **3 Specialized AI Agents**:
  - 📊 **Market Analyst**: Analyzes market trends, pricing patterns, and investment opportunities
  - 🏠 **Property Researcher**: Researches properties, neighborhoods, and location insights
  - 📝 **Report Generator**: Compiles comprehensive reports with actionable recommendations

- **Comprehensive Analysis**:
  - Market trends and pricing analysis
  - Location and neighborhood insights
  - Investment potential assessment
  - Risk evaluation
  - Actionable recommendations

- **Beautiful Streamlit UI**:
  - Interactive dashboard
  - Real-time agent execution tracking
  - Multiple report views (Executive Summary, Full Report, Key Insights)
  - Export in multiple formats (Markdown, Text, JSON)

## 📋 Prerequisites

- Python 3.8+
- API key from one of:
  - OpenAI (Recommended)
  - Groq (Fast, free tier available)
  - Ollama (Local, no API key needed)

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd RealEstate_MarketResearch_Crew
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your API key
   # For OpenAI:
   OPENAI_API_KEY=sk-...
   
   # OR for Groq:
   GROQ_API_KEY=gsk_...
   
   # OR use Ollama (local) - no API key needed
   ```

## 🎮 Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run ui/app.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Enter your research query**, for example:
   - "Analyze residential real estate market in Austin, Texas"
   - "Investment opportunities in Miami commercial properties"
   - "Rental market trends in San Francisco Bay Area"

4. **Configure settings** in the sidebar:
   - Select AI model (Groq, OpenAI, or Ollama)
   - Choose research type (Residential, Commercial, Investment, etc.)
   - Enable detailed analysis mode

5. **Run the analysis** and view results in multiple tabs:
   - 📋 Executive Summary
   - 📈 Full Report
   - 💡 Key Insights
   - 📊 Raw Data
   - 💾 Export

## 🏗️ Project Structure

```
RealEstate_MarketResearch_Crew/
├── src/
│   ├── agents/
│   │   ├── market_analyst.py          # Market analysis agent
│   │   ├── property_researcher.py     # Property research agent
│   │   └── report_generator.py        # Report generation agent
│   ├── tasks/
│   │   ├── market_analysis_task.py    # Market analysis task
│   │   ├── property_research_task.py  # Property research task
│   │   └── report_generation_task.py  # Report generation task
│   ├── crew.py                         # Crew orchestration
│   └── config.py                       # LLM configuration
├── ui/
│   └── app.py                          # Streamlit UI application
├── .env.example                        # Environment variables template
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## 🤖 Agent Details

### 1. Market Analyst Agent 📊
- **Role**: Analyzes market trends and economic indicators
- **Capabilities**:
  - Market overview and current conditions
  - Price analysis and historical trends
  - Supply and demand metrics
  - Economic indicators (employment, income, growth)
  - Investment potential and ROI estimates
  - Market comparisons and risk assessment

### 2. Property Researcher Agent 🏠
- **Role**: Researches properties and locations
- **Capabilities**:
  - Location analysis and demographics
  - Infrastructure assessment (transport, schools, hospitals)
  - Development plans and zoning
  - Amenities and local attractions
  - Safety and crime statistics
  - School district analysis
  - Future growth indicators

### 3. Report Generator Agent 📝
- **Role**: Compiles comprehensive reports
- **Capabilities**:
  - Executive summaries
  - Financial analysis
  - Risk assessment
  - Actionable recommendations
  - Professional formatting
  - Data-driven insights

## 🎨 Example Queries

```
"Analyze the luxury residential market in Beverly Hills, California"

"Investment opportunities in Austin, Texas for tech professionals"

"Compare rental yields between Miami and Orlando, Florida"

"Commercial real estate prospects in downtown Seattle"

"Affordable housing market analysis in Phoenix, Arizona under $400k"
```

## 🔧 Configuration Options

### Model Selection
- **Groq**: Fast, free tier available, good for quick analysis
- **OpenAI**: Best results, most comprehensive analysis (recommended)
- **Ollama**: Local deployment, privacy-focused, no API costs

### Research Types
- Residential
- Commercial
- Investment
- Rental Market
- Custom

### Export Formats
- Markdown (recommended for formatting)
- Plain Text
- JSON (for integration with other tools)

## 🛠️ Troubleshooting

**Issue**: API key not found
- **Solution**: Make sure you've created a `.env` file and added your API key

**Issue**: Agents not responding
- **Solution**: Check your API key is valid and you have credits/quota available

**Issue**: Ollama not working
- **Solution**: Make sure Ollama is installed and running (`ollama serve`)

**Issue**: Import errors
- **Solution**: Ensure all dependencies are installed (`pip install -r requirements.txt`)

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new agents
- Enhance existing agents
- Improve the UI
- Add new features
- Fix bugs

## 📧 Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Built with ❤️ using CrewAI and Streamlit**
