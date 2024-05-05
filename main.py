import sys
import subprocess
from pathlib import Path

from .problem import Problem
from .generators import *

def create_problem(
        problem_name=None, 
        source_code=None, 
        flags=[], 
        generator=None, 
        test_params=None, 
        output_dir=None
    ):
    if problem_name is None:    # infer from source file name
        problem_name = Path(source_code).stem

    try:
        subprocess.run(["g++", str(source_code), "-o", problem_name] + flags, check=True)
    except subprocess.CalledProcessError as err:
        print(err)
        sys.exit(1)

    return Problem(
        problem_name=problem_name, 
        source_code=source_code, 
        exec_path=problem_name, 
        generator=generator, 
        test_params=test_params, 
        output_dir=output_dir
    )

def get_generator(handle):
    return {
        "edge": edge_generator,
    }[handle]