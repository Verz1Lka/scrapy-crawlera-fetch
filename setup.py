import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="scrapy_simple_fetch_middleware",
    version="0.0.1",
    license="BSD",
    description="Scrapy downloader middleware to interact with Crawlera Simple Fetch API",
    long_description=long_description,
    author="Scrapinghub",
    author_email="info@scrapinghub.com",
    url="https://github.com/scrapinghub/scrapy-uncork",
    packages=["simple_fetch_middleware"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)