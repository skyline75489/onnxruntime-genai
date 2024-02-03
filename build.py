# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import subprocess
import os

def is_windows():
    return sys.platform.startswith("win")


def is_macOS():
    return sys.platform.startswith("darwin")


def is_linux():
    return sys.platform.startswith("linux")


def platform():
    return sys.platform


def run_subprocess(args, cwd=None, capture=False, dll_path=None, shell=False, env={}, log=None):  # noqa: B006
    env.update(os.environ.copy())
    stdout, stderr = (subprocess.PIPE, subprocess.STDOUT) if capture else (None, None)
    return subprocess.run(args, cwd=cwd, check=True, stdout=stdout, stderr=stderr, env=env, shell=shell)


def update_submodules():
    run_subprocess(["git", "submodule", "update", "--init", "--recursive"]).check_returncode()


def build():
    command = None
    if is_windows():
        command = ["cmake", "-G", '"Visual Studio 17 2022"', "-S", ".", "-B", "build"]
        run_subprocess(command).check_returncode()
    elif is_linux():
        cuda_version="cuda"
        cuda_arch=80
        cuda_compiler=f"/usr/local/{cuda_version}/bin/nvcc"

        env = {"CUDA_HOME": "/usr/local/cuda", "CUDNN_HOME": "/usr/lib/x86_64-linux-gnu/"}

        command = ["cmake", "-S", ".", "-B", "build", "-DCMAKE_CUDA_ARCHITECTURES=$cuda_arch", f"-DCMAKE_CUDA_COMPILER={cuda_compiler}", "-DCMAKE_POSITION_INDEPENDENT_CODE=ON", "-DUSE_CXX17=ON", "-DUSE_CUDA=ON"]
        run_subprocess(command, env=env).check_returncode()
        make_command = ["make"]
        run_subprocess(make_command, cwd="build", env=env).check_returncode()
    else:
        raise OSError(f"Unsupported platform {platform()}.")


if __name__ == "__main__":
    update_submodules()
    build()
