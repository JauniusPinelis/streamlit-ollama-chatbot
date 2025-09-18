================
CODE SNIPPETS
================
TITLE: Manual Install and Start
DESCRIPTION: Manually installs Ollama by downloading a tarball, extracting it, and starting the Ollama server. Includes steps for removing old libraries if upgrading.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_1

LANGUAGE: shell
CODE:
```
sudo rm -rf /usr/lib/ollama
curl -LO https://ollama.com/download/ollama-linux-amd64.tgz
sudo tar -C /usr -xzf ollama-linux-amd64.tgz
olama serve
olama -v
```

--------------------------------

TITLE: Shinkai Desktop
DESCRIPTION: A 'two-click install' solution for local AI, leveraging Ollama, file RAG, and other components for a streamlined setup.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_31

LANGUAGE: Unknown
CODE:
```
https://github.com/dcSpark/shinkai-apps
```

--------------------------------

TITLE: Enable and Start Ollama Service
DESCRIPTION: Commands to reload systemd, enable the Ollama service to start on boot, and start the service immediately.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_5

LANGUAGE: shell
CODE:
```
sudo systemctl daemon-reload
sudo systemctl enable ollama
sudo systemctl start ollama
```

--------------------------------

TITLE: Cloud Deployments with Ollama
DESCRIPTION: Guides and examples for deploying Ollama on various cloud platforms, enabling scalable AI model serving.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_62

LANGUAGE: CloudFormation
CODE:
```
Google Cloud: https://cloud.google.com/run/docs/tutorials/gpu-gemma2-with-ollama
Deploying Gemma 2 with Ollama on Google Cloud Run
```

LANGUAGE: Shell
CODE:
```
Fly.io: https://fly.io/docs/python/do-more/add-ollama/
Adding Ollama to Python applications on Fly.io
```

LANGUAGE: Shell
CODE:
```
Koyeb: https://www.koyeb.com/deploy/ollama
Deploying Ollama on Koyeb
```

--------------------------------

TITLE: NextChat Get Started Doc
DESCRIPTION: Documentation for NextChat on how to get started with Ollama models, covering configuration and usage.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_45

LANGUAGE: APIDOC
CODE:
```
NextChat - Ollama Model Integration:

Description: NextChat is a popular open-source chat application that allows users to connect to various LLM providers, including Ollama.

Configuration:
To use Ollama with NextChat, you typically need to:
1. Ensure Ollama is running locally.
2. Configure NextChat to use the Ollama API endpoint.
   - This usually involves setting the `OLLAMA_BASE_URL` environment variable or a similar configuration option within NextChat's settings.

Supported Models:
NextChat can list and utilize models available in your Ollama instance.

Usage:
Once configured, you can select Ollama models from the NextChat interface to start conversations.

Reference:
https://docs.nextchat.dev/models/ollama
```

--------------------------------

TITLE: Gollm Ollama Example
DESCRIPTION: Example of using Gollm with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_99

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"github.com/gollm/gollm"
)

func main() {
	client := gollm.NewClient("http://localhost:11434")
	response, err := client.Chat("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response.Response)
}
```

--------------------------------

TITLE: Install NVIDIA Container Toolkit (Debian/Ubuntu)
DESCRIPTION: Configures the NVIDIA repository and installs the NVIDIA Container Toolkit packages using apt.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_1

LANGUAGE: shell
CODE:
```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

--------------------------------

TITLE: LangChainGo Ollama Example
DESCRIPTION: Example of using LangChainGo with Ollama for completions.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_73

LANGUAGE: Go
CODE:
```
package main

import (
	"context"
	"fmt"
	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/ollama"
)

func main() {
	ctx := context.Background()
	llm, err := ollama.New(
		ollama.WithModel("llama2"),
	)
	if err != nil {
		panic(err)
	}

	completion, err := llm.Call(ctx, "What is the capital of France?", llms.ChainCallOpt{})
	if err != nil {
		panic(err)
	}

	fmt.Println(completion)
}
```

--------------------------------

TITLE: Install Ollama (Automatic)
DESCRIPTION: Installs Ollama using a curl script. This is the recommended and simplest method for installation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_0

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | sh
```

--------------------------------

TITLE: Install NVIDIA Container Toolkit (RHEL/CentOS/Fedora)
DESCRIPTION: Configures the NVIDIA repository and installs the NVIDIA Container Toolkit packages using yum or dnf.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_2

LANGUAGE: shell
CODE:
```
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo \
    | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
sudo yum install -y nvidia-container-toolkit
```

--------------------------------

TITLE: Build Ollama for Windows
DESCRIPTION: This script builds the Ollama CLI, Ollama app, and Ollama installer for Windows. It requires the Inno Setup compiler to be installed.

SOURCE: https://github.com/ollama/ollama/blob/main/app/README.md#_snippet_0

LANGUAGE: powershell
CODE:
```
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1
```

--------------------------------

TITLE: Agents-Flex Ollama Example
DESCRIPTION: Example of using Agents-Flex with Ollama for Java.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_104

LANGUAGE: Java
CODE:
```
import com.agentsflex.llm.ollama.OllamaLLMProvider;

OllamaLLMProvider ollamaProvider = new OllamaLLMProvider("http://localhost:11434", "llama2");

String response = ollamaProvider.doChat("What is the capital of France?");
System.out.println(response);
```

--------------------------------

TITLE: Run Ollama Docker Image (CPU Only)
DESCRIPTION: Starts the Ollama Docker container in detached mode, mounting a volume for persistent storage and exposing the default port.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_0

LANGUAGE: shell
CODE:
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

--------------------------------

TITLE: PromptingTools.jl Ollama Example
DESCRIPTION: Example of using PromptingTools.jl with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_97

LANGUAGE: Julia
CODE:
```
using PromptingTools

response = @prompt "What is the capital of France?" model=Ollama(model="llama2")
println(response.content)
```

--------------------------------

TITLE: Run Ollama Docker Image (NVIDIA GPU)
DESCRIPTION: Starts the Ollama Docker container with NVIDIA GPU support enabled using the '--gpus=all' flag.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_4

LANGUAGE: shell
CODE:
```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

--------------------------------

TITLE: Ollamaclient for Golang
DESCRIPTION: Example of using Ollamaclient for Golang.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_101

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"github.com/xyproto/ollamaclient"
)

func main() {
	client := ollamaclient.New("http://localhost:11434")
	response, err := client.Generate("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response)
}
```

--------------------------------

TITLE: Run Ollama Runner
DESCRIPTION: Starts the Ollama runner by specifying the model binary to load. This is the initial setup command.

SOURCE: https://github.com/ollama/ollama/blob/main/runner/README.md#_snippet_0

LANGUAGE: shell
CODE:
```
./runner -model <model binary>
```

--------------------------------

TITLE: GoLamify
DESCRIPTION: Example of using GoLamify with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_108

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"github.com/prasad89/golamify"
)

func main() {
	client := golamify.NewClient("http://localhost:11434")
	response, err := client.Chat("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response.Response)
}
```

--------------------------------

TITLE: Haverscript Examples
DESCRIPTION: Examples of using Haverscript with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_106

LANGUAGE: JavaScript
CODE:
```
const { Ollama } = require('haverscript');

const ollama = new Ollama('http://localhost:11434', 'llama2');

async function main() {
  const response = await ollama.chat('What is the capital of France?');
  console.log(response.response);
}

main();
```

--------------------------------

TITLE: LangChainRust Ollama Example
DESCRIPTION: Example of using LangChainRust with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_74

LANGUAGE: Rust
CODE:
```
use langchain_rust::chains::llm::LLMChain;
use langchain_rust::llms::ollama::Ollama;
use langchain_rust::prompt::PromptTemplate;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ollama = Ollama::new("http://localhost:11434", "llama2");

    let prompt = PromptTemplate::from("What is the capital of {{input}}");

    let chain = LLMChain::new(ollama, prompt);

    let result = chain.run(vec![("France".to_string(), "input")]).await?;

    println!("{}", result);

    Ok(())
}
```

--------------------------------

TITLE: Build and Run Ollama (General)
DESCRIPTION: This command builds and serves the Ollama application from the root directory of the repository. It requires Go to be installed.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_0

LANGUAGE: shell
CODE:
```
go run . serve
```

--------------------------------

TITLE: Ollama for Zig
DESCRIPTION: Example of using the ollama-zig package.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_112

LANGUAGE: Zig
CODE:
```
const ollama = @import("ollama-zig");

pub fn main() !void {
    var client = try ollama.Client.init("http://localhost:11434");
    var response = try client.chat("llama2", "What is the capital of France?");
    std.debug.print("{s}\n", .{response.response});
}
```

--------------------------------

TITLE: Gollama for Golang
DESCRIPTION: Example of using Gollama for Golang.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_100

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"github.com/jonathanhecl/gollama"
)

func main() {
	client := gollama.NewClient("http://localhost:11434")
	response, err := client.Generate("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response.Response)
}
```

--------------------------------

TITLE: Run Ollama Docker Image (AMD GPU)
DESCRIPTION: Starts the Ollama Docker container with AMD GPU support using the 'rocm' tag and specific device mappings.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_5

LANGUAGE: shell
CODE:
```
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

--------------------------------

TITLE: Run Ollama Examples
DESCRIPTION: Command to execute the Go examples provided in the directory. Assumes you are in the root of the project.

SOURCE: https://github.com/ollama/ollama/blob/main/api/examples/README.md#_snippet_0

LANGUAGE: shell
CODE:
```
go run example_name/main.go
```

--------------------------------

TITLE: Ollama PHP
DESCRIPTION: Example of using the ollama-php package.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_103

LANGUAGE: PHP
CODE:
```
use ArdaGnsrn\Ollama\Ollama;

$ollama = new Ollama('http://localhost:11434');
$response = $ollama->chat('llama2', 'What is the capital of France?');
echo $response['response'];
```

--------------------------------

TITLE: Ollama for Haskell
DESCRIPTION: Example of using the ollama-haskell package.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_109

LANGUAGE: Haskell
CODE:
```
import Ollama

main :: IO ()
main = do
  response <- ollama "llama2" "What is the capital of France?"
  putStrLn response
```

--------------------------------

TITLE: OllamaKit for Swift
DESCRIPTION: Example of using OllamaKit for Swift.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_84

LANGUAGE: Swift
CODE:
```
import OllamaKit

let ollama = OllamaKit(host: "http://localhost:11434")

Task {
    do {
        let response = try await ollama.send("What is the capital of France?")
        print(response.response)
    } catch {
        print("Error: \(error)")
    }
}
```

--------------------------------

TITLE: Run Ollama Desktop App
DESCRIPTION: Installs dependencies and starts the Ollama desktop application. Assumes the Ollama binary has already been built.

SOURCE: https://github.com/ollama/ollama/blob/main/macapp/README.md#_snippet_1

LANGUAGE: shell
CODE:
```
cd macapp
npm install
npm start
```

--------------------------------

TITLE: Ollama-ex for Elixir
DESCRIPTION: Example of using the ollama-ex package for Elixir.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_93

LANGUAGE: Elixir
CODE:
```
alias OllamaEx.Client

client = Client.new(host: "http://localhost:11434")
response = Client.chat(client, model: "llama2", prompt: "What is the capital of France?")
IO.puts(response.response)
```

--------------------------------

TITLE: LangChain for .NET Ollama Example
DESCRIPTION: Example of using LangChain for .NET with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_75

LANGUAGE: C#
CODE:
```
using LangChain.Chains.LLM;
using LangChain.Providers;
using LangChain.Providers.Ollama;

var ollama = new OllamaProvider("http://localhost:11434", "llama2");
var llmChain = new LLMChain(ollama);

var prompt = "What is the capital of France?";
var result = await llmChain.Run(prompt);

Console.WriteLine(result);
```

--------------------------------

TITLE: Portkey Ollama Integration
DESCRIPTION: Example of integrating Portkey with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_96

LANGUAGE: Python
CODE:
```
from portkey.llm import PortkeyLLM

llm = PortkeyLLM(provider='ollama', model='llama2')

response = llm.invoke("What is the capital of France?")
print(response.content)
```

--------------------------------

TITLE: Install Specific Ollama Version
DESCRIPTION: Installs a specific version of Ollama using the install script and the OLLAMA_VERSION environment variable.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_9

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.5.7 sh
```

--------------------------------

TITLE: Basic Modelfile Example
DESCRIPTION: An example of a Modelfile creating a model blueprint, setting parameters like temperature and context window size, and defining a system message.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_0

LANGUAGE: shell
CODE:
```
FROM llama3.2
# sets the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1
# sets the context window size to 4096, this controls how many tokens the LLM can use as context to generate the next token
PARAMETER num_ctx 4096

# sets a custom system message to specify the behavior of the chat assistant
SYSTEM You are Mario from super mario bros, acting as an assistant.
```

--------------------------------

TITLE: Start Ollama Server
DESCRIPTION: Starts the Ollama server process without launching the desktop application. This is useful for headless or background operations.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_16

LANGUAGE: shell
CODE:
```
./ollama serve
```

--------------------------------

TITLE: Python Examples
DESCRIPTION: Provides links to Python examples for using Ollama, hosted in a separate repository.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/examples.md#_snippet_0

LANGUAGE: python
CODE:
```
import ollama

# Example usage (assuming a model is available)
# response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
# print(response['message']['content'])
```

--------------------------------

TITLE: JavaScript Examples
DESCRIPTION: Provides links to JavaScript examples for using Ollama, hosted in a separate repository.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/examples.md#_snippet_1

LANGUAGE: javascript
CODE:
```
import ollama from 'ollama'

// Example usage (assuming a model is available)
// async function main() {
//   const response = await ollama.chat({ model: 'llama2', messages: [{ role: 'user', content: 'Why is the sky blue?' }] });
//   console.log(response.message.content);
// }
// main();
```

--------------------------------

TITLE: Install Ollama on Linux
DESCRIPTION: Installs Ollama on Linux using a curl script. This is the recommended method for Linux installations.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_0

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | sh
```

--------------------------------

TITLE: ARM64 Package Install
DESCRIPTION: Downloads and installs the Ollama package specifically for ARM64 architecture systems.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_3

LANGUAGE: shell
CODE:
```
curl -L https://ollama.com/download/ollama-linux-arm64.tgz -o ollama-linux-arm64.tgz
sudo tar -C /usr -xzf ollama-linux-arm64.tgz
```

--------------------------------

TITLE: Ollama for Dart
DESCRIPTION: Example of using the dart-ollama package for Dart.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_85

LANGUAGE: Dart
CODE:
```
import 'package:ollama/ollama.dart';

Future<void> main() async {
  final ollama = Ollama(host: 'http://localhost:11434');
  final response = await ollama.generate(model: 'llama2', prompt: 'What is the capital of France?');
  print(response.response);
}
```

--------------------------------

TITLE: OpenAI Compatibility Examples
DESCRIPTION: Demonstrates how to use Ollama with OpenAI compatibility, linking to specific documentation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/examples.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
OpenAI Compatibility:

Ollama provides an OpenAI-compatible API endpoint, allowing you to use existing OpenAI client libraries with Ollama.

Base URL:
  http://localhost:11434/v1

Models:
  The available models can be listed using the Ollama API or CLI.

Chat Completion:
  POST /chat/completions
  
  Request Body:
    model: string (required) - The name of the Ollama model to use.
    messages: array (required) - An array of message objects.
      role: string ('system', 'user', or 'assistant')
      content: string
    temperature: number (optional) - Controls randomness. Lower values make output more deterministic.
    stream: boolean (optional) - If true, partial message deltas are sent as server-sent events.

  Example Request:
  {
    "model": "llama2",
    "messages": [
      {"role": "user", "content": "Why is the sky blue?"}
    ],
    "stream": false
  }

  Example Response:
  {
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "model": "llama2",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "The sky appears blue due to a phenomenon called Rayleigh scattering..."
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "completion_tokens": 50,
      "total_tokens": 60
    }
  }

Embedding:
  POST /embeddings

  Request Body:
    model: string (required) - The name of the Ollama model to use for embeddings.
    input: string | array (required) - The input text or array of texts to get embeddings for.

  Example Request:
  {
    "model": "nomic-embed-text",
    "input": "The quick brown fox jumps over the lazy dog."
  }

  Example Response:
  {
    "id": "embed-123",
    "object": "embedding",
    "created": 1677652288,
    "model": "nomic-embed-text",
    "data": [
      {
        "index": 0,
        "embedding": [
          0.0022,
          -0.0081,
          ... // vector of numbers
        ]
      }
    ],
    "usage": {
      "prompt_tokens": 10,
      "total_tokens": 10
    }
  }

List Models:
  GET /api/tags

  Example Response:
  {
    "models": [
      {
        "name": "llama2",
        "modified_at": "2023-07-27T22:17:12.171942111Z",
        "size": 3493330000,
        "digest": "...",
        "details": {
          "parent_model": "",
          "format": "gguf",
          "families": ["llama"],
          "parameter_size": "7B",
          "quantization_level": "Q4_0"
        }
      }
    ]
  }
```

--------------------------------

TITLE: High-level function abstraction in Go
DESCRIPTION: Example of using the 'fun' library for Go with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_102

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"gitlab.com/tozd/go/fun"
)

func main() {
	client := fun.NewOllamaClient("http://localhost:11434")
	response, err := client.Chat("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response.Response)
}
```

--------------------------------

TITLE: Testcontainers Ollama Module
DESCRIPTION: Example of using Testcontainers to spin up an Ollama instance for testing.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_95

LANGUAGE: Java
CODE:
```
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.utility.DockerImageName;

public class OllamaTest {

    static GenericContainer ollamaContainer = new GenericContainer(DockerImageName.parse("ollama/ollama:latest"))
            .withExposedPorts(11434);

    public static void main(String[] args) {
        ollamaContainer.start();
        String ollamaUrl = "http://" + ollamaContainer.getHost() + ":" + ollamaContainer.getFirstMappedPort();
        System.out.println("Ollama running at: " + ollamaUrl);
        // Use ollamaUrl to configure your Ollama client
        ollamaContainer.stop();
    }
}
```

--------------------------------

TITLE: Update Ollama
DESCRIPTION: Updates Ollama to the latest version by re-running the installation script or re-downloading and extracting the binary.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_8

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | sh
# Or:
curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
sudo tar -C /usr -xzf ollama-linux-amd64.tgz
```

--------------------------------

TITLE: Ollama for R - ollama-r
DESCRIPTION: Example of using the ollama-r package for R.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_92

LANGUAGE: R
CODE:
```
library(ollama_r)

response <- ollama_chat(model = "llama2", messages = list(list("role" = "user", "content" = "What is the capital of France?")))
print(response$message$content)
```

--------------------------------

TITLE: Swollama for Swift
DESCRIPTION: Example of using Swollama for Swift.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_107

LANGUAGE: Swift
CODE:
```
import Swollama

let ollama = Ollama(host: "http://localhost:11434")

Task {
    do {
        let response = try await ollama.chat(model: "llama2", prompt: "What is the capital of France?")
        print(response.response)
    } catch {
        print("Error: \(error)")
    }
}
```

--------------------------------

TITLE: Ollama4j for Java
DESCRIPTION: Example of using Ollama4j for Java.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_82

LANGUAGE: Java
CODE:
```
import io.github.ollama4j.ollama4j.OllamaAPI;

public class Main {
    public static void main(String[] args) {
        OllamaAPI ollamaAPI = new OllamaAPI("http://localhost:11434");
        String response = ollamaAPI.chat("What is the capital of France?");
        System.out.println(response);
    }
}
```

--------------------------------

TITLE: Ollama for Ruby
DESCRIPTION: Example of using the Ollama gem for Ruby.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_79

LANGUAGE: Ruby
CODE:
```
require 'ollama-ai'

client = Ollama::Client.new
response = client.generate(model: 'llama2', prompt: 'What is the capital of France?')
puts response['response']
```

--------------------------------

TITLE: Ollama-rs for Rust
DESCRIPTION: Example of using the ollama-rs crate for Rust.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_80

LANGUAGE: Rust
CODE:
```
use ollama_rs::Ollama;

#[tokio::main]
async fn main() {
    let ollama = Ollama::new("http://localhost:11434");
    let response = ollama.send_message("What is the capital of France?").await.unwrap();
    println!("{}", response.response);
}
```

--------------------------------

TITLE: Ollama Connector for SAP ABAP
DESCRIPTION: Example of using the ABAP Ollama connector.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_94

LANGUAGE: ABAP
CODE:
```
DATA(lo_ollama) = NEW b_tocs_ollama_connector( iv_base_url = 'http://localhost:11434' ).
DATA(lv_response) = lo_ollama->chat( iv_model = 'llama2' iv_prompt = 'What is the capital of France?' ).
WRITE lv_response.
```

--------------------------------

TITLE: Parakeet GoLang Library
DESCRIPTION: Example of using Parakeet with Ollama in Go.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_105

LANGUAGE: Go
CODE:
```
package main

import (
	"fmt"
	"github.com/parakeet-nest/parakeet"
)

func main() {
	client := parakeet.NewClient("http://localhost:11434")
	response, err := client.Chat("llama2", "What is the capital of France?")
	if err != nil {
		panic(err)
	}
	fmt.Println(response.Response)
}
```

--------------------------------

TITLE: AMD GPU (ROCm) Package Install
DESCRIPTION: Downloads and installs the ROCm package for Ollama, specifically for systems with AMD GPUs.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_2

LANGUAGE: shell
CODE:
```
curl -L https://ollama.com/download/ollama-linux-amd64-rocm.tgz -o ollama-linux-amd64-rocm.tgz
sudo tar -C /usr -xzf ollama-linux-amd64-rocm.tgz
```

--------------------------------

TITLE: Ollama Systemd Service Configuration
DESCRIPTION: Creates a systemd service file for Ollama, enabling it to run as a background service. Includes user/group creation and service enabling.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_4

LANGUAGE: ini
CODE:
```
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=$PATH"

[Install]
WantedBy=multi-user.target
```

--------------------------------

TITLE: Configure Docker for NVIDIA and Restart
DESCRIPTION: Configures the Docker runtime to use the NVIDIA Container Toolkit and restarts the Docker service.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_3

LANGUAGE: shell
CODE:
```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

--------------------------------

TITLE: Ollama Pull Model Example
DESCRIPTION: Go code to demonstrate pulling a model from Ollama. This example shows how to initiate a model download and potentially track its progress.

SOURCE: https://github.com/ollama/ollama/blob/main/api/examples/README.md#_snippet_4

LANGUAGE: go
CODE:
```
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ollama/ollama/api"
)

func main() {
	client, err := api.NewClient()
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx := context.Background()

	// Example: Pulling the 'llama2' model
	resp, err := client.Pull(ctx, api.PullRequest{
		Name: "llama2",
	})
	if err != nil {
		log.Fatalf("Failed to pull model: %v", err)
	}

	// The response from Pull can be streamed if progress is needed.
	// For simplicity, we're just checking for errors here.
	fmt.Printf("Successfully initiated pull for model: %s\n", resp.Name)
}
```

--------------------------------

TITLE: Verify NVIDIA GPU Drivers
DESCRIPTION: Checks if NVIDIA drivers are installed and correctly configured by displaying GPU information.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_6

LANGUAGE: shell
CODE:
```
nvidia-smi
```

--------------------------------

TITLE: llm-axe Ollama Integration
DESCRIPTION: Example of using llm-axe with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_98

LANGUAGE: Python
CODE:
```
from llm_axe.llm import LLM

llm = LLM(provider="ollama", model="llama2")

response = llm.generate("What is the capital of France?")
print(response)
```

--------------------------------

TITLE: Ollama-hpp for C++
DESCRIPTION: Example of using ollama-hpp for C++.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_81

LANGUAGE: C++
CODE:
```
#include "ollama_hpp/ollama.hpp"
#include <iostream>

int main() {
    ollama::Ollama ollama("http://localhost:11434");
    auto response = ollama.chat("What is the capital of France?");
    std::cout << response.response << std::endl;
    return 0;
}
```

--------------------------------

TITLE: Run a Model with Ollama
DESCRIPTION: Downloads and runs a specified model using the Ollama CLI. This is a quick way to start interacting with a language model.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_1

LANGUAGE: shell
CODE:
```
ollama run gemma3
```

--------------------------------

TITLE: Install Metal Files
DESCRIPTION: This snippet defines the installation rules for Metal-related files. It installs the source Metal file (`ggml-metal.metal`) and the compiled Metal library (`default.metallib`) to the appropriate binary directory during the installation phase of the build process.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-metal/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
if (NOT GGML_METAL_EMBED_LIBRARY)
    install(
        FILES src/ggml-metal/ggml-metal.metal
        PERMISSIONS
            OWNER_READ
            OWNER_WRITE
            GROUP_READ
            WORLD_READ
        DESTINATION ${CMAKE_INSTALL_BINDIR})

        install(
            FILES ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
            DESTINATION ${CMAKE_INSTALL_BINDIR}
        )
endif()
```

--------------------------------

TITLE: LiteLLM Ollama Usage
DESCRIPTION: Example of using LiteLLM to interact with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_77

LANGUAGE: Python
CODE:
```
from litellm import completion

response = completion(
    model="ollama/llama2",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)
print(response)
```

--------------------------------

TITLE: LangChainDart
DESCRIPTION: Example of using LangChainDart with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_87

LANGUAGE: Dart
CODE:
```
import 'package:langchain_dart/langchain_dart.dart';

Future<void> main() async {
  final ollama = Ollama(baseUrl: 'http://localhost:11434', model: 'llama2');
  final response = await ollama.invoke('What is the capital of France?');
  print(response);
}
```

--------------------------------

TITLE: Ollama Chat Example
DESCRIPTION: Go code to demonstrate how to chat with an Ollama model. This example likely involves setting up a client and sending messages to the model.

SOURCE: https://github.com/ollama/ollama/blob/main/api/examples/README.md#_snippet_1

LANGUAGE: go
CODE:
```
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ollama/ollama/api"
)

func main() {
	client, err := api.NewClient()
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx := context.Background()

	stream, err := client.Chat(ctx, api.ChatRequest{
		Model: "llama2",
		Messages: []api.Message{
			{Role: "user", Content: "Why is the sky blue?"},
		},
	})
	if err != nil {
		log.Fatalf("Failed to chat: %v", err)
	}

	defer stream.Close()

	for {
		response, err := stream.Next() 
		if err != nil {
			if err == api.ErrEOF {
				break
			}
			log.Fatalf("Error receiving message: %v", err)
		}
		fmt.Print(response.Message.Content)
	}
	fmt.Println()
}
```

--------------------------------

TITLE: Ollama Related Projects and Examples
DESCRIPTION: Miscellaneous projects and examples showcasing specific use cases or advanced techniques with Ollama, such as MOE models, eBook summarization, and AWS Strands agents.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_69

LANGUAGE: Python
CODE:
```
# Ollama Mixture of Experts (MOE) in 50 lines of code
# Demonstrates a lightweight implementation of MOE with Ollama.
```

LANGUAGE: Python
CODE:
```
# Ollama eBook Summary
# A project focused on summarizing eBooks using Ollama.
```

LANGUAGE: Python
CODE:
```
# AWS-Strands-With-Ollama
# Examples of using AWS Strands Agents with Ollama.
```

--------------------------------

TITLE: OllamaSharp for .NET
DESCRIPTION: Example of using OllamaSharp for .NET applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_78

LANGUAGE: C#
CODE:
```
using OllamaSharp;

var ollama = new OllamaApiClient("http://localhost:11434");

var response = await ollama.SendAsync("What is the capital of France?");
Console.WriteLine(response.Response);
```

--------------------------------

TITLE: Haystack Ollama Integration
DESCRIPTION: Example of integrating Haystack with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_89

LANGUAGE: Python
CODE:
```
from haystack_integrations.components.llms.ollama import OllamaLLM

llm = OllamaLLM(model="llama2")

response = llm.invoke("What is the capital of France?")
print(response.content)
```

--------------------------------

TITLE: Create a Model from GGUF
DESCRIPTION: Guides through creating a custom Ollama model by importing a GGUF file. This involves creating a Modelfile and using the `ollama create` command.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_3

LANGUAGE: APIDOC
CODE:
```
FROM ./vicuna-33b.Q4_0.gguf
```

LANGUAGE: shell
CODE:
```
ollama create example -f Modelfile
```

LANGUAGE: shell
CODE:
```
ollama run example
```

--------------------------------

TITLE: Ollama for Laravel
DESCRIPTION: Example of integrating Ollama with Laravel.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_86

LANGUAGE: PHP
CODE:
```
use Cloudstudio\OllamaLaravel\Ollama;

$ollama = new Ollama();
$response = $ollama->generate(['model' => 'llama2', 'prompt' => 'What is the capital of France?']);
echo $response['response'];
```

--------------------------------

TITLE: Multiline Input Example
DESCRIPTION: Demonstrates how to handle multiline input in the Ollama CLI by wrapping text with triple quotes (`"""`).

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_9

LANGUAGE: shell
CODE:
```
>>> """Hello,
... world!
... """
I'm a basic program that prints the famous "Hello, world!" message to the console.
```

--------------------------------

TITLE: multi-llm-ts Ollama Integration
DESCRIPTION: Example of using multi-llm-ts with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_110

LANGUAGE: TypeScript
CODE:
```
import { Ollama } from "multi-llm-ts";

const ollama = new Ollama("http://localhost:11434", "llama2");

async function main() {
  const response = await ollama.chat("What is the capital of France?");
  console.log(response.response);
}

main();
```

--------------------------------

TITLE: Change Ollama Installation Directory
DESCRIPTION: Specifies how to change the installation directory for the Ollama application on Windows using a command-line flag during setup.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/windows.md#_snippet_0

LANGUAGE: powershell
CODE:
```
OllamaSetup.exe /DIR="d:\some\location"
```

--------------------------------

TITLE: Ollama Package Manager Availability
DESCRIPTION: Information on how to install and manage Ollama using various package managers across different operating systems and environments.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_67

LANGUAGE: Shell
CODE:
```
# Arch Linux (Pacman)
# sudo pacman -S ollama
```

LANGUAGE: Shell
CODE:
```
# Gentoo
# emerge app-misc/ollama
```

LANGUAGE: Shell
CODE:
```
# macOS (Homebrew)
# brew install ollama
```

LANGUAGE: Shell
CODE:
```
# Helm Chart for Kubernetes
# helm install ollama ollama-helm/ollama
```

LANGUAGE: Shell
CODE:
```
# Guix channel
# guix install ollama
```

LANGUAGE: Shell
CODE:
```
# Nix package
# nix-env -iA nixpkgs.ollama
```

LANGUAGE: Shell
CODE:
```
# Flox
# flox install ollama
```

--------------------------------

TITLE: Run Ollama Tests
DESCRIPTION: Executes all tests for the Ollama project using the Go testing framework.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_7

LANGUAGE: go
CODE:
```
go test ./...
```

--------------------------------

TITLE: Elixir LangChain Ollama
DESCRIPTION: Example of using Elixir LangChain with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_90

LANGUAGE: Elixir
CODE:
```
use Langchain.LLM

llm = Langchain.LLM.Ollama.new(model: "llama2")
response = Langchain.LLM.generate(llm, "What is the capital of France?")
IO.puts(response.response)
```

--------------------------------

TITLE: Ollama Show Modelfile Output Example
DESCRIPTION: An example of the output from `ollama show --modelfile`, showing the generated Modelfile content for a model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Ollama Show --modelfile Output:
  # Modelfile generated by "ollama show"
  # To build a new Modelfile based on this one, replace the FROM line with:
  # FROM llama3.2:latest
  FROM /Users/pdevine/.ollama/models/blobs/sha256-00e1317cbf74d901080d7100f57580ba8dd8de57203072dc6f668324ba545f29
  TEMPLATE """{{ if .System }}<|start_header_id|>system<|end_header_id|>

  {{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

  {{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

  {{ .Response }}<|eot_id|>"""
  PARAMETER stop "<|start_header_id|>"
  PARAMETER stop "<|end_header_id|>"
  PARAMETER stop "<|eot_id|>"
  PARAMETER stop "<|reserved_special_token"
```

--------------------------------

TITLE: View Ollama Service Logs
DESCRIPTION: Retrieves and displays the logs for the Ollama service using journalctl.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_10

LANGUAGE: shell
CODE:
```
journalctl -e -u ollama
```

--------------------------------

TITLE: Ollama API Interaction
DESCRIPTION: Examples and documentation for interacting with the Ollama API, enabling programmatic control and integration of Ollama models into custom applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_127

LANGUAGE: APIDOC
CODE:
```
Ollama API:
  Base URL: http://localhost:11434

  Endpoints:
    /api/tags
      GET: List available models.
      Example:
        curl http://localhost:11434/api/tags

    /api/generate
      POST: Generate a response from a model.
      Request Body:
        model: string (name of the model to use)
        prompt: string (the input prompt)
        stream: boolean (optional, whether to stream the response)
      Example:
        curl -X POST http://localhost:11434/api/generate -d '{"model": "llama2", "prompt": "Why is the sky blue?"}'

    /api/embeddings
      POST: Generate embeddings for a given prompt.
      Request Body:
        model: string (name of the model to use)
        prompt: string (the input prompt)
      Example:
        curl -X POST http://localhost:11434/api/embeddings -d '{"model": "llama2", "prompt": "Hello world"}'

    /api/pull
      POST: Pull a model from the registry.
      Request Body:
        name: string (name of the model to pull)
      Example:
        curl -X POST http://localhost:11434/api/pull -d '{"name": "llama2"}'

    /api/create
      POST: Create a new model from a Modelfile.
      Request Body:
        name: string (name for the new model)
        modelfile: string (content of the Modelfile)
      Example:
        curl -X POST http://localhost:11434/api/create -d '{"name": "my-model", "modelfile": "FROM llama2\n"}'
```

--------------------------------

TITLE: Frameworks and Toolkits
DESCRIPTION: This section covers frameworks and toolkits that utilize Ollama as a backend or integrate it into larger systems for building AI agents, RAG pipelines, and complex workflows.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_53

LANGUAGE: Python
CODE:
```
Project: LLMStack
Description: No-code multi-agent framework to build LLM agents and workflows
Link: https://github.com/trypromptly/LLMStack
```

LANGUAGE: Go
CODE:
```
Project: Go-CREW
Description: Powerful Offline RAG in Golang
Link: https://www.jonathanhecl.com/go-crew/
```

LANGUAGE: Python
CODE:
```
Project: Archyve
Description: RAG-enabling document library
Link: https://github.com/nickthecook/archyve
```

LANGUAGE: Python
CODE:
```
Project: crewAI with Mesop
Description: Mesop Web Interface to run crewAI with Ollama
Link: https://github.com/rapidarchitect/ollama-crew-mesop
```

LANGUAGE: Python
CODE:
```
Project: Nosia
Description: Easy to install and use RAG platform based on Ollama
Link: https://github.com/nosia-ai/nosia
```

LANGUAGE: Python
CODE:
```
Project: Hexabot
Description: A conversational AI builder
Link: https://github.com/hexastack/hexabot
```

--------------------------------

TITLE: Run Local Build
DESCRIPTION: Executes a model after starting a local build of Ollama. Requires the server to be running in a separate shell.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_17

LANGUAGE: shell
CODE:
```
./ollama run llama3.2
```

--------------------------------

TITLE: Ollama List Models Example
DESCRIPTION: Shows how to list all available models supported by the Ollama API. This is useful for discovering which models can be used for various tasks.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_9

LANGUAGE: javascript
CODE:
```
const listCompletion = await openai.models.list()
```

--------------------------------

TITLE: Ollama for R - rollama
DESCRIPTION: Example of using the rollama package for R.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_91

LANGUAGE: R
CODE:
```
library(rollama)

response <- ollama_generate(model = "llama2", prompt = "What is the capital of France?")
print(response$response)
```

--------------------------------

TITLE: StreamDeploy
DESCRIPTION: An LLM Application Scaffold that provides a starting point for building LLM-powered applications, likely supporting Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_39

LANGUAGE: Python
CODE:
```
https://github.com/StreamDeploy-DevRel/streamdeploy-llm-app-scaffold
```

--------------------------------

TITLE: Semantic Kernel - Python Ollama Connector
DESCRIPTION: Example of using Semantic Kernel with Ollama in Python.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_88

LANGUAGE: Python
CODE:
```
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion

kernel = Kernel()

kernel.add_chat_service("ollama_chat", OllamaChatCompletion("llama2", "http://localhost:11434"))

response = kernel.invoke("What is the capital of France?")
print(response)
```

--------------------------------

TITLE: LlmTornado C# Library
DESCRIPTION: Example of using LlmTornado with Ollama in C#.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_111

LANGUAGE: C#
CODE:
```
using LlmTornado.Providers.Ollama;

var ollama = new OllamaProvider("http://localhost:11434", "llama2");

var response = ollama.Chat("What is the capital of France?");
Console.WriteLine(response.Response);
```

--------------------------------

TITLE: LlamaIndex Ollama Integration
DESCRIPTION: Examples of integrating LlamaIndex with Ollama for LLM interactions.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_76

LANGUAGE: Python
CODE:
```
from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama2", request_timeout=120.0)

response = llm.complete("What is the capital of France?")
print(response)
```

--------------------------------

TITLE: LangChain Integrations
DESCRIPTION: Integrations with LangChain for Python and JavaScript, providing examples for local RAG.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_71

LANGUAGE: Python
CODE:
```
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama2")
print(llm.invoke("What is the capital of France?"))
```

LANGUAGE: JavaScript
CODE:
```
import { Ollama } from "langchain/llms/ollama";

const model = new Ollama({ model: "llama2" });
const res = await model.invoke(
  "What is the capital of France?"
);
console.log(res);
```

--------------------------------

TITLE: Run a Model Locally with Ollama
DESCRIPTION: Executes a model within the running Ollama Docker container.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_6

LANGUAGE: shell
CODE:
```
docker exec -it ollama ollama run llama3.2
```

--------------------------------

TITLE: AnythingLLM
DESCRIPTION: A comprehensive application for managing and interacting with LLMs, supporting Docker and native app installations on various OS. It integrates with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_49

LANGUAGE: JavaScript
CODE:
```
https://github.com/Mintplex-Labs/anything-llm
```

--------------------------------

TITLE: List Local Models
DESCRIPTION: Lists all models currently available on the local machine.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_13

LANGUAGE: shell
CODE:
```
ollama list
```

--------------------------------

TITLE: Build Ollama on Linux
DESCRIPTION: Configures and builds the Ollama project on Linux using CMake. Requires CMake to be installed. Supports optional GPU acceleration.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_4

LANGUAGE: shell
CODE:
```
cmake -B build
cmake --build build
```

--------------------------------

TITLE: ModelFusion Typescript Library
DESCRIPTION: Example of using ModelFusion with Ollama in TypeScript.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_83

LANGUAGE: TypeScript
CODE:
```
import { Ollama } from "@modelfusion/ollama";

const ollama = new Ollama({ model: "llama2" });

async function main() {
  const text = await ollama.generateText("What is the capital of France?");
  console.log(text);
}

main();
```

--------------------------------

TITLE: Customize Model Prompt with Modelfile
DESCRIPTION: Shows how to customize an existing Ollama model by creating a Modelfile that includes a system prompt and parameters. This allows for tailored model behavior.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_4

LANGUAGE: shell
CODE:
```
ollama pull llama3.2
```

LANGUAGE: APIDOC
CODE:
```
FROM llama3.2

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```

LANGUAGE: shell
CODE:
```
ollama create mario -f ./Modelfile
```

LANGUAGE: shell
CODE:
```
ollama run mario
```

--------------------------------

TITLE: Ollama Streaming Generate Text Example
DESCRIPTION: Go code to demonstrate generating text from an Ollama model with streaming enabled. This allows for receiving text chunks as they are generated.

SOURCE: https://github.com/ollama/ollama/blob/main/api/examples/README.md#_snippet_3

LANGUAGE: go
CODE:
```
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ollama/ollama/api"
)

func main() {
	client, err := api.NewClient()
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx := context.Background()

	stream, err := client.Generate(ctx, api.GenerateRequest{
		Model:  "llama2",
		Prompt: "Why is the sky blue?",
		Stream: true,
	})
	if err != nil {
		log.Fatalf("Failed to generate text: %v", err)
	}

	defer stream.Close()

	for {
		response, err := stream.Next()
		if err != nil {
			if err == api.ErrEOF {
				break
			}
			log.Fatalf("Error receiving message: %v", err)
		}
		fmt.Print(response.Response)
	}
	fmt.Println()
}
```

--------------------------------

TITLE: Enabling Synctest Experiment Globally for Go
DESCRIPTION: This command sets the `GOEXPERIMENT` environment variable to `synctest` permanently for all Go commands. This ensures the `synctest` package is enabled without needing to set it per session or command.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_12

LANGUAGE: shell
CODE:
```
go env -w GOEXPERIMENT=synctest
```

--------------------------------

TITLE: Download Specific Model Variants
DESCRIPTION: Demonstrates how to download specific versions or sizes of models from the Ollama library using the `ollama run` command with a tag.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_2

LANGUAGE: shell
CODE:
```
ollama run gemma3:1b
```

LANGUAGE: shell
CODE:
```
ollama run gemma3:12b
```

LANGUAGE: shell
CODE:
```
ollama run deepseek-r1:671b
```

LANGUAGE: shell
CODE:
```
ollama run llama4:scout
```

LANGUAGE: shell
CODE:
```
ollama run llama3.2:1b
```

LANGUAGE: shell
CODE:
```
ollama run llama3.2-vision:90b
```

LANGUAGE: shell
CODE:
```
ollama run llama3.1:405b
```

--------------------------------

TITLE: Build Ollama on Windows
DESCRIPTION: Configures and builds the Ollama project on Windows using CMake. Requires CMake and Visual Studio 2022 with the Native Desktop Workload. Supports optional GPU acceleration.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_2

LANGUAGE: shell
CODE:
```
cmake -B build
cmake --build build --config Release
```

--------------------------------

TITLE: Ollama Generate Text Example
DESCRIPTION: Go code to demonstrate generating text from an Ollama model. This example shows a non-streaming text generation request.

SOURCE: https://github.com/ollama/ollama/blob/main/api/examples/README.md#_snippet_2

LANGUAGE: go
CODE:
```
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ollama/ollama/api"
)

func main() {
	client, err := api.NewClient()
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	ctx := context.Background()

	resp, err := client.Generate(ctx, api.GenerateRequest{
		Model: "llama2",
		Prompt: "Why is the sky blue?",
	})
	if err != nil {
		log.Fatalf("Failed to generate text: %v", err)
	}

	fmt.Println(resp.Response)
}
```

--------------------------------

TITLE: QA-Pilot
DESCRIPTION: An interactive chat tool that utilizes Ollama models for rapid understanding and navigation of GitHub code repositories.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_35

LANGUAGE: Python
CODE:
```
https://github.com/reid41/QA-Pilot
```

--------------------------------

TITLE: LLocal.in
DESCRIPTION: An easy-to-use Electron Desktop Client for Ollama, providing a seamless local LLM interaction experience.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_30

LANGUAGE: JavaScript
CODE:
```
https://github.com/kartikm7/llocal
```

--------------------------------

TITLE: Running Ollama Go Tests (General)
DESCRIPTION: This command executes all Go tests within the current module and its subpackages. It's the standard way to verify the correctness and functionality of the codebase.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_10

LANGUAGE: shell
CODE:
```
go test ./...
```

--------------------------------

TITLE: List Running Models
DESCRIPTION: Shows which models are currently loaded and running in Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_14

LANGUAGE: shell
CODE:
```
ollama ps
```

--------------------------------

TITLE: Customize Ollama Service Configuration
DESCRIPTION: Provides methods to customize the Ollama service, either by editing the service file directly or creating an override configuration file.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_7

LANGUAGE: shell
CODE:
```
sudo systemctl edit ollama
# Or manually create /etc/systemd/system/ollama.service.d/override.conf with content:
# [Service]
# Environment="OLLAMA_DEBUG=1"
```

--------------------------------

TITLE: Build Ollama on macOS (Intel)
DESCRIPTION: Configures and builds the Ollama project on macOS with Intel processors using CMake. Requires CMake to be installed.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_1

LANGUAGE: shell
CODE:
```
cmake -B build
cmake --build build
```

--------------------------------

TITLE: HIP Compiler Warnings and Setup
DESCRIPTION: Provides warnings for unsupported compilers or legacy hipcc usage. Enables the HIP language and sets up HIP architectures.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
if (CXX_IS_HIPCC)
    if (LINUX)
        if (NOT ${CMAKE_CXX_COMPILER_ID} MATCHES "Clang")
            message(WARNING "Only LLVM is supported for HIP, hint: CXX=/opt/rocm/llvm/bin/clang++")
        endif()

        message(WARNING "Setting hipcc as the C++ compiler is legacy behavior."
                " Prefer setting the HIP compiler directly. See README for details.")
    endif()
else()
    # Forward AMDGPU_TARGETS to CMAKE_HIP_ARCHITECTURES.
    if (AMDGPU_TARGETS AND NOT CMAKE_HIP_ARCHITECTURES)
        set(CMAKE_HIP_ARCHITECTURES ${AMDGPU_TARGETS})
    endif()
    cmake_minimum_required(VERSION 3.21)
    enable_language(HIP)
endif()
```

--------------------------------

TITLE: Run Model with File Content Prompt
DESCRIPTION: Runs a model and passes the content of a local file (README.md) as part of the prompt using command substitution.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_11

LANGUAGE: shell
CODE:
```
ollama run llama3.2 "Summarize this file: $(cat README.md)"
```

--------------------------------

TITLE: Build Ollama Docker Image
DESCRIPTION: Builds the Ollama Docker image from the root directory of the repository.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_5

LANGUAGE: dockerfile
CODE:
```
docker build .
```

--------------------------------

TITLE: Ollama GUI Clients and Desktop Applications
DESCRIPTION: This section lists various graphical user interfaces and desktop applications designed to interact with Ollama. These tools often provide a user-friendly way to manage models, chat with LLMs, and configure settings.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_51

LANGUAGE: Python
CODE:
```
Project: Ollama-Kis
Description: A simple easy-to-use GUI with sample custom LLM for Drivers Education
Link: https://github.com/elearningshow/ollama-kis
```

LANGUAGE: Python
CODE:
```
Project: PyGPT
Description: AI desktop assistant for Linux, Windows, and Mac
Link: https://github.com/szczyglis-dev/py-gpt
```

LANGUAGE: Python
CODE:
```
Project: Alpaca
Description: An Ollama client application for Linux and macOS made with GTK4 and Adwaita
Link: https://github.com/Jeffser/Alpaca
```

LANGUAGE: Java
CODE:
```
Project: Ollama4j Web UI
Description: Java-based Web UI for Ollama built with Vaadin, Spring Boot, and Ollama4j
Link: https://github.com/ollama4j/ollama4j-web-ui
```

LANGUAGE: Swift
CODE:
```
Project: PyOllaMx
Description: macOS application capable of chatting with both Ollama and Apple MLX models.
Link: https://github.com/kspviswa/pyOllaMx
```

LANGUAGE: Python
CODE:
```
Project: Cherry Studio
Description: Desktop client with Ollama support
Link: https://github.com/kangfenmao/cherry-studio
```

LANGUAGE: Python
CODE:
```
Project: Tkinter-based client
Description: Python tkinter-based Client for Ollama
Link: https://github.com/chyok/ollama-gui
```

LANGUAGE: Python
CODE:
```
Project: Promptery
Description: desktop client for Ollama.
Link: https://github.com/promptery/promptery
```

LANGUAGE: Python
CODE:
```
Project: Ollama App
Description: Modern and easy-to-use multi-platform client for Ollama
Link: https://github.com/JHubi1/ollama-app
```

--------------------------------

TITLE: Ollama CLI Tools and Utilities
DESCRIPTION: Various command-line utilities and tools that interact with or manage Ollama, including model conversion and registry browsing.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_70

LANGUAGE: Shell
CODE:
```
# x-cmd ollama: A command-line tool for interacting with Ollama.
# Usage: x-cmd ollama --model llama2 "Generate code snippet"
```

LANGUAGE: Shell
CODE:
```
# bb7: A command-line tool that may interact with Ollama.
# Specific usage depends on the tool's implementation.
```

LANGUAGE: Shell
CODE:
```
# cmdh: Command history manager, potentially with AI integration via Ollama.
```

LANGUAGE: Shell
CODE:
```
# ooo: A tool for interacting with Ollama, possibly for model management or chat.
```

LANGUAGE: Shell
CODE:
```
# llm-ollama: Integration for Datasette's LLM CLI.
# Usage: datasette query "SELECT llm('What is data?', model='llama2')"
```

LANGUAGE: Shell
CODE:
```
# typechat-cli: CLI for TypeChat, which can integrate with LLMs like Ollama.
```

LANGUAGE: Shell
CODE:
```
# ShellOracle: AI assistant for shell commands, potentially using Ollama.
```

LANGUAGE: Shell
CODE:
```
# tlm: A tool for managing and interacting with LLMs, including Ollama.
```

LANGUAGE: Shell
CODE:
```
# podman-ollama: Integration for running Ollama with Podman.
```

LANGUAGE: Shell
CODE:
```
# gollama: A Go client or tool for interacting with Ollama.
```

LANGUAGE: Shell
CODE:
```
# ParLlama: A project related to parallel processing or interaction with Ollama.
```

--------------------------------

TITLE: IDE and Editor Integrations with Ollama
DESCRIPTION: Plugins and extensions for Integrated Development Environments (IDEs) and text editors that enable AI-powered coding assistance using Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_122

LANGUAGE: Python
CODE:
```
https://github.com/continuedev/continue
https://github.com/ex3ndr/llama-coder
https://github.com/bernardo-bruning/ollama-copilot
https://github.com/rjmacarthy/twinny
https://github.com/RussellCanfield/wingman-ai
https://github.com/yaroslavyaroslav/OpenAI-sublime-text
https://github.com/Palm1r/QodeAssist
```

LANGUAGE: TypeScript
CODE:
```
https://github.com/longy2k/obsidian-bmo-chatbot
```

LANGUAGE: Go
CODE:
```
https://github.com/samalba/dagger-chatbot
```

--------------------------------

TITLE: Run Ollama Docker Container (AMD GPU)
DESCRIPTION: Starts a detached Ollama Docker container with AMD GPU acceleration using the 'rocm' tag. It mounts a volume for persistent data and maps the default Ollama port.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_7

LANGUAGE: shell
CODE:
```
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

--------------------------------

TITLE: Ollama Basic Chat
DESCRIPTION: A chat client implementation using HyperDiv Reactive UI that connects with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_42

LANGUAGE: Python
CODE:
```
https://github.com/rapidarchitect/ollama_basic_chat/
```

--------------------------------

TITLE: Remove a Model
DESCRIPTION: Removes a specified model from the local Ollama installation.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_7

LANGUAGE: shell
CODE:
```
ollama rm llama3.2
```

--------------------------------

TITLE: Developer Tools and Extensions
DESCRIPTION: Tools and extensions that enhance the development experience with Ollama, including VSCode extensions and utility launchers.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_60

LANGUAGE: TypeScript
CODE:
```
AI Toolkit for Visual Studio Code: https://aka.ms/ai-tooklit/ollama-docs
Microsoft-official VSCode extension for chatting, testing, and evaluating models with Ollama support
```

LANGUAGE: Shell
CODE:
```
ollama launcher: https://github.com/NGC13009/ollama-launcher
Launcher for Ollama providing server launching, management, and configuration functions
```

--------------------------------

TITLE: Ollama CLI: Create Model
DESCRIPTION: Details the `ollama create` command for building models from a Modelfile, specifying the model name and the path to the Modelfile.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_5

LANGUAGE: shell
CODE:
```
ollama create mymodel -f ./Modelfile
```

--------------------------------

TITLE: Ollama API Reference
DESCRIPTION: Documentation for the Ollama API, covering endpoints, request/response formats, and common operations for interacting with Ollama models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_63

LANGUAGE: APIDOC
CODE:
```
Ollama API Overview:
  Base URL: http://localhost:11434 (default)

Endpoints:

1. /api/tags
   - GET: List available models.
   - Description: Retrieves a list of all models available on the Ollama instance.
   - Response:
     {
       "models": [
         {
           "digest": "sha256:...",
           "model": "llama2",
           "modified_at": "2023-08-01T10:00:00Z",
           "size": 3500000000,
           "details": {
             "parent_model": "",
             "format": "gguf",
             "families": ["llama"],
             "parameter_size": "7B",
             "quantization_level": "Q4_0"
           }
         }
       ]
     }

2. /api/pull
   - POST: Pull a model.
   - Request Body:
     {
       "name": "llama2",
       "insecure": false (optional)
     }
   - Description: Downloads a model from the Ollama registry.
   - Response:
     Stream of status updates.

3. /api/generate
   - POST: Generate a response from a model.
   - Request Body:
     {
       "model": "llama2",
       "prompt": "Why is the sky blue?",
       "stream": true (optional, default: false),
       "options": {
         "temperature": 0.8 (optional)
       }
     }
   - Description: Sends a prompt to the specified model and receives a generated response.
   - Response (if stream: false):
     {
       "model": "llama2",
       "created_at": "2023-08-01T10:05:00Z",
       "response": "The sky appears blue due to Rayleigh scattering...",
       "done": true
     }
   - Response (if stream: true):
     Stream of JSON objects, each containing a chunk of the response.

4. /api/chat
   - POST: Chat with a model.
   - Request Body:
     {
       "model": "llama2",
       "messages": [
         {"role": "user", "content": "Hi!"}
       ],
       "stream": true (optional, default: false)
     }
   - Description: Engages in a conversational chat with the model, maintaining context through message history.
   - Response (if stream: false):
     {
       "model": "llama2",
       "created_at": "2023-08-01T10:10:00Z",
       "message": {
         "role": "assistant",
         "content": "Hello! How can I help you today?"
       },
       "done": true
     }
   - Response (if stream: true):
     Stream of JSON objects, each containing a chunk of the chat response.

5. /api/embeddings
   - POST: Generate embeddings for a given text.
   - Request Body:
     {
       "model": "llama2",
       "prompt": "This is a test sentence."
     }
   - Description: Creates vector embeddings for the provided text using the specified model.
   - Response:
     {
       "embeddings": [0.1, 0.2, -0.3, ...]
     }

6. /api/delete
   - DELETE: Delete a model.
   - Request Body:
     {
       "name": "llama2"
     }
   - Description: Removes a model from the Ollama instance.

7. /api/show
   - POST: Show model details.
   - Request Body:
     {
       "name": "llama2"
     }
   - Description: Retrieves detailed information about a specific model.
   - Response:
     {
       "model": "llama2",
       "modified_at": "2023-08-01T10:00:00Z",
       "size": 3500000000,
       "digest": "sha256:...",
       "details": {
         "parent_model": "",
         "format": "gguf",
         "families": ["llama"],
         "parameter_size": "7B",
         "quantization_level": "Q4_0"
       }
     }

Options for /api/generate and /api/chat:
  - temperature: Controls randomness. Lower values make output more focused and deterministic (0.0 - 2.0).
  - top_k: Samples from the top K most likely next tokens (k > 0).
  - top_p: Samples from the smallest set of tokens whose cumulative probability exceeds P (0.0 - 1.0).
  - num_predict: Maximum number of tokens to predict.
  - stop: Sequences that will cause the generation to stop.
  - repeat_last_n: The number of tokens to consider for the repeat penalty (default: 512).
  - repeat_penalty: Penalizes repeated tokens (default: 1.1).
  - presence_penalty: Penalizes new tokens based on whether they appear in the text so far (default: 0).
  - frequency_penalty: Penalizes new tokens based on their frequency in the text so far (default: 0).
  - mirostat: Enable Mirostat sampling.
  - mirostat_lr: Learning rate for Mirostat.
  - mirostat_ent: Target entropy for Mirostat.
  - num_ctx: The size of the context window for the model (default: 2048).
  - num_batch: Batch size for prompt processing (default: 512).
  - num_gpu: The number of GPUs to use for computation (default: 1).
  - num_thread: The number of CPU threads to use (default: -1, auto).
  - split_on_word: Whether to split on word boundaries (default: true).
  - keep_alive: Keep the model loaded in memory for a specified duration (e.g., "5m", "1h").
  - keep_alive_timeout: Timeout for keep_alive.
  - tfs_z: Tail free sampling parameter (default: 1.0).
  - typical_p: Typical probability sampling parameter (default: 1.0).
  - use_mlock: Whether to use mlock to keep the model in memory (default: false).
  - use_mmap: Whether to use mmap to load the model (default: true).
  - numa: Whether to use NUMA optimization (default: false).
  - seed: Seed for random number generation.
  - low_vram: Whether to use lower VRAM optimization (default: false).
  - vocab_only: Whether to only load the vocabulary (default: false).
  - use_flash_attention: Whether to use Flash Attention (default: false).
  - main_gpu: The main GPU to use for computation (default: 0).
  - head_dims: The number of dimensions for each head (default: 0).
  - rnn_layer: Whether to use RNN layers (default: false).
  - main_gpu: The main GPU to use for computation (default: 0).
  - head_dims: The number of dimensions for each head (default: 0).
  - rnn_layer: Whether to use RNN layers (default: false).
  - embedding_only: Whether to only load the embedding weights (default: false).
  - context_fallback: Whether to fallback to a smaller context size if the requested size is too large (default: true).
  - rope_frequency: The frequency for RoPE scaling (default: 0).
  - rope_frequency_base: The base frequency for RoPE scaling (default: 0).
  - rope_scale: The scale factor for RoPE scaling (default: 0).
  - num_kv_heads: The number of KV heads (default: 0).
  - num_attention_heads: The number of attention heads (default: 0).
  - num_hidden_layers: The number of hidden layers (default: 0).
  - vocab_size: The size of the vocabulary (default: 0).
  - gpu_layers: The number of layers to offload to the GPU (default: 0).
  - batch_size: The batch size for prompt processing (default: 512).
  - prompt_batch_size: The batch size for prompt processing (default: 512).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 2048).
  - n_batch: Batch size for prompt processing (default: 512).
  - n_gpu: The number of GPUs to use for computation (default: 1).
  - n_thread: The number of CPU threads to use (default: -1, auto).
  - n_predict: Maximum number of tokens to predict.
  - n_ctx: The size of the context window for the model (default: 20
```

--------------------------------

TITLE: Build Ollama on Windows with ROCm
DESCRIPTION: Configures and builds the Ollama project on Windows for ROCm acceleration using CMake and Ninja. Requires specific C/C++ compilers.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_3

LANGUAGE: shell
CODE:
```
cmake -B build -G Ninja -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++
cmake --build build --config Release
```

--------------------------------

TITLE: Installing Specific Ollama Versions on Linux
DESCRIPTION: Shows how to install a specific version of Ollama on Linux using a curl command and specifying the `OLLAMA_VERSION` environment variable.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_3

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | OLLAMA_VERSION=0.5.7 sh
```

--------------------------------

TITLE: Ollama Text Completion Example
DESCRIPTION: Demonstrates how to create a text completion using the Ollama API. It specifies the model to use and the prompt for generating the completion.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_8

LANGUAGE: javascript
CODE:
```
const completion = await openai.completions.create({
    model: "llama3.2",
    prompt: "Say this is a test."
})
```

--------------------------------

TITLE: OllamaSpring
DESCRIPTION: A macOS client specifically built for interacting with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_29

LANGUAGE: Swift
CODE:
```
https://github.com/CrazyNeil/OllamaSpring
```

--------------------------------

TITLE: Running Ollama Go Tests with Synctest Experiment
DESCRIPTION: This command runs Go tests with the `synctest` experiment enabled, which is useful for catching build or test failures related to concurrency that might not appear without it. This is particularly relevant for Go 1.24+.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_11

LANGUAGE: shell
CODE:
```
GOEXPERIMENT=synctest go test ./...
```

--------------------------------

TITLE: Ollama Chat Request Example
DESCRIPTION: Demonstrates a basic chat request to the Ollama API with a specified model and messages. Includes parameters for model, messages, and stream.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_40

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ]
}'
```

--------------------------------

TITLE: Other Notable Projects
DESCRIPTION: This section includes other projects that integrate with Ollama, covering areas like containerization, AI writing assistance, and general LLM toolkits.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_56

LANGUAGE: Python
CODE:
```
Project: Painting Droid
Description: Painting app with AI integrations
Link: https://github.com/mateuszmigas/painting-droid
```

LANGUAGE: Python
CODE:
```
Project: Kerlig AI
Description: AI writing assistant for macOS
Link: https://www.kerlig.com/
```

LANGUAGE: Python
CODE:
```
Project: Harbor
Description: Containerized LLM Toolkit with Ollama as default backend
Link: https://github.com/av/harbor
```

LANGUAGE: Python
CODE:
```
Project: ARGO
Description: Locally download and run Ollama and Huggingface models with RAG and deep research on Mac/Windows/Linux
Link: https://github.com/xark-argo/argo
```

LANGUAGE: Python
CODE:
```
Project: Perfect Memory AI
Description: Productivity AI assists personalized by what you have seen on your screen, heard, and said in the meetings
Link: https://www.perfectmemory.ai/
```

--------------------------------

TITLE: ChatML Template Example
DESCRIPTION: An example of the ChatML template format, commonly used for models like DBRX, Neural Chat, and Orca 2. It structures the conversation with specific tokens to delineate roles and messages.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_2

LANGUAGE: go
CODE:
```
{{- range .Messages }}<|im_start|>{{ .Role }}
{{ .Content }}<|im_end|>
{{ end }}<|im_start|>assistant

```

--------------------------------

TITLE: Preload Model with Ollama CLI
DESCRIPTION: Shows how to preload a model directly from the Ollama command-line interface by running it with an empty input.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_13

LANGUAGE: shell
CODE:
```
ollama run llama3.2 ""
```

--------------------------------

TITLE: RWKV-Runner
DESCRIPTION: An offline LLM deployment tool for RWKV models, which can also be used as a client for ChatGPT and Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_26

LANGUAGE: Python
CODE:
```
https://github.com/josStorer/RWKV-Runner
```

--------------------------------

TITLE: Spring AI Ollama Chat Reference
DESCRIPTION: Reference for using Ollama with Spring AI for chat applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_72

LANGUAGE: Java
CODE:
```
import org.springframework.ai.ollama.OllamaChatClient;
import org.springframework.ai.chat.messages.UserMessage;

// Assuming OllamaChatClient is configured and available
OllamaChatClient chatClient = new OllamaChatClient("http://localhost:11434").withModel("llama2");

String response = chatClient.call(new UserMessage("Tell me a joke"));
System.out.println(response);
```

--------------------------------

TITLE: Uninstall Ollama
DESCRIPTION: Removes Ollama from the system, including stopping and disabling the service, removing the binary, user, group, and libraries.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_11

LANGUAGE: shell
CODE:
```
sudo systemctl stop ollama
sudo systemctl disable ollama
sudo rm /etc/systemd/system/ollama.service
sudo rm $(which ollama)
sudo rm -r /usr/share/ollama
sudo userdel ollama
sudo groupdel ollama
sudo rm -rf /usr/local/lib/ollama
```

--------------------------------

TITLE: Set Context Window Size
DESCRIPTION: Demonstrates how to set the context window size for Ollama. This can be done via an environment variable when starting the server or using a command within `ollama run`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_1

LANGUAGE: shell
CODE:
```
OLLAMA_CONTEXT_LENGTH=8192 ollama serve
```

LANGUAGE: shell
CODE:
```
/set parameter num_ctx 4096
```

--------------------------------

TITLE: Copy Ollama Model Request Example (Shell)
DESCRIPTION: Example `curl` command demonstrating how to send a POST request to the `/api/copy` endpoint to duplicate an Ollama model. It specifies the `source` model to be copied and the `destination` name for the new model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_58

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/copy -d '{  "source": "llama3.2",  "destination": "llama3-backup"}'
```

--------------------------------

TITLE: Conditional HIP and rocBLAS Installation
DESCRIPTION: This snippet demonstrates how CMake is used to conditionally install the rocBLAS library within the HIP installation directory. It iterates through a list of directories and installs rocBLAS if the HIP component is enabled.

SOURCE: https://github.com/ollama/ollama/blob/main/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
install(DIRECTORY ${HIP_LIB_BIN_INSTALL_DIR}/rocblas DESTINATION ${OLLAMA_HIP_INSTALL_DIR} COMPONENT HIP)
                break()
            endif()
        endforeach()
    endif()
endif()
```

--------------------------------

TITLE: Jirapt
DESCRIPTION: Integrates with Jira to generate issues, tasks, and epics, likely leveraging LLMs through Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_33

LANGUAGE: Python
CODE:
```
https://github.com/AliAhmedNada/jirapt
```

--------------------------------

TITLE: Pull Ollama Model Request Example (Shell)
DESCRIPTION: Example `curl` command demonstrating how to send a POST request to the `/api/pull` endpoint to download an Ollama model. The `model` parameter specifies the name of the model to be pulled from the library.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_62

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/pull -d '{  "model": "llama3.2"}'
```

--------------------------------

TITLE: Build Ollama Docker Image with ROCm
DESCRIPTION: Builds the Ollama Docker image with ROCm acceleration support using a build argument.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_6

LANGUAGE: dockerfile
CODE:
```
docker build --build-arg FLAVOR=rocm .
```

--------------------------------

TITLE: Uninstall Ollama Service (Shell)
DESCRIPTION: Removes the Ollama systemd service, disabling it from starting on boot and stopping it if it's currently running.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_12

LANGUAGE: shell
CODE:
```
sudo systemctl stop ollama
sudo systemctl disable ollama
sudo rm /etc/systemd/system/ollama.service
```

--------------------------------

TITLE: Show Model Information
DESCRIPTION: Displays detailed information about a specific local model.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_12

LANGUAGE: shell
CODE:
```
ollama show llama3.2
```

--------------------------------

TITLE: Copy a Model
DESCRIPTION: Copies an existing local model to a new name.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_8

LANGUAGE: shell
CODE:
```
ollama cp llama3.2 my-model
```

--------------------------------

TITLE: System and Workflow Integrations
DESCRIPTION: Projects that integrate Ollama into broader systems like server management, document processing, and agent-based workflows.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_61

LANGUAGE: Go
CODE:
```
1Panel: https://github.com/1Panel-dev/1Panel/
Web-based Linux Server Management Tool with Ollama integration
```

LANGUAGE: Python
CODE:
```
Mayan EDMS: https://gitlab.com/mayan-edms/mayan-edms
Document management system with Ollama-driven workflows for file organization and automation
```

LANGUAGE: Python
CODE:
```
screenpipe: https://github.com/mediar-ai/screenpipe
Build agents powered by screen history, potentially integrating with Ollama
```

LANGUAGE: Python
CODE:
```
Writeopia: https://github.com/Writeopia/Writeopia
Text editor with integration with Ollama
```

LANGUAGE: JavaScript
CODE:
```
AppFlowy: https://github.com/AppFlowy-IO/AppFlowy
AI collaborative workspace with Ollama, cross-platform and self-hostable
```

LANGUAGE: Python
CODE:
```
ai-hub: https://github.com/Aj-Seven/ai-hub
AI Hub supporting multiple models via API keys and chat via Ollama API
```

--------------------------------

TITLE: Ollama-chats RPG
DESCRIPTION: A project that enables RPG-style chat experiences using Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_43

LANGUAGE: Python
CODE:
```
https://github.com/drazdra/ollama-chats
```

--------------------------------

TITLE: Ollama Grid Search
DESCRIPTION: An application designed to evaluate and compare different LLM models available through Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_27

LANGUAGE: Python
CODE:
```
https://github.com/dezoito/ollama-grid-search
```

--------------------------------

TITLE: Lobe Chat Integration
DESCRIPTION: Documentation on how to integrate Lobe Chat with Ollama for self-hosting and local LLM interactions.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_41

LANGUAGE: APIDOC
CODE:
```
Lobe Chat - Ollama Integration:

Description: Lobe Chat is an open-source chatbot application that can be configured to use Ollama as its backend for language model interactions.

Integration Steps:
1. Self-host Lobe Chat.
2. Configure the environment variables or settings to point to your Ollama instance.
   - Typically involves setting an API endpoint URL for Ollama.

Key Features:
- Supports various Ollama models.
- Provides a rich chat interface.
- Enables local LLM deployment.

Reference:
https://lobehub.com/docs/self-hosting/examples/ollama
```

--------------------------------

TITLE: LLM-X
DESCRIPTION: A Progressive Web App (PWA) for interacting with LLMs, likely supporting Ollama for local model deployment.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_48

LANGUAGE: JavaScript
CODE:
```
https://github.com/mrdjohnson/llm-x
```

--------------------------------

TITLE: BrainSoup
DESCRIPTION: A flexible native client with RAG and multi-agent automation capabilities, designed to work with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_24

LANGUAGE: Unknown
CODE:
```
https://www.nurgo-software.com/products/brainsoup
```

--------------------------------

TITLE: Run Multimodal Model with Image
DESCRIPTION: Executes a multimodal model, providing an image file path as part of the prompt to analyze the image content.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_10

LANGUAGE: shell
CODE:
```
ollama run llava "What's in this image? /Users/jmorgan/Desktop/smile.png"
```

--------------------------------

TITLE: IntelliBar
DESCRIPTION: An AI-powered assistant for macOS that likely integrates with local LLM services like Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_44

LANGUAGE: Unknown
CODE:
```
intellibar.app/
```

--------------------------------

TITLE: Ollama Mobile and Cross-Platform Integrations
DESCRIPTION: Projects enabling Ollama usage on mobile platforms, including Apple Vision Pro, and cross-platform applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_68

LANGUAGE: Swift
CODE:
```
// SwiftChat: Cross-platform AI chat app supporting Apple Vision Pro
// Utilizes Ollama for backend model interactions.
```

LANGUAGE: Swift
CODE:
```
// Enchanted: Another iOS/iPadOS chat client potentially supporting Ollama.
```

--------------------------------

TITLE: Web & Desktop UIs for Ollama
DESCRIPTION: This section lists various user interfaces and applications built to interact with Ollama. These projects offer different functionalities such as chat interfaces, RAG capabilities, and cross-platform support.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_20

LANGUAGE: JavaScript
CODE:
```
https://github.com/open-webui/open-webui
https://github.com/aws-samples/swift-chat
https://github.com/AugustDev/enchanted
https://github.com/fmaclen/hollama
https://github.com/ParisNeo/lollms-webui
https://github.com/danny-avila/LibreChat
https://github.com/bionic-gpt/bionic-gpt
https://github.com/rtcfirefly/ollama-ui
https://github.com/jikkuatwork/saddle
https://github.com/ivanfioravanti/chatbot-ollama
https://github.com/mckaywrigley/chatbot-ui
https://github.com/ollama-interface/Ollama-Gui
https://github.com/richawo/minimal-llm-ui
https://github.com/kevinhermawan/Ollamac
https://github.com/enricoros/big-AGI
https://github.com/cheshire-cat-ai/core
https://github.com/semperai/amica
https://github.com/BruceMacD/chatd
https://github.com/kghandour/Ollama-SwiftUI
https://github.com/langgenius/dify
mindmac.app
https://github.com/jakobhoeg/nextjs-ollama-llm-ui
msty.app
https://github.com/Bin-Huang/Chatbox
https://github.com/tgraupmann/WinForm_Ollama_Copilot
https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web
https://github.com/mmo80/alpaca-webui
https://github.com/enoch1118/ollamaGUI
https://github.com/InternLM/OpenAOE
https://github.com/leonid20000/OdinRunes
https://github.com/mrdjohnson/llm-x
https://github.com/Mintplex-Labs/anything-llm
https://github.com/rapidarchitect/ollama_basic_chat
https://github.com/drazdra/ollama-chats
intellibar.app
https://github.com/AliAhmedNada/jirapt
https://github.com/AliAhmedNada/ojira
https://github.com/reid41/QA-Pilot
https://github.com/sugarforever/chat-ollama
https://github.com/Nagi-ovo/CRAG-Ollama-Chat
https://github.com/infiniflow/ragflow
https://github.com/StreamDeploy-DevRel/streamdeploy-llm-app-scaffold
https://github.com/swuecho/chat
https://github.com/lobehub/lobe-chat
https://github.com/datvodinh/rag-chatbot.git
www.nurgo-software.com/products/brainsoup
https://github.com/Renset/macai
https://github.com/josStorer/RWKV-Runner
https://github.com/dezoito/ollama-grid-search
https://github.com/Otacon/olpaka
casibase.org
https://github.com/CrazyNeil/OllamaSpring
https://github.com/kartikm7/llocal
https://github.com/dcSpark/shinkai-apps
https://github.com/zeyoyt/ailama
https://github.com/rapidarchitect/ollama_mesop/
https://github.com/SciPhi-AI/R2R
```

LANGUAGE: Python
CODE:
```
https://github.com/bionic-gpt/bionic-gpt
https://github.com/langgenius/dify
https://github.com/InternLM/OpenAOE
https://github.com/mrdjohnson/llm-x
https://github.com/rapidarchitect/ollama_basic_chat
https://github.com/Nagi-ovo/CRAG-Ollama-Chat
https://github.com/infiniflow/ragflow
https://github.com/StreamDeploy-DevRel/streamdeploy-llm-app-scaffold
https://github.com/datvodinh/rag-chatbot.git
https://github.com/josStorer/RWKV-Runner
https://github.com/SciPhi-AI/R2R
```

LANGUAGE: Swift
CODE:
```
https://github.com/aws-samples/swift-chat
https://github.com/AugustDev/enchanted
https://github.com/kghandour/Ollama-SwiftUI
```

LANGUAGE: React
CODE:
```
https://github.com/open-webui/open-webui
https://github.com/rtcfirefly/ollama-ui
https://github.com/ivanfioravanti/chatbot-ollama
https://github.com/mckaywrigley/chatbot-ui
https://github.com/ollama-interface/Ollama-Gui
https://github.com/richawo/minimal-llm-ui
https://github.com/lobehub/lobe-chat
```

LANGUAGE: Next.js
CODE:
```
https://github.com/jakobhoeg/nextjs-ollama-llm-ui
https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web
```

LANGUAGE: Typescript
CODE:
```
https://github.com/ollama-interface/Ollama-Gui
```

LANGUAGE: Flutter
CODE:
```
https://github.com/Otacon/olpaka
```

LANGUAGE: C#
CODE:
```
https://github.com/tgraupmann/WinForm_Ollama_Copilot
```

LANGUAGE: Go
CODE:
```
https://github.com/fmaclen/hollama
```

--------------------------------

TITLE: ojira
DESCRIPTION: A Jira Chrome plugin designed to easily generate descriptions for tasks, potentially using Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_34

LANGUAGE: JavaScript
CODE:
```
https://github.com/AliAhmedNada/ojira
```

--------------------------------

TITLE: Run Ollama Tests with synctest enabled
DESCRIPTION: Executes Ollama tests with the 'synctest' package enabled to catch potential build or test failures locally. This can also be set globally via 'go env -w GOEXPERIMENT=synctest'.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/development.md#_snippet_8

LANGUAGE: go
CODE:
```
GOEXPERIMENT=synctest go test ./...
```

--------------------------------

TITLE: Ollama Retrieve Model Example
DESCRIPTION: Illustrates how to retrieve detailed information about a specific model available in Ollama. This includes model name and other relevant metadata.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_10

LANGUAGE: javascript
CODE:
```
const model = await openai.models.retrieve("llama3.2")
```

--------------------------------

TITLE: Run a Model Locally with Ollama Docker
DESCRIPTION: Executes a command inside the running Ollama Docker container to download and run a specific model, such as llama3.2.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/docker.md#_snippet_8

LANGUAGE: shell
CODE:
```
docker exec -it ollama ollama run llama3.2
```

--------------------------------

TITLE: Ollama Push API Response (Streaming - Starting Upload)
DESCRIPTION: This JSON object indicates the start of a model layer upload during a streaming push operation, providing the digest and total size of the layer being uploaded.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_70

LANGUAGE: json
CODE:
```
{
  "status": "starting upload",
  "digest": "sha256:bc07c81de745696fdf5afca05e065818a8149fb0c77266fb584d9b2cba3711ab",
  "total": 1928429856
}
```

--------------------------------

TITLE: Automation and Workflow Tools
DESCRIPTION: Tools and workflows that automate tasks or provide interfaces for interacting with Ollama, including system management and custom workflows.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_125

LANGUAGE: Shell
CODE:
```
https://github.com/nischalj10/headless-ollama
https://github.com/xuyangbocn/terraform-aws-self-host-llm
```

LANGUAGE: JavaScript
CODE:
```
https://github.com/imoize/plasmoid-ollamacontrol
https://github.com/jakubburkiewicz/node-red-contrib-ollama
https://github.com/zeitlings/alfred-ollama
```

--------------------------------

TITLE: Browser Extensions and Integrations
DESCRIPTION: This section highlights browser extensions and other integrations that bring Ollama's capabilities directly into the browsing experience or other applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_54

LANGUAGE: JavaScript
CODE:
```
Project: Cline
Description: VSCode extension for multi-file/whole-repo coding
Link: https://github.com/cline/cline
```

LANGUAGE: JavaScript
CODE:
```
Project: SpaceLlama
Description: Firefox and Chrome extension to quickly summarize web pages with ollama in a sidebar
Link: https://github.com/tcsenpai/spacellama
```

LANGUAGE: JavaScript
CODE:
```
Project: YouLama
Description: Webapp to quickly summarize any YouTube video, supporting Invidious as well
Link: https://github.com/tcsenpai/youlama
```

LANGUAGE: JavaScript
CODE:
```
Project: OpenTalkGpt
Description: Chrome Extension to manage open-source models supported by Ollama, create custom models, and chat with models from a user-friendly UI
Link: https://github.com/adarshM84/OpenTalkGpt
```

--------------------------------

TITLE: Odin Runes
DESCRIPTION: A project related to Odin Runes that may involve LLM integration, potentially with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_47

LANGUAGE: Unknown
CODE:
```
https://github.com/leonid20000/OdinRunes
```

--------------------------------

TITLE: Ollama with Google Mesop
DESCRIPTION: An implementation of a Mesop Chat Client that integrates with Ollama, providing a chat interface for interacting with local LLM models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_22

LANGUAGE: Python
CODE:
```
https://github.com/rapidarchitect/ollama_mesop/
```

--------------------------------

TITLE: Ollama IDE and Editor Integrations
DESCRIPTION: Plugins and extensions for popular Integrated Development Environments (IDEs) and text editors that provide seamless integration with Ollama for features like code completion, generation, and chat.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_65

LANGUAGE: Emacs Lisp
CODE:
```
;; Ellama Emacs client
;; Usage: (ellama-chat "What is Ollama?")
```

LANGUAGE: Emacs Lisp
CODE:
```
;; Emacs client for Ollama
;; Usage: (ollama-send-message "Explain this code snippet")
```

LANGUAGE: Emacs Lisp
CODE:
```
;; neollama: UI client for interacting with models from within Neovim
;; Usage: Requires Neovim configuration to call Ollama functions
```

LANGUAGE: Emacs Lisp
CODE:
```
;; ollama.nvim: Neovim plugin for Ollama
;; Usage: :OllamaChat "Generate a Python function"
```

LANGUAGE: Emacs Lisp
CODE:
```
;; ollero.nvim: Neovim plugin for Ollama
;; Usage: :OlleroSend "Write a SQL query"
```

LANGUAGE: Emacs Lisp
CODE:
```
;; ollama-chat.nvim: Neovim chat client for Ollama
;; Usage: :OllamaChatNew "Summarize this document"
```

LANGUAGE: Emacs Lisp
CODE:
```
;; ogpt.nvim: Neovim client for GPT models including Ollama
;; Usage: :OgptSend "Create a commit message"
```

LANGUAGE: Emacs Lisp
CODE:
```
;; gptel Emacs client
;; Usage: (gptel-send-message "Explain the concept of recursion")
```

LANGUAGE: Emacs Lisp
CODE:
```
;; vim-intelligence-bridge: Simple interaction of "Ollama" with the Vim editor
;; Usage: Commands within Vim to send prompts to Ollama
```

LANGUAGE: Emacs Lisp
CODE:
```
;; orbiton: Configuration-free text editor with tab completion with Ollama.
;; Usage: Editor features for AI-assisted coding and completion
```

--------------------------------

TITLE: Note-Taking and Knowledge Management Plugins
DESCRIPTION: Plugins for note-taking applications like Obsidian and Logseq that integrate Ollama for AI-powered features such as summarization and quiz generation.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_124

LANGUAGE: JavaScript
CODE:
```
https://github.com/hinterdupfinger/obsidian-ollama
https://github.com/omagdy7/ollama-logseq
https://github.com/andersrex/notesollama
https://github.com/pfrankov/obsidian-local-gpt
https://github.com/ECuiDev/obsidian-quiz-generator
https://github.com/philffm/ai-summary-helper
```

LANGUAGE: TypeScript
CODE:
```
https://github.com/longy2k/obsidian-bmo-chatbot
```

--------------------------------

TITLE: Remove Ollama Libraries (Shell)
DESCRIPTION: Removes any installed Ollama libraries from the system. This command targets common library installation paths.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_15

LANGUAGE: shell
CODE:
```
sudo rm -rf /usr/local/lib/ollama
```

--------------------------------

TITLE: AiLama
DESCRIPTION: A Discord User App that allows interaction with Ollama from anywhere within Discord.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_32

LANGUAGE: JavaScript
CODE:
```
https://github.com/zeyoyt/ailama
```

--------------------------------

TITLE: Ollama Chat Response (Streaming with Tools)
DESCRIPTION: Example of a streaming response that includes a tool call from the Ollama API.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_25

LANGUAGE: json
CODE:
```
{
    "model": "llama3.2",
    "created_at": "2025-07-07T20:22:19.184789Z",
    "message": {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "function": {
                    "name": "get_weather",
                    "arguments": {
                        "city": "Tokyo"
                    }
                }
            }
        ]
    },
    "done": false
}

{
  "model":"llama3.2",
  "created_at":"2025-07-07T20:22:19.19314Z",
  "message": {
    "role": "assistant",
    "content": ""
  },
  "done_reason": "stop",
  "done": true,
  "total_duration": 182242375,
  "load_duration": 41295167,
  "prompt_eval_count": 169,
  "prompt_eval_duration": 24573166,
  "eval_count": 15,
  "eval_duration": 115959084
}
```

--------------------------------

TITLE: RAGFlow
DESCRIPTION: An open-source Retrieval-Augmented Generation engine built on deep document understanding, compatible with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_38

LANGUAGE: Python
CODE:
```
https://github.com/infiniflow/ragflow
```

--------------------------------

TITLE: Disabling Ollama Auto-Startup on Windows
DESCRIPTION: Steps to prevent Ollama from automatically starting when a user logs into a Windows machine.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_21

LANGUAGE: APIDOC
CODE:
```
Windows Startup Item Removal
  Description: To disable Ollama from starting automatically on Windows, remove the Ollama shortcut from the Startup folder.
  Path: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Ollama.lnk
```

--------------------------------

TITLE: Game Development Integration
DESCRIPTION: Tools and extensions for game development platforms like Unity that facilitate communication with Ollama for AI-driven features within games.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_126

LANGUAGE: C#
CODE:
```
https://github.com/HardCodeDev777/SimpleOllamaUnity
https://github.com/HardCodeDev777/UnityCodeLama
```

--------------------------------

TITLE: macai
DESCRIPTION: A macOS client for Ollama, ChatGPT, and other compatible API back-ends, offering a native experience for interacting with LLMs.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_25

LANGUAGE: Swift
CODE:
```
https://github.com/Renset/macai
```

--------------------------------

TITLE: Upgrade Ollama on Linux
DESCRIPTION: This command upgrades Ollama on Linux by re-running the official installation script. It fetches the latest version and applies it.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_0

LANGUAGE: shell
CODE:
```
curl -fsSL https://ollama.com/install.sh | sh
```

--------------------------------

TITLE: OllamaGUI
DESCRIPTION: A graphical user interface for Ollama, providing an easier way to manage and interact with local language models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_46

LANGUAGE: Python
CODE:
```
https://github.com/enoch1118/ollamaGUI
```

--------------------------------

TITLE: ChatOllama
DESCRIPTION: An open-source chatbot based on Ollama with Knowledge Bases, allowing for informed conversations.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_36

LANGUAGE: Python
CODE:
```
https://github.com/sugarforever/chat-ollama
```

--------------------------------

TITLE: Stop a Running Model
DESCRIPTION: Stops a model that is currently loaded and running.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_15

LANGUAGE: shell
CODE:
```
ollama stop llama3.2
```

--------------------------------

TITLE: chat
DESCRIPTION: A web application designed for team chat, which can be used with Ollama for LLM-powered communication.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_40

LANGUAGE: JavaScript
CODE:
```
https://github.com/swuecho/chat
```

--------------------------------

TITLE: Delete Ollama Model Request Example (Shell)
DESCRIPTION: Example `curl` command demonstrating how to send a DELETE request to the `/api/delete` endpoint to remove an Ollama model. The `model` parameter specifies the exact model name to be deleted.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_60

LANGUAGE: shell
CODE:
```
curl -X DELETE http://localhost:11434/api/delete -d '{  "model": "llama3:13b"}'
```

--------------------------------

TITLE: Running Ollama Benchmarks for a Specific Model
DESCRIPTION: This command demonstrates a common usage pattern for running the Ollama benchmark tests. It executes all benchmarks against the `llama3.3` model, providing a concrete example of how to specify the target model for performance evaluation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/benchmark.md#_snippet_1

LANGUAGE: bash
CODE:
```
go test -bench=. ./benchmark/... -m llama3.3
```

--------------------------------

TITLE: Web UIs and Interfaces for Ollama
DESCRIPTION: Web-based interfaces designed for interacting with Ollama models, offering chat functionalities, model control, and deployment options.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_58

LANGUAGE: JavaScript
CODE:
```
Ollama Chat WebUI for Docker: https://github.com/oslook/ollama-webui
Lightweight Ollama web UI with support for local Docker deployment
```

LANGUAGE: JavaScript
CODE:
```
MinimalNextOllamaChat: https://github.com/anilkay/MinimalNextOllamaChat
Minimal Web UI for Chat and Model Control using Next.js
```

LANGUAGE: JavaScript
CODE:
```
LocalLLM: https://github.com/qusaismael/localllm
Minimal Web-App to run Ollama models with a GUI
```

LANGUAGE: JavaScript
CODE:
```
Ollamazing: https://github.com/buiducnhat/ollamazing
Web extension to run Ollama models
```

LANGUAGE: JavaScript
CODE:
```
yla: https://github.com/danielekp/yla
Web interface to interact with customized models
```

LANGUAGE: JavaScript
CODE:
```
Flufy: https://github.com/Aharon-Bensadoun/Flufy
React, TypeScript, and Material-UI based chat interface for Ollama's API
```

LANGUAGE: JavaScript
CODE:
```
Lumina: https://github.com/cushydigit/lumina.git
Lightweight, minimal React.js frontend for interacting with Ollama servers
```

LANGUAGE: Python
CODE:
```
Tiny Notepad: https://pypi.org/project/tiny-notepad
Notepad-like interface to chat with Ollama, available on PyPI
```

--------------------------------

TITLE: Ollama Chat Request (Streaming with Tools)
DESCRIPTION: Example of a chat request with tool calling enabled. The request includes tool definitions, and the response may contain tool calls.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_24

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "what is the weather in tokyo?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather in a given city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city to get the weather for"
            }
          },
          "required": ["city"]
        }
      }
    }
  ],
  "stream": true
}'
```

--------------------------------

TITLE: Ollama HIP Backend Configuration
DESCRIPTION: Configures the HIP backend for Ollama, primarily for AMD GPUs. It sets the HIP platform, finds the hip package, filters AMDGPU_TARGETS based on OS and exclusions, and adds the ggml-hip subdirectory. It includes specific compile definitions for Windows and HIP, and handles installation of HIP targets and their runtime dependencies.

SOURCE: https://github.com/ollama/ollama/blob/main/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
set(WINDOWS_AMDGPU_TARGETS_EXCLUDE_REGEX "^gfx(906|908|90a|1200|1201):xnack[+-]$"
    CACHE STRING
    "Regular expression describing AMDGPU_TARGETS not supported on Windows. Override to force building these targets. Default \"^gfx(906|908|90a|1200|1201):xnack[+-]$\"."
)

check_language(HIP)
if(CMAKE_HIP_COMPILER)
    set(HIP_PLATFORM "amd")

    find_package(hip REQUIRED)
    if(NOT AMDGPU_TARGETS)
        list(FILTER AMDGPU_TARGETS INCLUDE REGEX "^gfx(900|94[012]|101[02]|1030|110[012]|120[01])")
    elseif(WIN32 AND WINDOWS_AMDGPU_TARGETS_EXCLUDE_REGEX)
        list(FILTER AMDGPU_TARGETS EXCLUDE REGEX ${WINDOWS_AMDGPU_TARGETS_EXCLUDE_REGEX})
    endif()

    if(AMDGPU_TARGETS)
        add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src/ggml-hip)

        if (WIN32)
            target_compile_definitions(ggml-hip PRIVATE GGML_CUDA_NO_PEER_COPY)
        endif()

        target_compile_definitions(ggml-hip PRIVATE GGML_HIP_NO_VMM)

        set(OLLAMA_HIP_INSTALL_DIR ${OLLAMA_INSTALL_DIR}/rocm)
        install(TARGETS ggml-hip
            RUNTIME_DEPENDENCY_SET rocm
            RUNTIME DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT HIP
            LIBRARY DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT HIP
        )
        install(RUNTIME_DEPENDENCY_SET rocm
                DIRECTORIES ${HIP_BIN_INSTALL_DIR} ${HIP_LIB_INSTALL_DIR}
                PRE_INCLUDE_REGEXES hipblas rocblas amdhip64 rocsolver amd_comgr hsa-runtime64 rocsparse tinfo rocprofiler-register drm drm_amdgpu numa elf
                PRE_EXCLUDE_REGEXES ".*"
                POST_EXCLUDE_REGEXES "system32"
            RUNTIME DESTINATION ${OLLAMA_HIP_INSTALL_DIR} COMPONENT HIP
            LIBRARY DESTINATION ${OLLAMA_HIP_INSTALL_DIR} COMPONENT HIP
        )

        foreach(HIP_LIB_BIN_INSTALL_DIR IN ITEMS ${HIP_BIN_INSTALL_DIR} ${HIP_LIB_INSTALL_DIR})
            if(EXISTS ${HIP_LIB_BIN_INSTALL_DIR}/rocblas)

```

--------------------------------

TITLE: OpenLIT Ollama Integration
DESCRIPTION: OpenLIT is an OpenTelemetry-native tool for monitoring Ollama applications and GPUs. It utilizes traces and metrics for comprehensive observability.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_131

LANGUAGE: APIDOC
CODE:
```
OpenLIT Integration:
  Purpose: Monitor Ollama Applications & GPUs.
  Technology: OpenTelemetry-native.
  Features: Traces and metrics for monitoring.
  Ollama Support: Native integration for Ollama.
  Repository: https://github.com/openlit/openlit
```

--------------------------------

TITLE: Casibase
DESCRIPTION: An open-source AI knowledge base and dialogue system that combines RAG, SSO, Ollama support, and multiple large language models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_28

LANGUAGE: Unknown
CODE:
```
casibase.org
```

--------------------------------

TITLE: FROM Instruction: Building Models
DESCRIPTION: Details the FROM instruction for specifying the base model, including building from existing Ollama models, Safetensors, or GGUF files.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_3

LANGUAGE: APIDOC
CODE:
```
FROM Instruction:
  Usage: FROM <model name>:<tag>

  Build from existing model:
    Example: FROM llama3.2
    Available models: https://github.com/ollama/ollama#model-library, https://ollama.com/library

  Build from a Safetensors model:
    Usage: FROM <model directory>
    Supported architectures: Llama (3, 3.1, 3.2), Mistral (1, 2, Mixtral), Gemma (1, 2), Phi3

  Build from a GGUF file:
    Usage: FROM ./ollama-model.gguf
    Path can be absolute or relative to the Modelfile.
```

--------------------------------

TITLE: Generate Completion Response Stream (Partial)
DESCRIPTION: Example of a partial JSON response received when streaming a text completion from the Ollama API.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_2

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-08-04T08:52:19.385406455-07:00",
  "response": "The",
  "done": false
}
```

--------------------------------

TITLE: Running Ollama Benchmarks with Model Placeholder
DESCRIPTION: This command executes all Go benchmark tests within the `./benchmark/...` directory for the Ollama server. It requires specifying a model name using the `-m` flag, which should be replaced with the actual model to be benchmarked.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/benchmark.md#_snippet_0

LANGUAGE: bash
CODE:
```
go test -bench=. ./benchmark/... -m $MODEL_NAME
```

--------------------------------

TITLE: Ollama Chat Request (No Streaming)
DESCRIPTION: Example of sending a chat message to the Ollama API with the response not being streamed.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_26

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": false
}'
```

--------------------------------

TITLE: Chat Completions with Aliased Model
DESCRIPTION: Example of using the chat completions endpoint with a model that has been aliased to `gpt-3.5-turbo`. This demonstrates compatibility with OpenAI-named models.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_19

LANGUAGE: json
CODE:
```
{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Hello!"
        }
    ]
}
```

--------------------------------

TITLE: R2R
DESCRIPTION: An open-source Retrieval-Augmented Generation (RAG) engine that can be used with Ollama for advanced document understanding and querying.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_50

LANGUAGE: Python
CODE:
```
https://github.com/SciPhi-AI/R2R
```

--------------------------------

TITLE: Ollama Completion API
DESCRIPTION: Demonstrates how to use the /completion endpoint to get text completions from a loaded model. It sends a JSON payload with a prompt to the server.

SOURCE: https://github.com/ollama/ollama/blob/main/runner/README.md#_snippet_1

LANGUAGE: shell
CODE:
```
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "hi"}' http://localhost:8080/completion
```

--------------------------------

TITLE: Basic Chat Response
DESCRIPTION: Example of a standard chat response from the Ollama API, including model details, message content, and performance metrics.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_27

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-12-12T14:13:43.416799Z",
  "message": {
    "role": "assistant",
    "content": "Hello! How are you today?"
  },
  "done": true,
  "total_duration": 5191566416,
  "load_duration": 2154458,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 383809000,
  "eval_count": 298,
  "eval_duration": 4799921000
}
```

--------------------------------

TITLE: Ollama API Generate Request (with suffix)
DESCRIPTION: Example of a request to the Ollama API's /api/generate endpoint, including a prompt, suffix for completion, and options for generation. This demonstrates how to use the API for code generation or text completion.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_6

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "codellama:code",
  "prompt": "def compute_gcd(a, b):",
  "suffix": "    return result",
  "options": {
    "temperature": 0
  },
  "stream": false
}'
```

--------------------------------

TITLE: Quantizing a Model during Creation
DESCRIPTION: This command demonstrates how to quantize a model during the creation process using the '--quantize' flag. It specifies the quantization method (e.g., 'q4_K_M') and shows the output of the quantization process.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_6

LANGUAGE: shell
CODE:
```
ollama create --quantize q4_K_M mymodel
transferring model data
quantizing F16 model to Q4_K_M
creating new layer sha256:735e246cc1abfd06e9cdcf95504d6789a6cd1ad7577108a70d9902fef503c1bd
creating new layer sha256:0853f0ad24e5865173bbf9ffcc7b0f5d56b66fd690ab1009867e45e7d2c4db0f
writing manifest
success
```

--------------------------------

TITLE: Listing Running Models (Request)
DESCRIPTION: This `curl` command sends a GET request to the `/api/ps` endpoint to retrieve a list of all models currently loaded and running in Ollama's memory.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_79

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/ps
```

--------------------------------

TITLE: Ollama CLI Commands for Model Management
DESCRIPTION: Demonstrates how to create an Ollama model from a Modelfile and how to view the Modelfile of an existing model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_1

LANGUAGE: shell
CODE:
```
ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>
ollama run choose-a-model-name
```

LANGUAGE: shell
CODE:
```
ollama show --modelfile llama3.2
```

--------------------------------

TITLE: Ollama Terminal Clients
DESCRIPTION: Various command-line interface (CLI) tools and clients for interacting with Ollama models directly from the terminal. These tools offer different features for model management, chat interfaces, and scriptable interactions.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_64

LANGUAGE: Shell
CODE:
```
# oterm: A terminal client for Ollama
# Example usage might involve commands like 'oterm chat --model llama2'
```

LANGUAGE: Shell
CODE:
```
# neollama: UI client for interacting with models from within Neovim
# Usage typically involves Neovim commands to interact with Ollama
```

LANGUAGE: Shell
CODE:
```
# shell-pilot: Interact with models via pure shell scripts on Linux or macOS
# Example: 'shell-pilot prompt "What is the capital of France?" --model mistral'
```

LANGUAGE: Shell
CODE:
```
# SwollamaCLI: Bundled with the Swollama Swift package
# CLI Usage: 'swollama --model llama3 "Hello, Ollama!"'
```

LANGUAGE: Shell
CODE:
```
# aichat: All-in-one LLM CLI tool with Ollama support
# Example: 'aichat --provider ollama --model llama2 "Write a poem."' 
```

LANGUAGE: Shell
CODE:
```
# PowershAI: PowerShell module for AI in the terminal, including Ollama
# Example: 'Invoke-OllamaChat -Model llama3 -Prompt "Explain quantum physics."' 
```

LANGUAGE: Shell
CODE:
```
# DeepShell: Self-hosted AI assistant with interactive shell and file analysis.
# Usage involves starting the DeepShell environment and interacting with AI features.
```

LANGUAGE: Shell
CODE:
```
# orca-cli: Ollama Registry CLI Application
# Commands: 'orca pull llama2', 'orca browse'
```

LANGUAGE: Shell
CODE:
```
# GGUF-to-Ollama: Importing GGUF to Ollama made easy
# Usage: 'gguf-to-ollama --file ./model.gguf --ollama-model-name my-gguf-model'
```

LANGUAGE: Shell
CODE:
```
# ollama-multirun: Bash script to run a prompt against multiple Ollama models
# Example: './ollama-multirun "What is AI?" --models llama2,mistral'
```

LANGUAGE: Shell
CODE:
```
# ollama-bash-toolshed: Bash scripts to chat with tools using models.
# Example: './ollama-bash-toolshed --tool calculator "What is 2+2?"'
```

--------------------------------

TITLE: CRAG Ollama Chat
DESCRIPTION: A simple web application for chat that incorporates web search with Corrective RAG using Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_37

LANGUAGE: Python
CODE:
```
https://github.com/Nagi-ovo/CRAG-Ollama-Chat
```

--------------------------------

TITLE: Basic Go Template Structure
DESCRIPTION: Demonstrates a simple Go template structure for iterating over messages, showing the role and content of each message. This is a fundamental example of how to format conversational data for LLMs.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_0

LANGUAGE: go
CODE:
```
{{- range .Messages }}
{{ .Role }}: {{ .Content }}
{{- end }}

```

--------------------------------

TITLE: Build Ollama Binary
DESCRIPTION: Builds the Ollama binary from the source code. This is a prerequisite for running the desktop application.

SOURCE: https://github.com/ollama/ollama/blob/main/macapp/README.md#_snippet_0

LANGUAGE: shell
CODE:
```
cd ..
go build .
```

--------------------------------

TITLE: Ollama RAG Chatbot
DESCRIPTION: A local chatbot that uses Ollama and RAG (Retrieval-Augmented Generation) to enable conversations with multiple PDFs.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_23

LANGUAGE: Python
CODE:
```
https://github.com/datvodinh/rag-chatbot.git
```

--------------------------------

TITLE: Chat Request with Conversation History
DESCRIPTION: An example of initiating a chat with the Ollama API that includes a conversation history. This allows for multi-turn conversations and context awareness.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_32

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    },
    {
      "role": "assistant",
      "content": "due to rayleigh scattering."
    },
    {
      "role": "user",
      "content": "how is that different than mie scattering?"
    }
  ]
}'
```

--------------------------------

TITLE: AI Desktop Applications
DESCRIPTION: Desktop applications providing a user interface for interacting with Ollama models. These applications are available for various operating systems and offer features like chat interfaces and model management.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_57

LANGUAGE: Go
CODE:
```
Witsy: https://github.com/nbonamy/witsy
Mac/Windows/Linux AI Desktop Application
```

LANGUAGE: Kotlin
CODE:
```
ChibiChat: https://github.com/CosmicEventHorizon/ChibiChat
Kotlin-based Android app for Ollama and Koboldcpp API endpoints
```

LANGUAGE: Rust
CODE:
```
GPTranslate: https://github.com/philberndt/GPTranslate
Rust and Tauri based AI-powered desktop translation application with Ollama support
```

LANGUAGE: Swift
CODE:
```
macLlama (macOS native): https://github.com/hellotunamayo/macLlama
Native macOS GUI application for interacting with Ollama models
```

LANGUAGE: Dart
CODE:
```
Ollamb: https://github.com/hengkysteen/ollamb
Cross-platform (Flutter) application for Ollama with a web demo available
```

--------------------------------

TITLE: Ollama Chat Response (Streaming)
DESCRIPTION: Example of a streaming JSON response from the Ollama chat API. This shows intermediate and final response formats.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_23

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-08-04T08:52:19.385406455-07:00",
  "message": {
    "role": "assistant",
    "content": "The",
    "images": null
  },
  "done": false
}

{
  "model": "llama3.2",
  "created_at": "2023-08-04T19:22:45.499127Z",
  "message": {
    "role": "assistant",
    "content": ""
  },
  "done": true,
  "total_duration": 4883583458,
  "load_duration": 1334875,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 342546000,
  "eval_count": 282,
  "eval_duration": 4535599000
}
```

--------------------------------

TITLE: OpenAI-Compatible TypeScript SDK
DESCRIPTION: Abso is an OpenAI-compatible SDK for TypeScript, allowing integration with any LLM provider. It simplifies making API calls to language models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_113

LANGUAGE: TypeScript
CODE:
```
import OpenAI from 'abso';

const openai = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'YOUR_BASE_URL'
});

async function main() {
  const chatCompletion = await openai.chat.completions.create({
    model: 'your-model',
    messages: [{role: 'user', content: 'Hello world!'}]
  });
  console.log(chatCompletion.choices[0].message.content);
}

main();
```

--------------------------------

TITLE: Retrieving Ollama Version (Request)
DESCRIPTION: This `curl` command sends a GET request to the `/api/version` endpoint to retrieve the current version of the Ollama server.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_85

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/version
```

--------------------------------

TITLE: Remove Ollama Binary (Shell)
DESCRIPTION: Removes the Ollama executable from the system's PATH. It finds the binary location using `which ollama`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_13

LANGUAGE: shell
CODE:
```
sudo rm $(which ollama)
```

--------------------------------

TITLE: RAG and Chatbot Frameworks with Ollama Support
DESCRIPTION: Frameworks and platforms that integrate Ollama for Retrieval-Augmented Generation (RAG) and building AI-powered chatbots, offering features like document storage and agent capabilities.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_59

LANGUAGE: Python
CODE:
```
Minima: https://github.com/dмайboroda/minima
RAG with on-premises or fully local workflow
```

LANGUAGE: Python
CODE:
```
Chipper: https://github.com/TilmanGriesel/chipper
AI interface for tinkerers with Ollama, Haystack RAG, and Python support
```

LANGUAGE: Python
CODE:
```
OpenDeepResearcher-via-searxng: https://github.com/benhaotang/OpenDeepResearcher-via-searxng
Deep Research equivalent endpoint with Ollama support for local running
```

LANGUAGE: Python
CODE:
```
AntSK: https://github.com/AIDotNet/AntSK
Out-of-the-box & Adaptable RAG Chatbot
```

LANGUAGE: Python
CODE:
```
MaxKB: https://github.com/1Panel-dev/MaxKB/
Ready-to-use & flexible RAG Chatbot
```

LANGUAGE: Python
CODE:
```
LangBot: https://github.com/RockChinQ/LangBot
LLM-based instant messaging bots platform with Agents, RAG features, and multi-platform support
```

LANGUAGE: Python
CODE:
```
AstrBot: https://github.com/Soulter/AstrBot/
User-friendly LLM-based multi-platform chatbot with WebUI, supporting RAG, LLM agents, and plugins
```

--------------------------------

TITLE: Ollama Chat Request (Streaming)
DESCRIPTION: Example of sending a chat message to the Ollama API with a streaming response. The response is a series of JSON objects.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_22

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ]
}'
```

--------------------------------

TITLE: Ollama API Generate Endpoint
DESCRIPTION: This is an example of how to use the Ollama API to generate text. It shows a `curl` request to the `/api/generate` endpoint, specifying the model, prompt, and context length option.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_4

LANGUAGE: APIDOC
CODE:
```
POST /api/generate

Request Body:
{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "options": {
    "num_ctx": 4096
  }
}

Description:
Generates text based on the provided model and prompt. The `options` object allows for model-specific configurations such as `num_ctx` to set the context window size.
```

--------------------------------

TITLE: Ollama CUDA Backend Configuration
DESCRIPTION: Configures the CUDA backend for Ollama. It checks for the CUDA compiler, sets CUDA architectures if not specified, finds the CUDAToolkit package, and adds the ggml-cuda subdirectory. It also handles installation of the CUDA targets, including runtime dependencies from the CUDAToolkit.

SOURCE: https://github.com/ollama/ollama/blob/main/CMakeLists.txt#_snippet_1

LANGUAGE: cmake
CODE:
```
check_language(CUDA)
if(CMAKE_CUDA_COMPILER)
    if(CMAKE_VERSION VERSION_GREATER_EQUAL "3.24" AND NOT CMAKE_CUDA_ARCHITECTURES)
        set(CMAKE_CUDA_ARCHITECTURES "native")
    endif()

    find_package(CUDAToolkit)
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src/ggml-cuda)
    install(TARGETS ggml-cuda
        RUNTIME_DEPENDENCIES
            DIRECTORIES ${CUDAToolkit_BIN_DIR} ${CUDAToolkit_LIBRARY_DIR}
            PRE_INCLUDE_REGEXES cublas cublasLt cudart
            PRE_EXCLUDE_REGEXES ".*"
        RUNTIME DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT CUDA
        LIBRARY DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT CUDA
    )
endif()
```

--------------------------------

TITLE: Ollama Embeddings Creation Example
DESCRIPTION: Demonstrates how to create embeddings for a list of input texts using the Ollama API. This is useful for natural language processing tasks like semantic search.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_11

LANGUAGE: javascript
CODE:
```
const embedding = await openai.embeddings.create({
  model: "all-minilm",
  input: ["why is the sky blue?", "why is the grass green?"]
})
```

--------------------------------

TITLE: Ollama Android Chat
DESCRIPTION: This project allows users to run the Ollama service directly on an Android device with a single click, eliminating the need for Termux. It provides a chat interface for interacting with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_117

LANGUAGE: Java
CODE:
```
// Example usage (conceptual):
// // In an Android Activity or Service:
// OllamaService ollamaService = new OllamaService(this);
// ollamaService.startOllama();
// ollamaService.sendMessage("ollama-android-chat", "Tell me a joke.");
```

--------------------------------

TITLE: Importing a Safetensors Adapter
DESCRIPTION: This snippet shows how to create a Modelfile to import a Safetensors adapter. It requires a FROM command pointing to the base model and an ADAPTER command pointing to the adapter directory. The 'ollama create' command is then used to build the model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_0

LANGUAGE: dockerfile
CODE:
```
FROM <base model name>
ADAPTER /path/to/safetensors/adapter/directory
```

--------------------------------

TITLE: Opik Ollama Integration
DESCRIPTION: Opik provides native integration for monitoring Ollama applications. It's an open-source platform for debugging, evaluating, and monitoring LLM applications, RAG systems, and agentic workflows.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_129

LANGUAGE: APIDOC
CODE:
```
Opik Integration:
  Purpose: Debug, evaluate, and monitor LLM applications, RAG systems, and agentic workflows.
  Features: Comprehensive tracing, automated evaluations, production-ready dashboards.
  Ollama Support: Native integration for Ollama applications.
  Documentation: https://www.comet.com/docs/opik/cookbook/ollama
```

--------------------------------

TITLE: Generate Completion Request (Streaming)
DESCRIPTION: Example of a curl request to the Ollama API to generate a text completion. The response is streamed as a series of JSON objects.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_1

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?"
}'
```

--------------------------------

TITLE: C++ Library for Ollama
DESCRIPTION: OllamaPlusPlus is a simple C++ library for interacting with Ollama. It provides basic functionalities to integrate Ollama's capabilities into C++ applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_115

LANGUAGE: C++
CODE:
```
// Example usage (conceptual):
// #include "ollama.hpp"
// 
// OllamaClient client("http://localhost:11434");
// std::string response = client.generate("llama2", "What is Ollama?");
// std::cout << response << std::endl;
```

--------------------------------

TITLE: Browser Extensions for Ollama Integration
DESCRIPTION: Browser extensions that integrate Ollama for tasks like writing assistance, grammar correction, translation, and general AI interaction within the browser.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_123

LANGUAGE: JavaScript
CODE:
```
https://github.com/n4ze3m/page-assist
https://docs.openinterpreter.com/language-model-setup/local-models/ollama
https://github.com/josStorer/chatGPTBox
https://github.com/ivostoykov/localAI
https://github.com/adarshM84/TextLLaMA
```

--------------------------------

TITLE: Multi-platform Ollama Client
DESCRIPTION: Ollama App is a modern and easy-to-use multi-platform client for Ollama. It provides a user-friendly interface for interacting with Ollama models on various operating systems.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_118

LANGUAGE: Dart
CODE:
```
// Example usage (conceptual):
// import 'package:ollama_app/ollama_client.dart';
// 
// final ollamaClient = OllamaClient(baseUrl: 'http://localhost:11434');
// 
// Future<void> generateResponse() async {
//   final response = await ollamaClient.generate(
//     model: 'llama3',
//     prompt: 'Explain Ollama.',
//   );
//   print(response.response);
// }
```

--------------------------------

TITLE: Ollama Version API Endpoint
DESCRIPTION: This snippet defines the HTTP method and path for retrieving the current Ollama server version. It accepts GET requests to `/api/version`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_84

LANGUAGE: text
CODE:
```
GET /api/version
```

--------------------------------

TITLE: Pull and Update Models
DESCRIPTION: Pulls a specified model from the Ollama registry. If the model already exists locally, this command updates it by pulling only the necessary differences.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_6

LANGUAGE: shell
CODE:
```
ollama pull llama3.2
```

--------------------------------

TITLE: Ollama Database Integrations
DESCRIPTION: Projects that integrate Ollama with databases, particularly for vector storage and retrieval using embeddings generated by Ollama models. This enables AI-powered querying and similarity search within databases.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_66

LANGUAGE: SQL
CODE:
```
-- pgai: PostgreSQL as a vector database
-- Example: CREATE VECTORIZER ollama_vectorizer LANGUAGE ollama;
-- Example: CREATE EXTENSION pgvector;
-- Example: SELECT ollama_vectorizer('What is AI?');
```

LANGUAGE: APIDOC
CODE:
```
MindsDB Handler for Ollama:
  Connects Ollama models with data platforms.
  Usage:
    CREATE DATABASE ollama_db WITH ENGINE = 'ollama', PARAMETERS = { 'host': 'localhost', 'port': 11434 };
    SELECT * FROM ollama_db.models WHERE name = 'llama2';
    SELECT generate_text('What is the weather like?', model='llama2') FROM dual;
```

LANGUAGE: Go
CODE:
```
// chromem-go: Go library for embedding and RAG with Ollama
// Example: Embeddings can be generated using Ollama's API and stored in a vector store.
// rag-wikipedia-ollama example demonstrates RAG pipeline.
```

--------------------------------

TITLE: Ollama API Generate Request (with images)
DESCRIPTION: Example of how to submit images to multimodal models like Llava using the Ollama API. Images should be provided as a list of base64-encoded strings in the 'images' field.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_12

LANGUAGE: shell
CODE:
```
To submit images to multimodal models such as `llava` or `bakllava`, provide a list of base64-encoded `images`:
```

--------------------------------

TITLE: Remove Ollama Data and User (Shell)
DESCRIPTION: Cleans up Ollama by removing its data directory, user, and group. This is part of a complete uninstallation process.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/linux.md#_snippet_14

LANGUAGE: shell
CODE:
```
sudo rm -r /usr/share/ollama
sudo userdel ollama
sudo groupdel ollama
```

--------------------------------

TITLE: List Running Models API Endpoint
DESCRIPTION: This snippet defines the HTTP method and path for the endpoint used to list models currently loaded into memory. It accepts GET requests to `/api/ps`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_78

LANGUAGE: text
CODE:
```
GET /api/ps
```

--------------------------------

TITLE: Generate Completion Request (No Streaming)
DESCRIPTION: Example of a curl request to the Ollama API to generate a text completion with streaming disabled, resulting in a single response.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_4

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

--------------------------------

TITLE: Generate Completion Response Stream (Final)
DESCRIPTION: Example of the final JSON response received when streaming a text completion from the Ollama API, including generation statistics.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_3

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-08-04T19:22:45.499127Z",
  "response": "",
  "done": true,
  "context": [
    1,
    2,
    3
  ],
  "total_duration": 10706818083,
  "load_duration": 6338219291,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 130079000,
  "eval_count": 259,
  "eval_duration": 4232710000
}
```

--------------------------------

TITLE: SYSTEM Instruction
DESCRIPTION: The SYSTEM instruction sets the system message for the model's template. It's used to guide the model's behavior or context.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_7

LANGUAGE: APIDOC
CODE:
```
SYSTEM """<system message>"""
  - Specifies the system message for the model's template.
```

--------------------------------

TITLE: Pushing and Running Models
DESCRIPTION: Commands to copy a model to a new name with a username prefix and then push it to ollama.com. It also shows how other users can run the shared model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_7

LANGUAGE: shell
CODE:
```
ollama cp mymodel myuser/mymodel
ollama push myuser/mymodel
```

LANGUAGE: shell
CODE:
```
ollama run myuser/mymodel
```

--------------------------------

TITLE: AI Experiments with Parameter Tweaking
DESCRIPTION: Reins is a tool that allows users to easily tweak parameters, customize system prompts per chat, and enhance AI experiments with reasoning model support. It focuses on improving the interaction with AI models.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_120

LANGUAGE: Python
CODE:
```
# Example usage (conceptual):
# from reins import ReinsClient
# 
# client = ReinsClient(ollama_url='http://localhost:11434')
# 
# response = client.chat(
#     model='llama3',
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Explain the concept of recursion."}
#     ],
#     temperature=0.7,
#     top_p=0.9
# )
# print(response['message']['content'])
```

--------------------------------

TITLE: Ollama API Generate Response (with suffix)
DESCRIPTION: Example response from the Ollama API when using a suffix in the generate request. This shows the completed code snippet generated by the model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_7

LANGUAGE: json5
CODE:
```
{
  "model": "codellama:code",
  "created_at": "2024-07-22T20:47:51.147561Z",
  "response": "\n  if a == 0:\n    return b\n  else:\n    return compute_gcd(b % a, a)\n\ndef compute_lcm(a, b):\n  result = (a * b) / compute_gcd(a, b)\n",
  "done": true,
  "done_reason": "stop",
  "context": [...],
  "total_duration": 1162761250,
  "load_duration": 6683708,
  "prompt_eval_count": 17,
  "prompt_eval_duration": 201222000,
  "eval_count": 63,
  "eval_duration": 953997000
}
```

--------------------------------

TITLE: Multimodal Chat Completion with Ollama
DESCRIPTION: This example demonstrates how to send a multimodal request (text and image) to the Ollama server using the OpenAI Python library. It includes encoding the image as a base64 data URL.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_2

LANGUAGE: python
CODE:
```
response = client.chat.completions.create(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": "data:image/png;base64,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
```

--------------------------------

TITLE: Ollama Model Parameters
DESCRIPTION: Defines the configurable parameters for Ollama models, including their purpose, default values, and example usage. These parameters control aspects like context window size, repetition penalties, temperature, and sampling strategies.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_5

LANGUAGE: APIDOC
CODE:
```
num_ctx:
  description: Sets the size of the context window used to generate the next token.
  defaultValue: 4096
  valueType: int
  example: num_ctx 4096

repeat_last_n:
  description: Sets how far back for the model to look back to prevent repetition.
  defaultValue: 64
  constraints: 0 = disabled, -1 = num_ctx
  valueType: int
  example: repeat_last_n 64

repeat_penalty:
  description: Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient.
  defaultValue: 1.1
  valueType: float
  example: repeat_penalty 1.1

temperature:
  description: The temperature of the model. Increasing the temperature will make the model answer more creatively.
  defaultValue: 0.8
  valueType: float
  example: temperature 0.7

seed:
  description: Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt.
  defaultValue: 0
  valueType: int
  example: seed 42

stop:
  description: Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Multiple stop patterns may be set by specifying multiple separate `stop` parameters in a modelfile.
  valueType: string
  example: stop "AI assistant:"

num_predict:
  description: Maximum number of tokens to predict when generating text.
  defaultValue: -1
  constraints: -1 = infinite generation
  valueType: int
  example: num_predict 42

top_k:
  description: Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative.
  defaultValue: 40
  valueType: int
  example: top_k 40

top_p:
  description: Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text.
  defaultValue: 0.9
  valueType: float
  example: top_p 0.9

min_p:
  description: Alternative to the top_p, and aims to ensure a balance of quality and variety. The parameter *p* represents the minimum probability for a token to be considered, relative to the probability of the most likely token. For example, with *p*=0.05 and the most likely token having a probability of 0.9, logits with a value less than 0.045 are filtered out.
  defaultValue: 0.0
  valueType: float
  example: min_p 0.05
```

--------------------------------

TITLE: GMAI - Gradle Managed AI
DESCRIPTION: GMAI is a Gradle plugin designed to automate the Ollama lifecycle management during build phases. It simplifies the process of integrating Ollama into your Gradle-based projects.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_128

LANGUAGE: gradle
CODE:
```
implementation("se.premex.gmai:gmai-plugin:1.0.0") // Example dependency, actual version may vary
```

--------------------------------

TITLE: Adding Templates via Modelfile
DESCRIPTION: Shows how to define a template within a Modelfile for a Llama 3 model. This example includes conditional rendering for a system prompt and iterates through messages, using specific tokens for role separation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_1

LANGUAGE: dockerfile
CODE:
```
FROM llama3.2

TEMPLATE """{{- if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>
{{- end }}
{{- range .Messages }}<|start_header_id|>{{ .Role }}<|end_header_id|>

{{ .Content }}<|eot_id|>
{{- end }}<|start_header_id|>assistant<|end_header_id|>

"""

```

--------------------------------

TITLE: Discord Bots with Ollama Integration
DESCRIPTION: Various Discord bots that leverage Ollama for AI chat, moderation, and personality creation. Some bots support multiple LLMs and integrations.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_121

LANGUAGE: Python
CODE:
```
https://github.com/mxyng/discollama
https://github.com/mekb-turtle/discord-ai-bot
https://github.com/ruecat/ollama-telegram
https://github.com/herval/cliobot
https://github.com/kevinthedang/discord-ollama
https://github.com/rapmd73/Companion
https://github.com/zyphixor/simple-discord-ai
https://github.com/jake83741/vnc-lm
```

--------------------------------

TITLE: Python Package for Custom Wikis
DESCRIPTION: Nichey is a Python package designed to generate custom wikis for research topics. It helps in organizing and presenting research information effectively.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_114

LANGUAGE: Python
CODE:
```
from nichey import generate_wiki

# Example usage:
# generate_wiki(topic='quantum_computing', output_dir='wiki_output')
```

--------------------------------

TITLE: Web Interfaces and Chat Clients
DESCRIPTION: This category includes web-based applications and chat interfaces that allow users to interact with Ollama. These often focus on ease of use, privacy, and specific chat functionalities.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_52

LANGUAGE: JavaScript
CODE:
```
Project: Sidellama
Description: browser-based LLM client
Link: https://github.com/gyopak/sidellama
```

LANGUAGE: JavaScript
CODE:
```
Project: ConfiChat
Description: Lightweight, standalone, multi-platform, and privacy-focused LLM chat interface with optional encryption
Link: https://github.com/1runeberg/confichat
```

LANGUAGE: JavaScript
CODE:
```
Project: LLMChat
Description: Privacy focused, 100% local, intuitive all-in-one chat interface
Link: https://github.com/trendy-design/llmchat
```

LANGUAGE: JavaScript
CODE:
```
Project: Local Multimodal AI Chat
Description: Ollama-based LLM Chat with support for multiple features, including PDF RAG, voice chat, image-based interactions, and integration with OpenAI.
Link: https://github.com/Leon-Sander/Local-Multimodal-AI-Chat
```

LANGUAGE: JavaScript
CODE:
```
Project: OrionChat
Description: OrionChat is a web interface for chatting with different AI providers
Link: https://github.com/EliasPereirah/OrionChat
```

LANGUAGE: JavaScript
CODE:
```
Project: Web management
Description: Web management page
Link: https://github.com/lemonit-eric-mao/ollama-web-management
```

LANGUAGE: React Native
CODE:
```
Project: chat-ollama
Description: a React Native client for Ollama
Link: https://github.com/annilq/chat-ollama
```

LANGUAGE: Flutter
CODE:
```
Project: ollama-chat-app
Description: Flutter-based chat app
Link: https://github.com/anan1213095357/ollama-chat-app
```

--------------------------------

TITLE: Preload Model with Ollama API (Chat Endpoint)
DESCRIPTION: Illustrates preloading a model using the `/api/chat` endpoint. Similar to the generate endpoint, this primes the model for faster interactions.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_12

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{"model": "mistral"}'
```

--------------------------------

TITLE: Ollama Client Initialization and Basic Operations
DESCRIPTION: Initializes the Ollama client and demonstrates basic operations such as creating chat completions, listing available models, retrieving a specific model, and generating embeddings. Requires the Ollama server to be running.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_3

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

completion = client.chat.completions.create(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": "Why is the sky blue?",
        }
    ],
    max_tokens=300,
)

completion = client.completions.create(
    model="llama3.2",
    prompt="Say this is a test",
)

list_completion = client.models.list()

model = client.models.retrieve("llama3.2")

embeddings = client.embeddings.create(
    model="all-minilm",
    input=["why is the sky blue?", "why is the grass green?"],
)
```

--------------------------------

TITLE: TagSpaces AI Integration
DESCRIPTION: TagSpaces is a platform for file-based applications that utilizes Ollama for generating tags and descriptions for files. This integration enhances file management and organization.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_21

LANGUAGE: JavaScript
CODE:
```
https://www.tagspaces.org
https://docs.tagspaces.org/ai/
```

--------------------------------

TITLE: Langfuse Ollama Integration
DESCRIPTION: Langfuse is an open-source LLM observability platform that supports Ollama. It enables teams to collaboratively monitor, evaluate, and debug AI applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_133

LANGUAGE: APIDOC
CODE:
```
Langfuse Integration:
  Purpose: Collaborative monitoring, evaluation, and debugging of AI applications.
  Features: Open-source LLM observability platform.
  Ollama Support: Integration available for Ollama.
  Documentation: https://langfuse.com/docs/integrations/ollama
```

--------------------------------

TITLE: Specialized and Experimental Projects
DESCRIPTION: This category includes projects with unique functionalities, experimental approaches, or specific use cases, such as multimodal AI, AI-to-AI communication, and advanced research tools.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_55

LANGUAGE: Python
CODE:
```
Project: AI Studio
Description: AI Studio
Link: https://github.com/MindWorkAI/AI-Studio
```

LANGUAGE: Python
CODE:
```
Project: AutoGPT Ollama integration
Description: AutoGPT Ollama integration
Link: https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/content/platform/ollama.md
```

LANGUAGE: Python
CODE:
```
Project: PartCAD
Description: CAD model generation with OpenSCAD and CadQuery
Link: https://github.com/openvmp/partcad/
```

LANGUAGE: Python
CODE:
```
Project: DualMind
Description: Experimental app allowing two models to talk to each other in the terminal or in a web interface
Link: https://github.com/tcsenpai/dualmind
```

LANGUAGE: Python
CODE:
```
Project: ollamarama-matrix
Description: Ollama chatbot for the Matrix chat protocol
Link: https://github.com/h1ddenpr0cess20/ollamarama-matrix
```

LANGUAGE: Python
CODE:
```
Project: G1
Description: Prototype of using prompting strategies to improve the LLM's reasoning through o1-like reasoning chains.
Link: https://github.com/bklieger-groq/g1
```

LANGUAGE: Python
CODE:
```
Project: Reddit Rate
Description: Search and Rate Reddit topics with a weighted summation
Link: https://github.com/rapidarchitect/reddit_analyzer
```

LANGUAGE: Python
CODE:
```
Project: VT
Description: A minimal multimodal AI chat app, with dynamic conversation routing. Supports local models via Ollama
Link: https://github.com/vinhnx/vt.ai
```

--------------------------------

TITLE: HoneyHive Ollama Integration
DESCRIPTION: HoneyHive integrates with Ollama to provide an AI observability and evaluation platform for AI agents. It helps evaluate agent performance, diagnose failures, and monitor quality in production.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_132

LANGUAGE: APIDOC
CODE:
```
HoneyHive Integration:
  Purpose: AI observability and evaluation platform for AI agents.
  Features: Evaluate agent performance, interrogate failures, monitor production quality.
  Ollama Support: Integration available for Ollama.
  Documentation: https://docs.honeyhive.ai/integrations/ollama
```

--------------------------------

TITLE: Create Chat Completion with Text Input
DESCRIPTION: Makes a chat completion request to the Ollama API using the initialized OpenAI client. This example sends a simple text message and specifies the model to use.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_6

LANGUAGE: javascript
CODE:
```
const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'llama3.2',
})
```

--------------------------------

TITLE: Ollama API Generate Request (Structured outputs)
DESCRIPTION: Example request to the Ollama API specifying a structured output format using the 'format' parameter with defined properties and types. This enables the model to return data in a predictable JSON structure.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_8

LANGUAGE: shell
CODE:
```
curl -X POST http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{
  "model": "llama3.1:8b",
  "prompt": "Ollama is 22 years old and is busy saving the world. Respond using JSON",
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "age": {
        "type": "integer"
      },
      "available": {
        "type": "boolean"
      }
    },
    "required": [
      "age",
      "available"
    ]
  }
}'
```

--------------------------------

TITLE: MLflow Tracing Ollama Integration
DESCRIPTION: MLflow Tracing is an open-source tool for LLM observability that supports Ollama. It offers a convenient API for logging and visualizing traces to simplify debugging and evaluation of GenAI applications.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_134

LANGUAGE: APIDOC
CODE:
```
MLflow Tracing Integration:
  Purpose: LLM observability tool for logging and visualizing traces.
  Features: Convenient API for debugging and evaluating GenAI applications.
  Ollama Support: Supports automatic tracing for Ollama applications.
  Documentation: https://mlflow.org/docs/latest/llms/tracing/index.html#automatic-tracing
```

--------------------------------

TITLE: Codestral Fill-in-Middle Template
DESCRIPTION: This Go template shows the configuration for Codestral models to support fill-in-middle. It utilizes `[SUFFIX]`, `[PREFIX]`, and the prompt to guide the model in generating text in the middle of the input.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_5

LANGUAGE: go
CODE:
```
[SUFFIX]{{ .Suffix }}[PREFIX] {{ .Prompt }}
```

--------------------------------

TITLE: Lunary Ollama Integration
DESCRIPTION: Lunary offers integration with Ollama, providing an open-source LLM observability platform. Key features include real-time analytics, prompt template management, PII masking, and comprehensive agent tracing.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_130

LANGUAGE: APIDOC
CODE:
```
Lunary Integration:
  Purpose: LLM observability platform.
  Features: Real-time analytics, prompt templates management, PII masking, comprehensive agent tracing.
  Ollama Support: Leading open-source integration for Ollama.
  Documentation: https://lunary.ai/docs/integrations/ollama
```

--------------------------------

TITLE: Ollama API Generate Response (Structured outputs)
DESCRIPTION: Example response from the Ollama API when requesting structured output. The 'response' field contains a JSON object adhering to the schema defined in the request.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_9

LANGUAGE: json
CODE:
```
{
  "model": "llama3.1:8b",
  "created_at": "2024-12-06T00:48:09.983619Z",
  "response": "{\n  \"age\": 22,\n  \"available\": true\n}",
  "done": true,
  "done_reason": "stop",
  "context": [1, 2, 3],
  "total_duration": 1075509083,
  "load_duration": 567678166,
  "prompt_eval_count": 28,
  "prompt_eval_duration": 236000000,
  "eval_count": 16,
  "eval_duration": 269000000
}
```

--------------------------------

TITLE: Cross-Platform AI Chat App
DESCRIPTION: SwiftChat is a lightning-fast, cross-platform AI chat application built with native UI for Android, iOS, and iPad. It leverages AI models for conversational experiences.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_116

LANGUAGE: Swift
CODE:
```
// Example usage (conceptual):
// import SwiftChat
// 
// let chatView = ChatView()
// chatView.viewModel.sendMessage("Hello, AI!")
```

--------------------------------

TITLE: Architecture-Specific and POSIX Conformance Settings
DESCRIPTION: Sets architecture-specific flags, handles static linking, profiling with gprof, and configures POSIX conformance levels for different operating systems (Linux, OpenBSD, Windows). It also defines Windows version for PrefetchVirtualMemory.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
# architecture specific
# TODO: probably these flags need to be tweaked on some architectures
#       feel free to update the Makefile for your architecture and send a pull request or issue
message(STATUS "CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")
if (MSVC)
    string(TOLOWER "${CMAKE_GENERATOR_PLATFORM}" CMAKE_GENERATOR_PLATFORM_LWR)
    message(STATUS "CMAKE_GENERATOR_PLATFORM: ${CMAKE_GENERATOR_PLATFORM}")
else ()
    set(CMAKE_GENERATOR_PLATFORM_LWR "")
endif ()

if (NOT MSVC)
    if (GGML_STATIC)
        add_link_options(-static)
        if (MINGW)
            add_link_options(-static-libgcc -static-libstdc++)
        endif()
    endif()
    if (GGML_GPROF)
        add_compile_options(-pg)
    endif()
endif()

if (MINGW)
    # Target Windows 8 for PrefetchVirtualMemory
    add_compile_definitions(_WIN32_WINNT=${GGML_WIN_VER})
endif()

#
# POSIX conformance
#

# clock_gettime came in POSIX.1b (1993)
# CLOCK_MONOTONIC came in POSIX.1-2001 / SUSv3 as optional
# posix_memalign came in POSIX.1-2001 / SUSv3
# M_PI is an XSI extension since POSIX.1-2001 / SUSv3, came in XPG1 (1985)

# Somehow in OpenBSD whenever POSIX conformance is specified
# some string functions rely on locale_t availability,
# which was introduced in POSIX.1-2008, forcing us to go higher
if (CMAKE_SYSTEM_NAME MATCHES "OpenBSD")
    add_compile_definitions(_XOPEN_SOURCE=700)
else()
    add_compile_definitions(_XOPEN_SOURCE=600)
endif()

# Data types, macros and functions related to controlling CPU affinity and

```

--------------------------------

TITLE: MESSAGE Instruction
DESCRIPTION: The MESSAGE instruction sets up a message history for the model. Multiple MESSAGE instructions can build a conversation to guide the model's responses. Valid roles include 'system', 'user', and 'assistant'.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_10

LANGUAGE: APIDOC
CODE:
```
MESSAGE <role> <message>
  - Sets a message in the conversation history.
  - Valid roles: system, user, assistant.

Example conversation:
MESSAGE user Is Toronto in Canada?
MESSAGE assistant yes
MESSAGE user Is Sacramento in Canada?
MESSAGE assistant no
MESSAGE user Is Ontario in Canada?
MESSAGE assistant yes
```

--------------------------------

TITLE: Ollama API Generate Response (JSON mode)
DESCRIPTION: Example response from the Ollama API when JSON mode is enabled. The 'response' field contains a JSON string, which should be parsed to access the structured data.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_11

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-11-09T21:07:55.186497Z",
  "response": "{\n\"morning\": {\n\"color\": \"blue\"\n},\n\"noon\": {\n\"color\": \"blue-gray\"\n},\n\"afternoon\": {\n\"color\": \"warm gray\"\n},\n\"evening\": {\n\"color\": \"orange\"\n}\n}
",
  "done": true,
  "context": [1, 2, 3],
  "total_duration": 4648158584,
  "load_duration": 4071084,
  "prompt_eval_count": 36,
  "prompt_eval_duration": 439038000,
  "eval_count": 180,
  "eval_duration": 4196918000
}
```

--------------------------------

TITLE: Ollama API Generate Response (Stream False)
DESCRIPTION: Example of a non-streaming response from the Ollama API's /api/generate endpoint. It includes model details, timestamps, generated text, and performance metrics.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_5

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-08-04T19:22:45.499127Z",
  "response": "The sky is blue because it is the color of the sky.",
  "done": true,
  "context": [1, 2, 3],
  "total_duration": 5043500667,
  "load_duration": 5025959,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 325953000,
  "eval_count": 290,
  "eval_duration": 4709213000
}
```

--------------------------------

TITLE: Ollama API Generate Request (JSON mode)
DESCRIPTION: Example request to the Ollama API using 'format: "json"' to ensure the model responds with a valid JSON object. It's recommended to also instruct the model within the prompt to respond in JSON.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_10

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'
```

--------------------------------

TITLE: Lightweight LLM Chat Interface
DESCRIPTION: ConfiChat is a lightweight, standalone, multi-platform, and privacy-focused LLM chat interface. It offers optional encryption for enhanced security and allows for easy customization of parameters and system prompts.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_119

LANGUAGE: JavaScript
CODE:
```
// Example usage (conceptual):
// import ConfiChat from 'confichat';
// 
// const chat = new ConfiChat({
//   model: 'mistral',
//   systemPrompt: 'You are a helpful assistant.'
// });
// 
// chat.sendMessage('What is the weather today?').then(response => {
//   console.log(response);
// });
```

--------------------------------

TITLE: Ollama Uninstall Commands
DESCRIPTION: Provides the necessary shell commands to completely remove Ollama from a macOS system. This includes deleting the application bundle, CLI link, user data, and cache files.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/macos.md#_snippet_0

LANGUAGE: shell
CODE:
```
sudo rm -rf /Applications/Ollama.app
sudo rm /usr/local/bin/ollama
rm -rf "~/Library/Application Support/Ollama"
rm -rf "~/Library/Saved Application State/com.electron.ollama.savedState"
rm -rf ~/Library/Caches/com.electron.ollama/
rm -rf ~/Library/Caches/ollama
rm -rf ~/Library/WebKit/com.electron.ollama
rm -rf ~/.ollama
```

--------------------------------

TITLE: KleidiAI Integration for Optimized Kernels
DESCRIPTION: Integrates the KleidiAI library to leverage optimized kernels for ARM architectures. This includes fetching the library, setting up include directories, and conditionally compiling specific kernel implementations based on detected CPU features like dotprod, i8mm, and sme.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_10

LANGUAGE: cmake
CODE:
```
if (GGML_CPU_AARCH64)
    target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_CPU_AARCH64)
endif()

if (GGML_CPU_KLEIDIAI)
    message(STATUS "Using KleidiAI optimized kernels if applicable")

    # Disable the KleidiAI tests
    set(KLEIDIAI_BUILD_TESTS  OFF)

    # Fetch KleidiAI sources:
    include(FetchContent)
    set(KLEIDIAI_COMMIT_TAG "v1.5.0")
    set(KLEIDIAI_DOWNLOAD_URL "https://github.com/ARM-software/kleidiai/archive/refs/tags/${KLEIDIAI_COMMIT_TAG}.tar.gz")
    set(KLEIDIAI_ARCHIVE_MD5  "ea22e1aefb800e9bc8c74d91633cc58e")

    if (POLICY CMP0135)
        cmake_policy(SET CMP0135 NEW)
    endif()

    FetchContent_Declare(KleidiAI_Download
        URL ${KLEIDIAI_DOWNLOAD_URL}
        DOWNLOAD_EXTRACT_TIMESTAMP NEW
        URL_HASH MD5=${KLEIDIAI_ARCHIVE_MD5})

    FetchContent_MakeAvailable(KleidiAI_Download)
    FetchContent_GetProperties(KleidiAI_Download
        SOURCE_DIR  KLEIDIAI_SRC
        POPULATED   KLEIDIAI_POPULATED)

    if (NOT KLEIDIAI_POPULATED)
        message(FATAL_ERROR "KleidiAI source downloaded failed.")
    endif()

    add_compile_definitions(GGML_USE_CPU_KLEIDIAI)

    # Remove kleidiai target after fetching it
    if (TARGET kleidiai)
        set_target_properties(kleidiai PROPERTIES EXCLUDE_FROM_ALL TRUE)
    endif()

    list(APPEND GGML_CPU_SOURCES
        ggml-cpu/kleidiai/kleidiai.cpp
        ggml-cpu/kleidiai/kernels.cpp
        ggml-cpu/kleidiai/kleidiai.h
        ggml-cpu/kleidiai/kernels.h
        )

    # KleidiAI
    include_directories(
        ${KLEIDIAI_SRC}/
        ${KLEIDIAI_SRC}/kai/
        ${KLEIDIAI_SRC}/kai/ukernels/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_fp32_bf16p_bf16p/
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/)

    set(ARCH_FLAGS_TEMP "${ARCH_FLAGS}")
    if (NOT ARCH_FLAGS_TEMP)
        string(REGEX MATCH "-march=[^ ]+" ARCH_FLAGS_TEMP "${CMAKE_C_FLAGS}")
    endif()
    string(FIND "${ARCH_FLAGS_TEMP}" "+dotprod" DOTPROD_ENABLED)
    string(FIND "${ARCH_FLAGS_TEMP}" "+i8mm" I8MM_ENABLED)
    string(FIND "${ARCH_FLAGS_TEMP}" "+sme" SME_ENABLED)

    set(PRIVATE_ARCH_FLAGS ${ARCH_FLAGS_TEMP})

    list(APPEND GGML_KLEIDIAI_SOURCES
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_lhs_quant_pack_qsi8d32p_f32.c
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_rhs_pack_nxk_qsi4c32ps1s0scalef16_qsu4c32s16s0_neon.c
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_lhs_quant_pack_qsi8d32p_f32_neon.c
        ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_rhs_pack_nxk_qsi4c32pscalef16_qsu4c32s16s0.c)

    if (NOT DOTPROD_ENABLED MATCHES -1)
        list(APPEND GGML_KLEIDIAI_SOURCES
            ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x8_qsi4c32p4x8_1x4x32_neon_dotprod.c
            ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x4_qsi4c32p4x4_1x4_neon_dotprod.c
            ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p4x4_qsi4c32p4x4_16x4_neon_dotprod.c)
    endif()

    if (NOT I8MM_ENABLED MATCHES -1)
        list(APPEND GGML_KLEIDIAI_SOURCES ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p4x8_qsi4c32p4x8_16x4_neon_i8mm.c)
    endif()
endif()
```

--------------------------------

TITLE: Ollama CLI: Running a Model with Turbo
DESCRIPTION: This snippet demonstrates how to run an Ollama model using the command-line interface, setting the OLLAMA_HOST environment variable to enable Turbo mode.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/turbo.md#_snippet_0

LANGUAGE: shell
CODE:
```
OLLAMA_HOST=ollama.com ollama run gpt-oss:120b
```

--------------------------------

TITLE: Ollama Prompt Template Syntax
DESCRIPTION: Details the structure and variables used in Ollama's prompt templates, which leverage Go's template syntax for dynamic prompt generation. This includes system messages, user prompts, and response handling.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_6

LANGUAGE: APIDOC
CODE:
```
TEMPLATE:
  description: The full prompt template to be passed into the model. It may include (optionally) a system message, a user's message and the response from the model. Note: syntax may be model specific. Templates use Go [template syntax](https://pkg.go.dev/text/template).

  variables:
    - name: {{ .System }}
      description: The system message used to specify custom behavior.
    - name: {{ .Prompt }}
      description: The user prompt message.
    - name: {{ .Response }}
      description: The response from the model. When generating a response, text after this variable is omitted.

  example:
    code: |
      TEMPLATE "{{ if .System }}<|im_start|>system
      {{ .System }}<|im_end|>
      {{ end }}{{ if .Prompt }}<|im_start|>user
      {{ .Prompt }}<|im_end|>
      {{ end }}<|im_start|>assistant
      "

```

--------------------------------

TITLE: Preload Model with Ollama API (Generate Endpoint)
DESCRIPTION: Demonstrates how to preload a model using the `/api/generate` endpoint by sending an empty request. This helps in reducing response times for subsequent requests.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_11

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{"model": "mistral"}'
```

--------------------------------

TITLE: Ollama REST API: Generate Response
DESCRIPTION: Generates a response from a model using the Ollama REST API. Requires a POST request to the `/api/generate` endpoint with a JSON payload specifying the model and prompt.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_18

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{ "model": "llama3.2", "prompt":"Why is the sky blue?" }'
```

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}
```

--------------------------------

TITLE: Ollama REST API: Chat with Model
DESCRIPTION: Enables a chat interaction with a model via the Ollama REST API. Uses a POST request to the `/api/chat` endpoint with a JSON payload including the model and a list of messages with roles and content.

SOURCE: https://github.com/ollama/ollama/blob/main/README.md#_snippet_19

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{ "model": "llama3.2", "messages": [ { "role": "user", "content": "why is the sky blue?" } ] }'
```

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}
```

--------------------------------

TITLE: Initialize OpenAI Client for Ollama
DESCRIPTION: Sets up the OpenAI JavaScript client to communicate with a local Ollama instance. It configures the base URL to point to the Ollama API and provides a placeholder API key.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_5

LANGUAGE: javascript
CODE:
```
import OpenAI from 'openai'

const openai = new OpenAI({
  baseURL: 'http://localhost:11434/v1/',

  // required but ignored
  apiKey: 'ollama',
})
```

--------------------------------

TITLE: Ollama Model Management API
DESCRIPTION: This section details the Ollama API endpoints for managing models. It covers operations such as copying models to a new name, deleting models, pulling models from the Ollama library, and pushing models to a library. Each endpoint includes its HTTP method, path, required parameters, optional parameters, and example requests and responses.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_49

LANGUAGE: APIDOC
CODE:
```
Copy a Model:
  POST /api/copy
  Copies a model to a new name from an existing model.
  Parameters:
    source: The name of the existing model.
    destination: The name for the new model.
  Examples:
    Request:
      curl http://localhost:11434/api/copy -d '{
        "source": "llama3.2",
        "destination": "llama3-backup"
      }'
    Response:
      Returns a 200 OK if successful, or a 404 Not Found if the source model doesn't exist.

Delete a Model:
  DELETE /api/delete
  Deletes a model and its associated data.
  Parameters:
    model: The name of the model to delete.
  Examples:
    Request:
      curl -X DELETE http://localhost:11434/api/delete -d '{
        "model": "llama3:13b"
      }'
    Response:
      Returns a 200 OK if successful, 404 Not Found if the model to be deleted doesn't exist.

Pull a Model:
  POST /api/pull
  Downloads a model from the Ollama library. Cancelled pulls are resumed, and multiple calls share download progress.
  Parameters:
    model: The name of the model to pull.
    insecure: (optional) Allows insecure connections to the library. Use only for development.
    stream: (optional) If false, the response is a single object; otherwise, it's a stream of objects.
  Examples:
    Request:
      curl http://localhost:11434/api/pull -d '{
        "model": "llama3.2"
      }'
    Response (stream=true):
      Manifest:
        {
          "status": "pulling manifest"
        }
      Downloading:
        {
          "status": "pulling digestname",
          "digest": "digestname",
          "total": 2142590208,
          "completed": 241970
        }
      Completion:
        {
          "status": "verifying sha256 digest"
        }
        {
          "status": "writing manifest"
        }
        {
          "status": "removing any unused layers"
        }
        {
          "status": "success"
        }
    Response (stream=false):
      {
        "status": "success"
      }

Push a Model:
  POST /api/push
  Uploads a model to a model library. Requires registration and a public key.
  Parameters:
    model: The name of the model to push (e.g., <namespace>/<model>:<tag>).
    insecure: (optional) Allows insecure connections to the library. Use only for development.
    stream: (optional) If false, the response is a single object; otherwise, it's a stream of objects.
  Examples:
    (No specific examples provided in the source text for push request body)
```

--------------------------------

TITLE: Granting Container Access to AMD GPU Devices
DESCRIPTION: When running Ollama in a container on Linux, you may need to explicitly grant access to GPU devices by adding the numeric group IDs found on the host system. This example assumes group ID 44 was identified for `/dev/dri/card0`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_8

LANGUAGE: bash
CODE:
```
docker run --group-add 44 ollama/ollama
```

--------------------------------

TITLE: CPU Backend Configuration with SME Extensions
DESCRIPTION: Configures the CPU backend, conditionally adding source files and compiler flags for SME (Scalable Matrix Extension) support. It sets up architecture-specific flags and definitions for the CPU backend target.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_11

LANGUAGE: cmake
CODE:
```
if (NOT SME_ENABLED MATCHES -1)
            list(APPEND GGML_KLEIDIAI_SOURCES
                ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1vlx4_qsi4c32p4vlx4_1vlx4vl_sme2_mopa.c
                ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_f32_qsi8d32p_qsi4c32p/kai_matmul_clamp_f32_qsi8d32p1x4_qsi4c32p4vlx4_1x4vl_sme2_sdot.c
                ${KLEIDIAI_SRC}/kai/ukernels/matmul/matmul_clamp_fp32_bf16p_bf16p/kai_matmul_clamp_f32_bf16p2vlx2_bf16p2vlx2_2vlx2vl_sme2_mopa.c
                ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_lhs_pack_bf16p2vlx2_f32_sme.c
                ${KLEIDIAI_SRC}/kai/ukernels/matmul/pack/kai_rhs_pack_kxn_bf16p2vlx2b_f32_x32_sme.c)
            set(PRIVATE_ARCH_FLAGS "-fno-tree-vectorize;${PRIVATE_ARCH_FLAGS}+sve+sve2")
        endif()

        set_source_files_properties(${GGML_KLEIDIAI_SOURCES} PROPERTIES COMPILE_OPTIONS "${PRIVATE_ARCH_FLAGS}")
        list(APPEND GGML_CPU_SOURCES ${GGML_KLEIDIAI_SOURCES})
    endif()

    message(STATUS "Adding CPU backend variant ${GGML_CPU_NAME}: ${ARCH_FLAGS} ${ARCH_DEFINITIONS}")
    target_sources(${GGML_CPU_NAME} PRIVATE ${GGML_CPU_SOURCES})
    target_compile_options(${GGML_CPU_NAME} PRIVATE ${ARCH_FLAGS})
    target_compile_definitions(${GGML_CPU_NAME} PRIVATE ${ARCH_DEFINITIONS})
```

--------------------------------

TITLE: Importing a Model from Safetensors Weights
DESCRIPTION: This snippet demonstrates creating a Modelfile to import a model directly from Safetensors weights. The FROM command should point to the directory containing the Safetensors weights. If the Modelfile is in the same directory, 'FROM .' can be used.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_3

LANGUAGE: dockerfile
CODE:
```
FROM /path/to/safetensors/directory
```

--------------------------------

TITLE: CMake Configuration for Ollama Metal Backend
DESCRIPTION: This snippet demonstrates how to configure the Metal backend for Ollama using CMake. It includes finding required frameworks (Foundation, Metal, MetalKit), adding the Metal backend library, linking these frameworks to the target library, and conditionally defining preprocessor macros based on build flags like GGML_METAL_NDEBUG and GGML_METAL_USE_BF16.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-metal/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
find_library(FOUNDATION_LIBRARY Foundation REQUIRED)
find_library(METAL_FRAMEWORK    Metal      REQUIRED)
find_library(METALKIT_FRAMEWORK MetalKit   REQUIRED)

message(STATUS "Metal framework found")

ggml_add_backend_library(ggml-metal
                         ggml-metal.m
                        )

target_link_libraries(ggml-metal PRIVATE
                      ${FOUNDATION_LIBRARY}
                      ${METAL_FRAMEWORK}
                      ${METALKIT_FRAMEWORK}
                      )

if (GGML_METAL_NDEBUG)
    add_compile_definitions(GGML_METAL_NDEBUG)
endif()

if (GGML_METAL_USE_BF16)
    add_compile_definitions(GGML_METAL_USE_BF16)
endif()
```

--------------------------------

TITLE: Basic Chat Completion with Ollama
DESCRIPTION: This snippet shows how to initialize the OpenAI client to point to an Ollama server and perform a basic chat completion request. It highlights the configuration for `base_url` and `api_key`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_1

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'user',
            'content': 'Say this is a test',
        }
    ],
    model='llama3.2',
)

print(chat_completion)
```

--------------------------------

TITLE: HIP Backend Library Creation
DESCRIPTION: Creates a CMake library target for the HIP backend, including the collected source and header files.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_7

LANGUAGE: cmake
CODE:
```
ggml_add_backend_library(ggml-hip
                         ${GGML_HEADERS_ROCM}
                         ${GGML_SOURCES_ROCM}
                        )
```

--------------------------------

TITLE: HIP Backend Library Linking
DESCRIPTION: Links the HIP backend library with necessary HIP and ROCm libraries.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_11

LANGUAGE: cmake
CODE:
```
target_link_libraries(ggml-hip PRIVATE ggml-base hip::host roc::rocblas roc::hipblas)
```

--------------------------------

TITLE: GGML CPU Backend Configuration
DESCRIPTION: Configures the GGML CPU backend library, setting its name, source files, compile features, and include directories. It also handles conditional compilation flags based on project settings.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
function(ggml_add_cpu_backend_variant_impl tag_name)
    if (tag_name)
        set(GGML_CPU_NAME ggml-cpu-${tag_name})
    else()
        set(GGML_CPU_NAME ggml-cpu)
    endif()

    ggml_add_backend_library(${GGML_CPU_NAME})

    list (APPEND GGML_CPU_SOURCES
        ggml-cpu/ggml-cpu.c
        ggml-cpu/ggml-cpu.cpp
        ggml-cpu/ggml-cpu-aarch64.cpp
        ggml-cpu/ggml-cpu-aarch64.h
        ggml-cpu/ggml-cpu-hbm.cpp
        ggml-cpu/ggml-cpu-hbm.h
        ggml-cpu/ggml-cpu-quants.c
        ggml-cpu/ggml-cpu-quants.h
        ggml-cpu/ggml-cpu-traits.cpp
        ggml-cpu/ggml-cpu-traits.h
        ggml-cpu/amx/amx.cpp
        ggml-cpu/amx/amx.h
        ggml-cpu/amx/mmq.cpp
        ggml-cpu/amx/mmq.h
        ggml-cpu/ggml-cpu-impl.h
        ggml-cpu/common.h
        ggml-cpu/binary-ops.h
        ggml-cpu/binary-ops.cpp
        ggml-cpu/unary-ops.h
        ggml-cpu/unary-ops.cpp
        ggml-cpu/simd-mappings.h
        ggml-cpu/vec.h
        ggml-cpu/vec.cpp
        ggml-cpu/ops.h
        ggml-cpu/ops.cpp
        )

    target_compile_features(${GGML_CPU_NAME} PRIVATE c_std_11 cxx_std_17)
    target_include_directories(${GGML_CPU_NAME} PRIVATE . ggml-cpu)

    # ... (rest of the function for Accelerate, OpenMP, LLAMAFILE, HBM, ARM optimizations)
endfunction()
```

--------------------------------

TITLE: CMake Configuration for BLAS Integration
DESCRIPTION: This snippet outlines the CMake logic for finding and configuring BLAS libraries. It checks for BLAS availability, sets compile definitions based on the BLAS vendor (e.g., Accelerate for Apple, MKL for Intel), and links the appropriate libraries and include directories. It also includes fallback mechanisms for finding include paths when PkgConfig is not sufficient.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-blas/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
if (GGML_STATIC)
    set(BLA_STATIC ON)
endif()

#if (CMAKE_VERSION VERSION_GREATER_EQUAL 3.22)
#    set(BLA_SIZEOF_INTEGER 8)
#endif()

set(BLA_VENDOR ${GGML_BLAS_VENDOR})
find_package(BLAS)

if (BLAS_FOUND)
    message(STATUS "BLAS found, Libraries: ${BLAS_LIBRARIES}")

    ggml_add_backend_library(ggml-blas
                             ggml-blas.cpp
                            )

    if (${GGML_BLAS_VENDOR} MATCHES "Apple")
        add_compile_definitions(ACCELERATE_NEW_LAPACK)
        add_compile_definitions(ACCELERATE_LAPACK_ILP64)
        add_compile_definitions(GGML_BLAS_USE_ACCELERATE)
    elseif ("${BLAS_INCLUDE_DIRS}" STREQUAL "")
        # BLAS_INCLUDE_DIRS is missing in FindBLAS.cmake.
        # see https://gitlab.kitware.com/cmake/cmake/-/issues/20268
        find_package(PkgConfig REQUIRED)
        if (${GGML_BLAS_VENDOR} MATCHES "Generic")
            pkg_check_modules(DepBLAS blas)
        elseif (${GGML_BLAS_VENDOR} MATCHES "OpenBLAS")
            # As of openblas v0.3.22, the 64-bit is named openblas64.pc
            pkg_check_modules(DepBLAS openblas64)
            if (NOT DepBLAS_FOUND)
                pkg_check_modules(DepBLAS openblas)
            endif()
        elseif (${GGML_BLAS_VENDOR} MATCHES "FLAME")
            add_compile_definitions(GGML_BLAS_USE_BLIS)
            pkg_check_modules(DepBLAS blis)
        elseif (${GGML_BLAS_VENDOR} MATCHES "ATLAS")
            pkg_check_modules(DepBLAS blas-atlas)
        elseif (${GGML_BLAS_VENDOR} MATCHES "FlexiBLAS")
            pkg_check_modules(DepBLAS flexiblas_api)
        elseif (${GGML_BLAS_VENDOR} MATCHES "Intel")
            add_compile_definitions(GGML_BLAS_USE_MKL)
            # all Intel* libraries share the same include path
            pkg_check_modules(DepBLAS mkl-sdl)
        elseif (${GGML_BLAS_VENDOR} MATCHES "NVHPC")
            # this doesn't provide pkg-config
            # suggest to assign BLAS_INCLUDE_DIRS on your own
            if ("${NVHPC_VERSION}" STREQUAL "")
                message(WARNING "Better to set NVHPC_VERSION")
            else()
                set(DepBLAS_FOUND ON)
                set(DepBLAS_INCLUDE_DIRS "/opt/nvidia/hpc_sdk/${CMAKE_SYSTEM_NAME}_${CMAKE_SYSTEM_PROCESSOR}/${NVHPC_VERSION}/math_libs/include")
            endif()
        endif()
        if (DepBLAS_FOUND)
            set(BLAS_INCLUDE_DIRS ${DepBLAS_INCLUDE_DIRS})
        else()
            message(WARNING "BLAS_INCLUDE_DIRS neither been provided nor been automatically" 
                  " detected by pkgconfig, trying to find cblas.h from possible paths...")
            find_path(BLAS_INCLUDE_DIRS
                NAMES cblas.h
                HINTS
                    /usr/include
                    /usr/local/include
                    /usr/include/openblas
                    /opt/homebrew/opt/openblas/include
                    /usr/local/opt/openblas/include
                    /usr/include/x86_64-linux-gnu/openblas/include
            )
        endif()
    endif()

    message(STATUS "BLAS found, Includes: ${BLAS_INCLUDE_DIRS}")

    target_compile_options(ggml-blas PRIVATE ${BLAS_LINKER_FLAGS})

    if (${BLAS_INCLUDE_DIRS} MATCHES "mkl" AND (${GGML_BLAS_VENDOR} MATCHES "Generic" OR ${GGML_BLAS_VENDOR} MATCHES "Intel"))
        add_compile_definitions(GGML_BLAS_USE_MKL)
    endif()

    target_link_libraries     (ggml-blas PRIVATE ${BLAS_LIBRARIES})
    target_include_directories(ggml-blas PRIVATE ${BLAS_INCLUDE_DIRS})
else()
    message(ERROR "BLAS not found, please refer to "
                  "https://cmake.org/cmake/help/latest/module/FindBLAS.html#blas-lapack-vendors"
                  " to set correct GGML_BLAS_VENDOR")
endif()
```

--------------------------------

TITLE: Ollama API Reference
DESCRIPTION: Provides an overview of the Ollama API, including the base URL and common endpoints for interacting with language models.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/windows.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
Base URL: http://localhost:11434

Endpoints:
- /api/generate: Generates text based on a prompt and model.
- /api/chat: Engages in a chat conversation with a model.
- /api/pull: Pulls a model from the Ollama registry.
- /api/tags: Lists available models.
- /api/delete: Deletes a model.
- /api/embeddings: Generates embeddings for a given prompt.
- /api/completion: (Deprecated) Use /api/generate.
- /api/context: Creates a context for chat interactions.
- /api/show: Shows information about a specific model.
- /api/create: Creates a new model from a Modelfile.
- /api/ps: Lists running Ollama services.
- /api/env: Gets Ollama environment information.
- /api/version: Gets the Ollama version.
- /api/health: Checks the health of the Ollama service.
- /api/config: Gets or sets Ollama configuration.
- /api/serve: Starts the Ollama server (typically used with system service managers).

Example API Call (Generate):
POST /api/generate
Body:
{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false
}

Response:
{
  "model": "llama3.2",
  "created_at": "2024-04-15T10:00:00.000Z",
  "response": "The sky appears blue due to a phenomenon called Rayleigh scattering...",
  "done": true,
  "context": [ ... ],
  "total_duration": 1234567890,
  "load_duration": 123456789,
  "prompt_eval_count": 10,
  "prompt_eval_duration": 12345678,
  "eval_count": 100,
  "eval_duration": 123456789
}
```

--------------------------------

TITLE: Run Ollama Docker with Proxy Configuration
DESCRIPTION: This command demonstrates how to run the Ollama Docker container with an HTTPS proxy configured via an environment variable. It also maps the container's port to the host machine.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_6

LANGUAGE: shell
CODE:
```
docker build -t ollama-with-ca .
docker run -d -e HTTPS_PROXY=https://my.proxy.example.com -p 11434:11434 ollama-with-ca
```

--------------------------------

TITLE: Pulling and Copying Models
DESCRIPTION: Demonstrates how to pull models locally using `ollama pull` and how to copy existing model names to new ones using `ollama cp` for compatibility with OpenAI default names.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_17

LANGUAGE: shell
CODE:
```
ollama pull llama3.2

ollama cp llama3.2 gpt-3.5-turbo
```

--------------------------------

TITLE: Importing a GGUF Adapter
DESCRIPTION: This snippet illustrates the Modelfile content for importing a GGUF-based adapter. It requires a FROM command for the base model and an ADAPTER command for the GGUF adapter file.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_5

LANGUAGE: dockerfile
CODE:
```
FROM <model name>
ADAPTER /path/to/file.gguf
```

--------------------------------

TITLE: Emscripten Build Configuration
DESCRIPTION: Applies specific compile flags for Emscripten builds to ensure compatibility and proper SIMD utilization.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_13

LANGUAGE: cmake
CODE:
```
if (EMSCRIPTEN)
        set_target_properties(${GGML_CPU_NAME} PROPERTIES COMPILE_FLAGS "-msimd128")
    endif()
endfunction()
```

--------------------------------

TITLE: Compiling CUDA Sources and Linking Libraries
DESCRIPTION: This snippet shows how to find and include CUDA source files (`.cu`) and header files (`.cuh`), including those from template instances. It then uses a custom CMake function `ggml_add_backend_library` to build a CUDA library and links it with necessary CUDA libraries like `cudart`, `cublas`, and `cublasLt`, with conditional linking for static libraries.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cuda/CMakeLists.txt#_snippet_1

LANGUAGE: cmake
CODE:
```
    file(GLOB   GGML_HEADERS_CUDA "*.cuh")
    list(APPEND GGML_HEADERS_CUDA "../../include/ggml-cuda.h")

    file(GLOB   GGML_SOURCES_CUDA "*.cu")
    file(GLOB   SRCS "template-instances/fattn-mma*.cu")
    list(APPEND GGML_SOURCES_CUDA ${SRCS})
    file(GLOB   SRCS "template-instances/mmq*.cu")
    list(APPEND GGML_SOURCES_CUDA ${SRCS})

    if (GGML_CUDA_FA_ALL_QUANTS)
        file(GLOB   SRCS "template-instances/fattn-vec*.cu")
        list(APPEND GGML_SOURCES_CUDA ${SRCS})
        add_compile_definitions(GGML_CUDA_FA_ALL_QUANTS)
    else()
        file(GLOB   SRCS "template-instances/fattn-vec*q4_0-q4_0.cu")
        list(APPEND GGML_SOURCES_CUDA ${SRCS})
        file(GLOB   SRCS "template-instances/fattn-vec*q8_0-q8_0.cu")
        list(APPEND GGML_SOURCES_CUDA ${SRCS})
        file(GLOB   SRCS "template-instances/fattn-vec*f16-f16.cu")
        list(APPEND GGML_SOURCES_CUDA ${SRCS})
    endif()

    ggml_add_backend_library(ggml-cuda
                             ${GGML_HEADERS_CUDA}
                             ${GGML_SOURCES_CUDA}
                            )

    if (GGML_STATIC)
        if (WIN32)
            # As of 12.3.1 CUDA Toolkit for Windows does not offer a static cublas library
            target_link_libraries(ggml-cuda PRIVATE CUDA::cudart_static CUDA::cublas CUDA::cublasLt)
        else ()
            target_link_libraries(ggml-cuda PRIVATE  CUDA::cudart_static CUDA::cublas_static CUDA::cublasLt_static)
        endif()
    else()
        target_link_libraries(ggml-cuda PRIVATE CUDA::cudart CUDA::cublas CUDA::cublasLt)
    endif()

    if (GGML_CUDA_NO_VMM)
        # No VMM requested, no need to link directly with the cuda driver lib (libcuda.so)
    else()
        target_link_libraries(ggml-cuda PRIVATE CUDA::cuda_driver)
    endif()

    set(CUDA_CXX_FLAGS "")

    set(CUDA_FLAGS -use_fast_math -extended-lambda)

    if (CUDAToolkit_VERSION VERSION_GREATER_EQUAL "12.8")
        # Options are:
        # - none (not recommended)

```

--------------------------------

TITLE: Configure Ollama Server Environment Variables
DESCRIPTION: Provides instructions for setting environment variables to configure the Ollama server on macOS, Linux (systemd), and Windows. This includes setting variables like `OLLAMA_HOST` and `OLLAMA_MODELS`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_3

LANGUAGE: shell
CODE:
```
launchctl setenv OLLAMA_HOST "0.0.0.0:11434"
```

LANGUAGE: ini
CODE:
```
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

LANGUAGE: shell
CODE:
```
systemctl daemon-reload
systemctl restart ollama
```

--------------------------------

TITLE: Configuring Docker for NVIDIA GPUs
DESCRIPTION: Provides the configuration change needed in Docker's `daemon.json` to resolve GPU discovery issues by setting the cgroup driver to `cgroupfs`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_4

LANGUAGE: json
CODE:
```
{
  "exec-opts": ["native.cgroupdriver=cgroupfs"]
}
```

--------------------------------

TITLE: Enabling Flash Attention in Ollama
DESCRIPTION: Instructions to enable Flash Attention for reduced memory usage with growing context sizes by setting an environment variable.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_19

LANGUAGE: APIDOC
CODE:
```
OLLAMA_FLASH_ATTENTION
  Description: Set to '1' to enable Flash Attention.
  Usage: Set the environment variable when starting the Ollama server.
```

--------------------------------

TITLE: NVIDIA GPU Troubleshooting Commands
DESCRIPTION: A collection of commands and techniques for troubleshooting NVIDIA GPU detection and initialization issues with Ollama, including checking container runtime, loading drivers, and increasing log verbosity.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_5

LANGUAGE: shell
CODE:
```
docker run --gpus all ubuntu nvidia-smi
```

LANGUAGE: shell
CODE:
```
sudo nvidia-modprobe -u
```

LANGUAGE: shell
CODE:
```
sudo rmmod nvidia_uvm
sudo modprobe nvidia_uvm
```

LANGUAGE: shell
CODE:
```
export CUDA_ERROR_LEVEL=50
```

LANGUAGE: shell
CODE:
```
sudo dmesg | grep -i nvrm
```

LANGUAGE: shell
CODE:
```
sudo dmesg | grep -i nvidia
```

--------------------------------

TITLE: Stop/Unload Model with Ollama CLI
DESCRIPTION: Demonstrates how to immediately stop and unload a model from memory using the `ollama stop` command.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_14

LANGUAGE: shell
CODE:
```
ollama stop llama3.2
```

--------------------------------

TITLE: ARM Feature Detection and Configuration
DESCRIPTION: This snippet demonstrates how CMake checks for specific ARM CPU features (dotprod, i8mm, sve, sme) by compiling small test programs. It then appends the appropriate compiler flags and defines preprocessor macros based on the detected features, enabling optimized code paths.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
function(check_arm_feature)
    set(CMAKE_REQUIRED_FLAGS ${CMAKE_REQUIRED_FLAGS_SAVE})
    check_cxx_source_runs("#include <arm_neon.h>\nint main() { int8x16_t _a, _b; volatile int32x4_t _s = vdotq_s32(_s, _a, _b); return 0; }")
    check_cxx_source_runs("#include <arm_neon.h>\nint main() { int8x16_t _a, _b; volatile int32x4_t _s = vmmlaq_s32(_s, _a, _b); return 0; }")
    check_cxx_source_runs("#include <arm_sve.h>\nint main()  { svfloat32_t _a, _b; volatile svfloat32_t _c = svadd_f32_z(svptrue_b8(), _a, _b); return 0; }")
    check_cxx_source_runs("#include <arm_sve.h>\n__arm_locally_streaming int main() { __asm__ volatile(\"smstart; smstop;\"); return 0; }")
    list(APPEND ARCH_FLAGS "${ARM_MCPU_FLAG}${ARM_MCPU_FLAG_FIX}")
else()
    if (GGML_CPU_ARM_ARCH)
        list(APPEND ARCH_FLAGS -march=${GGML_CPU_ARM_ARCH})
    endif()
endif()

if (CMAKE_HOST_SYSTEM_NAME STREQUAL "Windows")
    set(FEAT_INPUT_FILE "NUL")
else()
    set(FEAT_INPUT_FILE "/dev/null")
endif()

execute_process(
    COMMAND ${CMAKE_C_COMPILER} ${ARCH_FLAGS} -dM -E -
    INPUT_FILE ${FEAT_INPUT_FILE}
    OUTPUT_VARIABLE ARM_FEATURE
    RESULT_VARIABLE ARM_FEATURE_RESULT
)
if (ARM_FEATURE_RESULT)
    message(WARNING "Failed to get ARM features")
else()
    foreach(feature DOTPROD SVE MATMUL_INT8 FMA FP16_VECTOR_ARITHMETIC SME)
        string(FIND "${ARM_FEATURE}" "__ARM_FEATURE_${feature} 1" feature_pos)
        if (NOT ${feature_pos} EQUAL -1)
            message(STATUS "ARM feature ${feature} enabled")
        endif()
    endforeach()
endif()
```

--------------------------------

TITLE: CPU Backend Configuration
DESCRIPTION: Configures the CPU backend, either by adding a default variant or all available variants if GGML_CPU_ALL_VARIANTS is enabled. It includes checks for required conditions like GGML_BACKEND_DL.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_9

LANGUAGE: cmake
CODE:
```
ggml_add_backend(CPU)

if (GGML_CPU_ALL_VARIANTS)
    if (NOT GGML_BACKEND_DL)
        message(FATAL_ERROR "GGML_CPU_ALL_VARIANTS requires GGML_BACKEND_DL")
    endif()
    add_custom_target(ggml-cpu)
    ggml_add_cpu_backend_variant(x64)
    ggml_add_cpu_backend_variant(sse42        SSE42)
    ggml_add_cpu_backend_variant(sandybridge  SSE42 AVX)
    ggml_add_cpu_backend_variant(haswell      SSE42 AVX F16C AVX2 BMI2 FMA)
    ggml_add_cpu_backend_variant(skylakex     SSE42 AVX F16C AVX2 BMI2 FMA AVX512)
    ggml_add_cpu_backend_variant(icelake      SSE42 AVX F16C AVX2 BMI2 FMA AVX512 AVX512_VBMI AVX512_VNNI)
    ggml_add_cpu_backend_variant(alderlake    SSE42 AVX F16C AVX2 BMI2 FMA AVX_VNNI)
elseif (GGML_CPU)
    ggml_add_cpu_backend_variant_impl("")
endif()
```

--------------------------------

TITLE: Dynamic Loading Feature Detection
DESCRIPTION: Sets up a separate library target for feature detection when dynamic loading (GGML_BACKEND_DL) is enabled. This ensures feature detection is compiled without architecture-specific flags, preventing conflicts.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_12

LANGUAGE: cmake
CODE:
```
if (GGML_BACKEND_DL)
        if (GGML_NATIVE)
            message(FATAL_ERROR "GGML_NATIVE is not compatible with GGML_BACKEND_DL, consider using GGML_CPU_ALL_VARIANTS")
        endif()

        set(GGML_CPU_FEATS_NAME ${GGML_CPU_NAME}-feats)
        add_library(${GGML_CPU_FEATS_NAME} OBJECT ggml-cpu/cpu-feats-x86.cpp)
        target_include_directories(${GGML_CPU_FEATS_NAME} PRIVATE . .. ../include)
        target_compile_definitions(${GGML_CPU_FEATS_NAME} PRIVATE ${ARCH_DEFINITIONS})
        target_compile_definitions(${GGML_CPU_FEATS_NAME} PRIVATE GGML_BACKEND_DL GGML_BACKEND_BUILD GGML_BACKEND_SHARED)
        set_target_properties(${GGML_CPU_FEATS_NAME} PROPERTIES POSITION_INDEPENDENT_CODE ON)
        target_link_libraries(${GGML_CPU_NAME} PRIVATE ${GGML_CPU_FEATS_NAME})
```

--------------------------------

TITLE: Conditional Library Linking
DESCRIPTION: Demonstrates conditional linking of libraries based on CMake variables and system detection. This includes linking the Accelerate framework on Apple systems, OpenMP for parallel processing, and memkind for CPU HBM support.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
if (APPLE AND GGML_ACCELERATE)
    find_library(ACCELERATE_FRAMEWORK Accelerate)
    if (ACCELERATE_FRAMEWORK)
        message(STATUS "Accelerate framework found")

        target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_ACCELERATE)
        target_compile_definitions(${GGML_CPU_NAME} PRIVATE ACCELERATE_NEW_LAPACK)
        target_compile_definitions(${GGML_CPU_NAME} PRIVATE ACCELERATE_LAPACK_ILP64)

        target_link_libraries(${GGML_CPU_NAME} PRIVATE ${ACCELERATE_FRAMEWORK})
    else()
        message(WARNING "Accelerate framework not found")
    endif()
endif()

if (GGML_OPENMP)
    find_package(OpenMP)
    if (OpenMP_FOUND)
        target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_OPENMP)

        target_link_libraries(${GGML_CPU_NAME} PRIVATE OpenMP::OpenMP_C OpenMP::OpenMP_CXX)
    else()
        message(WARNING "OpenMP not found")
    endif()
endif()

if (GGML_LLAMAFILE)
    target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_LLAMAFILE)

    list(APPEND GGML_CPU_SOURCES
                ggml-cpu/llamafile/sgemm.cpp
                ggml-cpu/llamafile/sgemm.h)
endif()

if (GGML_CPU_HBM)
    find_library(memkind memkind REQUIRED)

    message(STATUS "Using memkind for CPU HBM")

    target_compile_definitions(${GGML_CPU_NAME} PRIVATE GGML_USE_CPU_HBM)

    target_link_libraries(${GGML_CPU_NAME} PUBLIC memkind)
endif()
```

--------------------------------

TITLE: Apply Patches to Vendored llama.cpp
DESCRIPTION: Applies a set of predefined patches to the vendored llama.cpp repository. This is the initial step when setting up or updating the vendored code.

SOURCE: https://github.com/ollama/ollama/blob/main/llama/README.md#_snippet_0

LANGUAGE: shell
CODE:
```
make -f Makefile.sync apply-patches
```

--------------------------------

TITLE: Linking Libraries for ggml-base
DESCRIPTION: Links the Threads::Threads library to ggml-base and conditionally links the math library 'm' on non-Windows systems or when ONEAPI_ROOT is not defined.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_12

LANGUAGE: cmake
CODE:
```
target_link_libraries(ggml-base PRIVATE Threads::Threads)

find_library(MATH_LIBRARY m)
if (MATH_LIBRARY)
    if (NOT WIN32 OR NOT DEFINED ENV{ONEAPI_ROOT})
        target_link_libraries(ggml-base PRIVATE m)
    endif()
endif()
```

--------------------------------

TITLE: ADAPTER Instruction (Safetensor and GGUF)
DESCRIPTION: The ADAPTER instruction applies a fine-tuned LoRA adapter to the base model. It supports Safetensor and GGUF formats and requires the base model to be specified with a FROM instruction. Using an adapter tuned from a different base model may lead to erratic behavior.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_8

LANGUAGE: APIDOC
CODE:
```
ADAPTER <path to safetensor adapter>
  - Applies a Safetensor LoRA adapter.
  - Supported models include Llama, Mistral, and Gemma variants.

ADAPTER ./ollama-lora.gguf
  - Applies a GGUF LoRA adapter.
```

--------------------------------

TITLE: Run Ollama Integration Tests
DESCRIPTION: This command enables and runs the integration tests for the Ollama project. It requires the `integration` tag to be passed to the Go test runner.

SOURCE: https://github.com/ollama/ollama/blob/main/integration/README.md#_snippet_0

LANGUAGE: go
CODE:
```
go test -tags=integration ./...
```

--------------------------------

TITLE: ggml Main Library and Backend Linking
DESCRIPTION: Creates the main ggml library, linking it with the base library and registering various backends. It handles platform-specific linking, such as the 'dl' library on Linux.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_15

LANGUAGE: cmake
CODE:
```
add_library(ggml
            ggml-backend-reg.cpp)

target_link_libraries(ggml PUBLIC ggml-base)

if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_libraries(ggml PRIVATE dl)
endif()
```

--------------------------------

TITLE: Check Ollama Model GPU Loading
DESCRIPTION: The `ollama ps` command displays currently loaded models, their size, processor usage (CPU/GPU), context, and estimated remaining time. This helps in diagnosing if models are loaded onto the GPU.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_2

LANGUAGE: shell
CODE:
```
ollama ps
```

--------------------------------

TITLE: Setting Context Size with Modelfile
DESCRIPTION: Explains how to adjust a model's context size by creating a `Modelfile` with the `PARAMETER num_ctx` directive and then creating a new model using `ollama create`.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_18

LANGUAGE: shell
CODE:
```
FROM <some model>
PARAMETER num_ctx <context size>

ollama create mymodel

curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{ \
        "model": "mymodel", \
        "messages": [ \
            { \
                "role": "user", \
                "content": "Hello!" \
            } \
        ] \
    }'
```

--------------------------------

TITLE: loongarch64 Architecture Optimizations
DESCRIPTION: Applies compiler flags for the loongarch64 architecture, enabling specific instruction sets like LASX and LSX if configured.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_7

LANGUAGE: cmake
CODE:
```
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "loongarch64")
    message(STATUS "loongarch64 detected")

    list(APPEND ARCH_FLAGS -march=loongarch64)
    if (GGML_LASX)
        list(APPEND ARCH_FLAGS -mlasx)
    endif()
    if (GGML_LSX)
        list(APPEND ARCH_FLAGS -mlsx)
    endif()

```

--------------------------------

TITLE: Ollama Python Library: Chat with Turbo
DESCRIPTION: This Python code shows how to use the Ollama client library to interact with a Turbo-enabled model. It includes setting up the client with an API key and streaming responses from a chat conversation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/turbo.md#_snippet_1

LANGUAGE: python
CODE:
```
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={'Authorization': '<api key>'}
)

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)
```

--------------------------------

TITLE: HIP Library Discovery and Version Check
DESCRIPTION: Finds required HIP libraries (hip, hipblas, rocblas) and checks if the HIP version meets the minimum requirement (V5.5).

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
find_package(hip     REQUIRED)
find_package(hipblas REQUIRED)
find_package(rocblas REQUIRED)

if (${hip_VERSION} VERSION_LESS 5.5)
    message(FATAL_ERROR "At least ROCM/HIP V5.5 is required")
endif()

message(STATUS "HIP and hipBLAS found")
```

--------------------------------

TITLE: Importing a GGUF Model
DESCRIPTION: This snippet shows the Modelfile content required to import a GGUF-based model. The FROM command should point to the path of the GGUF file.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_4

LANGUAGE: dockerfile
CODE:
```
FROM /path/to/file.gguf
```

--------------------------------

TITLE: Link-Time Optimization (LTO) and Ccache Integration
DESCRIPTION: Enables Link-Time Optimization (LTO) if supported by the compiler and integrates ccache or sccache for faster compilation by caching build artifacts. It also includes a workaround for a buggy Apple linker version.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_1

LANGUAGE: cmake
CODE:
```
if (GGML_LTO)
    include(CheckIPOSupported)
    check_ipo_supported(RESULT result OUTPUT output)
    if (result)
        set(CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
    else()
        message(WARNING "IPO is not supported: ${output}")
    endif()
endif()

if (GGML_CCACHE AND NOT CMAKE_C_COMPILER_LAUNCHER AND NOT CMAKE_CXX_COMPILER_LAUNCHER)
    find_program(GGML_CCACHE_FOUND ccache)
    find_program(GGML_SCCACHE_FOUND sccache)

    if (GGML_CCACHE_FOUND OR GGML_SCCACHE_FOUND)
        if(GGML_CCACHE_FOUND)
            set(GGML_CCACHE_VARIANT ccache)
        else()
            set(GGML_CCACHE_VARIANT sccache)
        endif()
        # TODO: should not be set globally
        if (GGML_SYCL AND GGML_CCACHE_FOUND AND WIN32)
            set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "ccache compiler_type=icl")
        else ()
            set_property(GLOBAL PROPERTY RULE_LAUNCH_COMPILE "${GGML_CCACHE_VARIANT}")
        endif ()
        set(ENV{CCACHE_SLOPPINESS} time_macros)
        message(STATUS "${GGML_CCACHE_VARIANT} found, compilation results will be cached. Disable with GGML_CCACHE=OFF.")
    else()
        message(STATUS "Warning: ccache not found - consider installing it for faster compilation or disable this warning with GGML_CCACHE=OFF")
    endif ()
endif()

# this version of Apple ld64 is buggy
execute_process(
    COMMAND ${CMAKE_C_COMPILER} ${CMAKE_EXE_LINKER_FLAGS} -Wl,-v
    ERROR_VARIABLE output
    OUTPUT_QUIET
)

if (output MATCHES "dyld-1015\.7")
    add_compile_definitions(HAVE_BUGGY_APPLE_LINKER)
endif()
```

--------------------------------

TITLE: ggml Base Library Definition
DESCRIPTION: Defines the base ggml library, including core header and source files. It sets up include directories and conditionally defines GGML_BACKEND_DL.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_4

LANGUAGE: cmake
CODE:
```
if (NOT BUILD_SHARED_LIBS)
    message(FATAL_ERROR "GGML_BACKEND_DL requires BUILD_SHARED_LIBS")
endif()

add_library(ggml-base
            ../include/ggml.h
            ../include/ggml-alloc.h
            ../include/ggml-backend.h
            ../include/ggml-cpp.h
            ../include/ggml-opt.h
            ../include/gguf.h
            ggml.c
            ggml-alloc.c
            ggml-backend.cpp
            ggml-opt.cpp
            ggml-threading.cpp
            ggml-threading.h
            ggml-quants.c
            ggml-quants.h
            gguf.cpp)

target_include_directories(ggml-base PRIVATE .)
if (GGML_BACKEND_DL)
    target_compile_definitions(ggml-base PUBLIC GGML_BACKEND_DL)
endif()
```

--------------------------------

TITLE: s390x Architecture Detection and Optimization
DESCRIPTION: Detects s390x processor architecture and applies appropriate compiler flags based on the detected machine type (e.g., z15, z16, z17). Includes conditional compilation for VX/VXE features and a fallback to 'native' optimization for unknown targets.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_9

LANGUAGE: cmake
CODE:
```
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "s390x")
    message(STATUS "s390x detected")
    file(READ "/proc/cpuinfo" CPUINFO_CONTENTS)
    string(REGEX REPLACE "machine[ \t\r\n]*=[ \t\r\n]*([0-9]+)" "\1" S390X_M ${CPUINFO_CONTENTS})

    # TODO: Separation to determine activation of VX/VXE/VXE2
    if (${S390X_M} MATCHES "8561|8562")
        message(STATUS "z15 target")
        list(APPEND ARCH_FLAGS -march=z15)
    elseif (${S390X_M} MATCHES "3931")
        message(STATUS "z16 target")
        list(APPEND ARCH_FLAGS -march=z16)
    elseif (${S390X_M} MATCHES "9175|99176")
        # NOTE: Only available from GCC 15.1.0 onwards. Any z17 machine with compile issues must first verify their GCC version.
        message(STATUS "z17 target")
        list(APPEND ARCH_FLAGS -march=z17)
    else()
        message(STATUS "Unknown target")
        message(WARNING "Unknown target. If you are compiling for z14 and earlier, you might have to add -DGGML_VXE=OFF.")
        list(APPEND ARCH_FLAGS -march=native -mtune=native)
    endif()

    if (GGML_VXE)
        list(APPEND ARCH_FLAGS -mvx -mzvector)
    endif()
else()
    message(STATUS "Unknown architecture")
endif()
```

--------------------------------

TITLE: Creating a Model from a Safetensors Adapter
DESCRIPTION: This shell command is used to create a new Ollama model after defining a Modelfile for a Safetensors adapter. Replace 'my-model' with the desired name for your new model.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_1

LANGUAGE: shell
CODE:
```
ollama create my-model
```

--------------------------------

TITLE: Ollama Server Configuration Options
DESCRIPTION: Environment variables to configure Ollama's concurrency and resource management. These settings control the maximum number of loaded models, parallel requests per model, and the request queue size.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_18

LANGUAGE: APIDOC
CODE:
```
OLLAMA_MAX_LOADED_MODELS
  Description: The maximum number of models that can be loaded concurrently provided they fit in available memory.
  Default: 3 * number of GPUs or 3 for CPU inference.

OLLAMA_NUM_PARALLEL
  Description: The maximum number of parallel requests each model will process at the same time.
  Default: 1.

OLLAMA_MAX_QUEUE
  Description: The maximum number of requests Ollama will queue when busy before rejecting additional requests.
  Default: 512.
```

--------------------------------

TITLE: ggml Library Compile Features and Linking
DESCRIPTION: Sets common compile features (C++17) and include directories for the ggml-base and ggml targets. It also links against the Threads library and the system math library ('m').

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_21

LANGUAGE: cmake
CODE:
```
foreach (target ggml-base ggml)
    target_include_directories(${target} PUBLIC    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include> $<INSTALL_INTERFACE:include>)
    target_compile_features   (${target} PRIVATE c_std_11 cxx_std_17) # don't bump
endforeach()

target_link_libraries(ggml-base PRIVATE Threads::Threads)

find_library(MATH_LIBRARY m)
if (MATH_LIBRARY)
    if (NOT WIN32 OR NOT DEFINED ENV{ONEAPI_ROOT})
        target_link_libraries(ggml-base PRIVATE m)
    endif()
endif()

if (CMAKE_SYSTEM_NAME MATCHES "Android")
    target_link_libraries(ggml-base PRIVATE dl)
endif()

if(CMAKE_SYSTEM_NAME MATCHES "visionOS")

```

--------------------------------

TITLE: Ollama Modelfile Structure and Instructions
DESCRIPTION: Defines the general format of an Ollama Modelfile, including comments and the various instructions that can be used.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
Modelfile Format:
  # comment
  INSTRUCTION arguments

Instructions:
  FROM <model name>:<tag> (required): Defines the base model to use.
  PARAMETER <parameter> <parametervalue>: Sets parameters for model execution.
  TEMPLATE """...""" : The full prompt template for the model.
  SYSTEM """...""" : Specifies the system message for the template.
  ADAPTER <adapter path>: Defines (Q)LoRA adapters to apply.
  LICENSE """...""" : Specifies the legal license.
  MESSAGE """...""" : Specifies message history.
```

--------------------------------

TITLE: CUDA Toolkit Configuration and Architecture Selection
DESCRIPTION: This snippet demonstrates how to find the CUDA Toolkit, set the `CMAKE_CUDA_ARCHITECTURES` based on various conditions (native support, FP16, DMMV_F16, toolkit version), and enable the CUDA language. It includes comments explaining the different architecture codes and their meanings.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cuda/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
cmake_minimum_required(VERSION 3.18)  # for CMAKE_CUDA_ARCHITECTURES

find_package(CUDAToolkit)

if (CUDAToolkit_FOUND)
    message(STATUS "CUDA Toolkit found")

    if (NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
        # native == GPUs available at build time
        # 50     == Maxwell, lowest CUDA 12 standard
        # 60     == P100, FP16 CUDA intrinsics
        # 61     == Pascal, __dp4a instruction (per-byte integer dot product)
        # 70     == V100, FP16 tensor cores
        # 75     == Turing, int8 tensor cores
        # 80     == Ampere, asynchronous data loading, faster tensor core instructions
        # 86     == RTX 3000, needs CUDA v11.1
        # 89     == RTX 4000, needs CUDA v11.8
        #
        # XX-virtual == compile CUDA code as PTX, do JIT compilation to binary code on first run
        # XX-real    == compile CUDA code as device code for this specific architecture
        # no suffix  == compile as both PTX and device code
        #
        # The default behavior for a non-native is to build virtual architectures as needed to cover all features needed
        #     for best performance and to also build real architectures for the most commonly used GPUs.
        if (GGML_NATIVE AND CUDAToolkit_VERSION VERSION_GREATER_EQUAL "11.6" AND CMAKE_VERSION VERSION_GREATER_EQUAL "3.24")
            set(CMAKE_CUDA_ARCHITECTURES "native")
        elseif(GGML_CUDA_F16 OR GGML_CUDA_DMMV_F16)
            if (CUDAToolkit_VERSION VERSION_GREATER_EQUAL "11.8")
                set(CMAKE_CUDA_ARCHITECTURES "60-virtual;61-virtual;70-virtual;75-virtual;80-virtual;86-real;89-real")
            else()
                set(CMAKE_CUDA_ARCHITECTURES "60-virtual;61-virtual;70-virtual;75-virtual;80-virtual;86-real")
            endif()
        else()
            if (CUDAToolkit_VERSION VERSION_GREATER_EQUAL "11.8")
                set(CMAKE_CUDA_ARCHITECTURES "50-virtual;61-virtual;70-virtual;75-virtual;80-virtual;86-real;89-real")
            else()
                set(CMAKE_CUDA_ARCHITECTURES "50-virtual;61-virtual;70-virtual;75-virtual;80-virtual;86-real")
            endif()
        endif()
    endif()
    message(STATUS "Using CUDA architectures: ${CMAKE_CUDA_ARCHITECTURES}")

    enable_language(CUDA)

```

--------------------------------

TITLE: Generate Text with Ollama API
DESCRIPTION: Demonstrates how to interact with the Ollama API to generate text. It sends a POST request with a model, prompt, and stream setting, then parses the JSON response.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/windows.md#_snippet_1

LANGUAGE: powershell
CODE:
```
(Invoke-WebRequest -method POST -Body '{"model":"llama3.2", "prompt":"Why is the sky blue?", "stream": false}' -uri http://localhost:11434/api/generate ).Content | ConvertFrom-json
```

--------------------------------

TITLE: Compile Metal Shaders to Metallib
DESCRIPTION: This snippet handles the compilation of Metal shaders into a `.metallib` file. It uses `xcrun` commands to compile the Metal source (`.metal`) into an intermediate assembly (`.air`) and then into a library (`.metallib`). It supports debug flags like `-fno-fast-math` and `-fno-inline` for debugging purposes, and allows specifying macOS version and Metal standard versions.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-metal/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
if (NOT GGML_METAL_EMBED_LIBRARY)
    if (GGML_METAL_SHADER_DEBUG)
        # custom command to do the following:
        #   xcrun -sdk macosx metal    -fno-fast-math -c ggml-metal.metal -o ggml-metal.air
        #   xcrun -sdk macosx metallib                   ggml-metal.air   -o default.metallib
        #
        # note: this is the only way I found to disable fast-math in Metal. it's ugly, but at least it works
        #       disabling fast math is needed in order to pass tests/test-backend-ops
        # note: adding -fno-inline fixes the tests when using MTL_SHADER_VALIDATION=1
        # note: unfortunately, we have to call it default.metallib instead of ggml.metallib
        #       ref: https://github.com/ggerganov/whisper.cpp/issues/1720
        set(XC_FLAGS -fno-fast-math -fno-inline -g)
    else()
        set(XC_FLAGS -O3)
    endif()

    # Append macOS metal versioning flags
    if (GGML_METAL_MACOSX_VERSION_MIN)
        message(STATUS "Adding  -mmacosx-version-min=${GGML_METAL_MACOSX_VERSION_MIN} flag to metal compilation")
        list   (APPEND XC_FLAGS -mmacosx-version-min=${GGML_METAL_MACOSX_VERSION_MIN})
    endif()

    if (GGML_METAL_STD)
        message(STATUS "Adding  -std=${GGML_METAL_STD} flag to metal compilation")
        list   (APPEND XC_FLAGS -std=${GGML_METAL_STD})
    endif()

    add_custom_command(
        OUTPUT ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        COMMAND xcrun -sdk macosx metal ${XC_FLAGS} -c ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal.metal -o - | \
            xcrun -sdk macosx metallib - -o ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        COMMAND rm -f ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-common.h
        COMMAND rm -f ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ggml-metal.metal
        DEPENDS ggml-metal.metal ${METALLIB_COMMON}
        COMMENT "Compiling Metal kernels"
        )

    # FIXME: only add to the ggml-metal target?
    add_custom_target(
        ggml-metal-lib ALL
        DEPENDS ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/default.metallib
        )
endif() # GGML_METAL_EMBED_LIBRARY
```

--------------------------------

TITLE: Embed Metal Library into Assembly
DESCRIPTION: This snippet configures the build process to embed Metal shaders directly into an assembly file. It merges common header files and Metal source code, then uses `sed` and `echo` commands to create an assembly file containing the Metal library. This is useful for distributing Metal functionality as part of the compiled binary.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-metal/CMakeLists.txt#_snippet_1

LANGUAGE: cmake
CODE:
```
if (GGML_METAL_EMBED_LIBRARY)
    enable_language(ASM)

    add_compile_definitions(GGML_METAL_EMBED_LIBRARY)

    set(METALLIB_SOURCE "${CMAKE_CURRENT_SOURCE_DIR}/ggml-metal.metal")
    set(METALLIB_IMPL   "${CMAKE_CURRENT_SOURCE_DIR}/ggml-metal-impl.h")

    file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/autogenerated")

    # merge ggml-common.h and ggml-metal.metal into a single file
    set(METALLIB_EMBED_ASM        "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.s")
    set(METALLIB_SOURCE_EMBED     "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.metal")
    set(METALLIB_SOURCE_EMBED_TMP "${CMAKE_BINARY_DIR}/autogenerated/ggml-metal-embed.metal.tmp")

    add_custom_command(
        OUTPUT ${METALLIB_EMBED_ASM}
        COMMAND echo "Embedding Metal library"
        COMMAND sed -e '/__embed_ggml-common.h__/r         ${METALLIB_COMMON}' -e '/__embed_ggml-common.h__/d'         < ${METALLIB_SOURCE}           > ${METALLIB_SOURCE_EMBED_TMP}
        COMMAND sed -e '/#include "ggml-metal-impl.h"/r ${METALLIB_IMPL}'   -e '/#include "ggml-metal-impl.h"/d' < ${METALLIB_SOURCE_EMBED_TMP} > ${METALLIB_SOURCE_EMBED}
        COMMAND echo ".section __DATA,__ggml_metallib"          >  ${METALLIB_EMBED_ASM}
        COMMAND echo ".globl _ggml_metallib_start"              >> ${METALLIB_EMBED_ASM}
        COMMAND echo "_ggml_metallib_start:"                    >> ${METALLIB_EMBED_ASM}
        COMMAND echo ".incbin \"${METALLIB_SOURCE_EMBED}\"" >> ${METALLIB_EMBED_ASM}
        COMMAND echo ".globl _ggml_metallib_end"                >> ${METALLIB_EMBED_ASM}
        COMMAND echo "_ggml_metallib_end:"                      >> ${METALLIB_EMBED_ASM}
        DEPENDS ../ggml-common.h ggml-metal.metal ggml-metal-impl.h
        COMMENT "Generate assembly for embedded Metal library"
    )

    target_sources(ggml-metal PRIVATE ${METALLIB_EMBED_ASM})
else()
    # ... (rest of the else block for non-embedded compilation)
endif() # GGML_METAL_EMBED_LIBRARY
```

--------------------------------

TITLE: ARM Architecture Optimizations
DESCRIPTION: Detects ARM architecture and applies specific compiler flags and checks for CPU features. It includes logic to handle MSVC on ARM and checks for FP16 format support and NEON instructions using `check_cxx_compiler_flag` and `check_cxx_source_runs`.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_1

LANGUAGE: cmake
CODE:
```
if (CMAKE_OSX_ARCHITECTURES      STREQUAL "arm64" OR
    CMAKE_GENERATOR_PLATFORM_LWR STREQUAL "arm64" OR
    (NOT CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_GENERATOR_PLATFORM_LWR AND
        CMAKE_SYSTEM_PROCESSOR MATCHES "^(aarch64|arm.*|ARM64)$"))

    message(STATUS "ARM detected")

    if (MSVC AND NOT CMAKE_C_COMPILER_ID STREQUAL "Clang")
        message(FATAL_ERROR "MSVC is not supported for ARM, use clang")
    else()
        check_cxx_compiler_flag(-mfp16-format=ieee GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E)
        if (NOT "${GGML_COMPILER_SUPPORTS_FP16_FORMAT_I3E}" STREQUAL "")
            list(APPEND ARCH_FLAGS -mfp16-format=ieee)
        endif()

        if (GGML_NATIVE)
            # -mcpu=native does not always enable all the features in some compilers,
            # so we check for them manually and enable them if available

            execute_process(
                COMMAND ${CMAKE_C_COMPILER} -mcpu=native -E -v -
                INPUT_FILE "/dev/null"
                OUTPUT_QUIET
                ERROR_VARIABLE ARM_MCPU
                RESULT_VARIABLE ARM_MCPU_RESULT
            )
            if (NOT ARM_MCPU_RESULT)
                string(REGEX MATCH "-mcpu=[^ ']+" ARM_MCPU_FLAG "${ARM_MCPU}")
            endif()
            if ("${ARM_MCPU_FLAG}" STREQUAL "")
                set(ARM_MCPU_FLAG -mcpu=native)
                message(STATUS "ARM -mcpu not found, -mcpu=native will be used")
            endif()

            include(CheckCXXSourceRuns)

            function(check_arm_feature tag code)
                set(CMAKE_REQUIRED_FLAGS_SAVE ${CMAKE_REQUIRED_FLAGS})
                set(CMAKE_REQUIRED_FLAGS "${ARM_MCPU_FLAG}+${tag}")
                check_cxx_source_runs("${code}" GGML_MACHINE_SUPPORTS_${tag})
                if (GGML_MACHINE_SUPPORTS_${tag})
                    set(ARM_MCPU_FLAG_FIX "${ARM_MCPU_FLAG_FIX}+${tag}" PARENT_SCOPE)
                else()
                    set(CMAKE_REQUIRED_FLAGS "${ARM_MCPU_FLAG}+no${tag}")
                    check_cxx_source_compiles("int main() { return 0; }" GGML_MACHINE_SUPPORTS_no${tag})
                    if (GGML_MACHINE_SUPPORTS_no${tag})
                        # ... (logic for handling unsupported features)
                    endif()
                endif()
                set(CMAKE_REQUIRED_FLAGS ${CMAKE_REQUIRED_FLAGS_SAVE})
            endfunction()

            # Example usage of check_arm_feature for NEON
            # check_arm_feature(neon "int main() { return __builtin_neon_load_f32((float*)0); } ")
        endif()
    endif()
endif()
```

--------------------------------

TITLE: HIP Source and Header File Globbing
DESCRIPTION: Collects HIP source (.cu) and header (.cuh) files, including template instances, for compilation.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_6

LANGUAGE: cmake
CODE:
```
file(GLOB   GGML_HEADERS_ROCM "../ggml-cuda/*.cuh")
list(APPEND GGML_HEADERS_ROCM "../../include/ggml-cuda.h")

file(GLOB   GGML_SOURCES_ROCM "../ggml-cuda/*.cu")
file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-mma*.cu")
list(APPEND GGML_SOURCES_ROCM ${SRCS})
file(GLOB   SRCS "../ggml-cuda/template-instances/mmq*.cu")
list(APPEND GGML_SOURCES_ROCM ${SRCS})

if (GGML_CUDA_FA_ALL_QUANTS)
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    add_compile_definitions(GGML_CUDA_FA_ALL_QUANTS)
else()
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q4_0-q4_0.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*q8_0-q8_0.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
    file(GLOB   SRCS "../ggml-cuda/template-instances/fattn-vec*f16-f16.cu")
    list(APPEND GGML_SOURCES_ROCM ${SRCS})
endif()
```

--------------------------------

TITLE: Structured Output Parsing with Pydantic
DESCRIPTION: Demonstrates how to use the Ollama client with Pydantic models for structured output parsing in chat completions. It defines Pydantic schemas for the expected response and handles successful parsing or refusals.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_4

LANGUAGE: python
CODE:
```
from pydantic import BaseModel
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Define the schema for the response
class FriendInfo(BaseModel):
    name: str
    age: int
    is_available: bool

class FriendList(BaseModel):
    friends: list[FriendInfo]

try:
    completion = client.beta.chat.completions.parse(
        temperature=0,
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": "I have two friends. The first is Ollama 22 years old busy saving the world, and the second is Alonso 23 years old and wants to hang out. Return a list of friends in JSON format"}
        ],
        response_format=FriendList,
    )

    friends_response = completion.choices[0].message
    if friends_response.parsed:
        print(friends_response.parsed)
    elif friends_response.refusal:
        print(friends_response.refusal)
except Exception as e:
    print(f"Error: {e}")
```

--------------------------------

TITLE: ggml CPU Backend Variant Definitions
DESCRIPTION: Configures and adds various CPU backend variants with specific instruction set optimizations. This includes a check that `GGML_CPU_ALL_VARIANTS` requires `GGML_BACKEND_DL`.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_19

LANGUAGE: cmake
CODE:
```
ggml_add_backend(CPU)

if (GGML_CPU_ALL_VARIANTS)
    if (NOT GGML_BACKEND_DL)
        message(FATAL_ERROR "GGML_CPU_ALL_VARIANTS requires GGML_BACKEND_DL")
    endif()
    add_custom_target(ggml-cpu)
    ggml_add_cpu_backend_variant(x64)
    ggml_add_cpu_backend_variant(sse42        SSE42)
    ggml_add_cpu_backend_variant(sandybridge  SSE42 AVX)
    ggml_add_cpu_backend_variant(haswell      SSE42 AVX F16C AVX2 BMI2 FMA)
    ggml_add_cpu_backend_variant(skylakex     SSE42 AVX F16C AVX2 BMI2 FMA AVX512)
    ggml_add_cpu_backend_variant(icelake      SSE42 AVX F16C AVX2 BMI2 FMA AVX512 AVX512_VBMI AVX512_VNNI)
    ggml_add_cpu_backend_variant(alderlake    SSE42 AVX F16C AVX2 BMI2 FMA AVX_VNNI)
elseif (GGML_CPU)
    ggml_add_cpu_backend_variant_impl("")
endif()
```

--------------------------------

TITLE: RISC-V Architecture Optimizations
DESCRIPTION: Configures compiler flags for RISC-V (riscv64) architectures, specifically enabling the RVV (Vector Extension) and optionally the ZFH (Half-Precision Floating-Point) extension.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_8

LANGUAGE: cmake
CODE:
```
elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "riscv64")
    message(STATUS "RISC-V detected")
    if (GGML_RVV)
        if (GGML_RV_ZFH)
            list(APPEND ARCH_FLAGS -march=rv64gcv_zfhmin -DGGML_RV_ZFH -mabi=lp64d)
        else()
            list(APPEND ARCH_FLAGS -march=rv64gcv -mabi=lp64d)
        endif()
    endif()

```

--------------------------------

TITLE: PowerPC Architecture Optimizations
DESCRIPTION: Configures compiler flags for PowerPC (ppc64le, powerpc) architectures. It detects the CPU type (e.g., POWER10, POWER9) to apply appropriate optimization flags and handles native tuning.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_6

LANGUAGE: cmake
CODE:
```
elseif ("${CMAKE_SYSTEM_PROCESSOR} " STREQUAL "ppc64le " OR "${CMAKE_SYSTEM_PROCESSOR} " STREQUAL "powerpc ")
    message(STATUS "PowerPC detected")
    if (GGML_NATIVE)
        if (${CMAKE_SYSTEM_PROCESSOR} MATCHES "ppc64")
            file(READ "/proc/cpuinfo" POWER10_M)
        elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "powerpc")
            execute_process(COMMAND bash -c "prtconf |grep 'Implementation' | head -n 1" OUTPUT_VARIABLE POWER10_M)
        endif()

        string(REGEX MATCHALL "POWER *([0-9]+)" MATCHED_STRING "${POWER10_M}")
        string(REGEX REPLACE "POWER *([0-9]+)" "\\1" EXTRACTED_NUMBER "${MATCHED_STRING}")

        if (EXTRACTED_NUMBER GREATER_EQUAL 10)
            list(APPEND ARCH_FLAGS -mcpu=power10 -mpowerpc64)
        elseif (EXTRACTED_NUMBER EQUAL 9)
            list(APPEND ARCH_FLAGS -mcpu=power9 -mpowerpc64)
        elseif (${CMAKE_SYSTEM_PROCESSOR} MATCHES "ppc64le")
            list(APPEND ARCH_FLAGS -mcpu=powerpc64le -mtune=native)
        else()
            list(APPEND ARCH_FLAGS -mcpu=native -mtune=native -mpowerpc64)
        endif()
    else()
        if (GGML_CPU_POWERPC_CPUTYPE)
            list(APPEND ARCH_FLAGS -mcpu=${GGML_CPU_POWERPC_CPUTYPE})
        endif()
    endif()

```

--------------------------------

TITLE: Other Backend Inclusions
DESCRIPTION: Includes and configures various other hardware acceleration backends for ggml, such as BLAS, CUDA, Metal, Vulkan, and OpenCL.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_10

LANGUAGE: cmake
CODE:
```
ggml_add_backend(BLAS)
ggml_add_backend(CANN)
ggml_add_backend(CUDA)
ggml_add_backend(HIP)
ggml_add_backend(Kompute)
ggml_add_backend(METAL)
ggml_add_backend(MUSA)
ggml_add_backend(RPC)
ggml_add_backend(SYCL)
ggml_add_backend(Vulkan)
ggml_add_backend(OpenCL)
```

--------------------------------

TITLE: Chat Request with Tools
DESCRIPTION: Demonstrates a chat request to the Ollama API that includes tool definitions, allowing the model to call external functions. The response shows the model's tool call.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_28

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "what is the weather in tokyo?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather in a given city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city to get the weather for"
            }
          },
          "required": ["city"]
        }
      }
    }
  ],
  "stream": false 
}'
```

--------------------------------

TITLE: x86 Feature Detection and Configuration (MSVC)
DESCRIPTION: This section details the process for detecting x86 CPU features when using the MSVC compiler. It includes logic for enabling AVX, AVX2, AVX512 (with various extensions like VBMI, VNNI, BF16), and AMX instructions by setting compiler flags and defining corresponding preprocessor macros.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_4

LANGUAGE: cmake
CODE:
```
if (MSVC)
    if (GGML_NATIVE)
        include(ggml-cpu/cmake/FindSIMD.cmake)
    endif ()
    if (GGML_AVX512)
        list(APPEND ARCH_FLAGS /arch:AVX512)
        list(APPEND ARCH_DEFINITIONS GGML_AVX512)
        if (GGML_AVX512_VBMI)
            list(APPEND ARCH_DEFINITIONS __AVX512VBMI__) 
            if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                list(APPEND ARCH_FLAGS -mavx512vbmi)
            endif()
        endif()
        if (GGML_AVX512_VNNI)
            list(APPEND ARCH_DEFINITIONS __AVX512VNNI__ GGML_AVX512_VNNI)
            if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                list(APPEND ARCH_FLAGS -mavx512vnni)
            endif()
        endif()
        if (GGML_AVX512_BF16)
            list(APPEND ARCH_DEFINITIONS __AVX512BF16__ GGML_AVX512_BF16)
            if (CMAKE_C_COMPILER_ID STREQUAL "Clang")
                list(APPEND ARCH_FLAGS -mavx512bf16)
            endif()
        endif()
        if (GGML_AMX_TILE)
            list(APPEND ARCH_DEFINITIONS __AMX_TILE__ GGML_AMX_TILE)
        endif()
        if (GGML_AMX_INT8)
            list(APPEND ARCH_DEFINITIONS __AMX_INT8__ GGML_AMX_INT8)
        endif()
        if (GGML_AMX_BF16)
            list(APPEND ARCH_DEFINITIONS __AMX_BF16__ GGML_AMX_BF16)
        endif()
    elseif (GGML_AVX2)
        list(APPEND ARCH_FLAGS /arch:AVX2)
        list(APPEND ARCH_DEFINITIONS GGML_AVX2 GGML_FMA GGML_F16C)
    elseif (GGML_AVX)
        list(APPEND ARCH_FLAGS /arch:AVX)
        list(APPEND ARCH_DEFINITIONS GGML_AVX)
    elseif (GGML_SSE42)
        list(APPEND ARCH_FLAGS /arch:SSE4.2)
        list(APPEND ARCH_DEFINITIONS GGML_SSE42)
    endif ()
    if (GGML_AVX_VNNI)
        list(APPEND ARCH_DEFINITIONS __AVXVNNI__ GGML_AVX_VNNI)
    endif()
endif()
```

--------------------------------

TITLE: Mistral Tool Calling Template
DESCRIPTION: This Go template defines the structure for interacting with Mistral models that support tool calling. It handles user prompts, system messages, available tools, and assistant responses including tool calls.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_3

LANGUAGE: go
CODE:
```
{{- range $index, $_ := .Messages }}
{{- if eq .Role "user" }}
{{- if and (le (len (slice $.Messages $index)) 2) $.Tools }}[AVAILABLE_TOOLS] {{ json $.Tools }}[/AVAILABLE_TOOLS]
{{- end }}[INST] {{ if and (eq (len (slice $.Messages $index)) 1) $.System }}{{ $.System }}

{{ end }}{{ .Content }}[/INST]
{{- else if eq .Role "assistant" }}
{{- if .Content }} {{ .Content }}</s>
{{- else if .ToolCalls }}[TOOL_CALLS] [
{{- range .ToolCalls }}{"name": "{{ .Function.Name }}", "arguments": {{ json .Function.Arguments }}}}
{{- end }}]</s>
{{- end }}
{{- else if eq .Role "tool" }}[TOOL_RESULTS] {"content": {{ .Content }}}[/TOOL_RESULTS]
{{- end }}
{{- end }}

```

--------------------------------

TITLE: Checking CPU Features
DESCRIPTION: A command to display CPU flags, which can help in understanding which LLM libraries your system supports.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_2

LANGUAGE: shell
CODE:
```
cat /proc/cpuinfo| grep flags | head -1
```

--------------------------------

TITLE: Ollama API - Create Model
DESCRIPTION: This API endpoint is used to create new models in Ollama. It supports creating models from existing models, GGUF files, or Safetensors directories. Parameters include the model name, source model (optional), files, adapters, template, license, system prompt, model parameters, messages, and stream settings.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_45

LANGUAGE: APIDOC
CODE:
```
POST /api/create

Parameters:
- `model`: (string, required) name of the model to create
- `from`: (string, optional) name of an existing model to create the new model from
- `files`: (object, optional) a dictionary of file names to SHA256 digests of blobs to create the model from
- `adapters`: (object, optional) a dictionary of file names to SHA256 digests of blobs for LORA adapters
- `template`: (string, optional) the prompt template for the model
- `license`: (string or list, optional) the license or licenses for the model
- `system`: (string, optional) the system prompt for the model
- `parameters`: (object, optional) a dictionary of parameters for the model (see [Modelfile](./modelfile.md#valid-parameters-and-values) for a list of parameters)
- `messages`: (list, optional) a list of message objects used to create a conversation
- `stream`: (boolean, optional) if `false` the response will be returned as a single response object, rather than a stream of objects
- `quantize`: (string, optional) quantize a non-quantized (e.g. float16) model

Quantization Types:
| Type       | Recommended |
|------------|-------------|
| q4_K_M     | *           |
| q4_K_S     |             |
| q8_0       | *           |

Example Usage:
1. Create a new model from an existing model:
   ```shell
   curl http://localhost:11434/api/create -d '{ "model": "mario", "from": "llama3.2", "system": "You are Mario from Super Mario Bros." }'
   ```
   Response is a stream of JSON objects indicating status.

2. Quantize a model:
   ```shell
   curl http://localhost:11434/api/create -d '{ "model": "llama3.2:quantized", "from": "llama3.2:3b-instruct-fp16", "quantize": "q4_K_M" }'
   ```
   Response is a stream of JSON objects indicating quantization progress.

3. Create a model from a GGUF file:
   ```shell
   curl http://localhost:11434/api/create -d '{ "model": "my-gguf-model", "files": { "test.gguf": "sha256:432f310a77f4650a88d0fd59ecdd7cebed8d684bafea53cbff0473542964f0c3" } }'
   ```
   Requires pushing the GGUF file using `/api/blobs/:digest` first.

4. Create a model from a Safetensors directory:
   Requires pushing each file using `/api/blobs/:digest` first. Files are cached until server restart.
```

--------------------------------

TITLE: ggml Other Backend Registrations
DESCRIPTION: Registers various other hardware and compute backends for ggml, including BLAS, CANN, CUDA, HIP, Metal, Vulkan, and OpenCL, by calling the `ggml_add_backend` function.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_20

LANGUAGE: cmake
CODE:
```
ggml_add_backend(BLAS)
ggll_add_backend(CANN)
ggll_add_backend(CUDA)
ggll_add_backend(HIP)
ggll_add_backend(Kompute)
ggll_add_backend(METAL)
ggll_add_backend(MUSA)
ggll_add_backend(RPC)
ggll_add_backend(SYCL)
ggll_add_backend(Vulkan)
ggll_add_backend(OpenCL)
```

--------------------------------

TITLE: Common Target Include Directories and Compile Features
DESCRIPTION: Sets common include directories and compile features (C++17, C11) for the ggml-base and ggml targets.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_11

LANGUAGE: cmake
CODE:
```
foreach (target ggml-base ggml)
    target_include_directories(${target} PUBLIC    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include> $<INSTALL_INTERFACE:include>)
    target_compile_features   (${target} PRIVATE c_std_11 cxx_std_17) # don't bump
endforeach()
```

--------------------------------

TITLE: Ollama Chat Request with Reproducible Outputs
DESCRIPTION: Shows how to make a chat request with options for reproducible outputs, including seed and temperature settings.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_41

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    }
  ],
  "options": {
    "seed": 101,
    "temperature": 0
  }
}'
```

--------------------------------

TITLE: Generate Patches for Vendored Code
DESCRIPTION: A workflow for generating new patches when modifying vendored code. It ensures the tracking repository is clean, applies existing patches, and then formats new changes into patches.

SOURCE: https://github.com/ollama/ollama/blob/main/llama/README.md#_snippet_2

LANGUAGE: shell
CODE:
```
make -f Makefile.sync clean apply-patches
# Make changes in ./vendor/
# Create a branch, cherry-pick commit, submit PR to llama.cpp
make -f Makefile.sync format-patches
```

--------------------------------

TITLE: ggml Backend Registration Function
DESCRIPTION: A CMake function to register and include backend subdirectories. It sets compile definitions based on backend usage and prints status messages.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_17

LANGUAGE: cmake
CODE:
```
function(ggml_add_backend backend)
    string(TOUPPER "GGML_${backend}" backend_id)
    if (${backend_id})
        string(TOLOWER "ggml-${backend}" backend_target)
        add_subdirectory(${backend_target})
        message(STATUS "Including ${backend} backend")
        if (NOT GGML_BACKEND_DL)
            string(TOUPPER "GGML_USE_${backend}" backend_use)
            target_compile_definitions(ggml PUBLIC ${backend_use})
        endif()
    endif()
endfunction()
```

--------------------------------

TITLE: x86 Architecture Optimizations
DESCRIPTION: Configures compiler flags and definitions for x86 processors, enabling various instruction set extensions like SSE, AVX, FMA, BMI2, and AVX512 variants. It also handles MSVC-specific definitions for BMI2.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cpu/CMakeLists.txt#_snippet_5

LANGUAGE: cmake
CODE:
```
if (GGML_BMI2)
    # MSVC does not define macro __BMI2__
    list(APPEND ARCH_DEFINITIONS __BMI2__ GGML_BMI2)
endif()
else ()
    if (GGML_NATIVE)
        list(APPEND ARCH_FLAGS -march=native)
    else ()
        if (GGML_SSE42)
            list(APPEND ARCH_FLAGS -msse4.2)
            list(APPEND ARCH_DEFINITIONS GGML_SSE42)
        endif()
        if (GGML_F16C)
            list(APPEND ARCH_FLAGS -mf16c)
            list(APPEND ARCH_DEFINITIONS GGML_F16C)
        endif()
        if (GGML_FMA)
            list(APPEND ARCH_FLAGS -mfma)
            list(APPEND ARCH_DEFINITIONS GGML_FMA)
        endif()
        if (GGML_BMI2)
            list(APPEND ARCH_FLAGS -mbmi2)
            list(APPEND ARCH_DEFINITIONS GGML_BMI2)
        endif()
        if (GGML_AVX)
            list(APPEND ARCH_FLAGS -mavx)
            list(APPEND ARCH_DEFINITIONS GGML_AVX)
        endif()
        if (GGML_AVX2)
            list(APPEND ARCH_FLAGS -mavx2)
            list(APPEND ARCH_DEFINITIONS GGML_AVX2)
        endif()
        if (GGML_AVX_VNNI)
            list(APPEND ARCH_FLAGS -mavxvnni)
            list(APPEND ARCH_DEFINITIONS GGML_AVX_VNNI)
        endif()
        if (GGML_AVX512)
            list(APPEND ARCH_FLAGS -mavx512f)
            list(APPEND ARCH_FLAGS -mavx512cd)
            list(APPEND ARCH_FLAGS -mavx512vl)
            list(APPEND ARCH_FLAGS -mavx512dq)
            list(APPEND ARCH_FLAGS -mavx512bw)
            list(APPEND ARCH_DEFINITIONS GGML_AVX512)
        endif()
        if (GGML_AVX512_VBMI)
            list(APPEND ARCH_FLAGS -mavx512vbmi)
            list(APPEND ARCH_DEFINITIONS GGML_AVX512_VBMI)
        endif()
        if (GGML_AVX512_VNNI)
            list(APPEND ARCH_FLAGS -mavx512vnni)
            list(APPEND ARCH_DEFINITIONS GGML_AVX512_VNNI)
        endif()
        if (GGML_AVX512_BF16)
            list(APPEND ARCH_FLAGS -mavx512bf16)
            list(APPEND ARCH_DEFINITIONS GGML_AVX512_BF16)
        endif()
        if (GGML_AMX_TILE)
            list(APPEND ARCH_FLAGS -mamx-tile)
            list(APPEND ARCH_DEFINITIONS GGML_AMX_TILE)
        endif()
        if (GGML_AMX_INT8)
            list(APPEND ARCH_FLAGS -mamx-int8)
            list(APPEND ARCH_DEFINITIONS GGML_AMX_INT8)
        endif()
        if (GGML_AMX_BF16)
            list(APPEND ARCH_FLAGS -mamx-bf16)
            list(APPEND ARCH_DEFINITIONS GGML_AMX_BF16)
        endif()
    endif()
endif()
```

--------------------------------

TITLE: CUDA Build Flags Configuration
DESCRIPTION: Configures CUDA build flags based on compression mode, fatal warnings, and host compiler detection. It dynamically sets compiler options for optimal performance and compatibility.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cuda/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
if (GGML_USE_CUDA)
    # -speed (nvcc's default)
    # -balance
    # -size
    list(APPEND CUDA_FLAGS -compress-mode=${GGML_CUDA_COMPRESSION_MODE})
endif()

if (GGML_FATAL_WARNINGS)
    list(APPEND CUDA_FLAGS -Werror all-warnings)
endif()

if (GGML_ALL_WARNINGS AND NOT MSVC)
    set(NVCC_CMD ${CMAKE_CUDA_COMPILER} .c)
    if (NOT CMAKE_CUDA_HOST_COMPILER STREQUAL "")
        list(APPEND NVCC_CMD -ccbin ${CMAKE_CUDA_HOST_COMPILER})
    endif()

    execute_process(
        COMMAND ${NVCC_CMD} -Xcompiler --version
        OUTPUT_VARIABLE CUDA_CCFULLVER
        ERROR_QUIET
    )

    if (NOT CUDA_CCFULLVER MATCHES clang)
        set(CUDA_CCID "GNU")
        execute_process(
            COMMAND ${NVCC_CMD} -Xcompiler "-dumpfullversion -dumpversion"
            OUTPUT_VARIABLE CUDA_CCVER
            ERROR_QUIET
            OUTPUT_STRIP_TRAILING_WHITESPACE
        )
    else()
        if (CUDA_CCFULLVER MATCHES Apple)
            set(CUDA_CCID "AppleClang")
        else()
            set(CUDA_CCID "Clang")
        endif()
        string(REGEX REPLACE "^.* version ([0-9.]*).*$" "\1" CUDA_CCVER ${CUDA_CCFULLVER})
    endif()

    message(STATUS "CUDA host compiler is ${CUDA_CCID} ${CUDA_CCVER}")

    ggml_get_flags(${CUDA_CCID} ${CUDA_CCVER})
    list(APPEND CUDA_CXX_FLAGS ${CXX_FLAGS} ${GF_CXX_FLAGS})  # This is passed to -Xcompiler later
endif()

if (NOT MSVC)
    list(APPEND CUDA_CXX_FLAGS -Wno-pedantic)
endif()

list(JOIN   CUDA_CXX_FLAGS " " CUDA_CXX_FLAGS_JOINED)  # pass host compiler flags as a single argument

if (NOT CUDA_CXX_FLAGS_JOINED STREQUAL "")
    list(APPEND CUDA_FLAGS -Xcompiler ${CUDA_CXX_FLAGS_JOINED})
endif()

target_compile_options(ggml-cuda PRIVATE "<$<COMPILE_LANGUAGE:CUDA>:${CUDA_FLAGS}>")
else()
    message(FATAL_ERROR "CUDA Toolkit not found")
endif()
```

--------------------------------

TITLE: Generate Patches for Vendored Code
DESCRIPTION: Generates new patches for changes made in the `./vendor/` directory. This is part of the workflow for contributing fixes or features that impact vendored code.

SOURCE: https://github.com/ollama/ollama/blob/main/llama/README.md#_snippet_3

LANGUAGE: Shell
CODE:
```
make -f Makefile.sync format-patches
```

--------------------------------

TITLE: ggml CPU Backend Variant Function
DESCRIPTION: Defines a function to add CPU backend variants, enabling specific instruction sets (e.g., SSE4.2, AVX2, AVX512) for optimized performance. It manages feature flags and calls an implementation function.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_18

LANGUAGE: cmake
CODE:
```
function(ggml_add_cpu_backend_variant tag_name)
    set(GGML_CPU_TAG_NAME ${tag_name})
    # other: OPENMP LLAMAFILE CPU_HBM
    foreach (feat NATIVE
                  SSE42
                  AVX AVX2 BMI2 AVX_VNNI FMA F16C
                  AVX512 AVX512_VBMI AVX512_VNNI AVX512_BF16
                  AMX_TILE AMX_INT8 AMX_BF16)
        set(GGML_${feat} OFF)
    endforeach()

    foreach (feat ${ARGN})
        set(GGML_${feat} ON)
    endforeach()

    ggml_add_cpu_backend_variant_impl(${tag_name})
    add_dependencies(ggml-cpu ggml-cpu-${tag_name})
endfunction()
```

--------------------------------

TITLE: Generating Content with Ollama API (Shell)
DESCRIPTION: This `curl` command demonstrates how to make a POST request to the Ollama `/api/generate` endpoint. It specifies the `llava` model, a text prompt, disables streaming, and includes a base64-encoded image for multimodal generation. The `images` array expects base64-encoded image data.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_87

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llava",
  "prompt":"What is in this picture?",
  "stream": false,
  "images": ["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"'
}
```

--------------------------------

TITLE: Create Model
DESCRIPTION: Creates a new model on the Ollama server by providing model configuration and file digests. It returns a stream of status updates.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_46

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/create -d '{
  "model": "fred",
  "files": {
    "config.json": "sha256:dd3443e529fb2290423a0c65c2d633e67b419d273f170259e27297219828e389",
    "generation_config.json": "sha256:88effbb63300dbbc7390143fbbdd9d9fa50587b37e8bfd16c8c90d4970a74a36",
    "special_tokens_map.json": "sha256:b7455f0e8f00539108837bfa586c4fbf424e31f8717819a6798be74bef813d05",
    "tokenizer.json": "sha256:bbc1904d35169c542dffbe1f7589a5994ec7426d9e5b609d07bab876f32e97ab",
    "tokenizer_config.json": "sha256:24e8a6dc2547164b7002e3125f10b415105644fcf02bf9ad8b674c87b1eaaed6",
    "model.safetensors": "sha256:1ff795ff6a07e6a68085d206fb84417da2f083f68391c2843cd2b8ac6df8538f"
  }
}'
```

--------------------------------

TITLE: Accessing Ollama Server Logs
DESCRIPTION: Provides commands to view Ollama server logs on different operating systems (macOS, Linux with systemd, Docker containers, and Windows). Logs are crucial for diagnosing issues.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_0

LANGUAGE: shell
CODE:
```
cat ~/.ollama/logs/server.log
```

LANGUAGE: shell
CODE:
```
journalctl -u ollama --no-pager --follow --pager-end
```

LANGUAGE: shell
CODE:
```
docker logs <container-name>
```

LANGUAGE: powershell
CODE:
```
$env:OLLAMA_DEBUG="1"
& "ollama app.exe"
```

--------------------------------

TITLE: ggml CPU Backend Variant Function
DESCRIPTION: Defines a function to add CPU backend variants with specific instruction set features. It iterates through supported features and sets corresponding compile definitions.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_8

LANGUAGE: cmake
CODE:
```
function(ggml_add_cpu_backend_variant tag_name)
    set(GGML_CPU_TAG_NAME ${tag_name})
    # other: OPENMP LLAMAFILE CPU_HBM
    foreach (feat NATIVE
                  SSE42
                  AVX AVX2 BMI2 AVX_VNNI FMA F16C
                  AVX512 AVX512_VBMI AVX512_VNNI AVX512_BF16
                  AMX_TILE AMX_INT8 AMX_BF16)
        set(GGML_${feat} OFF)
    endforeach()

    foreach (feat ${ARGN})
        set(GGML_${feat} ON)
    endforeach()

    ggml_add_cpu_backend_variant_impl(${tag_name})
    add_dependencies(ggml-cpu ggml-cpu-${tag_name})
endfunction()
```

--------------------------------

TITLE: Configure Integration Tests for Existing Server
DESCRIPTION: Configure integration tests to run against an already running Ollama server. Set the OLLAMA_TEST_EXISTING environment variable to a non-empty string to enable this mode. This is useful for testing against remote or persistent server instances.

SOURCE: https://github.com/ollama/ollama/blob/main/integration/README.md#_snippet_1

LANGUAGE: bash
CODE:
```
export OLLAMA_TEST_EXISTING=true
```

--------------------------------

TITLE: ggml Backend Library Function
DESCRIPTION: A CMake function to add backend libraries, handling both shared (MODULE) and static library creation based on GGML_BACKEND_DL. It manages target properties, compile definitions, and dependencies.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_6

LANGUAGE: cmake
CODE:
```
function(ggml_add_backend_library backend)
    if (GGML_BACKEND_DL)
        add_library(${backend} MODULE ${ARGN})
        # write the shared library to the output directory
        set_target_properties(${backend} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_DL)
        add_dependencies(ggml ${backend})
    else()
        add_library(${backend} ${ARGN})
        target_link_libraries(ggml PUBLIC ${backend})
        install(TARGETS ${backend} LIBRARY)
    endif()

    target_link_libraries(${backend} PRIVATE ggml-base)
    target_include_directories(${backend} PRIVATE ..)

    if (${BUILD_SHARED_LIBS})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_BUILD)
        target_compile_definitions(${backend} PUBLIC  GGML_BACKEND_SHARED)
    endif()

    if(NOT GGML_AVAILABLE_BACKENDS)
        set(GGML_AVAILABLE_BACKENDS "${backend}"
            CACHE INTERNAL "List of backends for cmake package")
    else()
        list(FIND GGML_AVAILABLE_BACKENDS "${backend}" has_backend)
        if(has_backend EQUAL -1)
            set(GGML_AVAILABLE_BACKENDS "${GGML_AVAILABLE_BACKENDS};${backend}"
                CACHE INTERNAL "List of backends for cmake package")
        endif()
    endif()
endfunction()
```

--------------------------------

TITLE: Testing an Imported Model
DESCRIPTION: This shell command is used to run and test a model that has been successfully imported into Ollama. Replace 'my-model' with the name of the model you wish to test.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/import.md#_snippet_2

LANGUAGE: shell
CODE:
```
ollama run my-model
```

--------------------------------

TITLE: Ollama List Running Models API
DESCRIPTION: Provides the API endpoint to list models currently loaded in Ollama's memory. The response includes details about each model, such as its name, size, and configuration.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_53

LANGUAGE: APIDOC
CODE:
```
GET /api/ps
List models that are currently loaded into memory.
```

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/ps
```

LANGUAGE: json
CODE:
```
{
  "models": [
    {
      "name": "mistral:latest",
      "model": "mistral:latest",
      "size": 5137025024,
      "digest": "2ae6f6dd7a3dd734790bbbf58b8909a606e0e7e97e94b7604e0aa7ae4490e6d8",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7.2B",
        "quantization_level": "Q4_0"
      },
      "expires_at": "2024-06-04T14:38:31.83753-07:00",
      "size_vram": 5137025024
    }
  ]
}
```

--------------------------------

TITLE: Ollama Load Model
DESCRIPTION: Demonstrates how to load a model into memory by sending a chat request with an empty messages array.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_43

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": []
}'
```

--------------------------------

TITLE: Platform-Specific Preprocessor Definitions
DESCRIPTION: This snippet demonstrates how CMake is used to define preprocessor macros tailored to specific operating systems. It includes definitions for GNU extensions on Linux and Android, Darwin extensions for macOS and iOS, BSD extensions for FreeBSD, NetBSD, and OpenBSD, and security-related definitions for Windows.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_3

LANGUAGE: cmake
CODE:
```
if (CMAKE_SYSTEM_NAME MATCHES "Linux" OR CMAKE_SYSTEM_NAME MATCHES "Android")
    add_compile_definitions(_GNU_SOURCE)
endif()

if (
    CMAKE_SYSTEM_NAME MATCHES "Darwin" OR
    CMAKE_SYSTEM_NAME MATCHES "iOS"    OR
    CMAKE_SYSTEM_NAME MATCHES "tvOS"   OR
    CMAKE_SYSTEM_NAME MATCHES "DragonFly"
)
    add_compile_definitions(_DARWIN_C_SOURCE)
endif()

if (CMAKE_SYSTEM_NAME MATCHES "FreeBSD")
    add_compile_definitions(__BSD_VISIBLE)
endif()
if (CMAKE_SYSTEM_NAME MATCHES "NetBSD")
    add_compile_definitions(_NETBSD_SOURCE)
endif()
if (CMAKE_SYSTEM_NAME MATCHES "OpenBSD")
    add_compile_definitions(_BSD_SOURCE)
endif()

if (WIN32)
    add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
endif()
```

--------------------------------

TITLE: Configure Ollama Docker with Proxy and CA Certificate
DESCRIPTION: This snippet shows how to build a Docker image for Ollama that includes a custom CA certificate and configures it to use an HTTPS proxy. This is useful when Ollama needs to connect to external services through a secure proxy.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_5

LANGUAGE: dockerfile
CODE:
```
FROM ollama/ollama
COPY my-ca.pem /usr/local/share/ca-certificates/my-ca.crt
RUN update-ca-certificates
```

--------------------------------

TITLE: Ollama API Reference
DESCRIPTION: This section provides a comprehensive reference for the Ollama API endpoints. It covers model generation, chat completions, model management (create, list, show, copy, delete, pull, push), embeddings, running models, and version information. It also details API conventions regarding model names, durations, and streaming responses.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_0

LANGUAGE: APIDOC
CODE:
```
Project: /ollama/ollama

API Endpoints:
- Generate a completion: POST /api/generate
- Generate a chat completion: POST /api/chat
- Create a Model: POST /api/create
- List Local Models: GET /api/tags
- Show Model Information: POST /api/show
- Copy a Model: POST /api/copy
- Delete a Model: DELETE /api/delete
- Pull a Model: POST /api/pull
- Push a Model: POST /api/push
- Generate Embeddings: POST /api/embeddings
- List Running Models: GET /api/ps
- Version: GET /

API Conventions:
- Model Names: Follow `model:tag` format (e.g., `orca-mini:3b-q8_0`, `llama3:70b`). Tag defaults to `latest` if not provided.
- Durations: All durations are returned in nanoseconds.
- Streaming Responses: Certain endpoints stream responses as JSON objects. Streaming can be disabled by providing `{"stream": false}`.

Generate a completion:
  POST /api/generate
  Generates a response for a given prompt with a provided model. This is a streaming endpoint.
  Parameters:
    - model: (required) the [model name](#model-names)
    - prompt: the prompt to generate a response for
    - suffix: the text after the model response
    - images: (optional) a list of base64-encoded images (for multimodal models)
    - think: (for thinking models) should the model think before responding?
  Advanced parameters (optional):
    - format: the format to return a response in. Format can be `json` or a JSON schema.
    - options: additional model parameters (e.g., `temperature`). See [Modelfile documentation](./modelfile.md#valid-parameters-and-values).
    - system: system message to override `Modelfile` system message.
    - template: prompt template to use (overrides `Modelfile` template).
    - stream: if `false`, the response will be returned as a single object, rather than a stream.
    - raw: if `true`, no formatting will be applied to the prompt.
    - keep_alive: controls how long the model stays loaded (default: `5m`).
    - context (deprecated): context returned from a previous `/generate` request.
  Structured outputs: Supported by providing a JSON schema in the `format` parameter.
  JSON mode: Enable by setting `format` to `json`. Instruct the model to use JSON in the prompt.

  Examples:
    Generate request (Streaming):
      Request:
        curl http://localhost:11434/api/generate -d '{ "model": "llama3.2", "prompt": "Why is the sky blue?" }'
      Response:
        A stream of JSON objects is returned:
        {
          "model": "llama3.2",
          "created_at": "2023-08-04T08:52:19.385406455-07:00",
          "response": "The",
          "done": false
        }
        The final response includes statistics:
        - total_duration: time spent generating the response
        - load_duration: time spent loading the model
        - prompt_eval_count: number of tokens in the prompt
        - prompt_eval_duration: time spent evaluating the prompt
        - eval_count: number of tokens in the response
        - eval_duration: time spent generating the response
        - context: encoding of the conversation for memory
        - response: empty if streamed, otherwise the full response
        To calculate token/s: `eval_count` / `eval_duration` * `10^9`.
        {
          "model": "llama3.2",
          "created_at": "2023-08-04T19:22:45.499127Z",
          "response": "",
          "done": true,
          "context": [1, 2, 3],
          "total_duration": 10706818083,
          "load_duration": 6338219291,
          "prompt_eval_count": 26,
          "prompt_eval_duration": 130079000,
          "eval_count": 259,
          "eval_duration": 4232710000
        }

    Request (No streaming):
      A response can be received in one reply when streaming is off.
      Request:
        curl http://localhost:11434/api/generate -d '{ "model": "llama3.2", "prompt": "Why is the sky blue?", "stream": false }'

```

--------------------------------

TITLE: Tunnel Ollama with Ngrok
DESCRIPTION: This command uses ngrok to create a secure public URL for your local Ollama instance, making it accessible over the internet. It specifies the host header to ensure correct routing.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_8

LANGUAGE: shell
CODE:
```
ngrok http 11434 --host-header="localhost:11434"
```

--------------------------------

TITLE: Load a Model
DESCRIPTION: Loads a model into memory by providing an empty prompt. This is useful for pre-loading models before making generation requests.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_18

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2"
}'
```

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-12-18T19:52:07.071755Z",
  "response": "",
  "done": true
}
```

--------------------------------

TITLE: Setting K/V Cache Quantization Type
DESCRIPTION: Configure the quantization type for the K/V context cache to manage memory usage, especially when Flash Attention is enabled. Options include f16, q8_0, and q4_0.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_20

LANGUAGE: APIDOC
CODE:
```
OLLAMA_KV_CACHE_TYPE
  Description: Specifies the quantization type for the K/V cache.
  Default: 'f16' (high precision, high memory usage).
  Available Options:
    - f16: High precision and memory usage (default).
    - q8_0: 8-bit quantization, uses approximately 1/2 the memory of f16 with minimal precision loss.
    - q4_0: 4-bit quantization, uses approximately 1/4 the memory of f16 with a small-medium loss in precision.
```

--------------------------------

TITLE: Configure Ollama to Allow Additional Web Origins
DESCRIPTION: This command demonstrates how to set the OLLAMA_ORIGINS environment variable to allow cross-origin requests from specific origins, including all browser extensions. This is necessary for web applications or browser extensions to interact with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_10

LANGUAGE: shell
CODE:
```
# Allow all Chrome, Firefox, and Safari extensions
OLLAMA_ORIGINS=chrome-extension://*,moz-extension://*,safari-web-extension://* ollama serve
```

--------------------------------

TITLE: Ollama CMake Configuration
DESCRIPTION: Core CMake configuration for the Ollama project. Sets the minimum CMake version, project name, build type, shared library settings, C++ standards, and extensions. It also configures GGML build options, including backend support (DL, Shared), caching, and specific features like LlamaFile and CUDA optimizations.

SOURCE: https://github.com/ollama/ollama/blob/main/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
cmake_minimum_required(VERSION 3.21)

project(Ollama C CXX)

include(CheckLanguage)

find_package(Threads REQUIRED)

set(CMAKE_BUILD_TYPE Release)
set(BUILD_SHARED_LIBS ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(GGML_BUILD ON)
set(GGML_SHARED ON)
set(GGML_CCACHE ON)
set(GGML_BACKEND_DL ON)
set(GGML_BACKEND_SHARED ON)
set(GGML_SCHED_MAX_COPIES 4)

set(GGML_LLAMAFILE ON)
set(GGML_CUDA_PEER_MAX_BATCH_SIZE 128)
set(GGML_CUDA_GRAPHS ON)
set(GGML_CUDA_FA ON)
set(GGML_CUDA_COMPRESSION_MODE default)

if((CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_OSX_ARCHITECTURES MATCHES "arm64")
    OR (NOT CMAKE_OSX_ARCHITECTURES AND NOT CMAKE_SYSTEM_PROCESSOR MATCHES "arm|aarch64|ARM64|ARMv[0-9]+_))
    set(GGML_CPU_ALL_VARIANTS ON)
endif()

if (CMAKE_OSX_ARCHITECTURES MATCHES "x86_64")
    set(CMAKE_BUILD_RPATH "@loader_path")
    set(CMAKE_INSTALL_RPATH "@loader_path")
endif()

set(OLLAMA_BUILD_DIR ${CMAKE_BINARY_DIR}/lib/ollama)
set(OLLAMA_INSTALL_DIR ${CMAKE_INSTALL_PREFIX}/lib/ollama)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY         ${OLLAMA_BUILD_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG   ${OLLAMA_BUILD_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${OLLAMA_BUILD_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY         ${OLLAMA_BUILD_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG   ${OLLAMA_BUILD_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${OLLAMA_BUILD_DIR})

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src/ggml-cpu)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src/ggml-cpu/amx)

add_compile_definitions(NDEBUG)

set(GGML_CPU ON)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/ml/backend/ggml/ggml/src)
set_property(TARGET ggml PROPERTY EXCLUDE_FROM_ALL TRUE)

get_target_property(CPU_VARIANTS ggml-cpu MANUALLY_ADDED_DEPENDENCIES)
if(NOT CPU_VARIANTS)
    set(CPU_VARIANTS "ggml-cpu")
endif()

install(TARGETS ggml-base ${CPU_VARIANTS}
    RUNTIME_DEPENDENCIES
        PRE_EXCLUDE_REGEXES ".*"
    RUNTIME DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT CPU
    LIBRARY DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT CPU
    FRAMEWORK DESTINATION ${OLLAMA_INSTALL_DIR} COMPONENT CPU
)
```

--------------------------------

TITLE: ggml Main Library Definition and Linking
DESCRIPTION: Defines the main ggml library, linking it with the base library and conditionally with the dl library on Linux. It also handles linking backend libraries.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_5

LANGUAGE: cmake
CODE:
```
add_library(ggml
            ggml-backend-reg.cpp)

target_link_libraries(ggml PUBLIC ggml-base)

if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_libraries(ggml PRIVATE dl)
endif()
```

--------------------------------

TITLE: ggml Backend Library Function
DESCRIPTION: A CMake function to add backend libraries, supporting both MODULE (shared) and static library types based on `GGML_BACKEND_DL`. It manages compile definitions, output directories, and dependencies.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_16

LANGUAGE: cmake
CODE:
```
function(ggml_add_backend_library backend)
    if (GGML_BACKEND_DL)
        add_library(${backend} MODULE ${ARGN})
        # write the shared library to the output directory
        set_target_properties(${backend} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_DL)
        add_dependencies(ggml ${backend})
    else()
        add_library(${backend} ${ARGN})
        target_link_libraries(ggml PUBLIC ${backend})
        install(TARGETS ${backend} LIBRARY)
    endif()

    target_link_libraries(${backend} PRIVATE ggml-base)
    target_include_directories(${backend} PRIVATE ..)

    if (${BUILD_SHARED_LIBS})
        target_compile_definitions(${backend} PRIVATE GGML_BACKEND_BUILD)
        target_compile_definitions(${backend} PUBLIC  GGML_BACKEND_SHARED)
    endif()

    if(NOT GGML_AVAILABLE_BACKENDS)
        set(GGML_AVAILABLE_BACKENDS "${backend}"
            CACHE INTERNAL "List of backends for cmake package")
    else()
        list(FIND GGML_AVAILABLE_BACKENDS "${backend}" has_backend)
        if(has_backend EQUAL -1)
            set(GGML_AVAILABLE_BACKENDS "${GGML_AVAILABLE_BACKENDS};${backend}"
                CACHE INTERNAL "List of backends for cmake package")
        endif()
    endif()
endfunction()
```

--------------------------------

TITLE: Ollama JavaScript Library: Chat with Turbo
DESCRIPTION: This TypeScript code illustrates how to use the Ollama JavaScript library to perform chat operations with a Turbo-enabled model. It covers client initialization with an API key and streaming chat responses.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/turbo.md#_snippet_2

LANGUAGE: typescript
CODE:
```
import { Ollama } from 'ollama';

const ollama = new Ollama({
  host: 'https://ollama.com',
  headers: {
	  Authorization: "Bearer <api key>"
  }
});

const response = await ollama.chat({
  model: 'gpt-oss:120b',
  messages: [{ role: 'user', content: 'Explain quantum computing' }],
  stream: true
});

for await (const part of response) {
    process.stdout.write(part.message.content)
}
```

--------------------------------

TITLE: Update Vendored llama.cpp Base Commit
DESCRIPTION: Instructions for updating the base commit of the vendored llama.cpp repository. This involves modifying `FETCH_HEAD` and resolving potential patch conflicts.

SOURCE: https://github.com/ollama/ollama/blob/main/llama/README.md#_snippet_1

LANGUAGE: shell
CODE:
```
make -f Makefile.sync apply-patches
# Resolve conflicts in ./vendor/ if any
git am --continue
make -f Makefile.sync format-patches sync
```

--------------------------------

TITLE: HIP Compile Definitions
DESCRIPTION: Sets various compile definitions to enable or disable specific HIP features and configurations.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_8

LANGUAGE: cmake
CODE:
```
# TODO: do not use CUDA definitions for HIP
if (NOT GGML_BACKEND_DL)
    target_compile_definitions(ggml PUBLIC GGML_USE_CUDA)
endif()

add_compile_definitions(GGML_USE_HIP)

if (GGML_CUDA_FORCE_MMQ)
    add_compile_definitions(GGML_CUDA_FORCE_MMQ)
endif()

if (GGML_CUDA_FORCE_CUBLAS)
    add_compile_definitions(GGML_CUDA_FORCE_CUBLAS)
endif()

if (GGML_CUDA_NO_PEER_COPY)
    add_compile_definitions(GGML_CUDA_NO_PEER_COPY)
endif()

if (GGML_HIP_GRAPHS)
    add_compile_definitions(GGML_HIP_GRAPHS)
endif()

if (GGML_HIP_NO_VMM)
    add_compile_definitions(GGML_HIP_NO_VMM)
endif()

if (GGML_HIP_ROCWMMA_FATTN)
    add_compile_definitions(GGML_HIP_ROCWMMA_FATTN)
endif()

if (NOT GGML_CUDA_FA)
    add_compile_definitions(GGML_CUDA_NO_FA)
endif()
```

--------------------------------

TITLE: Chat Completions API
DESCRIPTION: This section details the `/v1/chat/completions` endpoint for interacting with chat models. It supports text-based conversations and can be extended for multimodal inputs.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_12

LANGUAGE: APIDOC
CODE:
```
POST /v1/chat/completions

Description:
  Sends a request to the Ollama chat completions API to generate a response from a language model.

Request Body:
  application/json
  {
    "model": "string",
    "messages": [
      {
        "role": "string",
        "content": "string" | [{"type": "text", "text": "string"} | {"type": "image_url", "image_url": {"url": "string"}}]
      }
    ],
    "stream": "boolean",
    "options": {},
    "template": "string",
    "context": ["integer"],
    "keep_alive": "string"
  }

Parameters:
  model (string, required): The name of the model to use for the chat completion.
  messages (array of objects, required): An array of message objects representing the conversation history.
    role (string, required): The role of the author of the message (e.g., "system", "user", "assistant").
    content (string | array of objects, required): The content of the message. Can be a string for text or an array for multimodal content.
      type (string): The type of content (e.g., "text", "image_url").
      text (string): The text content of the message.
      image_url (object): An object containing the URL of the image.
        url (string, required): The URL of the image. Can be a data URL.
  stream (boolean, optional): Whether to stream the response. Defaults to false.
  options (object, optional): Additional model-specific options.
  template (string, optional): A prompt template to use for the chat completion.
  context (array of integers, optional): The context from a previous response to continue the conversation.
  keep_alive (string, optional): How long to keep the model in memory.

Response:
  (object): The chat completion response from the model.
    model (string): The model that generated the response.
    created_at (string): The timestamp when the response was created.
    response (object):
      content (string): The content of the assistant's message.
    done (boolean): Indicates if the response is the final one.
    context (array of integers): The context for the next turn.
    total_duration (integer): The total time in nanoseconds it took to generate the response.
    load_duration (integer): The time in nanoseconds it took to load the model.
    prompt_eval_count (integer): The number of tokens in the prompt.
    eval_count (integer): The number of tokens in the response.
    nested_eval_count (integer): The number of tokens in nested responses.

Example:
  curl http://localhost:11434/v1/chat/completions \
      -H "Content-Type: application/json" \
      -d '{ "model": "llama3.2", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}] }'

Example with Image:
  curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{ "model": "llava", "messages": [{"role": "user", "content": [{"type": "text", "text": "What's in this image?"}, {"type": "image_url", "image_url": {"url": "data:image/png;base64,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"}}]}'
        }
      ]
    }
  ]
}
```
```

--------------------------------

TITLE: Disabling Ollama Auto-Startup on macOS
DESCRIPTION: Instructions for disabling Ollama's automatic startup on macOS, covering different versions of the operating system.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_22

LANGUAGE: APIDOC
CODE:
```
macOS Login Item Management
  Description: Disable Ollama from starting automatically on macOS.
  macOS Monterey (v12):
    - Navigate to System Settings -> Users & Groups -> Login Items.
    - Select the 'Ollama' entry and click the '-' (minus) button to remove it.
  macOS Ventura (v13) and later:
    - Open System Settings and search for 'Login Items'.
    - Locate 'Ollama' under 'Allow in the Background'.
    - Click the slider to disable it.
```

--------------------------------

TITLE: Android Specific Linking
DESCRIPTION: Links the 'dl' library for ggml-base on Android systems.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_13

LANGUAGE: cmake
CODE:
```
if (CMAKE_SYSTEM_NAME MATCHES "Android")
    target_link_libraries(ggml-base PRIVATE dl)
endif()
```

--------------------------------

TITLE: Completions API
DESCRIPTION: Provides text completion functionality, supporting streaming, JSON mode, and reproducible outputs. It outlines the supported request fields for completions.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
/v1/completions

Supported features:
- Completions
- Streaming
- JSON mode
- Reproducible outputs
- Logprobs

Supported request fields:
- model
- prompt
- frequency_penalty
- presence_penalty
- seed
- stop
- stream
- stream_options
  - include_usage
- temperature
- top_p
- max_tokens
- suffix
- best_of
- echo
- logit_bias
- user
- n

Notes:
- `prompt` currently only accepts a string
```

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/v1/completions \
    -H "Content-Type: application/json" \
    -d '{ \
        "model": "llama3.2", \
        "prompt": "Say this is a test" \
    }'
```

--------------------------------

TITLE: HIP Source File Language Setting
DESCRIPTION: Sets the language for HIP source files to CXX if hipcc is used, otherwise to HIP.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_9

LANGUAGE: cmake
CODE:
```
if (CXX_IS_HIPCC)
    set_source_files_properties(${GGML_SOURCES_ROCM} PROPERTIES LANGUAGE CXX)
    target_link_libraries(ggml-hip PRIVATE hip::device)
else()
    set_source_files_properties(${GGML_SOURCES_ROCM} PROPERTIES LANGUAGE HIP)
endif()
```

--------------------------------

TITLE: Forcing LLM Library Selection
DESCRIPTION: Demonstrates how to override Ollama's automatic LLM library detection by setting the `OLLAMA_LLM_LIBRARY` environment variable. This is useful for compatibility or performance tuning.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_1

LANGUAGE: shell
CODE:
```
OLLAMA_LLM_LIBRARY="cpu_avx2" ollama serve
```

--------------------------------

TITLE: Ollama Chat Request with Tools
DESCRIPTION: Illustrates a chat request that utilizes tools, defining a function `get_current_weather` with parameters for location and format.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_42

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "What is the weather today in Paris?"
    }
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The location to get the weather for, e.g. San Francisco, CA"
            },
            "format": {
              "type": "string",
              "description": "The format to return the weather in, e.g. 'celsius' or 'fahrenheit'",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location", "format"]
        }
      }
    }
  ]
}'
```

--------------------------------

TITLE: rocWMMA Header Check
DESCRIPTION: Checks for the presence of the rocWMMA header file if the GGML_HIP_ROCWMMA_FATTN option is enabled.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_4

LANGUAGE: cmake
CODE:
```
if (GGML_HIP_ROCWMMA_FATTN)
    CHECK_INCLUDE_FILE_CXX("rocwmma/rocwmma.hpp" FOUND_ROCWMMA)
    if (NOT ${FOUND_ROCWMMA})
        message(FATAL_ERROR "rocwmma has not been found")
    endif()
endif()
```

--------------------------------

TITLE: Ollama API Endpoints
DESCRIPTION: Provides documentation for various Ollama API endpoints, including checking blob existence, pushing blobs, listing local models, and showing model information.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_47

LANGUAGE: APIDOC
CODE:
```
API Documentation:

Check if a Blob Exists:
  Method: HEAD
  Endpoint: /api/blobs/:digest
  Description: Ensures that the file blob (Binary Large Object) used with create a model exists on the server. This checks your Ollama server and not ollama.com.
  Query Parameters:
    - digest: the SHA256 digest of the blob
  Responses:
    - 200 OK: if the blob exists
    - 404 Not Found: if it does not
  Example Request:
    curl -I http://localhost:11434/api/blobs/sha256:29fdb92e57cf0827ded04ae6461b5931d01fa595843f55d36f5b275a52087dd2

Push a Blob:
  Method: POST
  Endpoint: /api/blobs/:digest
  Description: Push a file to the Ollama server to create a "blob" (Binary Large Object).
  Query Parameters:
    - digest: the expected SHA256 digest of the file
  Responses:
    - 201 Created: if the blob was successfully created
    - 400 Bad Request: if the digest used is not expected
  Example Request:
    curl -T model.gguf -X POST http://localhost:11434/api/blobs/sha256:29fdb92e57cf0827ded04ae6461b5931d01fa595843f55d36f5b275a52087dd2

List Local Models:
  Method: GET
  Endpoint: /api/tags
  Description: List models that are available locally.
  Response:
    A single JSON object containing a list of models with their details.
  Example Request:
    curl http://localhost:11434/api/tags
  Example Response:
    {
      "models": [
        {
          "name": "deepseek-r1:latest",
          "model": "deepseek-r1:latest",
          "modified_at": "2025-05-10T08:06:48.639712648-07:00",
          "size": 4683075271,
          "digest": "0a8c266910232fd3291e71e5ba1e058cc5af9d411192cf88b6d30e92b6e73163",
          "details": {
            "parent_model": "",
            "format": "gguf",
            "family": "qwen2",
            "families": [
              "qwen2"
            ],
            "parameter_size": "7.6B",
            "quantization_level": "Q4_K_M"
          }
        },
        {
          "name": "llama3.2:latest",
          "model": "llama3.2:latest",
          "modified_at": "2025-05-04T17:37:44.706015396-07:00",
          "size": 2019393189,
          "digest": "a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72",
          "details": {
            "parent_model": "",
            "format": "gguf",
            "family": "llama",
            "families": [
              "llama"
            ],
            "parameter_size": "3.2B",
            "quantization_level": "Q4_K_M"
          }
        }
      ]
    }

Show Model Information:
  Method: POST
  Endpoint: /api/show
  Description: Show information about a model including details, modelfile, template, parameters, license, system prompt.
  Parameters:
    - model: name of the model to show
    - verbose: (optional) if set to `true`, returns full data for verbose response fields
  Example Request:
    curl http://localhost:11434/api/show -d '{
      "model": "llava"
    }'
```

--------------------------------

TITLE: CodeLlama Fill-in-Middle Template
DESCRIPTION: This Go template demonstrates how to configure models for fill-in-middle functionality, specifically for CodeLlama models. It uses `<PRE>`, `<SUF>`, and `<MID>` tokens to indicate the preceding text, suffix, and the middle part to be generated.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/template.md#_snippet_4

LANGUAGE: go
CODE:
```
<PRE> {{ .Prompt }} <SUF>{{ .Suffix }} <MID> 
```

--------------------------------

TITLE: LICENSE Instruction
DESCRIPTION: The LICENSE instruction specifies the legal license under which the model is shared or distributed. The license text is provided within triple quotes.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/modelfile.md#_snippet_9

LANGUAGE: APIDOC
CODE:
```
LICENSE """
<license text>
"""
  - Specifies the legal license for the model.
```

--------------------------------

TITLE: Compiler Flags and Sanitizers
DESCRIPTION: Configures compiler flags and enables various sanitizers (thread, address, undefined) for debug builds. It also handles fatal warnings and general warning flags for different compilers (GNU, Clang, MSVC).

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
include(CheckCXXCompilerFlag)
include("../cmake/common.cmake")

add_compile_definitions(GGML_SCHED_MAX_COPIES=${GGML_SCHED_MAX_COPIES})

# enable libstdc++ assertions for debug builds
if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    add_compile_definitions($<$<CONFIG:Debug>:_GLIBCXX_ASSERTIONS>)
endif()

if (NOT MSVC)
    if (GGML_SANITIZE_THREAD)
        add_compile_options(-fsanitize=thread)
        link_libraries     (-fsanitize=thread)
    endif()

    if (GGML_SANITIZE_ADDRESS)
        add_compile_options(-fsanitize=address -fno-omit-frame-pointer)
        link_libraries     (-fsanitize=address)
    endif()

    if (GGML_SANITIZE_UNDEFINED)
        add_compile_options(-fsanitize=undefined)
        link_libraries     (-fsanitize=undefined)
    endif()
endif()

if (GGML_FATAL_WARNINGS)
    if (CMAKE_CXX_COMPILER_ID MATCHES "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
        list(APPEND C_FLAGS   -Werror)
        list(APPEND CXX_FLAGS -Werror)
    elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
        add_compile_options(/WX)
    endif()
endif()

if (GGML_ALL_WARNINGS)
    if (NOT MSVC)
        list(APPEND WARNING_FLAGS -Wall -Wextra -Wpedantic -Wcast-qual -Wno-unused-function)
        list(APPEND C_FLAGS       -Wshadow -Wstrict-prototypes -Wpointer-arith -Wmissing-prototypes
                                  -Werror=implicit-int -Werror=implicit-function-declaration)
        list(APPEND CXX_FLAGS     -Wmissing-declarations -Wmissing-noreturn)

        list(APPEND C_FLAGS   ${WARNING_FLAGS})
        list(APPEND CXX_FLAGS ${WARNING_FLAGS})

        ggml_get_flags(${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION})

        add_compile_options("$<$<COMPILE_LANGUAGE:C>:${C_FLAGS};${GF_C_FLAGS}>"
                            "$<$<COMPILE_LANGUAGE:CXX>:${CXX_FLAGS};${GF_CXX_FLAGS}>")
    else()
        # todo : msvc
        set(C_FLAGS   "")
        set(CXX_FLAGS "")
    endif()
endif()
```

--------------------------------

TITLE: Tunnel Ollama with Cloudflare Tunnel
DESCRIPTION: This command configures Cloudflare Tunnel to expose your local Ollama instance. It uses the `--url` flag to specify the local Ollama service and `--http-host-header` for correct host forwarding.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_9

LANGUAGE: shell
CODE:
```
cloudflared tunnel --url http://localhost:11434 --http-host-header="localhost:11434"
```

--------------------------------

TITLE: Ollama API: Manifest for 'smol' model
DESCRIPTION: This entry details the Docker v2 manifest for the 'smol' model in the Ollama library. It specifies the schema version, media type, configuration details, and layers including model and config blob digests and sizes.

SOURCE: https://github.com/ollama/ollama/blob/main/server/internal/registry/testdata/registry.txt#_snippet_0

LANGUAGE: APIDOC
CODE:
```
GET /v2/library/smol/manifests/latest

Response Body:
{
  "schemaVersion": 2,
  "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
  "config": {
    "mediaType": "application/vnd.docker.container.image.v1+json",
    "digest": "sha256:ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356",
    "size": 3
  },
  "layers": [
    {
      "mediaType": "application/vnd.ollama.image.model",
      "digest": "sha256:68e0ec597aee59d35f8dc44942d7b17d471ade10d3aca07a5bb7177713950312",
      "size": 5
    }
  ]
}
```

--------------------------------

TITLE: Ollama Model Configuration (JSON5)
DESCRIPTION: This JSON5 snippet represents the configuration and details of an Ollama model, including its Modelfile content, parameters, template, and detailed model information such as architecture, file type, parameter count, and tokenizer settings.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_50

LANGUAGE: JSON
CODE:
```
{
  "modelfile": "# Modelfile generated by \"ollama show\"\n# To build a new Modelfile based on this one, replace the FROM line with:\n# FROM llava:latest\n\nFROM /Users/matt/.ollama/models/blobs/sha256:200765e1283640ffbd013184bf496e261032fa75b99498a9613be4e94d63ad52\nTEMPLATE \"\"\"{{ .System }}\nUSER: {{ .Prompt }}\nASSISTANT: \"\"\nPARAMETER num_ctx 4096\nPARAMETER stop \"\u003c/s\u003e\"\nPARAMETER stop \"USER:\"\nPARAMETER stop \"ASSISTANT:\"",
  "parameters": "num_keep                       24\nstop                           \"<|start_header_id|>\"\nstop                           \"<|end_header_id|>\"\nstop                           \"<|eot_id|>",
  "template": "{{ if .System }}<|start_header_id|>system<|end_header_id|>\n\n{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>\n\n{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>\n\n{{ .Response }}<|eot_id|>",
  "details": {
    "parent_model": "",
    "format": "gguf",
    "family": "llama",
    "families": [
      "llama"
    ],
    "parameter_size": "8.0B",
    "quantization_level": "Q4_0"
  },
  "model_info": {
    "general.architecture": "llama",
    "general.file_type": 2,
    "general.parameter_count": 8030261248,
    "general.quantization_version": 2,
    "llama.attention.head_count": 32,
    "llama.attention.head_count_kv": 8,
    "llama.attention.layer_norm_rms_epsilon": 0.00001,
    "llama.block_count": 32,
    "llama.context_length": 8192,
    "llama.embedding_length": 4096,
    "llama.feed_forward_length": 14336,
    "llama.rope.dimension_count": 128,
    "llama.rope.freq_base": 500000,
    "llama.vocab_size": 128256,
    "tokenizer.ggml.bos_token_id": 128000,
    "tokenizer.ggml.eos_token_id": 128009,
    "tokenizer.ggml.merges": [],
    "tokenizer.ggml.model": "gpt2",
    "tokenizer.ggml.pre": "llama-bpe",
    "tokenizer.ggml.token_type": [],
    "tokenizer.ggml.tokens": []
  },
  "capabilities": [
    "completion",
    "vision"
  ]
}
```

--------------------------------

TITLE: Nvidia GPU Compatibility
DESCRIPTION: Lists Nvidia GPUs supported by Ollama, categorized by compute capability and family. Includes a link to check compute compatibility and notes on driver version requirements.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_0

LANGUAGE: markdown
CODE:
```
## Nvidia
Ollama supports Nvidia GPUs with compute capability 5.0+ and driver version 531 and newer.

Check your compute compatibility to see if your card is supported:
[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)

| Compute Capability | Family              | Cards                                                                                                       |
| ------------------ | ------------------- | ----------------------------------------------------------------------------------------------------------- |
| 12.0               | GeForce RTX 50xx    | `RTX 5060` `RTX 5060 Ti` `RTX 5070` `RTX 5070 Ti` `RTX 5080` `RTX 5090`                                     |
|                    | NVIDIA Professioal  | `RTX PRO 4000 Blackwell` `RTX PRO 4500 Blackwell` `RTX PRO 5000 Blackwell` `RTX PRO 6000 Blackwell`         |
| 9.0                | NVIDIA              | `H200` `H100`                                                                                               |
| 8.9                | GeForce RTX 40xx    | `RTX 4090` `RTX 4080 SUPER` `RTX 4080` `RTX 4070 Ti SUPER` `RTX 4070 Ti` `RTX 4070 SUPER` `RTX 4070` `RTX 4060 Ti` `RTX 4060`  |
|                    | NVIDIA Professional | `L4` `L40` `RTX 6000`                                                                                       |
| 8.6                | GeForce RTX 30xx    | `RTX 3090 Ti` `RTX 3090` `RTX 3080 Ti` `RTX 3080` `RTX 3070 Ti` `RTX 3070` `RTX 3060 Ti` `RTX 3060` `RTX 3050 Ti` `RTX 3050`   |
|                    | NVIDIA Professional | `A40` `RTX A6000` `RTX A5000` `RTX A4000` `RTX A3000` `RTX A2000` `A10` `A16` `A2`                          |
| 8.0                | NVIDIA              | `A100` `A30`                                                                                                |
| 7.5                | GeForce GTX/RTX     | `GTX 1650 Ti` `TITAN RTX` `RTX 2080 Ti` `RTX 2080` `RTX 2070` `RTX 2060`                                    |
|                    | NVIDIA Professional | `T4` `RTX 5000` `RTX 4000` `RTX 3000` `T2000` `T1200` `T1000` `T600` `T500`                                 |
|                    | Quadro              | `RTX 8000` `RTX 6000` `RTX 5000` `RTX 4000`                                                                 |
| 7.0                | NVIDIA              | `TITAN V` `V100` `Quadro GV100`                                                                             |
| 6.1                | NVIDIA TITAN        | `TITAN Xp` `TITAN X`                                                                                        |
|                    | GeForce GTX         | `GTX 1080 Ti` `GTX 1080` `GTX 1070 Ti` `GTX 1070` `GTX 1060` `GTX 1050 Ti` `GTX 1050`                       |
|                    | Quadro              | `P6000` `P5200` `P4200` `P3200` `P5000` `P4000` `P3000` `P2200` `P2000` `P1000` `P620` `P600` `P500` `P520` |
|                    | Tesla               | `P40` `P4`                                                                                                  |
| 6.0                | NVIDIA              | `Tesla P100` `Quadro GP100`                                                                                 |
| 5.2                | GeForce GTX         | `GTX TITAN X` `GTX 980 Ti` `GTX 980` `GTX 970` `GTX 960` `GTX 950`                                          |
|                    | Quadro              | `M6000 24GB` `M6000` `M5000` `M5500M` `M4000` `M2200` `M2000` `M620`                                        |
|                    | Tesla               | `M60` `M40`                                                                                                 |
| 5.0                | GeForce GTX         | `GTX 750 Ti` `GTX 750` `NVS 810`                                                                            |
|                    | Quadro              | `K2200` `K1200` `K620` `M1200` `M520` `M5000M` `M4000M` `M3000M` `M2000M` `M1000M` `K620M` `M600M` `M500M`  |

For building locally to support older GPUs, see [developer.md](./development.md#linux-cuda-nvidia)
```

--------------------------------

TITLE: Ollama Model Push API
DESCRIPTION: Demonstrates the API request and response for pushing a model to Ollama. It covers streaming and non-streaming responses, including status updates during the upload process.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_51

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/push -d '{
  "model": "mattw/pygmalion:latest"
}'
```

LANGUAGE: json
CODE:
```
{ "status": "retrieving manifest" }
```

LANGUAGE: json
CODE:
```
{
  "status": "starting upload",
  "digest": "sha256:bc07c81de745696fdf5afca05e065818a8149fb0c77266fb584d9b2cba3711ab",
  "total": 1928429856
}
```

LANGUAGE: json
CODE:
```
{
  "status": "starting upload",
  "digest": "sha256:bc07c81de745696fdf5afca05e065818a8149fb0c77266fb584d9b2cba3711ab",
  "total": 1928429856
}
```

LANGUAGE: json
CODE:
```
{"status":"pushing manifest"}
{"status":"success"}
```

LANGUAGE: json
CODE:
```
{ "status": "success" }
```

--------------------------------

TITLE: Shared Library Build Configuration
DESCRIPTION: Configures build properties for shared libraries, including setting position-independent code and defining GGML_BUILD and GGML_SHARED for targets.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_14

LANGUAGE: cmake
CODE:
```
target_compile_definitions(ggml-base PUBLIC _DARWIN_C_SOURCE)
endif()

if (BUILD_SHARED_LIBS)
    foreach (target ggml-base ggml)
        set_target_properties(${target} PROPERTIES POSITION_INDEPENDENT_CODE ON)
        target_compile_definitions(${target} PRIVATE GGML_BUILD)
        target_compile_definitions(${target} PUBLIC  GGML_SHARED)
    endforeach()
endif()
```

--------------------------------

TITLE: Ollama Chat API Reference
DESCRIPTION: This section details the parameters and structure for making chat requests to the Ollama API. It covers required and optional parameters for messages, tools, and advanced configurations like streaming and output formatting.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_21

LANGUAGE: APIDOC
CODE:
```
Ollama Chat API:

Endpoint: /api/chat

Parameters:
- model: (required) The name of the model to use.
- messages: An array of message objects representing the chat history.
  - role: The role of the message sender ('system', 'user', 'assistant', 'tool').
  - content: The text content of the message.
  - thinking: (optional, for thinking models) The model's thinking process.
  - images: (optional, for multimodal models) A list of image data.
  - tool_calls: (optional) A list of tool calls made by the model.
  - tool_name: (optional) The name of the tool executed to inform the model.
- tools: (optional) A list of tool definitions in JSON format for the model to use.
  - type: The type of tool (e.g., 'function').
  - function:
    - name: The name of the function.
    - description: A description of what the function does.
    - parameters: JSON schema defining the function's parameters.
- think: (optional, for thinking models) Boolean, whether the model should think before responding.
- format: (optional) The desired output format ('json' or a JSON schema).
- options: (optional) Additional model parameters (e.g., 'temperature').
- stream: (optional) Boolean, if false, returns a single response object; otherwise, streams objects.
- keep_alive: (optional) Duration the model stays loaded (default: '5m').

Response:
- A stream of JSON objects (if stream is true) or a single JSON object.
- Each object contains:
  - model: The model used.
  - created_at: Timestamp of creation.
  - message: The message object from the assistant.
  - done: Boolean indicating if the response is complete.
  - total_duration: Total time for the request.
  - load_duration: Time taken to load the model.
  - prompt_eval_count: Number of tokens in the prompt.
  - prompt_eval_duration: Time spent evaluating the prompt.
  - eval_count: Number of tokens generated.
  - eval_duration: Time spent generating the response.
  - done_reason: Reason for completion (e.g., 'stop').
```

--------------------------------

TITLE: Static Linking Restriction
DESCRIPTION: Prevents static linking for HIP/ROCm builds, as it is not supported.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_10

LANGUAGE: cmake
CODE:
```
if (GGML_STATIC)
    message(FATAL_ERROR "Static linking not supported for HIP/ROCm")
endif()
```

--------------------------------

TITLE: Container Permissions for AMD GPUs on Linux
DESCRIPTION: Provides the command to adjust SELinux settings on Linux hosts, allowing containers to access AMD GPU devices. This is a common requirement for running Ollama in containerized environments with GPU acceleration.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_6

LANGUAGE: APIDOC
CODE:
```
sudo setsebool container_use_devices=1
```

--------------------------------

TITLE: ROCm Path Configuration
DESCRIPTION: Sets the ROCm path based on environment variables or default locations. This is crucial for finding ROCm components.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_0

LANGUAGE: cmake
CODE:
```
if (NOT EXISTS $ENV{ROCM_PATH})
    if (NOT EXISTS /opt/rocm)
        set(ROCM_PATH /usr)
    else()
        set(ROCM_PATH /opt/rocm)
    endif()
else()
    set(ROCM_PATH $ENV{ROCM_PATH})
endif()

list(APPEND CMAKE_PREFIX_PATH  ${ROCM_PATH})
list(APPEND CMAKE_PREFIX_PATH "${ROCM_PATH}/lib64/cmake")
```

--------------------------------

TITLE: Generating Embeddings with Multiple Inputs (Request)
DESCRIPTION: This `curl` command illustrates how to request embeddings for multiple text inputs by providing an array of strings to the `input` parameter of the `/api/embed` endpoint.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_76

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/embed -d '{
  "model": "all-minilm",
  "input": ["Why is the sky blue?", "Why is the grass green?"]
}'
```

--------------------------------

TITLE: Ollama Model Information Response (JSON5)
DESCRIPTION: This JSON object represents a comprehensive response from an Ollama API call, likely 'ollama show', detailing a model's configuration. It includes the Modelfile content, runtime parameters, template structure, and detailed model metadata such as architecture, parameter count, and tokenizer information, along with its capabilities.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_56

LANGUAGE: json5
CODE:
```
{
  "modelfile": "# Modelfile generated by \"ollama show\"\n# To build a new Modelfile based on this one, replace the FROM line with:\n# FROM llava:latest\n\nFROM /Users/matt/.ollama/models/blobs/sha256:200765e1283640ffbd013184bf496e261032fa75b99498a9613be4e94d63ad52\nTEMPLATE \"\"\"{{ .System }}\nUSER: {{ .Prompt }}\nASSISTANT: \"\"\"\nPARAMETER num_ctx 4096\nPARAMETER stop \"\u003c/s\u003e\"\nPARAMETER stop \"USER:\"\nPARAMETER stop \"ASSISTANT:\"",
  "parameters": "num_keep                       24\nstop                           \"<|start_header_id|>\"\nstop                           \"<|end_header_id|>\"\nstop                           \"<|eot_id|>\"",
  "template": "{{ if .System }}<|start_header_id|>system<|end_header_id|>\n\n{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>\n\n{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>\n\n{{ .Response }}<|eot_id|>",
  "details": {
    "parent_model": "",
    "format": "gguf",
    "family": "llama",
    "families": [
      "llama"
    ],
    "parameter_size": "8.0B",
    "quantization_level": "Q4_0"
  },
  "model_info": {
    "general.architecture": "llama",
    "general.file_type": 2,
    "general.parameter_count": 8030261248,
    "general.quantization_version": 2,
    "llama.attention.head_count": 32,
    "llama.attention.head_count_kv": 8,
    "llama.attention.layer_norm_rms_epsilon": 0.00001,
    "llama.block_count": 32,
    "llama.context_length": 8192,
    "llama.embedding_length": 4096,
    "llama.feed_forward_length": 14336,
    "llama.rope.dimension_count": 128,
    "llama.rope.freq_base": 500000,
    "llama.vocab_size": 128256,
    "tokenizer.ggml.bos_token_id": 128000,
    "tokenizer.ggml.eos_token_id": 128009,
    "tokenizer.ggml.merges": [],
    "tokenizer.ggml.model": "gpt2",
    "tokenizer.ggml.pre": "llama-bpe",
    "tokenizer.ggml.token_type": [],
    "tokenizer.ggml.tokens": []
  },
  "capabilities": [
    "completion",
    "vision"
  ]
}
```

--------------------------------

TITLE: Ollama List Running Models API Response
DESCRIPTION: This JSON object represents the response from the `/api/ps` endpoint, providing a list of currently loaded models, including their names, sizes, digests, and detailed metadata.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_80

LANGUAGE: json
CODE:
```
{
  "models": [
    {
      "name": "mistral:latest",
      "model": "mistral:latest",
      "size": 5137025024,
      "digest": "2ae6f6dd7a3dd734790bbbf58b8909a606e0e7e97e94b7604e0aa7ae4490e6d8",
      "details": {
        "parent_model": "",
        "format": "gguf",
        "family": "llama",
        "families": [
          "llama"
        ],
        "parameter_size": "7.2B",
        "quantization_level": "Q4_0"
      },
      "expires_at": "2024-06-04T14:38:31.83753-07:00",
      "size_vram": 5137025024
    }
  ]
}
```

--------------------------------

TITLE: Ollama Embedding API
DESCRIPTION: Demonstrates how to use the /embedding endpoint to generate embeddings for a given text prompt. It sends a JSON payload with the prompt to the server.

SOURCE: https://github.com/ollama/ollama/blob/main/runner/README.md#_snippet_2

LANGUAGE: shell
CODE:
```
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "turn me into an embedding"}' http://localhost:8080/embedding
```

--------------------------------

TITLE: Checking Kernel Driver Messages for AMD GPU Errors
DESCRIPTION: Use these commands to check the system's kernel ring buffer for messages related to the amdgpu or kfd drivers, which can help diagnose GPU-related issues.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_7

LANGUAGE: bash
CODE:
```
sudo dmesg | grep -i amdgpu
sudo dmesg | grep -i kfd
```

--------------------------------

TITLE: Ollama GPU Overrides and Selection (Linux)
DESCRIPTION: Explains how to override unsupported ROCm targets using the HSA_OVERRIDE_GFX_VERSION environment variable and how to select specific GPUs using ROCR_VISIBLE_DEVICES. This is for advanced users facing compatibility issues or managing multiple GPUs.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_5

LANGUAGE: APIDOC
CODE:
```
Environment Variables:
  HSA_OVERRIDE_GFX_VERSION: Set to 'x.y.z' to force a specific LLVM target (e.g., "10.3.0" for RX 5400).
  HSA_OVERRIDE_GFX_VERSION_<device_number>: For individual GPU overrides (e.g., HSA_OVERRIDE_GFX_VERSION_0="10.3.0").
  ROCR_VISIBLE_DEVICES: Comma-separated list of GPU IDs or UUIDs to use (e.g., "0,2" or "<uuid1>,<uuid2>").
  To force CPU usage, set ROCR_VISIBLE_DEVICES to "-1".

LLVM Target to Example GPU Mapping:
  gfx900: Radeon RX Vega 56
  gfx906: Radeon Instinct MI50
  gfx908: Radeon Instinct MI100
  gfx90a: Radeon Instinct MI210
  gfx940: Radeon Instinct MI300
  gfx941: 
  gfx942: 
  gfx1030: Radeon PRO V620
  gfx1100: Radeon PRO W7900
  gfx1101: Radeon PRO W7700
  gfx1102: Radeon RX 7600
```

--------------------------------

TITLE: Debugging AMD GPU Issues with Environment Variables
DESCRIPTION: These environment variables can be set to enable more verbose logging and debugging information when troubleshooting AMD GPU discovery and inference problems with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/troubleshooting.md#_snippet_6

LANGUAGE: shell
CODE:
```
export AMD_LOG_LEVEL=3
export OLLAMA_DEBUG=1
```

--------------------------------

TITLE: HIP Compiler Flags
DESCRIPTION: Sets a workaround for old compilers by specifying the maximum threads per block for HIP compilation.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-hip/CMakeLists.txt#_snippet_5

LANGUAGE: cmake
CODE:
```
set(CMAKE_HIP_FLAGS "${CMAKE_HIP_FLAGS} --gpu-max-threads-per-block=1024")
```

--------------------------------

TITLE: ggml Backend Inclusion Function
DESCRIPTION: A CMake function to include and configure different ggml backends. It checks for backend availability and sets compile definitions accordingly.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_7

LANGUAGE: cmake
CODE:
```
function(ggml_add_backend backend)
    string(TOUPPER "GGML_${backend}" backend_id)
    if (${backend_id})
        string(TOLOWER "ggml-${backend}" backend_target)
        add_subdirectory(${backend_target})
        message(STATUS "Including ${backend} backend")
        if (NOT GGML_BACKEND_DL)
            string(TOUPPER "GGML_USE_${backend}" backend_use)
            target_compile_definitions(ggml PUBLIC ${backend_use})
        endif()
    endif()
endfunction()
```

--------------------------------

TITLE: Create Chat Completion with Text and Image Input
DESCRIPTION: Demonstrates a multimodal chat completion request, sending both text and an image (encoded in base64) to the Ollama API. This allows for image-based queries.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_7

LANGUAGE: javascript
CODE:
```
const response = await openai.chat.completions.create({
    model: "llava",
    messages: [
        {
        role: "user",
        content: [
            { type: "text", text: "What's in this image?" },
            {
            type: "image_url",
            image_url: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG0AAABmCAYAAADBPx+VAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAA3VSURBVHgB7Z27r0zdG8fX743i1bi1ikMoFMQloXRpKFFIqI7LH4BEQ+NWIkjQuSWCRIEoULk0gsK1kCBI0IhrQVT7tz/7zZo888yz1r7MnDl7z5xvsjkzs2fP3uu71nNfa7lkAsm7d++Sffv2JbNmzUqcc8m0adOSzZs3Z+/XES4ZckAWJEGWPiCxjsQNLWmQsWjRIpMseaxcuTKpG/7HP27I8P79e7dq1ars/yL4/v27S0ejqwv+cUOGEGGpKHR37tzJCEpHV9tnT58+dXXCJDdECBE2Ojrqjh071hpNECjx4cMHVycM1Uhbv359B2F79+51586daxN/+pyRkRFXKyRDAqxEp4yMlDDzXG1NPnnyJKkThoK0VFd1ELZu3TrzXKxKfW7dMBQ6bcuWLW2v0VlHjx41z717927ba22U9APcw7Nnz1oGEPeL3m3p2mTAYYnFmMOMXybPPXv2bNIPpFZr1NHn4HMw0KRBjg9NuRw95s8PEcz/6DZELQd/09C9QGq5RsmSRybqkwHGjh07OsJSsYYm3ijPpyHzoiacg35MLdDSIS/O1yM778jOTwYUkKNHWUzUWaOsylE00MyI0fcnOwIdjvtNdW/HZwNLGg+sR1kMepSNJXmIwxBZiG8tDTpEZzKg0GItNsosY8USkxDhD0Rinuiko2gfL/RbiD2LZAjU9zKQJj8RDR0vJBR1/Phx9+PHj9Z7REF4nTZkxzX4LCXHrV271qXkBAPGfP/atWvu/PnzHe4C97F48eIsRLZ9+3a3f/9+87dwP1JxaF7/3r17ba+5l4EcaVo0lj3SBq5kGTJSQmLWMjgYNei2GPT1MuMqGTDEFHzeQSP2wi/jGnkmPJ/nhccs44jvDAxpVcxnq0F6eT8h4ni/iIWpR5lPyA6ETkNXoSukvpJAD3AsXLiwpZs49+fPn5ke4j10TqYvegSfn0OnafC+Tv9ooA/JPkgQysqQNBzagXY55nO/oa1F7qvIPWkRL12WRpMWUvpVDYmxAPehxWSe8ZEXL20sadYIozfmNch4QJPAfeJgW3rNsnzphBKNJM2KKODo1rVOMRYik5ETy3ix4qWNI81qAAirizgMIc+yhTytx0JWZuNI03qsrgWlGtwjoS9XwgUhWGyhUaRZZQNNIEwCiXD16tXcAHUs79co0vSD8rrJCIW98pzvxpAWyyo3HYwqS0+H0BjStClcZJT5coMm6D2LOF8TolGJtK9fvyZpyiC5ePFi9nc/oJU4eiEP0jVoAnHa9wyJycITMP78+eMeP37sXrx44d6+fdt6f82aNdkx1pg9e3Zb5W+RSRE+n+VjksQWifvVaTKFhn5O8my63K8Qabdv33b379/PiAP//vuvW7BggZszZ072/+TJk91YgkafPn166zXB1rQHFvouAWHq9z3SEevSUerqCn2/dDCeta2jxYbr69evk4MHDyY7d+7MjhMnTiTPnz9Pfv/+nfQT2ggpO2dMF8cghuoM7Ygj5iWCqRlGFml0QC/ftGmTmzt3rmsaKDsgBSPh0/8yPeLLBihLkOKJc0jp8H8vUzcxIA1k6QJ/c78tWEyj5P3o4u9+jywNPdJi5rAH9x0KHcl4Hg570eQp3+vHXGyrmEeigzQsQsjavXt38ujRo44LQuDDhw+TW7duRS1HGgMxhNXHgflaNTOsHyKvHK5Ijo2jbFjJBQK9YwFd6RVMzfgRBmEfP37suBBm/p49e1qjEP2mwTViNRo0VJWH1deMXcNK08uUjVUu7s/zRaL+oLNxz1bpANco4npUgX4G2eFbpDFyQoQxojBCpEGSytmOH8qrH5Q9vuzD6ofQylkCUmh8DBAr+q8JCyVNtWQIidKQE9wNtLSQnS4jDSsxNHogzFuQBw4cyM61UKVsjfr3ooBkPSqqQHesUPWVtzi9/vQi1T+rJj7WiTz4Pt/l3LxUkr5P2VYZaZ4URpsE+st/dujQoaBBYokbrz/8TJNQYLSonrPS9kUaSkPeZyj1AWSj+d+VBoy1pIWVNed8P0Ll/ee5HdGRhrHhR5GGN0r4LGZBaj8oFDJitBTJzIZgFcmU0Y8ytWMZMzJOaXUSrUs5RxKnrxmbb5YXO9VGUhtpXldhEUogFr3IzIsvlpmdosVcGVGXFWp2oU9kLFL3dEkSz6NHEY1sjSRdIuDFWEhd8KxFqsRi1uM/nz9/zpxnwlESONdg6dKlbsaMGS4EHFHtjFIDHwKOo46l4TxSuxgDzi+rE2jg+BaFruOX4HXa0Nnf1lwAPufZeF8/r6zD97WK2qFnGjBxTw5qNGPxT+5T/r7/7RawFC3j4vTp09koCxkeHjqbHJqArmH5UrFKKksnxrK7FuRIs8STfBZv+luugXZ2pR/pP9Ois4z+TiMzUUkUjD0iEi1fzX8GmXyuxUBRcaUfykV0YZnlJGKQpOiGB76x5GeWkWWJc3mOrK6S7xdND+W5N6XyaRgtWJFe13GkaZnKOsYqGdOVVVbGupsyA/l7emTLHi7vwTdirNEt0qxnzAvBFcnQF16xh/TMpUuXHDowhlA9vQVraQhkudRdzOnK+04ZSP3DUhVSP61YsaLtd/ks7ZgtPcXqPqEafHkdqa84X6aCeL7YWlv6edGFHb+ZFICPlljHhg0bKuk0CSvVznWsotRu433alNdFrqG45ejoaPCaUkWERpLXjzFL2Rpllp7PJU2a/v7Ab8N05/9t27Z16KUqoFGsxnI9EosS2niSYg9SpU6B4JgTrvVW1flt1sT+0ADIJU2maXzcUTraGCRaL1Wp9rUMk16PMom8QhruxzvZIegJjFU7LLCePfS8uaQdPny4jTTL0dbee5mYokQsXTIWNY46kuMbnt8Kmec+LGWtOVIl9cT1rCB0V8WqkjAsRwta93TbwNYoGKsUSChN44lgBNCoHLHzquYKrU6qZ8lolCIN0Rh6cP0Q3U6I6IXILYOQI513hJaSKAorFpuHXJNfVlpRtmYBk1Su1obZr5dnKAO+L10Hrj3WZW+E3qh6IszE37F6EB+68mGpvKm4eb9bFrlzrok7fvr0Kfv727dvWRmdVTJHw0qiiCUSZ6wCK+7XL/AcsgNyL74DQQ730sv78Su7+t/A36MdY0sW5o40ahslXr58aZ5HtZB8GH64m9EmMZ7FpYw4T6QnrZfgenrhFxaSiSGXtPnz57e9TkNZLvTjeqhr734CNtrK41L40sUQckmj1lGKQ0rC37x544r8eNXRpnVE3ZZY7zXo8NomiO0ZUCj2uHz58rbXoZ6gc0uA+F6ZeKS/jhRDUq8MKrTho9fEkihMmhxtBI1DxKFY9XLpVcSkfoi8JGnToZO5sU5aiDQIW716ddt7ZLYtMQlhECdBGXZZMWldY5BHm5xgAroWj4C0hbYkSc/jBmggIrXJWlZM6pSETsEPGqZOndr2uuuR5rF169a2HoHPdurUKZM4CO1WTPqaDaAd+GFGKdIQkxAn9RuEWcTRyN2KSUgiSgF5aWzPTeA/lN5rZubMmR2bE4SIC4nJoltgAV/dVefZm72AtctUCJU2CMJ327hxY9t7EHbkyJFseq+EJSY16RPo3Dkq1kkr7+q0bNmyDuLQcZBEPYmHVdOBiJyIlrRDq41YPWfXOxUysi5fvtyaj+2BpcnsUV/oSoEMOk2CQGlr4ckhBwaetBhjCwH0ZHtJROPJkyc7UjcYLDjmrH7ADTEBXFfOYmB0k9oYBOjJ8b4aOYSe7QkKcYhFlq3QYLQhSidNmtS2RATwy8YOM3EQJsUjKiaWZ+vZToUQgzhkHXudb/PW5YMHD9yZM2faPsMwoc7RciYJXbGuBqJ1UIGKKLv915jsvgtJxCZDubdXr165mzdvtr1Hz5LONA8jrUwKPqsmVesKa49S3Q4WxmRPUEYdTjgiUcfUwLx589ySJUva3oMkP6IYddq6HMS4o55xBJBUeRjzfa4Zdeg56QZ43LhxoyPo7Lf1kNt7oO8wWAbNwaYjIv5lhyS7kRf96dvm5Jah8vfvX3flyhX35cuX6HfzFHOToS1H4BenCaHvO8pr8iDuwoUL7tevX+b5ZdbBair0xkFIlFDlW4ZknEClsp/TzXyAKVOmmHWFVSbDNw1l1+4f90U6IY/q4V27dpnE9bJ+v87QEydjqx/UamVVPRG+mwkNTYN+9tjkwzEx+atCm/X9WvWtDtAb68Wy9LXa1UmvCDDIpPkyOQ5ZwSzJ4jMrvFcr0rSjOUh+GcT4LSg5ugkW1Io0/ 
```

--------------------------------

TITLE: Chat Completions API
DESCRIPTION: Handles chat-based interactions with Ollama models, supporting streaming, JSON mode, vision, tools, and reproducible outputs. It details supported request fields for chat completions.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
/v1/chat/completions

Supported features:
- Chat completions
- Streaming
- JSON mode
- Reproducible outputs
- Vision
- Tools
- Logprobs

Supported request fields:
- model
- messages
  - Text content
  - Image content
    - Base64 encoded image
    - Image URL
  - Array of content parts
- frequency_penalty
- presence_penalty
- response_format
- seed
- stop
- stream
- stream_options
  - include_usage
- temperature
- top_p
- max_tokens
- tools
- tool_choice
- logit_bias
- user
- n
```

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{ \
        "model": "llama3.2", \
        "messages": [ \
            { \
                "role": "user", \
                "content": "Hello!" \
            } \
        ] \
    }'
```

--------------------------------

TITLE: OpenAI API Compatibility
DESCRIPTION: Ollama offers experimental compatibility with select OpenAI API endpoints. This allows developers to use existing applications designed for the OpenAI API with Ollama. Note that this feature is experimental and may undergo significant changes. For complete API access, refer to the Ollama Python library, JavaScript library, or REST API documentation.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_0

LANGUAGE: APIDOC
CODE:
```
OpenAI Compatibility:
  - Experimental feature subject to change.
  - Allows connection of existing OpenAI API applications to Ollama.
  - For full functionality, use Ollama Python library, Ollama JavaScript library, or Ollama REST API.
  - Reference: https://platform.openai.com/docs/api-reference
```

--------------------------------

TITLE: Pushing Model to Ollama API (Request)
DESCRIPTION: This `curl` command initiates a push operation to the Ollama API, sending a JSON payload to specify the model to be pushed. It targets the `/api/push` endpoint on the local Ollama server.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_68

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/push -d '{
  "model": "mattw/pygmalion:latest"
}'
```

--------------------------------

TITLE: Push Ollama Model API Endpoint (HTTP)
DESCRIPTION: Defines the HTTP POST endpoint for uploading an Ollama model to a model library. This operation requires prior registration with ollama.ai and adding a public key.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_67

LANGUAGE: http
CODE:
```
POST /api/push
```

--------------------------------

TITLE: CMake Build Settings for Ollama
DESCRIPTION: Configures compile definitions and target properties for the Ollama build process, particularly for shared library builds. It sets `_DARWIN_C_SOURCE` for `ggml-base` and enables `POSITION_INDEPENDENT_CODE` along with `GGML_BUILD` and `GGML_SHARED` definitions for targets when `BUILD_SHARED_LIBS` is enabled.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/CMakeLists.txt#_snippet_22

LANGUAGE: cmake
CODE:
```
target_compile_definitions(ggml-base PUBLIC _DARWIN_C_SOURCE)
endif()

if (BUILD_SHARED_LIBS)
    foreach (target ggml-base ggml)
        set_target_properties(${target} PROPERTIES POSITION_INDEPENDENT_CODE ON)
        target_compile_definitions(${target} PRIVATE GGML_BUILD)
        target_compile_definitions(${target} PUBLIC  GGML_SHARED)
    endforeach()
endif()
```

--------------------------------

TITLE: Ollama API: Blob content for config digest
DESCRIPTION: This entry provides the content of a specific blob associated with the 'smol' model in Ollama. This blob contains the configuration details for the model, identified by its SHA256 digest.

SOURCE: https://github.com/ollama/ollama/blob/main/server/internal/registry/testdata/registry.txt#_snippet_2

LANGUAGE: APIDOC
CODE:
```
GET /v2/library/smol/blobs/sha256:ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356

Response Body:
{}
```

--------------------------------

TITLE: Unload Model Immediately with Ollama API (Generate Endpoint)
DESCRIPTION: Shows how to use the `keep_alive` parameter set to 0 with the `/api/generate` endpoint to unload a model immediately after generating a response.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_16

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": 0}'
```

--------------------------------

TITLE: CUDA Compile Definitions Management
DESCRIPTION: This section details the conditional compilation definitions set for the CUDA backend. It includes flags for peer-to-peer batch size, CUDA graphs, forced matrix multiplication kernels (MMQ), CUBLAS usage, virtual memory management (VMM), FP16 support, and disabling peer-to-peer copy operations.

SOURCE: https://github.com/ollama/ollama/blob/main/ml/backend/ggml/ggml/src/ggml-cuda/CMakeLists.txt#_snippet_2

LANGUAGE: cmake
CODE:
```
    add_compile_definitions(GGML_CUDA_PEER_MAX_BATCH_SIZE=${GGML_CUDA_PEER_MAX_BATCH_SIZE})

    if (GGML_CUDA_GRAPHS)
        add_compile_definitions(GGML_CUDA_USE_GRAPHS)
    endif()

    if (GGML_CUDA_FORCE_MMQ)
        add_compile_definitions(GGML_CUDA_FORCE_MMQ)
    endif()

    if (GGML_CUDA_FORCE_CUBLAS)
        add_compile_definitions(GGML_CUDA_FORCE_CUBLAS)
    endif()

    if (GGML_CUDA_NO_VMM)
        add_compile_definitions(GGML_CUDA_NO_VMM)
    endif()

    if (NOT GGML_CUDA_FA)
        add_compile_definitions(GGML_CUDA_NO_FA)
    endif()

    if (GGML_CUDA_F16 OR GGML_CUDA_DMMV_F16)
        add_compile_definitions(GGML_CUDA_F16)
    endif()

    if (GGML_CUDA_NO_PEER_COPY)
        add_compile_definitions(GGML_CUDA_NO_PEER_COPY)
    endif()

```

--------------------------------

TITLE: Expose Ollama with Nginx Proxy
DESCRIPTION: This Nginx configuration allows you to expose the Ollama HTTP server to your network. It forwards requests from a specified server name to the Ollama instance running on localhost:11434.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_7

LANGUAGE: nginx
CODE:
```
server {
    listen 80;
    server_name example.com;  # Replace with your domain or IP
    location / {
        proxy_pass http://localhost:11434;
        proxy_set_header Host localhost:11434;
    }
}
```

--------------------------------

TITLE: Ollama API Endpoints for Model Management
DESCRIPTION: Documentation for the `/api/generate` and `/api/chat` endpoints, focusing on the `keep_alive` parameter. This parameter controls the duration a model remains loaded in memory.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_17

LANGUAGE: APIDOC
CODE:
```
API Endpoints:
  /api/generate
  /api/chat

Parameters:
  model: (string, required) The name of the model to use.
  keep_alive: (string | number | null, optional) Controls how long the model stays in memory.
    - Duration string (e.g., "10m", "24h")
    - Number in seconds (e.g., 3600)
    - Negative number (e.g., -1) to keep loaded indefinitely.
    - 0 to unload immediately after response.

Usage:
  Send a POST request with a JSON body containing the model name and optionally `keep_alive` parameter.

Example (keep alive for 1 hour):
  curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": "1h"}'

Example (unload immediately):
  curl http://localhost:11434/api/chat -d '{"model": "llama3.2", "keep_alive": 0}'

Environment Variable Override:
  OLLAMA_KEEP_ALIVE: Sets the default keep-alive duration for all models. The API parameter overrides this setting.
```

--------------------------------

TITLE: Manage Model Keep-Alive with Ollama API (Generate Endpoint)
DESCRIPTION: Explains how to use the `keep_alive` parameter with the `/api/generate` endpoint to control how long a model stays in memory. Setting it to -1 keeps the model loaded indefinitely.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/faq.md#_snippet_15

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{"model": "llama3.2", "keep_alive": -1}'
```

--------------------------------

TITLE: Ollama Version API
DESCRIPTION: Shows the API endpoint for retrieving the current Ollama version. The response is a simple JSON object containing the version string.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_55

LANGUAGE: APIDOC
CODE:
```
GET /api/version
Retrieve the Ollama version
```

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/version
```

LANGUAGE: json
CODE:
```
{
  "version": "0.5.1"
}
```

--------------------------------

TITLE: Chat Request with History and Tools
DESCRIPTION: A chat request that includes both conversation history and tool definitions. This allows the model to respond based on past interactions and utilize provided tools.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_35

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "what is the weather in Toronto?"
    },
    // the message from the model appended to history
    {
      "role": "assistant",
      "content": "",
      "tool_calls": [
        {
          "function": {
            "name": "get_temperature",
            "arguments": {
              "city": "Toronto"
            }
          },
        }
      ]
    },
    // the tool call result appended to history
    {
      "role": "tool",
      "content": "11 degrees celsius",
      "tool_name": "get_temperature",
    }
  ],
  "stream": false,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather in a given city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city to get the weather for"
            }
          },
          "required": ["city"]
        }
      }
    }
  ]
}'
```

--------------------------------

TITLE: Generate Text Response (With Options)
DESCRIPTION: Generates a text response with custom runtime options for the model, such as `num_predict`, `temperature`, and `repeat_penalty`. All available options can be set individually.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_17

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Why is the sky blue?",
  "stream": false,
  "options": {
    "num_keep": 5,
    "seed": 42,
    "num_predict": 100,
    "top_k": 20,
    "top_p": 0.9,
    "min_p": 0.0,
    "typical_p": 0.7,
    "repeat_last_n": 33,
    "temperature": 0.8,
    "repeat_penalty": 1.2,
    "presence_penalty": 1.5,
    "frequency_penalty": 1.0,
    "penalize_newline": true,
    "stop": ["\n", "user:"],
    "numa": false,
    "num_ctx": 1024,
    "num_batch": 2,
    "num_gpu": 1,
    "main_gpu": 0,
    "use_mmap": true,
    "num_thread": 8
  }
}'
```

LANGUAGE: json
CODE:
```
{
  "model": "llama3.2",
  "created_at": "2023-08-04T19:22:45.499127Z",
  "response": "The sky is blue because it is the color of the sky.",
  "done": true,
  "context": [1, 2, 3],
  "total_duration": 4935886791,
  "load_duration": 534986708,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 107345000,
  "eval_count": 237,
  "eval_duration": 4289432000
}
```

--------------------------------

TITLE: Model Management API
DESCRIPTION: Enables listing available models and retrieving details for a specific model. It clarifies the meaning of 'created' and 'owned_by' fields.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/openai.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
/v1/models

Notes:
- `created` corresponds to when the model was last modified
- `owned_by` corresponds to the ollama username, defaulting to "library"

/v1/models/{model}

Notes:
- `created` corresponds to when the model was last modified
- `owned_by` corresponds to the ollama username, defaulting to "library"
```

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/v1/models

curl http://localhost:11434/v1/models/llama3.2
```

--------------------------------

TITLE: Generating Embeddings with Single Input (Request)
DESCRIPTION: This `curl` command demonstrates how to request embeddings for a single text input using the `/api/embed` endpoint, specifying the model and the input text.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_74

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/embed -d '{
  "model": "all-minilm",
  "input": "Why is the sky blue?"
}'
```

--------------------------------

TITLE: Chat Request for Structured Output
DESCRIPTION: A chat request configured to return a structured JSON output. This is achieved using the 'format' parameter with a defined schema.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_30

LANGUAGE: shell
CODE:
```
curl -X POST http://localhost:11434/api/chat -H "Content-Type: application/json" -d '{
  "model": "llama3.1",
  "messages": [{"role": "user", "content": "Ollama is 22 years old and busy saving the world. Return a JSON object with the age and availability."}],
  "stream": false,
  "format": {
    "type": "object",
    "properties": {
      "age": {
        "type": "integer"
      },
      "available": {
        "type": "boolean"
      }
    },
    "required": [
      "age",
      "available"
    ]
  },
  "options": {
    "temperature": 0
  }
}'
```

--------------------------------

TITLE: AMD ROCm GPU Support (Windows)
DESCRIPTION: Lists AMD GPU families and specific models supported by ROCm v6.1 on Windows. This table helps Windows users verify their hardware compatibility with Ollama.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_4

LANGUAGE: APIDOC
CODE:
```
AMD Radeon RX:
  7900 XTX, 7900 XT, 7900 GRE, 7800 XT, 7700 XT, 7600 XT, 7600, 6950 XT, 6900 XTX, 6900XT, 6800 XT, 6800
AMD Radeon PRO:
  W7900, W7800, W7700, W7600, W7500, W6900X, W6800X Duo, W6800X, W6800, V620
```

--------------------------------

TITLE: GPU Selection with CUDA_VISIBLE_DEVICES
DESCRIPTION: Explains how to control which NVIDIA GPUs Ollama uses by setting the `CUDA_VISIBLE_DEVICES` environment variable. It recommends using UUIDs for reliability and suggests using an invalid ID to force CPU usage.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_1

LANGUAGE: bash
CODE:
```
export CUDA_VISIBLE_DEVICES=GPU-UUID-1,GPU-UUID-2
# or for CPU only
export CUDA_VISIBLE_DEVICES=-1
```

--------------------------------

TITLE: Ollama Version API Response
DESCRIPTION: This JSON object represents the response from the `/api/version` endpoint, providing the current version string of the Ollama server.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_86

LANGUAGE: json
CODE:
```
{
  "version": "0.5.1"
}
```

--------------------------------

TITLE: AMD ROCm GPU Support (Linux)
DESCRIPTION: Lists AMD GPU families and specific models supported by ROCm on Linux. This information is crucial for users to determine compatibility when setting up Ollama with AMD hardware.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_3

LANGUAGE: APIDOC
CODE:
```
AMD Radeon RX:
  7900 XTX, 7900 XT, 7900 GRE, 7800 XT, 7700 XT, 7600 XT, 7600, 6950 XT, 6900 XTX, 6900XT, 6800 XT, 6800, Vega 64, Vega 56
AMD Radeon PRO:
  W7900, W7800, W7700, W7600, W7500, W6900X, W6800X Duo, W6800X, W6800, V620, V420, V340, V320, Vega II Duo, Vega II, Vega II, SSG
AMD Instinct:
  MI300X, MI300A, MI300, MI250X, MI250, MI210, MI200, MI100, MI60, MI50
```

--------------------------------

TITLE: Apple Metal GPU Support
DESCRIPTION: Confirms Ollama's support for GPU acceleration on Apple devices utilizing the Metal API. This indicates compatibility with Macs and other Apple hardware.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/gpu.md#_snippet_7

LANGUAGE: APIDOC
CODE:
```
Ollama supports GPU acceleration on Apple devices via the Metal API.
```

--------------------------------

TITLE: Ollama Chat Request with Images
DESCRIPTION: This section describes how to make a chat request to the Ollama service, specifically when including image data. It outlines the expected parameters and format for sending image content.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_37

LANGUAGE: APIDOC
CODE:
```
Chat Request (with images):
  POST /api/chat

  Request Body:
    model: string (required) - The model to use for the chat.
    messages: array of objects (required) - The conversation history.
      - role: string (required) - The role of the message sender ('user' or 'assistant').
      - content: string (required) - The message content.
    stream: boolean (optional) - Whether to stream the response.
    options: object (optional) - Model-specific options.
    images: array of strings (optional) - Base64 encoded images to include in the prompt.

  Example:
    POST /api/chat
    {
      "model": "llava",
      "messages": [
        {
          "role": "user",
          "content": "What is in this image?",
          "images": ["base64_encoded_image_data_here"]
        }
      ]
    }
```

--------------------------------

TITLE: Generate Text Response (Raw Mode)
DESCRIPTION: Generates a text response using raw mode, bypassing templating for full prompt control. Note that raw mode does not return context.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_15

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "[INST] why is the sky blue? [/INST]",
  "raw": true,
  "stream": false
}'
```

--------------------------------

TITLE: Ollama API Chat Endpoint Documentation
DESCRIPTION: Documentation for the Ollama API's chat endpoint. This endpoint allows users to send messages to a specified model and receive AI-generated responses. It supports text-based messages and can also handle image data for multimodal interactions.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_39

LANGUAGE: APIDOC
CODE:
```
POST /api/chat

Send a chat message.

Request Body:
{
  "model": "string",
  "messages": [
    {
      "role": "string",
      "content": "string",
      "images": [
        "string"
      ]
    }
  ],
  "stream": "boolean",
  "options": {
    "temperature": "number"
  },
  "template": "string"
}

Parameters:
- model (string, required): The model to use for the chat.
- messages (array of objects, required):
  - role (string, required): The role of the message sender (e.g., 'user', 'assistant').
  - content (string, required): The text content of the message.
  - images (array of strings, optional): An array of Base64 encoded image strings.
- stream (boolean, optional): Whether to stream the response. Defaults to false.
- options (object, optional): Model-specific options.
  - temperature (number, optional): Controls the randomness of the output. Higher values make output more random.
- template (string, optional): A prompt template to use.

Response Body (if stream is false):
{
  "message": {
    "role": "string",
    "content": "string",
    "images": [
      "string"
    ]
  },
  "done": "boolean"
}

Response Body (if stream is true):
Stream of JSON objects, each containing:
{
  "message": {
    "role": "string",
    "content": "string",
    "images": [
      "string"
    ]
  },
  "done": "boolean"
}

Example:
```shell
curl http://localhost:11434/api/chat -d '{
  "model": "llava",
  "messages": [
    {
      "role": "user",
      "content": "what is in this image?",
      "images": ["base64_encoded_image_data"]
    }
  ]
}'
```
```

--------------------------------

TITLE: Generate Content with Image
DESCRIPTION: This API endpoint allows users to generate content by providing a prompt and an image. The `stream` parameter controls whether the response is streamed. The `images` parameter accepts a base64 encoded string of the image.

SOURCE: https://github.com/ollama/ollama/blob/main/docs/api.md#_snippet_13

LANGUAGE: shell
CODE:
```
curl http://localhost:11434/api/generate -d '{
  "model": "llava",
  "prompt":"What is in this picture?",
  "stream": false,
  "images": ["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
```