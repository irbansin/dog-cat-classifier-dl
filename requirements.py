# requirements.py

required_packages = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "tensorflow",
    "tensorflow-hub",
    "Pillow",
    "opencv-python",
    "ipywidgets",
    "kagglehub"
]

if __name__ == "__main__":
    import subprocess
    for pkg in required_packages:
        subprocess.check_call(["pip", "install", pkg])