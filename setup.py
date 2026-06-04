# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="robocasa",
    packages=[package for package in find_packages() if package.startswith("robocasa")],
    install_requires=[
        "numpy==1.23.3",
        "numba==0.56.4",
        "scipy>=1.2.3",
        "mujoco==3.2.6",
        "pygame",
        "Pillow",
        "opencv-python",
        "pyyaml",
        "pynput",
        "tqdm",
        "termcolor",
        "imageio",
        "h5py",
        "lxml",
        "hidapi",
        "tianshou==0.4.10",
        # --- whole-body IK + data tooling needed by the GR1 / abstract paths ---
        # mink 0.0.10 is the last release that (a) keeps the `mink.tasks.exceptions`
        # import path used by robosuite's mink_controller and (b) requires
        # mujoco>=3.1.6 (compatible with the pinned mujoco==3.2.6). mink 0.0.11+
        # moved that symbol (ImportError) and 1.x requires mujoco>=3.3 (conflicts
        # with 3.2.6), so an unpinned mink breaks `--robots GR1TwoHand`.
        "mink==0.0.10",
        "quadprog",          # default QP backend for mink.solve_ik
        "huggingface_hub",   # used by scripts/download_mimicdroid_dataset.py
    ],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="RoboCasa: Large-Scale Simulation of Household Tasks for Generalist Robots",
    author="Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, Yuke Zhu",
    url="https://github.com/robocasa/robocasa",
    author_email="soroush@cs.utexas.edu",
    version="0.2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
