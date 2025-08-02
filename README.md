# 🤖 Basic Agent - LLM Studies

This directory is part of the [LLM-Studies](https://github.com/EmersonFariaOliveira/LLM-Studies) repository and contains practical examples of building **basic agents with LLMs (Large Language Models)** using tools such as LangChain.

## 📚 Purpose

Explore how agents work by leveraging LLMs to make decisions based on tools and prompts, with a focus on simple and educational applications, including:

- Structuring a basic agent
- Registering and using tools (`@tool`)
- Using `bind_tools()` with OpenAI models
- Step-by-step agent execution with memory, history, and control

## 🧰 Technologies Used

- Python 3.9+
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI API](https://platform.openai.com/)
- Pydantic 2.x
- Custom tools with `@tool`

## 📁 Structure

```
basic_agent/
├── main.ipynb        # Example agent using registered tools
README.md             # This file
```

## 💡 Available Tools

- `tool_add`: Adds two numbers
- `tool_subtract`: Subtracts two numbers
- `tool_multiply`: Multiplies two numbers
- `tool_divide`: Divides two numbers
- `tool_sqrt`: Square root
- `tool_power`: Exponentiation
- `tool_sum`: Sum of a list of numbers

## 📌 Notes

- Tools use `Annotated[...]` with `Field(description=...)` to generate OpenAI-compatible schemas.
- The agent is built using `ChatOpenAI().bind_tools([...])`.

## 📄 License

This project is licensed under the MIT License.
