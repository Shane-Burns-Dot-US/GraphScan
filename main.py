import subprocess
import os
import json
import logging
import ast
import traceback
from graphviz import Digraph, Graph

#!! Change this to the path where your Python files are located
sample_directory = '/mnt/c/your_folder_path'  # Updated path for Linux

# Check if the script is in the correct directory
script_directory = os.path.dirname(os.path.abspath(__file__))
if script_directory != os.getcwd():
    raise EnvironmentError("The script is not in the current working directory. "
                           "Please ensure that the 'main.py' file is located in "
                           "the directory from which you are running the script.")

# Check if the sample directory is in the correct format for the current OS
if os.name == 'posix' and '\\' in sample_directory:
    raise ValueError("The directory path appears to be in Windows format, but you are running on Linux. "
                     "Please update the 'sample_directory' variable to use the Linux file path format.")

logging.basicConfig(filename='graph_scan.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def decide_graph_type(component_map):
    return ['directed', 'undirected']

def parse_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            node = ast.parse(file.read(), filename=file_path)
        class_names = [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]
        function_names = [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]
        print(f"Classes found: {class_names}, Functions found: {function_names}")
        return {'classes': class_names, 'functions': function_names}
    except SyntaxError as se:
        logging.error(f"SyntaxError in file {file_path}: {se}")
        return {'classes': [], 'functions': []}


logging.basicConfig(filename='graph_scan.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def decide_graph_type(component_map):
    return ['directed', 'undirected']

def parse_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            node = ast.parse(file.read(), filename=file_path)
        class_names = [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]
        function_names = [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]
        return {'classes': class_names, 'functions': function_names}
    except SyntaxError as se:
        logging.error(f"SyntaxError in file {file_path}: {se}")
        return {'classes': [], 'functions': []}

def generate_graph(component_map, file_name, graph_type, directory_path):
    print(f"Generating {graph_type} graph for {file_name}")
    graph = Digraph(name=f'{file_name}_{graph_type}') if graph_type == 'directed' else Graph(name=f'{file_name}_{graph_type}')
    for cls in component_map['classes']:
        graph.node(cls, cls, shape='box')
    for func in component_map['functions']:
        graph.node(func, func)
    for cls in component_map['classes']:
        for func in component_map['functions']:
            graph.edge(cls, func)
    output_file_name = f'{file_name}_{graph_type}.png'
    output_file_path = os.path.join(directory_path, output_file_name)
    print(f"Output path for the graph: {output_file_path}")
    try:
        graph.render(output_file_path, format='png', cleanup=True, view=True)
        print(f"Graph saved to {output_file_path}")
    except Exception as e:
        print(f"Failed to render graph: {e}")
        traceback.print_exc()
        output_file_path = None
    return output_file_path

def generate_all_graphs(component_map, file_name, directory_path):
    graphs_info = []
    types = decide_graph_type(component_map)
    for graph_type in types:
        graph_path = generate_graph(component_map, file_name, graph_type, directory_path)
        if graph_path:
            graphs_info.append(graph_path)
    return graphs_info

def graph_scan_enhanced(directory_path):
    error_report = []
    graphs_info = []
    os.makedirs(directory_path, exist_ok=True)
    print(f"Searching for Python files in {directory_path}")
    for subdir, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(subdir, file)
                print(f"Found Python file: {file_path}")
                try:
                    component_map = parse_python_file(file_path)
                    if component_map['classes'] or component_map['functions']:
                        graphs_info.extend(generate_all_graphs(component_map, os.path.splitext(file)[0], subdir))
                    else:
                        print(f"No components found in {file_path}")
                except Exception as e:
                    error_message = f"Error processing {file_path}: {e}"
                    print(error_message)
                    logging.error(error_message)
                    traceback.print_exc()  # Print the traceback
                    error_report.append({'file': file_path, 'error': str(e)})
    report_path = os.path.join(directory_path, 'graph_scan_error_report.json')
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as report_file:
        json.dump(error_report, report_file)
    return graphs_info, report_path

generated_graphs, error_report_path = graph_scan_enhanced(sample_directory)
print(f"Generated graphs: {generated_graphs}")
print(f"Error report path: {error_report_path}")

# Function to check if Graphviz is installed
def check_graphviz_installation():
    try:
        # Run 'dot -V' which should return the version of Graphviz if installed
        subprocess.run(['dot', '-V'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Graphviz is correctly installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise EnvironmentError("Graphviz does not appear to be installed or is not in the system's PATH.")

# Call the check at the beginning to ensure Graphviz is installed
check_graphviz_installation()
