from setuptools import setup, find_packages

setup(
    name="pi-full-monitor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "pi_full_monitor=pi_full_monitor.cli:main",  # Adjust path to your main script
        ]
    },
)
