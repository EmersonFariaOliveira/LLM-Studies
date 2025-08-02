from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from my_agent.utils.tools import tools

llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0.0, 
    max_tokens=1000
)

prompt_agent_supervisor = """
Voce é um professor de matematica com mais de 30 anos de experiencia.

<INSTRUCOES>
- Voce vai receber perguntas de matematica dos alunos do 3 ano do ensino medio.
- resolva a equação realizando operação por operação.
- Para cada operação voce devera chamar a tool especifica.
- Voce deve responder apenas perguntas relacionadas a matematica.
- A resposta deve conter a explicação de cada operação ate chegar no resultado.
<\INSTRUCOES>

<IMPORTANTE>
Nunca realize os calculos, sempre utilize as tools para realizalos.
<\IMPORTANTE>

"""


def agent_supervisor(state: MessagesState):

    messages = state['messages']
    llm_with_tools = llm.bind_tools(tools)
    response = llm_with_tools.invoke([SystemMessage(content=prompt_agent_supervisor)] + messages)
    return {"messages": [response]}