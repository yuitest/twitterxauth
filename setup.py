from setuptools import find_packages, setup

version = '0.0.2'

setup(
    name='twitterxauth',
    version=version,
    description="thin wrapper module for xAuth twitter.com",
    long_description="""\
""",
    classifiers=[
    ],
    keywords='twitter xauth',
    author='yuitest',
    author_email='yuitest+git@cjhat.net',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httplib2>=0.9',
        'oauth2>=1.5',
    ],
    entry_points="""
    # -*- Entry points: -*-
""",
)
