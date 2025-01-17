from setuptools import setup, find_packages

setup(
    name="pi_full_monitor",
    version="1.0.0",
    description="A Raspberry Pi performance monitoring CLI tool",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pi_full_monitor=pi_monitor.monitor:main',
        ],
    },
    install_requires=[
        "psutil>=6.0.0",
        "rich>=13.0.0"
    ],
    python_requires=">=3.7",
)
