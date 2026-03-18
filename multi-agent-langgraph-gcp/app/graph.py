from langgraph.graph import StateGraph
from app.schemas.state import DataState
from app.agents.profiling import profiling_agent
from app.agents.analysis import analysis_agent
from app.agents.modelling import modelling_agent

def build_graph():
    graph = StateGraph(DataState)

    graph.add_node("profiling", profiling_agent)
    graph.add_node("analysis", analysis_agent)
    graph.add_node("modelling", modelling_agent)

    graph.set_entry_point("profiling")

    graph.add_edge("profiling", "analysis")
    graph.add_edge("analysis", "modelling")

    return graph.compile()