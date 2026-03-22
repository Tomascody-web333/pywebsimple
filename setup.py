from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("LICENSE", "r", encoding="utf-8") as fh:
    license_text = fh.read()

setup(
    name="pywebsimple",
    version="0.1.0",
    author="Tomascody-web333",
    author_email="general@homeserverlab.org",
    description="Create websites with only HTML, CSS and Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tomascody-web333/pywebsimple",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Flask>=2.0.0",
    ],
    keywords="web framework python html css",
    project_urls={
        "Documentation": "https://homeserverlab.org/pywebsimple",
        "Source": "https://github.com/Tomascody-web333/pywebsimple",
        "Tracker": "https://github.com/Tomascody-web333/pywebsimple/issues",
    },
)