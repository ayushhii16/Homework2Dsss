from setuptools import setup, find_packages

setup(
    name="math-quiz-ayushi",
    version="0.1",
    description="A simple math quiz game in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Ayushi Jaimani",
    author_email="ayushhii16@gmail.com",
    url="https://github.com/ayushhii16/Homework2Dsss.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
    test_suite='tests', 
)