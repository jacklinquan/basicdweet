from setuptools import setup

setup(
    name="basicdweet",
    version="0.2.0",
    description="A python module for very basic APIs of the free dweet service.",
    long_description="https://github.com/jacklinquan/basicdweet",
    long_description_content_type="text/markdown",
    url="https://github.com/jacklinquan/basicdweet",
    author="Quan Lin",
    author_email="jacklinquan@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    packages=["basicdweet"],
    install_requires=["requests"],
)
