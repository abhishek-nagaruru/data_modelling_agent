from app.llm.vertex_llm import VertexLLM

llm = VertexLLM()

def profiling_agent(state):
    prompt = f"""
    You are a data profiling expert.

    Given dataset schema:
    {state['dataset']}

    Provide:
    - column types
    - null analysis
    - distribution insights
    """
    result = llm.generate(prompt)

    return {**state, "profile": result}