from setuptools import setup, find_packages

setup(
    name="pi-monitor",
    version="1.0.0",
    description="A CLI dashboard to monitor Raspberry Pi performance.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "pi-monitor=pi_monitor.monitor:main",
        ]
    },
    python_requires=">=3.7",
)
