from app.llm.vertex_llm import VertexLLM

llm = VertexLLM()

def modelling_agent(state):
    prompt = f"""
    Based on this analysis:
    {state['analysis']}

    Generate:
    - schema design
    - table relationships
    - modelling suggestions
    """
    result = llm.generate(prompt)

    return {**state, "model": result}