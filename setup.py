from setuptools import setup, find_packages

setup(
    name="pi_full_monitor",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "psutil",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "pi_full_monitor=pi_full_monitor:main",
        ],
    },
    author="Your Name",
    author_email="you@example.com",
    description="A full performance monitoring tool for Raspberry Pi",
    url="https://github.com/exfil0/pi_full_monitor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.7",
)
