================
CODE SNIPPETS
================
TITLE: Run Examples
DESCRIPTION: This snippet shows how to execute the example Python scripts within the directory. It requires Python 3 to be installed.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_0

LANGUAGE: sh
CODE:
```
# Run example
python3 examples/<example>.py
```

--------------------------------

TITLE: List Ollama Models
DESCRIPTION: Example demonstrating how to list all models downloaded to Ollama, along with their properties.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_6

LANGUAGE: python
CODE:
```
import ollama

# List models
models = ollama.list()
for model in models['models']:
    print(f"- {model['name']}")
```

--------------------------------

TITLE: Create Ollama Model
DESCRIPTION: Example demonstrating how to create a new Ollama model from a Modelfile.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_10

LANGUAGE: python
CODE:
```
import ollama

# Create a model from a Modelfile
# with open('Modelfile', 'r') as f:
#     modelfile_content = f.read()
# ollama.create(model='my-custom-model', modelfile=modelfile_content)
```

--------------------------------

TITLE: Tools/Function Calling with a Model
DESCRIPTION: Examples demonstrating how to use tools and function calling with Ollama models. Includes simple examples, asynchronous calls, using multiple tools, and enabling thinking mode.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_3

LANGUAGE: python
CODE:
```
import ollama

# Simple tools example
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'What is the weather in San Francisco?',
        }
    ],
    tools=[
        {
            'type': 'function',
            'function': {
                'name': 'get_weather',
                'description': 'get the weather for a location',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'location': {
                            'type': 'string',
                            'description': 'the location to get the weather for',
                        }
                    },
                    'required': ['location'],
                },
            }
        }
    ]
)

# print(response['message']['tool_calls'][0]['function']['arguments'])

# Async tools example
# async def async_tools():
#     response = await ollama.chat(
#         model='llama2',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'What is the weather in San Francisco?',
#             }
#         ],
#         tools=[
#             {
#                 'type': 'function',
#                 'function': {
#                     'name': 'get_weather',
#                     'description': 'get the weather for a location',
#                     'parameters': {
#                         'type': 'object',
#                         'properties': {
#                             'location': {
#                                 'type': 'string',
#                                 'description': 'the location to get the weather for',
#                             }
#                         },
#                         'required': ['location'],
#                     },
#                 }
#             }
#         ]
#     )
#     print(response['message']['tool_calls'][0]['function']['arguments'])

# asyncio.run(async_tools())

# Multi-tool example
# response = ollama.chat(
#     model='llama2',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'What is the weather in Paris and what is the capital of France?',
#         }
#     ],
#     tools=[
#         {
#             'type': 'function',
#             'function': {
#                 'name': 'get_weather',
#                 'description': 'get the weather for a location',
#                 'parameters': {
#                     'type': 'object',
#                     'properties': {
#                         'location': {
#                             'type': 'string',
#                             'description': 'the location to get the weather for',
#                         }
#                     },
#                     'required': ['location'],
#                 },
#             }
#         },
#         {
#             'type': 'function',
#             'function': {
#                 'name': 'get_capital',
#                 'description': 'get the capital of a country',
#                 'parameters': {
#                     'type': 'object',
#                     'properties': {
#                         'country': {
#                             'type': 'string',
#                             'description': 'the country to get the capital for',
#                         }
#                     },
#                     'required': ['country'],
#                 },
#             }
#         }
#     ]
# )
# 
# print(response['message']['tool_calls'])

# gpt-oss tools example
# response = ollama.chat(
#     model='gpt-oss',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'What is the weather in London?',
#         }
#     ],
#     tools=[
#         {
#             'type': 'function',
#             'function': {
#                 'name': 'get_weather',
#                 'description': 'get the weather for a location',
#                 'parameters': {
#                     'type': 'object',
#                     'properties': {
#                         'location': {
#                             'type': 'string',
#                             'description': 'the location to get the weather for',
#                         }
#                     },
#                     'required': ['location'],
#                 },
#             }
#         }
#     ]
# )
# 
# print(response['message']['tool_calls'][0]['function']['arguments'])

# gpt-oss tools stream example
# stream = ollama.chat(
#     model='gpt-oss',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'What is the weather in London?',
#         }
#     ],
#     tools=[
#         {
#             'type': 'function',
#             'function': {
#                 'name': 'get_weather',
#                 'description': 'get the weather for a location',
#                 'parameters': {
#                     'type': 'object',
#                     'properties': {
#                         'location': {
#                             'type': 'string',
#                             'description': 'the location to get the weather for',
#                         }
#                     },
#                     'required': ['location'],
#                 },
#             }
#         }
#     ],
#     stream=True
# )
# 
# for chunk in stream:
#     print(chunk['message']['tool_calls'][0]['function']['arguments'], end='', flush=True)
```

--------------------------------

TITLE: Pull Ollama Model
DESCRIPTION: Example for downloading a model from Ollama. Requires the `tqdm` library for progress visualization.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_9

LANGUAGE: python
CODE:
```
import ollama

# Pull a model
# ollama.pull('llama2')

# To use tqdm for progress, you would typically integrate it with the streaming response if available, or handle it manually.
```

--------------------------------

TITLE: Install Ollama Python Library
DESCRIPTION: Installs the Ollama Python library using pip. Ensure Python 3.8+ is installed.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_0

LANGUAGE: sh
CODE:
```
pip install ollama
```

--------------------------------

TITLE: Show Ollama Model Details
DESCRIPTION: Example for displaying detailed properties and capabilities of a specific Ollama model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_7

LANGUAGE: python
CODE:
```
import ollama

# Show model details
model_info = ollama.show(model='llama2')
print(f"Name: {model_info['name']}")
print(f"Digest: {model_info['digest']}")
print(f"Size: {model_info['size']} bytes")
print(f"Modelfile: {model_info['modelfile']}")
```

--------------------------------

TITLE: Pull a Model
DESCRIPTION: This example demonstrates how to pull a model from the Ollama registry. It requires the 'tqdm' library for progress visualization.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_16

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

# Ensure you have 'tqdm' installed: pip install tqdm
try:
    response = client.pull('llama2', stream=True)
    for chunk in response:
        print(chunk['status'], end=' ', flush=True)
    print("\nModel pulled successfully.")
except Exception as e:
    print(f"Error pulling model: {e}")

```

--------------------------------

TITLE: List Downloaded Models
DESCRIPTION: This example demonstrates how to list all models currently downloaded and available on the Ollama instance using the Python client.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_13

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

models = client.list()

for model in models['models']:
    print(f"- {model['name']} (Size: {model['size'] // (1024*1024)} MB)")

```

--------------------------------

TITLE: Show Model Properties
DESCRIPTION: This example shows how to retrieve detailed properties and information about a specific Ollama model, such as its parameters and template.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_14

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

model_details = client.show(name='llama2')

print(f"Model: {model_details['model']}")
print(f"Parameters: {model_details['parameters']}")
print(f"Template: {model_details['template']}")

```

--------------------------------

TITLE: Create a Model from Modelfile
DESCRIPTION: This example demonstrates how to create a new Ollama model from a Modelfile. The Modelfile specifies the base model, system prompt, and parameters.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_17

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

# Assume 'Modelfile' exists in the current directory
# Example Modelfile content:
# FROM ./my-base-model
# SYSTEM "You are a helpful assistant."
# PARAMETER temperature 0.8

try:
    response = client.create(model='my-custom-model', path='Modelfile', stream=True)
    for chunk in response:
        print(chunk['status'], end=' ', flush=True)
    print("\nModel created successfully.")
except Exception as e:
    print(f"Error creating model: {e}")

```

--------------------------------

TITLE: Show Ollama Model Status
DESCRIPTION: Example to display the status of running Ollama models, including their CPU and GPU usage.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_8

LANGUAGE: python
CODE:
```
import ollama

# Show running models
ps_info = ollama.ps()
for running_model in ps_info['running']:
    print(f"- {running_model['name']} (CPU: {running_model['cpu']}, GPU: {running_model['gpu']})")
```

--------------------------------

TITLE: Show Model Status (ps)
DESCRIPTION: This example demonstrates how to check the status of running models on the Ollama server, including CPU and GPU usage.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_15

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

status = client.ps()

if not status['models']:
    print("No models are currently running.")
else:
    for model_info in status['models']:
        print(f"Model: {model_info['name']}, CPU: {model_info['cpu']}%, Memory: {model_info['memory']}%")

```

--------------------------------

TITLE: Generate Embeddings
DESCRIPTION: This example demonstrates how to generate embedding vectors for a given text prompt using an Ollama model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_18

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

response = client.embeddings(
    model='llama2',
    prompt='This is a test sentence.',
)

print(f"Embedding vector (first 5 elements): {response['embedding'][:5]}...")
print(f"Embedding dimension: {len(response['embedding'])}")

```

--------------------------------

TITLE: Enable Thinking Mode
DESCRIPTION: Examples for enabling and controlling the 'thinking' mode in Ollama models, which allows the model to reason step-by-step.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_12

LANGUAGE: python
CODE:
```
import ollama

# Enable thinking mode
# response = ollama.chat(
#     model='llama2',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Solve this math problem: 5 + 3 * 2'
#         }
#     ],
#     options={'num_predict': 100, 'temperature': 0.8, 'stop': ['\n']},
#     stream=True
# )
# 
# for chunk in response:
#     print(chunk['message']['content'], end='', flush=True)

# Thinking (levels) - Choose the thinking level
# response = ollama.chat(
#     model='llama2',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Solve this math problem: 5 + 3 * 2'
#         }
#     ],
#     options={'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'embedding_only': False, 'context': None, 'system': None, 'template': None, 'format': None, 'keep_alive': None, 'timeout': None, 'model': 'llama2', 'options': {'num_predict': 100, 'temperature': 0.8, 'stop': ['\n'], 'num_ctx': 4096, 'num_batch': 20, 'num_gpu': 1, 'num_gpus': 1, 'main_gpu': 0, 'low_vram': False, 'mmap': True, 'mlock': False, 'embeddings': True, 'num_thread': 1, 'repeat_last_n': 64, 'repeat_penalty': 1.1, 'presence_penalty': 0.0, 'frequency_penalty': 0.0, 'top_k': 40, 'top_p': 0.9, 'tfs_z': 1.0, 'mirostat': 0.0, 'mirostat_lr': 0.0, 'mirostat_ent': 0.0, 'num_keep': 0, 'seed': 0, 'num_return_sequences': 1, 'temperature': 0.8, 'stop': ['\n'], 'num_predict': 100, 'beam_size': 1, 'logits_bias': None, 'num_ctx': 4096, '
```

--------------------------------

TITLE: Multimodal Chat with Images
DESCRIPTION: Examples for engaging in chat conversations with multimodal models that can process images. Includes both chat and generation use cases.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_4

LANGUAGE: python
CODE:
```
import ollama

# Multimodal chat
# response = ollama.chat(
#     model='llava',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'What is in this image?',
#             'attachments': [
#                 './test.png'
#             ]
#         }
#     ]
# )
# print(response['message']['content'])

# Multimodal generate
# response = ollama.generate(
#     model='llava',
#     prompt='What is in this image?',
#     images=['./test.png']
# )
# print(response['response'])
```

--------------------------------

TITLE: Generate Text with a Model
DESCRIPTION: Examples for generating text using Ollama models. Covers basic generation, asynchronous generation, streamed outputs, and filling in the middle of text.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_2

LANGUAGE: python
CODE:
```
import ollama

# Generate text
response = ollama.generate(model='llama2', prompt='Why is the sky blue?')
print(response['response'])

# Async generate
# async def async_generate():
#     response = await ollama.generate(model='llama2', prompt='Why is the sky blue?')
#     print(response['response'])
# 
# asyncio.run(async_generate())

# Generate stream
# stream = ollama.generate(
#     model='llama2',
#     prompt='Why is the sky blue?',
#     stream=True,
# )
# 
# for chunk in stream:
#     print(chunk['response'], end='', flush=True)

# Fill in the middle
# response = ollama.generate(
#     model='llama2',
#     prompt='The quick brown fox', 
#     suffix=' jumps over the lazy dog',
#     options={"stop": ["\n"]}
# )
# print(response['response'])
```

--------------------------------

TITLE: Chat with a Model
DESCRIPTION: Examples for interacting with Ollama models in a chat format. Includes basic chat, asynchronous chat, streamed outputs, and maintaining conversation history.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_1

LANGUAGE: python
CODE:
```
import ollama

# Basic chat
response = ollama.chat(model='llama2', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response['message']['content'])

# Async chat
import asyncio

async def async_chat():
    response = await ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue?',
            },
        ],
    )
    print(response['message']['content'])

# asyncio.run(async_chat())

# Streamed chat
# stream = ollama.chat(
#     model='llama2',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Why is the sky blue?',
#         },
#     ],
#     stream=True,
# )
# 
# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)

# Chat with history
# messages = [
#   {
#     'role': 'user',
#     'content': 'Hello!',
#   },
# ]
# 
# response = ollama.chat(model='llama2', messages=messages)
# messages.append(response['message'])
# 
# response = ollama.chat(model='llama2', messages=messages)
# print(response['message']['content'])
```

--------------------------------

TITLE: Generate Embeddings with Ollama
DESCRIPTION: Example for generating embeddings (vector representations) for given text using an Ollama model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_11

LANGUAGE: python
CODE:
```
import ollama

# Generate embeddings
response = ollama.embeddings(model='llama2', prompt='This is a test sentence.')
# print(response['embedding'][:10]) # Print first 10 dimensions
```

--------------------------------

TITLE: Generate Structured Outputs
DESCRIPTION: Examples for generating structured data, such as JSON, from Ollama models. Supports both synchronous and asynchronous operations, and can include image inputs.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_5

LANGUAGE: python
CODE:
```
import ollama

# Structured outputs
# response = ollama.chat(
#     model='llama2',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Provide a JSON object with the following information: name, age, city. Name: John Doe, Age: 30, City: New York'
#         }
#     ],
#     format='json'
# )
# print(response['message']['content'])

# Async structured outputs
# async def async_structured_outputs():
#     response = await ollama.chat(
#         model='llama2',
#         messages=[
#             {
#                 'role': 'user',
#                 'content': 'Provide a JSON object with the following information: name, age, city. Name: John Doe, Age: 30, City: New York'
#             }
#         ],
#         format='json'
#     )
#     print(response['message']['content'])
# 
# asyncio.run(async_structured_outputs())

# Structured outputs with image
# response = ollama.chat(
#     model='llava',
#     messages=[
#         {
#             'role': 'user',
#             'content': 'Describe this image in JSON format with keys "description" and "objects".',
#             'attachments': [
#                 './test.png'
#             ]
#         }
#     ],
#     format='json'
# )
# print(response['message']['content'])
```

--------------------------------

TITLE: Enable Thinking Mode (Generate)
DESCRIPTION: This example shows how to enable 'thinking' mode for text generation by setting specific options, allowing the model to output intermediate reasoning steps.

SOURCE: https://github.com/ollama/ollama-python/blob/main/examples/README.md#_snippet_19

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client('http://localhost:11434')

# Setting num_predict to a high value and a specific stop token
# can encourage the model to output its thought process.
response = client.generate(
    model='llama2',
    prompt='Solve the following math problem step-by-step: 5 + 3 * 2',
    options={
        'num_predict': 100, # Predict more tokens to allow for steps
        'stop': ['\n\n'], # Stop after a double newline, often separating thoughts
    },
    stream=True
)

for chunk in response:
    print(chunk['response'], end='', flush=True)
print()

```

--------------------------------

TITLE: Dependency Hashes for Ollama Python
DESCRIPTION: This snippet details the dependencies required for the Ollama Python project. It includes package names, versions, and their corresponding SHA256 hashes, which are crucial for verifying the integrity and authenticity of the installed packages. The dependencies are listed with their direct requirements and also indicate which packages they are transitively required by.

SOURCE: https://github.com/ollama/ollama-python/blob/main/requirements.txt#_snippet_3

LANGUAGE: python
CODE:
```
--hash=sha256:e0fd26b16394ead34a424eecf8a31a1f5137094cabe84a1bcb10fa6ba39d3d31 
--hash=sha256:e2bb4d3e5873c37bb3dd58714d4cd0b0e6238cebc4177ac8fe878f8b3aa8e74c 
--hash=sha256:eb026e5a4c1fee05726072337ff51d1efb6f59090b7da90d30ea58625b1ffb39 
--hash=sha256:eda3f5c2a021bbc5d976107bb302e0131351c2ba54343f8a496dc8783d3d3a6a 
--hash=sha256:ef592d4bad47296fb11f96cd7dc898b92e795032b4894dfb4076cfccd43a9308 
--hash=sha256:f141ee28a0ad2123b6611b6ceff018039df17f32ada8b534e6aa039545a3efb2 
--hash=sha256:f66d89ba397d92f840f8654756196d93804278457b5fbede59598a1f9f90b228 
--hash=sha256:f6f8e111843bbb0dee4cb6594cdc73e79b3329b526037ec242a3e49012495b3b 
--hash=sha256:fa8e459d4954f608fa26116118bb67f56b93b209c39b008277ace29937453dc9 
--hash=sha256:fd1aea04935a508f62e0d0ef1f5ae968774a32afc306fb8545e06f5ff5cdf3ad
```

LANGUAGE: python
CODE:
```
sniffio==1.3.1 
    --hash=sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2 
    --hash=sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc
```

LANGUAGE: python
CODE:
```
typing-extensions==4.12.2 
    --hash=sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d 
    --hash=sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8
```

--------------------------------

TITLE: Async Chat with Ollama
DESCRIPTION: Demonstrates asynchronous chat interactions using `AsyncClient`. It shows how to make an async call and run it using `asyncio`.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_4

LANGUAGE: python
CODE:
```
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  response = await AsyncClient().chat(model='gemma3', messages=[message])

asyncio.run(chat())
```

--------------------------------

TITLE: Custom Ollama Client
DESCRIPTION: Shows how to create a custom Ollama client with specific host and headers. It passes extra keyword arguments to the underlying `httpx.Client`.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_3

LANGUAGE: python
CODE:
```
from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
```

--------------------------------

TITLE: Ollama API: Create Model
DESCRIPTION: Creates a new Ollama model from a specified base model and system prompt.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_10

LANGUAGE: APIDOC
CODE:
```
ollama.create(model='example', from_='gemma3', system="You are Mario from Super Mario Bros.")
```

--------------------------------

TITLE: Project Dependencies
DESCRIPTION: This snippet lists the direct and transitive dependencies for the Ollama Python project. It includes package names, version constraints, and SHA256 hashes for integrity verification. These dependencies are crucial for setting up and running the project correctly.

SOURCE: https://github.com/ollama/ollama-python/blob/main/requirements.txt#_snippet_1

LANGUAGE: python
CODE:
```
annotated-types==0.7.0 \
    --hash=sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53 \
    --hash=sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89
    # via pydantic
anyio==4.5.2 ; python_full_version < '3.9' \
    --hash=sha256:23009af4ed04ce05991845451e11ef02fc7c5ed29179ac9a420e5ad0ac7ddc5b \
    --hash=sha256:c011ee36bc1e8ba40e5a81cb9df91925c218fe9b778554e0b56a21e1b5d4716f
    # via httpx
anyio==4.8.0 ; python_full_version >= '3.9' \
    --hash=sha256:1d9fe889df5212298c0c0723fa20479d1b94883a2df44bd3897aa91083316f7a \
    --hash=sha256:b5011f270ab5eb0abf13385f851315585cc37ef330dd88e27ec3d34d651fd47a
    # via httpx
certifi==2025.1.31 \
    --hash=sha256:3d5da6925056f6f18f119200434a4780a94263f10d1c21d032a6f6b2baa20651 \
    --hash=sha256:ca78db4565a652026a4db2bcdf68f2fb589ea80d0be70e03929ed730746b84fe
    # via
    #   httpcore
    #   httpx
exceptiongroup==1.2.2 ; python_full_version < '3.11' \
    --hash=sha256:3111b9d131c238bec2f8f516e123e14ba243563fb135d3fe885990585aa7795b \
    --hash=sha256:47c2edf7c6738fafb49fd34290706d1a1a2f4d1c6df275526b62cbb4aa5393cc
    # via anyio
h11==0.14.0 \
    --hash=sha256:8f19fbbe99e72420ff35c00b27a34cb9937e902a8b810e2c88300c6f0a3b699d \
    --hash=sha256:e3fe4ac4b851c468cc8363d500db52c2ead036020723024a109d37346efaa761
    # via httpcore
httpcore==1.0.7 \
    --hash=sha256:8551cb62a169ec7162ac7be8d4817d561f60e08eaa485234898414bb5a8a0b4c \
    --hash=sha256:a3fff8f43dc260d5bd363d9f9cf1830fa3a458b332856f34282de498ed420edd
    # via httpx
httpx==0.28.1 \
    --hash=sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc \
    --hash=sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad
    # via ollama
idna==3.10 \
    --hash=sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9 \
    --hash=sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3
    # via
    #   anyio
    #   httpx
pydantic==2.10.6 \
    --hash=sha256:427d664bf0b8a2b34ff5dd0f5a18df00591adcee7198fbd71981054cef37b584 \
    --hash=sha256:ca5daa827cce33de7a42be142548b0096bf05a7e7b365aebfa5f8eeec7128236
    # via ollama
pydantic-core==2.27.2 \
    --hash=sha256:00bad2484fa6bda1e216e7345a798bd37c68fb2d97558edd584942aa41b7d278 \
    --hash=sha256:0296abcb83a797db256b773f45773da397da75a08f5fcaef41f2044adec05f50 \
    --hash=sha256:03d0f86ea3184a12f41a2d23f7ccb79cdb5a18e06993f8a45baa8dfec746f0e9 \
    --hash=sha256:044a50963a614ecfae59bb1eaf7ea7efc4bc62f49ed594e18fa1e5d953c40e9f \
    --hash=sha256:05e3a55d124407fffba0dd6b0c0cd056d10e983ceb4e5dbd10dda135c31071d6 \
    --hash=sha256:08e125dbdc505fa69ca7d9c499639ab6407cfa909214d500897d02afb816e7cc \
    --hash=sha256:097830ed52fd9e427942ff3b9bc17fab52913b2f50f2880dc4a5611446606a54 \
    --hash=sha256:0d1e85068e818c73e048fe28cfc769040bb1f475524f4745a5dc621f75ac7630 \
    --hash=sha256:0d75070718e369e452075a6017fbf187f788e17ed67a3abd47fa934d001863d9 \
    --hash=sha256:14d4a5c49d2f009d62a2a7140d3064f686d17a5d1a268bc641954ba181880236 \
    --hash=sha256:172fce187655fece0c90d90a678424b013f8fbb0ca8b036ac266749c09438cb7 \
    --hash=sha256:18a101c168e4e092ab40dbc2503bdc0f62010e95d292b27827871dc85450d7ee \
    --hash=sha256:1a4207639fb02ec2dbb76227d7c751a20b1a6b4bc52850568e52260cae64ca3b \
    --hash=sha256:1c1fd185014191700554795c99b347d64f2bb637966c4cfc16998a0ca700d048 \
    --hash=sha256:1e2cb691ed9834cd6a8be61228471d0a503731abfb42f82458ff27be7b2186fc \
    --hash=sha256:1ebaf1d0481914d004a573394f4be3a7616334be70261007e47c2a6fe7e50130 \
    --hash=sha256:220f892729375e2d736b97d0e51466252ad84c51857d4d15f5e9692f9ef12be4 \
    --hash=sha256:251136cdad0cb722e93732cb45ca5299fb56e1344a833640bf93b2803f8d1bfd \
    --hash=sha256:26f0d68d4b235a2bae0c3fc585c585b4ecc51382db0e3ba402a22cbc440915e4 \
    --hash=sha256:26f32e0adf166a84d0cb63be85c562ca8a6fa8de28e5f0d92250c6b7e9e2aff7 \
    --hash=sha256:280d219beebb0752699480fe8f1dc61ab6615c2046d76b7ab7ee38858de0a4e7 \
    --hash=sha256:28ccb213807e037460326424ceb8b5245acb88f32f3d2777427476e1b32c48c4 \
    --hash=sha256:2bf14caea37e91198329b828eae1618c068dfb8ef17bb33287a7ad4b61ac314e \
    --hash=sha256:2d367ca20b2f14095a8f4fa1210f5a7b78b8a20009ecced6b12818f455b1e9fa \
    --hash=sha256:30c5f68ded0c36466acede341551106821043e9afaad516adfb6e8fa80a4e6a6 \
    --hash=sha256:337b443af21d488716f8d0b6164de833e788aa6bd7e3a39c005febc1284f4962 \
    --hash=sha256:3911ac9284cd8a1792d3cb26a2da18f3ca26c6908cc434a18f730dc0db7bfa3b \
    --hash=sha256:3d591580c34f4d731592f0e9fe40f9cc1b430d297eecc70b962e93c5c668f15f \
    --hash=sha256:3de3ce3c9ddc8bbd88f6e0e304dea0e66d843ec9de1b0042b0911c1663ffd474 \
    --hash=sha256:3de9961f2a346257caf0aa508a4da705467f53778e9ef6fe744c038119737ef5 \
    --hash=sha256:40d02e7d45c9f8af700f3452f329ead92da4c5f4317ca9b896de7ce7199ea459 \
    --hash=sha256:42c5f762659e47fdb7b16956c71598292f60a03aa92f8b6351504359dbdba6cf
```

--------------------------------

TITLE: Ollama API: Ps
DESCRIPTION: Lists running Ollama models and their status.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_16

LANGUAGE: APIDOC
CODE:
```
ollama.ps()
```

--------------------------------

TITLE: Ollama API: List Models
DESCRIPTION: Lists all the models available in Ollama.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_8

LANGUAGE: APIDOC
CODE:
```
ollama.list()
```

--------------------------------

TITLE: Ollama API: Generate
DESCRIPTION: Generates text based on a prompt using a specified Ollama model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_7

LANGUAGE: APIDOC
CODE:
```
ollama.generate(model='gemma3', prompt='Why is the sky blue?')
```

--------------------------------

TITLE: Basic Chat with Ollama
DESCRIPTION: Demonstrates how to perform a basic chat interaction with an Ollama model. It shows how to access the response content directly or via object attributes.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_1

LANGUAGE: python
CODE:
```
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
```

--------------------------------

TITLE: Ollama API: Push Model
DESCRIPTION: Pushes an Ollama model to the registry.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
ollama.push('user/gemma3')
```

--------------------------------

TITLE: Ollama API: Chat
DESCRIPTION: Initiates a chat conversation with an Ollama model. Requires a model name and a list of messages.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_6

LANGUAGE: APIDOC
CODE:
```
ollama.chat(model='gemma3', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
```

--------------------------------

TITLE: Ollama Python Component Hashes
DESCRIPTION: This snippet contains a list of SHA256 hashes, likely used for verifying the integrity of downloaded models or project components. Each hash is prefixed with '--hash=sha256:'.

SOURCE: https://github.com/ollama/ollama-python/blob/main/requirements.txt#_snippet_2

LANGUAGE: shell
CODE:
```
--hash=sha256:47956ae78b6422cbd46f772f1746799cbb862de838fd8d1fbd34a82e05b0983a 
--hash=sha256:491a2b73db93fab69731eaee494f320faa4e093dbed776be1a829c2eb222c34c 
--hash=sha256:4c9775e339e42e79ec99c441d9730fccf07414af63eac2f0e48e08fd38a64d76 
--hash=sha256:4e0b4220ba5b40d727c7f879eac379b822eee5d8fff418e9d3381ee45b3b0362 
--hash=sha256:50a68f3e3819077be2c98110c1f9dcb3817e93f267ba80a2c05bb4f8799e2ff4 
--hash=sha256:519f29f5213271eeeeb3093f662ba2fd512b91c5f188f3bb7b27bc5973816934 
--hash=sha256:521eb9b7f036c9b6187f0b47318ab0d7ca14bd87f776240b90b21c1f4f149320 
--hash=sha256:57762139821c31847cfb2df63c12f725788bd9f04bc2fb392790959b8f70f118 
--hash=sha256:5e4f4bb20d75e9325cc9696c6802657b58bc1dbbe3022f32cc2b2b632c3fbb96 
--hash=sha256:5e68c4446fe0810e959cdff46ab0a41ce2f2c86d227d96dc3847af0ba7def306 
--hash=sha256:669e193c1c576a58f132e3158f9dfa9662969edb1a250c54d8fa52590045f046 
--hash=sha256:688d3fd9fcb71f41c4c015c023d12a79d1c4c0732ec9eb35d96e3388a120dcf3 
--hash=sha256:6fb4aadc0b9a0c063206846d603b92030eb6f03069151a625667f982887153e2 
--hash=sha256:7041c36f5680c6e0f08d922aed302e98b3745d97fe1589db0a3eebf6624523af 
--hash=sha256:71b24c7d61131bb83df10cc7e687433609963a944ccf45190cfc21e0887b08c9 
--hash=sha256:77d1bca19b0f7021b3a982e6f903dcd5b2b06076def36a652e3907f596e29f67 
--hash=sha256:7969e133a6f183be60e9f6f56bfae753585680f3b7307a8e555a948d443cc05a 
--hash=sha256:7a66efda2387de898c8f38c0cf7f14fca0b51a8ef0b24bfea5849f1b3c95af27 
--hash=sha256:7d0c8399fcc1848491f00e0314bd59fb34a9c008761bcb422a057670c3f65e35 
--hash=sha256:7d14bd329640e63852364c306f4d23eb744e0f8193148d4044dd3dacdaacbd8b 
--hash=sha256:7e17b560be3c98a8e3aa66ce828bdebb9e9ac6ad5466fba92eb74c4c95cb1151 
--hash=sha256:8083d4e875ebe0b864ffef72a4304827015cff328a1be6e22cc850753bfb122b 
--hash=sha256:82f91663004eb8ed30ff478d77c4d1179b3563df6cdb15c0817cd1cdaf34d154 
--hash=sha256:82f986faf4e644ffc189a7f1aafc86e46ef70372bb153e7001e8afccc6e54133 
--hash=sha256:83097677b8e3bd7eaa6775720ec8e0405f1575015a463285a92bfdfe254529ef 
--hash=sha256:85210c4d99a0114f5a9481b44560d7d1e35e32cc5634c656bc48e590b669b145 
--hash=sha256:8c19d1ea0673cd13cc2f872f6c9ab42acc4e4f492a7ca9d3795ce2b112dd7e15 
--hash=sha256:8d9b3388db186ba0c099a6d20f0604a44eabdeef1777ddd94786cdae158729e4 
--hash=sha256:8e10c99ef58cfdf2a66fc15d66b16c4a04f62bca39db589ae8cba08bc55331bc 
--hash=sha256:953101387ecf2f5652883208769a79e48db18c6df442568a0b5ccd8c2723abee 
--hash=sha256:9c3ed807c7b91de05e63930188f19e921d1fe90de6b4f5cd43ee7fcc3525cb8c 
--hash=sha256:9e0c8cfefa0ef83b4da9588448b6d8d2a2bf1a53c3f1ae5fca39eb3061e2f0b0 
--hash=sha256:9fdbe7629b996647b99c01b37f11170a57ae675375b14b8c13b8518b8320ced5 
--hash=sha256:a0fcd29cd6b4e74fe8ddd2c90330fd8edf2e30cb52acda47f06dd615ae72da57 
--hash=sha256:ac4dbfd1691affb8f48c2c13241a2e3b60ff23247cbcf981759c768b6633cf8b 
--hash=sha256:b0cb791f5b45307caae8810c2023a184c74605ec3bcbb67d13846c28ff731ff8 
--hash=sha256:ba5dd002f88b78a4215ed2f8ddbdf85e8513382820ba15ad5ad8955ce0ca19a1 
--hash=sha256:bca101c00bff0adb45a833f8451b9105d9df18accb8743b08107d7ada14bd7da 
--hash=sha256:bd8086fa684c4775c27f03f062cbb9eaa6e17f064307e86b21b9e0abc9c0f02e 
--hash=sha256:bec317a27290e2537f922639cafd54990551725fc844249e64c523301d0822fc 
--hash=sha256:c10eb4f1659290b523af58fa7cffb452a61ad6ae5613404519aee4bfbf1df993 
--hash=sha256:c33939a82924da9ed65dab5a65d427205a73181d8098e79b6b426bdf8ad4e656 
--hash=sha256:c61709a844acc6bf0b7dce7daae75195a10aac96a596ea1b776996414791ede4 
--hash=sha256:c70c26d2c99f78b125a3459f8afe1aed4d9687c24fd677c6a4436bc042e50d6c 
--hash=sha256:c817e2b40aba42bac6f457498dacabc568c3b7a986fc9ba7c8d9d260b71485fb 
--hash=sha256:cabb9bcb7e0d97f74df8646f34fc76fbf793b7f6dc2438517d7a9e50eee4f14d 
--hash=sha256:cc3f1a99a4f4f9dd1de4fe0312c114e740b5ddead65bb4102884b384c15d8bc9 
--hash=sha256:cca63613e90d001b9f2f9a9ceb276c308bfa2a43fafb75c8031c4f66039e8c6e 
--hash=sha256:ce8918cbebc8da707ba805b7fd0b382816858728ae7fe19a942080c24e5b7cd1 
--hash=sha256:d2088237af596f0a524d3afc39ab3b036e8adb054ee57cbb1dcf8e09da5b29cc 
--hash=sha256:d262606bf386a5ba0b0af3b97f37c83d7011439e3dc1a9298f21efb292e42f1a 
--hash=sha256:d2d63f1215638d28221f664596b1ccb3944f6e25dd18cd3b86b0a4c408d5ebb9 
--hash=sha256:d3e8d504bdd3f10835468f29008d72fc8359d95c9c415ce6e767203db6127506 
--hash=sha256:d4041c0b966a84b4ae7a09832eb691a35aec90910cd2dbe7a208de59be77965b 
--hash=sha256:d716e2e30c6f140d7560ef1538953a5cd1a87264c737643d481f2779fc247fe1 
--hash=sha256:d81d2068e1c1228a565af076598f9e7451712700b673de8f502f0334f281387d 
--hash=sha256:d9640b0059ff4f14d1f37321b94061c6db164fbe49b334b31643e0528d100d99 
--hash=sha256:de3cd1899e2c279b140adde9357c4495ed9d47131b4a4eaff9052f23398076b3
```

--------------------------------

TITLE: Async Streaming Responses from Ollama
DESCRIPTION: Illustrates how to handle streaming responses asynchronously using `AsyncClient`. It uses an async generator to process streamed chunks.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_5

LANGUAGE: python
CODE:
```
import asyncio
from ollama import AsyncClient

async def chat():
  message = {'role': 'user', 'content': 'Why is the sky blue?'}
  async for part in await AsyncClient().chat(model='gemma3', messages=[message], stream=True):
    print(part['message']['content'], end='', flush=True)

asyncio.run(chat())
```

--------------------------------

TITLE: Ollama API Reference
DESCRIPTION: This section provides a comprehensive reference for the Ollama API endpoints, detailing available methods, parameters, request bodies, and responses. It covers functionalities such as model management, generation, embeddings, and chat interactions.

SOURCE: https://github.com/ollama/ollama-python/blob/main/requirements.txt#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Ollama API Reference:

Models:
  GET /api/tags
    Description: List available models.
    Returns: JSON object containing a list of model tags.

  POST /api/pull
    Description: Pull a model from a registry.
    Request Body:
      - name: string (required) - The name of the model to pull.
      - insecure: boolean (optional) - Allow insecure connections.
      - stream: boolean (optional) - Stream the response.
    Returns: JSON object with status information.

  POST /api/push
    Description: Push a model to a registry.
    Request Body:
      - name: string (required) - The name of the model to push.
      - insecure: boolean (optional) - Allow insecure connections.
      - stream: boolean (optional) - Stream the response.
    Returns: JSON object with status information.

  DELETE /api/delete
    Description: Delete a model.
    Request Body:
      - name: string (required) - The name of the model to delete.
      - insecure: boolean (optional) - Allow insecure connections.
    Returns: JSON object with status information.

Generation:
  POST /api/generate
    Description: Generate a response from a model.
    Request Body:
      - model: string (required) - The name of the model to use.
      - prompt: string (required) - The prompt to send to the model.
      - system: string (optional) - The system prompt.
      - template: string (optional) - The prompt template.
      - stream: boolean (optional) - Stream the response.
      - options: object (optional) - Model-specific options.
      - keep_alive: integer (optional) - How long to keep the model in memory.
    Returns: JSON object with the generated response or a stream of responses.

Chat:
  POST /api/chat
    Description: Chat with a model.
    Request Body:
      - model: string (required) - The name of the model to use.
      - messages: array of objects (required) - The conversation history.
        - role: string ('user' or 'assistant')
        - content: string
      - stream: boolean (optional) - Stream the response.
      - options: object (optional) - Model-specific options.
      - keep_alive: integer (optional) - How long to keep the model in memory.
    Returns: JSON object with the chat response or a stream of responses.

Embeddings:
  POST /api/embeddings
    Description: Generate embeddings for a prompt.
    Request Body:
      - model: string (required) - The name of the model to use.
      - prompt: string (required) - The prompt to generate embeddings for.
      - options: object (optional) - Model-specific options.
    Returns: JSON object containing the embeddings.

Generate:
  POST /api/generate
    Description: Generate text using a model.
    Parameters:
      - model: string (required) - The model to use.
      - prompt: string (required) - The prompt for generation.
      - stream: boolean (optional) - Whether to stream the response.
    Returns: JSON object with the generated text or a stream of text chunks.
```

--------------------------------

TITLE: Ollama API: Pull Model
DESCRIPTION: Pulls an Ollama model from the registry to the local machine.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
ollama.pull('gemma3')
```

--------------------------------

TITLE: Error Handling with Ollama Responses
DESCRIPTION: Demonstrates how to catch and handle `ollama.ResponseError` exceptions, which occur on API errors or during streaming issues. It shows checking the status code and potentially pulling a missing model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_17

LANGUAGE: python
CODE:
```
model = 'does-not-yet-exist'

try:
  ollama.chat(model)
except ollama.ResponseError as e:
  print('Error:', e.error)
  if e.status_code == 404:
    ollama.pull(model)
```

--------------------------------

TITLE: Ollama API: Show Model Details
DESCRIPTION: Retrieves detailed information about a specific Ollama model.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_9

LANGUAGE: APIDOC
CODE:
```
ollama.show('gemma3')
```

--------------------------------

TITLE: Streaming Responses from Ollama
DESCRIPTION: Enables streaming responses from Ollama by setting `stream=True`. This allows processing the response in chunks as they are generated.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_2

LANGUAGE: python
CODE:
```
from ollama import chat

stream = chat(
    model='gemma3',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```

--------------------------------

TITLE: Ollama API: Copy Model
DESCRIPTION: Copies an existing Ollama model to a new name.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_11

LANGUAGE: APIDOC
CODE:
```
ollama.copy('gemma3', 'user/gemma3')
```

--------------------------------

TITLE: Ollama API: Embeddings
DESCRIPTION: Generates embeddings for given input text using a specified Ollama model. Supports single strings or batches of strings.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
ollama.embed(model='gemma3', input='The sky is blue because of rayleigh scattering')
ollama.embed(model='gemma3', input=['The sky is blue because of rayleigh scattering', 'Grass is green because of chlorophyll'])
```

--------------------------------

TITLE: Ollama API: Delete Model
DESCRIPTION: Deletes an Ollama model by its name.

SOURCE: https://github.com/ollama/ollama-python/blob/main/README.md#_snippet_12

LANGUAGE: APIDOC
CODE:
```
ollama.delete('gemma3')
```