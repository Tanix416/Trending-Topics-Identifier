import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_ipynb(notebook_path):
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

    # Create an execution preprocessor
    execute_preprocessor = ExecutePreprocessor(timeout=-1, kernel_name='python3')

    # Execute the notebook
    try:
        execute_preprocessor.preprocess(notebook, {'metadata': {'path': '.'}})
    except Exception as e:
        raise Exception(f"Error executing the notebook: {e}")

if __name__ == '__main__':
    notebook_path = 'pintrest.ipynb'
    run_ipynb(notebook_path)
    notebook_path = 'x.ipynb'
    run_ipynb(notebook_path)
    notebook_path = 'thread.ipynb'
    run_ipynb(notebook_path)
    notebook_path = 'dataPost.ipynb'
    run_ipynb(notebook_path)
    

