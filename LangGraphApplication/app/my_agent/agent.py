from langgraph.graph import MessagesState, StateGraph
from my_agent.utils.tools import tools
from my_agent.utils.nodes import agent_supervisor

from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START

builder = StateGraph(MessagesState)

builder.add_node("agent_supervisor", agent_supervisor)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent_supervisor")
builder.add_conditional_edges("agent_supervisor", tools_condition)

builder.add_edge(START, "agent_supervisor")

builder.add_edge("tools", "agent_supervisor")

graph = builder.compile()