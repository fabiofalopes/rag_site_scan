# GroqCloud - Tool Use

Criado em: October 10, 2024 10:35 AM
URL: https://console.groq.com/docs/tool-use

Tool use is a powerful feature that allows Large Language Models (LLMs) to interact with external resources, such as APIs, databases, and the web, to gather dynamic data they wouldn't otherwise have access to in their pre-trained (or static) state and perform actions beyond simple text generation.

Tool use bridges the gap between the data that the LLMs were trained on with dynamic data and real-world actions, which opens up a wide array of realtime use cases for us to build powerful applications with, especially with Groq's insanely fast inference speed. 🚀

## How Tool Use Works

Groq API tool use structure is compatible with OpenAI's tool use structure, which allows for easy integration. See the following cURL example of a tool use request:

```
curl https://api.groq.com/openai/v1/chat/completions \-H "Content-Type: application/json" \-H "Authorization: Bearer $GROQ_API_KEY" \-d '{
  "model": "llama3-groq-70b-8192-tool-use-preview",
  "messages": [
    {
      "role": "user",
      "content": "What'\''s the weather like in Boston today?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"]
        }
      }
    }
  ],
  "tool_choice": "auto"
}'
```

To integrate tools with Groq API, follow these steps:

- Provide tools (or predefined functions) to the LLM for performing actions and accessing external data in real-time in addition to your user prompt within your Groq API request
- Define how the tools should be used to teach the LLM how to use them effectively (e.g. by defining input and output formats)
- Let the LLM autonomously decide whether or not the provided tools are needed for a user query by evaluating the user query, determining whether the tools can enhance its response, and utilizing the tools accordingly
- Extract tool input, execute the tool code, and return results
- Let the LLM use the tool result to formulate a response to the original prompt

This process allows the LLM to perform tasks such as real-time data retrieval, complex calculations, and external API interaction, all while maintaining a natural conversation with our end user.

## Tool Use with Groq

Groq API endpoints support tool use to almost instantly deliver structured JSON output that can be used to directly invoke functions from desired external resources.

### [Supported Models](https://console.groq.com/docs/tool-use#supported-models)

**Groq Fine-Tuned Models**

These models have been finetuned by Groq specifically for tool use and are currently in public preview:

- **`llama3-groq-70b-8192-tool-use-preview`**
- **`llama3-groq-8b-8192-tool-use-preview`**

Check out our launch [post](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/) for more information.

**Note:** When using our fine-tuned models in your workflow, we recommend implementing a routing system. [Learn more below.](https://console.groq.com/docs/tool-use#routing-system)

**Llama 3.1 Models**

The following Llama-3.1 models are also recommended for tool use due to their versatility and performance:

- **`llama-3.1-70b-versatile`**
- **`llama-3.1-8b-instant`**

**Note:** For wide scenario multi-turn tool use, we recommend using the native tool use feature of the Llama 3.1 models. For multi-turn with a narrow scenarios, fine-tuned tool use models might work well. We recommend trying both and seeing which works best for your specific use case!

**Other Supported Models**

The following models powered by Groq also support tool use:

- **`llama3-70b-8192`**
- **`llama3-8b-8192`**
- **`mixtral-8x7b-32768`** (parallel tool use not supported)
- **`gemma-7b-it`** (parallel tool use not supported)
- **`gemma2-9b-it`** (parallel tool use not supported)

## Tools Specifications

Tool use is part of the [Groq API chat completion request payload](https://console.groq.com/docs/api-reference#chat-create).

### [Tool Call and Tool Response Structure](https://console.groq.com/docs/tool-use#tool-call-and-tool-response-structure)

**Tool Call Structure**

Groq API tool calls are structured to be OpenAI-compatible. The following is an example tool call structure:

```
{  "model": "llama3-groq-70b-8192-tool-use-preview",  "messages": [    {      "role": "system",      "content": "You are a weather assistant. Use the get_weather function to retrieve weather information for a given location."    },    {      "role": "user",      "content": "What's the weather like in New York today?"    }  ],  "tools": [    {      "type": "function",      "function": {        "name": "get_weather",        "description": "Get the current weather for a location",        "parameters": {          "type": "object",          "properties": {            "location": {              "type": "string",              "description": "The city and state, e.g. San Francisco, CA"            },            "unit": {              "type": "string",              "enum": ["celsius", "fahrenheit"],              "description": "The unit of temperature to use. Defaults to fahrenheit."            }          },          "required": ["location"]        }      }    }  ],  "tool_choice": "auto",  "max_tokens": 4096}'
```

**Tool Call Response**

The following is an example tool call response based on the above:

```
"model": "llama3-groq-70b-8192-tool-use-preview","choices": [{    "index": 0,    "message": {        "role": "assistant",        "tool_calls": [{            "id": "call_d5wg",            "type": "function",            "function": {                "name": "get_weather",                "arguments": "{\"location\": \"New York, NY\"}"            }        }]    },    "logprobs": null,    "finish_reason": "tool_calls"}],
```

When a model decides to use a tool, it returns a response with a `tool_calls` object containing:

- `id`: a unique identifier for the tool call
- `type`: the type of tool call, i.e. function
- `name`: the name of the tool being used
- `parameters`: an object containing the input being passed to the tool

### [Setting Up Tools](https://console.groq.com/docs/tool-use#setting-up-tools)

To get started, let's go through an example of tool use with Groq API that you can use as a base to build more tools on your own.

### Step 1: Create Tool

Let's install Groq SDK, set up our Groq client, and create a function called `calculate` to evaluate a mathematical expression that we will represent as a tool.

Note: In this example, we're defining a function as our tool, but your tool can be any function or an external resource (e.g. dabatase, web search engine, external API).

```
pip install groq
```

```
1from groq import Groq
2import json
3
4# Initialize the Groq client5client = Groq()6# Specify the model to be used (we recommend our fine-tuned models or the Llama 3.1 models)7MODEL = 'llama3-groq-70b-8192-tool-use-preview'8
9def calculate(expression):10    """Evaluate a mathematical expression"""11    try:12        # Attempt to evaluate the math expression13        result = eval(expression)14        return json.dumps({"result": result})15    except:16        # Return an error message if the math expression is invalid17        return json.dumps({"error": "Invalid expression"})
```

### Step 2: Pass Tool Definition and Messages to Model

Next, we'll define our `calculate` tool within an array of available `tools` and call our Groq API chat completion. You can read more about tool schema and supported required and optional fields above in **Tool Specifications.**

By defining our tool, we'll inform our model about what our tool does and have the model decide whether or not to use the tool. We should be as descriptive and specific as possible for our model to be able to make the correct tool use decisions.

In addition to our `tools` array, we will provide our `messages` array (e.g. containing system prompt, assistant prompt, and/or user prompt).

### Step 3: Receive and Handle Tool Results

After executing our chat completion, we'll extract our model's response and check for tool calls.

If the model decides that no tools should be used and does not generate a tool or function call, then the response will be a normal chat completion (i.e. `response_message = response.choices[0].message`) with a direct model reply to the user query.

If the model decides that tools should be used and generates a tool or function call, we will:

- Define available tool or function,
- Add the model's response to the conversation by appending our message
- Process the tool call and add the tool response to our message
- Make a second Groq API call with the updated conversation
- Return the final response

```
1# imports calculate function from step 12def run_conversation(user_prompt):3    # Initialize the conversation with system and user messages4    messages=[5        {6            "role": "system",7            "content": "You are a calculator assistant. Use the calculate function to perform mathematical operations and provide the results."8        },9        {10            "role": "user",11            "content": user_prompt,12        }13    ]14    # Define the available tools (i.e. functions) for our model to use15    tools = [16        {17            "type": "function",18            "function": {19                "name": "calculate",20                "description": "Evaluate a mathematical expression",21                "parameters": {22                    "type": "object",23                    "properties": {24                        "expression": {25                            "type": "string",26                            "description": "The mathematical expression to evaluate",27                        }28                    },29                    "required": ["expression"],30                },31            },32        }33    ]34    # Make the initial API call to Groq35    response = client.chat.completions.create(36        model=MODEL, # LLM to use37        messages=messages, # Conversation history38        stream=False39        tools=tools, # Available tools (i.e. functions) for our LLM to use40        tool_choice="auto", # Let our LLM decide when to use tools41        max_tokens=4096 # Maximum number of tokens to allow in our response42    )43    # Extract the response and any tool call responses44    response_message = response.choices[0].message
45    tool_calls = response_message.tool_calls
46    if tool_calls:47        # Define the available tools that can be called by the LLM48        available_functions = {49            "calculate": calculate,50        }51        # Add the LLM's response to the conversation52        messages.append(response_message)53
54        # Process each tool call55        for tool_call in tool_calls:56            function_name = tool_call.function.name
57            function_to_call = available_functions[function_name]58            function_args = json.loads(tool_call.function.arguments)59            # Call the tool and get the response60            function_response = function_to_call(61                expression=function_args.get("expression")62            )63            # Add the tool response to the conversation64            messages.append(65                {66                    "tool_call_id": tool_call.id,
67                    "role": "tool", # Indicates this message is from tool use68                    "name": function_name,69                    "content": function_response,70                }71            )72        # Make a second API call with the updated conversation73        second_response = client.chat.completions.create(74            model=MODEL,75            messages=messages
76        )77        # Return the final response78        return second_response.choices[0].message.content
79# Example usage80user_prompt = "What is 25 * 4 + 10?"81print(run_conversation(user_prompt))
```

### [Routing System](https://console.groq.com/docs/tool-use#routing-system)

If you use our models fine-tuned for tool use, we recommended to use them as part of a routing system:

- **Query Analysis**: Implement a routing system that analyzes incoming user queries to determine their nature and requirements.
- **Model Selection**: Based on the query analysis, route the request to the most appropriate model:
    - For queries involving function calling, API interactions, or structured data manipulation, use the Llama 3 Groq Tool Use models.
    - For general knowledge, open-ended conversations, or tasks not specifically related to tool use, route to a general-purpose language model, such as Llama 3 70B.

The following is the `calculate` tool we built in the above steps enhanced to include a routing system that routes our request to Llama 3 70B if the user query does not require the tool:

```
1from groq import Groq
2import json
3
4# Initialize the Groq client 5client = Groq()6
7# Define models8ROUTING_MODEL = "llama3-70b-8192"9TOOL_USE_MODEL = "llama3-groq-70b-8192-tool-use-preview"10GENERAL_MODEL = "llama3-70b-8192"11
12def calculate(expression):13    """Tool to evaluate a mathematical expression"""14    try:15        result = eval(expression)16        return json.dumps({"result": result})17    except:18        return json.dumps({"error": "Invalid expression"})19
20def route_query(query):21    """Routing logic to let LLM decide if tools are needed"""22    routing_prompt = f"""
23    Given the following user query, determine if any tools are needed to answer it.
24    If a calculation tool is needed, respond with 'TOOL: CALCULATE'.
25    If no tools are needed, respond with 'NO TOOL'.
26
27    User query: {query}28
29    Response:
30    """31
32    response = client.chat.completions.create(33        model=ROUTING_MODEL,34        messages=[35            {"role": "system", "content": "You are a routing assistant. Determine if tools are needed based on the user query."},36            {"role": "user", "content": routing_prompt}37        ],38        max_tokens=20  # We only need a short response39    )40
41    routing_decision = response.choices[0].message.content.strip()42
43    if "TOOL: CALCULATE" in routing_decision:44        return "calculate tool needed"45    else:46        return "no tool needed"47
48def run_with_tool(query):49    """Use the tool use model to perform the calculation"""50    messages = [51        {52            "role": "system",53            "content": "You are a calculator assistant. Use the calculate function to perform mathematical operations and provide the results.",54        },55        {56            "role": "user",57            "content": query,58        }59    ]60    tools = [61        {62            "type": "function",63            "function": {64                "name": "calculate",65                "description": "Evaluate a mathematical expression",66                "parameters": {67                    "type": "object",68                    "properties": {69                        "expression": {70                            "type": "string",71                            "description": "The mathematical expression to evaluate",72                        }73                    },74                    "required": ["expression"],75                },76            },77        }78    ]79    response = client.chat.completions.create(80        model=TOOL_USE_MODEL,81        messages=messages,82        tools=tools,83        tool_choice="auto",84        max_tokens=409685    )86    response_message = response.choices[0].message
87    tool_calls = response_message.tool_calls
88    if tool_calls:89        messages.append(response_message)90        for tool_call in tool_calls:91            function_args = json.loads(tool_call.function.arguments)92            function_response = calculate(function_args.get("expression"))93            messages.append(94                {95                    "tool_call_id": tool_call.id,96                    "role": "tool",97                    "name": "calculate",98                    "content": function_response,99                }100            )101        second_response = client.chat.completions.create(102            model=TOOL_USE_MODEL,103            messages=messages
104        )105        return second_response.choices[0].message.content
106    return response_message.content
107
108def run_general(query):109    """Use the general model to answer the query since no tool is needed"""110    response = client.chat.completions.create(111        model=GENERAL_MODEL,112        messages=[113            {"role": "system", "content": "You are a helpful assistant."},114            {"role": "user", "content": query}115        ]116    )117    return response.choices[0].message.content
118
119def process_query(query):120    """Process the query and route it to the appropriate model"""121    route = route_query(query)122    if route == "calculate":123        response = run_with_tool(query)124    else:125        response = run_general(query)126
127    return {128        "query": query,129        "route": route,130        "response": response
131    }132
133# Example usage134if __name__ == "__main__":135    queries = [136        "What is the capital of the Netherlands?",137        "Calculate 25 * 4 + 10"138    ]139
140    for query in queries:141        result = process_query(query)142        print(f"Query: {result['query']}")143        print(f"Route: {result['route']}")144        print(f"Response: {result['response']}\n")
```

## Parallel Tool Use

We learned about tool use and built single-turn tool use examples above. Now let's take tool use a step further and imagine a workflow where multiple tools can be called simultaneously, enabling more efficient and effective responses.

This concept is known as **parallel tool use** and is key for building agentic workflows that can deal with complex queries, which is a great example of where inference speed becomes increasingly important (and thankfully we can access fast inference speed with Groq API).

N**ote:** Parallel tool use is natively enabled for all Llama 3 and Llama 3.1 models!

Here's an example of parallel tool use with a tool for getting the temperature and the tool for getting the weather condition to show parallel tool use with Groq API in action:

```
1import json
2from groq import Groq
3import os
4
5# Initialize Groq client6client = Groq()7model = "llama3-groq-70b-8192-tool-use-preview"8
9# Define weather tools10def get_temperature(location: str):11    # This is a mock tool/function. In a real scenario, you would call a weather API.12    temperatures = {"New York": 22, "London": 18, "Tokyo": 26, "Sydney": 20}13    return temperatures.get(location, "Temperature data not available")14
15def get_weather_condition(location: str):16    # This is a mock tool/function. In a real scenario, you would call a weather API.17    conditions = {"New York": "Sunny", "London": "Rainy", "Tokyo": "Cloudy", "Sydney": "Clear"}18    return conditions.get(location, "Weather condition data not available")19
20# Define system messages and tools21messages = [22    {"role": "system", "content": "You are a helpful weather assistant."},23    {"role": "user", "content": "What's the weather like in New York and London?"},24]25
26tools = [27    {28        "type": "function",29        "function": {30            "name": "get_temperature",31            "description": "Get the temperature for a given location",32            "parameters": {33                "type": "object",34                "properties": {35                    "location": {36                        "type": "string",37                        "description": "The name of the city",38                    }39                },40                "required": ["location"],41            },42        },43    },44    {45        "type": "function",46        "function": {47            "name": "get_weather_condition",48            "description": "Get the weather condition for a given location",49            "parameters": {50                "type": "object",51                "properties": {52                    "location": {53                        "type": "string",54                        "description": "The name of the city",55                    }56                },57                "required": ["location"],58            },59        },60    }61]62
63# Make the initial request64response = client.chat.completions.create(65    model=model, messages=messages, tools=tools, tool_choice="auto", max_tokens=409666)67
68response_message = response.choices[0].message
69tool_calls = response_message.tool_calls
70
71# Process tool calls72messages.append(response_message)73
74available_functions = {75    "get_temperature": get_temperature,76    "get_weather_condition": get_weather_condition,77}78
79for tool_call in tool_calls:80    function_name = tool_call.function.name
81    function_to_call = available_functions[function_name]82    function_args = json.loads(tool_call.function.arguments)83    function_response = function_to_call(**function_args)84
85    messages.append(86        {87            "role": "tool",88            "content": str(function_response),89            "tool_call_id": tool_call.id,90        }91    )92
93# Make the final request with tool call results94final_response = client.chat.completions.create(95    model=model, messages=messages, tools=tools, tool_choice="auto", max_tokens=409696)97
98print(final_response.choices[0].message.content)
```

## Error Handling

Groq API tool use is designed to verify whether a model generates a valid tool call object. When a model fails to generate a valid tool call object, Groq API will return a 400 error with an explanation in the "failed_generation" field of the JSON body that is returned.

### [Next Steps](https://console.groq.com/docs/tool-use#next-steps)

For more information and examples of working with multiple tools in parallel using Groq API and Instructor, see our Groq API Cookbook tutorial [here](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/parallel-tool-use/parallel-tool-use.ipynb).

## Tool Use with Structured Outputs (Python)

Groq API offers best-effort matching for parameters, which means the model could occasionally miss parameters or misinterpret types for more complex tool calls. We recommend the [Instuctor](https://python.useinstructor.com/hub/groq/) library to simplify the process of working with structured data and to ensure that the model's output adheres to a predefined schema.

Here's an example of how to implement tool use using the Instructor library with Groq API:

```
pip install instructor pydantic
```

```
1import instructor
2from pydantic import BaseModel, Field
3from groq import Groq
4
5# Define the tool schema6tool_schema = {7    "name": "get_weather_info",8    "description": "Get the weather information for any location.",9    "parameters": {10        "type": "object",11        "properties": {12            "location": {13                "type": "string",14                "description": "The location for which we want to get the weather information (e.g., New York)"15            }16        },17        "required": ["location"]18    }19}20
21# Define the Pydantic model for the tool call22class ToolCall(BaseModel):23    input_text: str = Field(description="The user's input text")24    tool_name: str = Field(description="The name of the tool to call")25    tool_parameters: str = Field(description="JSON string of tool parameters")26
27class ResponseModel(BaseModel):28    tool_calls: list[ToolCall]29
30# Patch Groq() with instructor31client = instructor.from_groq(Groq(), mode=instructor.Mode.JSON)32
33def run_conversation(user_prompt):34    # Prepare the messages35    messages = [36        {37            "role": "system",38            "content": f"You are an assistant that can use tools. You have access to the following tool: {tool_schema}"39        },40        {41            "role": "user",42            "content": user_prompt,43        }44    ]45
46    # Make the Groq API call47    response = client.chat.completions.create(48        model="llama-3.1-70b-versatile",49        response_model=ResponseModel,50        messages=messages,51        temperature=0.7,52        max_tokens=1000,53    )54
55    return response.tool_calls
56
57# Example usage58user_prompt = "What's the weather like in San Francisco?"59tool_calls = run_conversation(user_prompt)60
61for call in tool_calls:62    print(f"Input: {call.input_text}")63    print(f"Tool: {call.tool_name}")64    print(f"Parameters: {call.tool_parameters}")65    print()
```

### [Benefits of Using Structured Outputs](https://console.groq.com/docs/tool-use#benefits-of-using-structured-outputs)

- Type Safety: Pydantic models ensure that output adheres to the expected structure, reducing the risk of errors.
- Automatic Validation: Instructor automatically validates the model's output against the defined schema.

### [Next Steps](https://console.groq.com/docs/tool-use#next-steps)