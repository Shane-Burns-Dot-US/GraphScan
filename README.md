# GraphScan
GraphScan is an open-source tool that creates Graphviz visuals of codebases for LLMs, overcoming their context limitations by providing clear, token-dense graphs.

# GraphScan Verbose

GraphScan is an innovative open-source tool engineered to enhance the comprehension and navigation of intricate codebases for developers and AI models, including advanced Large Language Models (LLMs). Utilizing Graphviz's powerful visualization technology, GraphScan automates the creation of detailed graphical documentation that clearly illustrates the interconnections and structures within a code repository.

## Problem

In the realm of software development and AI programming, Large Language Models such as GPT-4 are often constrained by their context window's size, limiting their ability to fully understand expansive codebases. This restriction can impede the LLM's efficiency in offering accurate code suggestions and insights.

## Solution

GraphScan transcends these limitations by transforming code architectures into dense, information-rich graphical formats. These visualizations serve as a bridge, allowing both LLMs and developers to swiftly grasp the codebase's architecture and interrelationships, all within a glance, and without being hindered by context window limitations.

## Features

- **Graphical Documentation**: Generates visual documentation of code repositories using Graphviz, enhancing code understandability.
- **AI/LLM-Friendly Format**: Creates dense, informative visualizations tailored for LLMs, facilitating a deeper understanding of complex code structures.
- **Customizable Scans**: Users can tailor scans to focus on various codebase elements, such as classes, functions, variables, etc.
- **Developer Workflow Integration**: Designed for seamless integration into developer workflows and AI-assisted programming environments.
- **Open Source Collaboration**: Invites community-driven development and enhancement through open-source collaboration.

## Getting Started

### Prerequisites

- Python 3.6+
- Graphviz installed and configured in the system's PATH

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/graphscan.git
```

Enter the directory:

```bash
cd graphscan
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Execute `main.py`, specifying the target directory:

```bash
python main.py --directory '/path/to/your/project'
```

### Configuration

Customize your scan with command-line flags:

- `--all`: Comprehensive details
- `--imports`: Import statements
- `--functions`: Functions
- `--classes`: Classes
- `--variables`: Variables

## Contributing

Community contributions are welcome! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and our code of conduct.

## License

GraphScan is distributed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.

## Acknowledgments

- Thanks to the Graphviz team for their exceptional graph visualization software.
