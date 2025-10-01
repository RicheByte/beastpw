from setuptools import setup, find_packages

setup(
    name="beastpw",
    version="3.0.0",
    description="Rebel Password Generator for ethical hacking and CTFs",
    author="PlinyTheHacker",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "beastpw": ["config.json"]
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "beastpw=beastpw.core:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)