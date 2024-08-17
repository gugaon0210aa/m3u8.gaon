from setuptools import setup, find_packages

setup(
    name="m3u8.gaon",  # 패키지 이름
    version="0.1.0",  # 초기 버전
    author="gugaon0210",
    author_email="ngng01010@naver.com",
    description="A simple package to download and combine m3u8 video segments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gugaon0210aa/m3u8.gaon",  # GitHub URL
    packages=find_packages(),
    install_requires=[
        "requests",
        "m3u8",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
