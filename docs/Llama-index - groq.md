Here's a cleaned and formatted version of the documentation:

---

### Groq

Welcome to Groq! 🚀 At Groq, we've developed the world's first **Language Processing Unit™ (LPU)**. The Groq LPU features a deterministic, single-core streaming architecture, setting the standard for **GenAI inference speed** with predictable and repeatable performance for any given workload.

Beyond the architecture, our software is designed to empower developers with the tools needed to create innovative, powerful AI applications. With Groq as your engine, you can:

- Achieve uncompromised low latency and performance for real-time AI and HPC inferences 🔥
- Know the exact performance and compute time for any given workload 🔮
- Take advantage of our cutting-edge technology to stay ahead of the competition 💪

For more information, visit our [website](https://groq.com) and join our [Discord community](https://discord.com/invite/groq) to connect with our developers!

---

### Setup

If you're opening this notebook on Colab, you may need to install LlamaIndex 🦙:

```bash
% pip install llama-index-llms-groq
!pip install llama-index
```

```python
from llama_index.llms.groq import Groq
```

Note: None of PyTorch, TensorFlow (>= 2.0), or Flax have been found. Models won't be available; only tokenizers, configurations, and file/data utilities can be used.

To use Groq, create an API key at the Groq console, then set it as an environment variable:

```bash
export GROQ_API_KEY=<your_api_key>
```

Alternatively, you can pass your API key directly when initializing the LLM:

```python
llm = Groq(model="llama3-70b-8192", api_key="your_api_key")
```

A list of available LLM models can be found [here](https://groq.com/models).

---

### Example Usage

**Completion Example:**

```python
response = llm.complete("Explain the importance of low latency LLMs")
print(response)
```

**Output:**

> Low latency Large Language Models (LLMs) are important in certain applications due to their ability to process and respond to inputs quickly. Latency refers to the time delay between a user's request and the system's response. In some real-time or time-sensitive applications, low latency is critical to ensure a smooth user experience and prevent delays or lag.

> For example, in conversational agents or chatbots, users expect quick and responsive interactions. If the system takes too long to respond, it can negatively impact the user experience. Similarly, in applications like real-time language translation or speech recognition, low latency is essential to provide accurate and timely feedback.

> Furthermore, low latency LLMs can enable new use cases requiring real-time processing of language inputs, such as autonomous vehicles that need real-time speech recognition and natural language understanding.

> In summary, low latency LLMs are crucial for providing a smooth user experience, enabling real-time processing, and unlocking new use cases.

---

**Chat Example:**

```python
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are a pirate with a colorful personality"),
    ChatMessage(role="user", content="What is your name"),
]
resp = llm.chat(messages)
print(resp)
```

**Output:**

> Arr, I be known as Captain Redbeard, the fiercest pirate on the seven seas! But ye can call me Cap'n Redbeard for short. I'm a fearsome pirate with a love for treasure and adventure, and I'm always ready for a good time! Whether I'm swabbin' the deck or swiggin' grog, I'm always up for a bit of fun. So hoist the Jolly Roger and let's set sail for adventure, me hearties!

---

### Streaming

**Using `stream_complete` Endpoint**

```python
response = llm.stream_complete("Explain the importance of low latency LLMs")
for r in response:
    print(r.delta, end="")
```

**Output:**

> Low latency Large Language Models (LLMs) are important in the field of AI and NLP due to several reasons:
> 
> 1. **Real-time applications:** Essential for chatbots, voice assistants, and translation services where immediate response is crucial.
> 2. **Improved user experience:** Provides seamless and responsive interactions, increasing user engagement.
> 3. **Better decision-making:** Crucial for fields like financial trading and autonomous vehicles where real-time data is necessary.
> 4. **Scalability:** Supports handling higher volumes of requests efficiently.
> 5. **Competitive advantage:** Crucial for industries where responsiveness is critical, like online gaming or e-commerce.

**Using `stream_chat` Endpoint**

```python
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are a pirate with a colorful personality"),
    ChatMessage(role="user", content="What is your name"),
]
resp = llm.stream_chat(messages)
for r in resp:
    print(r.delta, end="")
```

**Output:**

> Arr, I be known as Captain Candybeard! A more colorful and swashbuckling pirate, ye will never find!

---