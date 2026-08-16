"""
Autonomous Agent Framework -- Interactive Streamlit Dashboard
Physical UI to test and inspect Multi-Agent Swarm execution & StateGraphs.
Run: streamlit run app.py
"""
import sys
import os
import time
import streamlit as st

# Ensure src/ is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from agent_framework.core.multi_agent import MultiAgentSystem
from agent_framework.core.tools import ToolRegistry, tool

st.set_page_config(
    page_title="Autonomous Agent Framework | Swarm Inspector",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-header {
        color: #94a3b8;
        font-size: 1.0rem;
        margin-bottom: 24px;
    }
    .node-card {
        padding: 16px;
        border-radius: 12px;
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤖 Autonomous Agent Framework</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Multi-Agent Swarm & StateGraph Visual Inspector & Interactive Execution Playground</div>', unsafe_allow_html=True)

st.sidebar.title("⚙️ Control Panel")
st.sidebar.markdown("### Agent Team Topology")
st.sidebar.info("""
**Active Roles**:
- 🎯 **Supervisor**: Routes workflow & evaluates state
- 🔎 **Researcher**: Web & data research gathering
- ✍️ **Writer**: Synthesis & content drafting
- 🛡️ **Reviewer**: Quality assurance & safety validation
""")

# Sample queries
sample_queries = [
    "Analyze real-time market trends in autonomous AI agents and LangGraph systems.",
    "Evaluate security constraints for self-healing distributed microservices.",
    "Draft a technical blueprint for multi-modal agentic rag pipelines."
]

selected_sample = st.sidebar.selectbox("Select a Sample Query", ["Custom Query"] + sample_queries)

if selected_sample != "Custom Query":
    user_query = selected_sample
else:
    user_query = st.text_area("Enter Goal / Query for Swarm:", value="Perform market analysis on distributed AI architectures", height=100)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🚀 Execute Swarm Workflow")
    if st.button("Ignite Swarm Execution", type="primary", use_container_width=True):
        if not user_query.strip():
            st.error("Please enter a valid query for the agent swarm.")
        else:
            with st.spinner("Executing StateGraph Multi-Agent Swarm..."):
                system = MultiAgentSystem()
                start_time = time.time()
                response = system.execute(user_query)
                elapsed = time.time() - start_time

            st.success(f"Swarm Workflow Completed in {elapsed:.3f} seconds!")

            # Execution Trace
            st.markdown("#### 🔄 Step-by-Step Node Execution Trace")
            history = response.get("history", [])

            for idx, item in enumerate(history):
                node_name = item.get("node", "Unknown")
                node_data = item.get("data", {})
                phase = node_data.get("phase", "processing")
                
                with st.expander(f"Step {idx+1}: Node [{node_name}] | Phase: {phase}", expanded=(idx == len(history)-1)):
                    st.json(node_data)

            # Final Payload
            st.markdown("#### 🎯 Aggregated Multi-Agent Payload")
            st.json(response.get("final_data", {}))

with col2:
    st.markdown("### 🧰 Agent Tool Registry")
    st.markdown("Inspect registered tools available to worker agents:")
    
    registry = ToolRegistry()
    
    @tool(name="web_search", description="Simulates live web search retrieval")
    def web_search(query: str) -> str:
        return f"Retrieved 5 articles for '{query}'"
    
    @tool(name="vector_query", description="Queries local vector database for embeddings")
    def vector_query(concept: str) -> list:
        return ["doc_01", "doc_02", "doc_03"]

    registry.register(web_search)
    registry.register(vector_query)

    tools_manifest = registry.list_tools()
    for t in tools_manifest:
        st.markdown(f"""
        <div class="node-card">
            <strong>🔧 {t['name']}</strong><br/>
            <span style="color:#94a3b8; font-size:0.9rem;">{t['description']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Swarm Metrics")
    st.metric("Total Swarm Nodes", "4 Nodes")
    st.metric("Registered Tools", f"{len(tools_manifest)} Tools")
    st.metric("Routing Logic", "Dynamic Supervisor")
