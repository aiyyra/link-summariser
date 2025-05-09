To keep up with recent updates, reading article is a must.

Recent advancement in tech especially in AI fields makes it hard to keep up with all of these massive amount of articles/ blogs.

# This project aims to leverage the power of llm agents to help me being up to date.

It is important to note that I encourage readings and you need to read a lot of article. This summariser would not be enough if you want to further expands your arsenal as an AI engineer/ practitioner.

# The outline of this project is as below:

## Aim:

1. Leverage agentic architecture in this project as part of personal learning path.
2. Make autonomous agent that is capable to receive link and make a websearch.
3. Perceive/ Process all the content in the webpage and parse it into a summariser.
4. Run the system only in terminal

## Possible Refinement:

1. Parse adds.
2. Make another agent to help in breaking down knowledge obtain. (Easy to understand output)
3. Make other agent to help make websearch and retrieve related source for more compact and quality output

## Update

### 28-3-2025

#### Planning

- Use Gemini as its provide generous free API calls. ✔️
- Use Langchain for ease of implementation. ✔️
- The programme will only run in terminal (removed overthinking for UI). ✔️
- Make a basic chat program ✔️

#### Notes

- Could use chat template but will ignore for now
- Could check other model in huggingface and use huggingface interface for more robust model for our usecase.

### 29-3-2025

#### Planning

- Create a basic tool that could be call by model for doing a websearch (it is a simplify websearch that retrieve link and research the link). ❌
- for now, just add every source code of the pages into the chat history and paste it in terminal as a whole, we will summarise later. ✔️

#### Notes

- At first, i was trying to use SerpAPI for web searching, however on my research I found that Tavily API provide a more robust searching and simpler integration to our use case. For that, we will use Tavily for this project.
- Changing model to groq, this ensure we got the system prompt that gemini lacks. It is also free :>
- We finish researching and adding Tavily as our websearch solution. however we still didn't implement a tool call for the agent to call.
- An update to the poetry dependencies also happened, as i keep to toml file at other folder, the change is not potrayed in github.

### 30-3-2025

#### Planning

- Going to reconstruct myself, as i was quite blur on how to actually make an agent.
- First, make an agent without tool that can follow the ReAct (reasoning action loop).
- If possible, implement our tool, which is extracting/ searching the web.

#### Notes

- I was somewhat blur on agent architecture in langchain, so we will learn it from the ground up.
