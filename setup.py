"""
    Twilio - Api

    This is the public Twilio REST API.  # noqa: E501

    The version of the OpenAPI document: 1.8.0
    Contact: support@twilio.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="Twilio - Api",
    author="Twilio Support",
    author_email="support@twilio.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Twilio - Api"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    This is the public Twilio REST API.  # noqa: E501
    """
)
