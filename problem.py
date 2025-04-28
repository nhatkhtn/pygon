import time
import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

class Problem:
    def __init__(self, problem_name, source_code=None, brute_force_exec=None, exec_path=None, generator=None, test_params=None, output_dir=None):
        self.problem_name = problem_name
        self.exec_path = exec_path
        self.brute_force_exec = brute_force_exec
        self.generator = generator
        self.test_params = test_params
        
        if output_dir is None:
            self.output_dir = Path(self.problem_name)
        else:
            self.output_dir = Path(output_dir) / self.problem_name

    def generate(self, regen_func=None):
        if self.output_dir.exists():
            logger.warning(f"Output dir for problem {self.problem_name} already exists!\n"
                            "Please make sure the directory is empty or does not contain any redundant files/tests.")
        else:
            self.output_dir.mkdir(exist_ok=True)

        for i, param in enumerate(self.test_params):
            num_regens = 0
            while True:
                input_name = f"{i}.in"
                with open(self.output_dir / input_name, 'w') as f:
                    self.generator(out=f, **param)

                output_name = f"{i}.out"
                with open(self.output_dir / input_name, 'r') as fin:
                    with open(self.output_dir / output_name, 'w') as fout:
                        start = time.time()

                        try:
                            subprocess.run([self.exec_path], stdin=fin, stdout=fout, check=True)
                        except subprocess.CalledProcessError as err:
                            print(err)
                        
                        end = time.time()

                if regen_func is not None:
                    with open(self.output_dir / input_name, 'r') as fin:
                        with open(self.output_dir / output_name, 'r') as fout:
                            if not regen_func(fin, fout):
                                print(f"Test {i} finished in {end - start:.6f} seconds")
                                if num_regens > 0:
                                    print(f"Test {i} re-generated {num_regens} times.")
                                break
                else:
                    print(f"Test {i} finished in {end - start:.6f} seconds")
                    break
                num_regens += 1
                
            
    def check(self):
        for i, _ in enumerate(self.test_params):
            input_name = f"{i}.in"
            output_name = f"{i}.out"
            checker_output_name = "checker.out"

            output_path = self.output_dir / output_name
            checker_output_path = checker_output_name
            with open(self.output_dir / input_name, 'r', encoding='utf-8') as fin:
                with open(checker_output_path, 'w', encoding='utf-8') as fout:
                    start = time.time()
                    try:
                        subprocess.run(["python", self.brute_force_exec], stdin=fin, stdout=fout, check=True)
                    except subprocess.CalledProcessError as err:
                        print(f"Checker failed on test {i}")
                        print(err)
                    end = time.time()

            try:
                subprocess.run(["fc", str(output_path), str(checker_output_path)], check=True)
            except subprocess.CalledProcessError as err:
                print(err)
                print(f"Checker returned WA on test {i}")
                break

            print(f"Test {i} finished in {end - start:.6f} seconds")
                