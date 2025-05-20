from setuptools import setup, find_packages

setup(
    name="constructioncompany",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.110.0",
        "uvicorn==0.23.2",
        "pydantic==2.5.2",
        "python-multipart==0.0.18",
        "httpx==0.27.0"
    ],
    extras_require={
        "dev": [
            "pytest==8.3.5",
            "pytest-cov==4.1.0"
        ]
    }
)