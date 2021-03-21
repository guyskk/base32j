from setuptools import setup

setup(
    name='base32j',
    version='0.0.1',
    description='Base32 exclude letter i j l o, without padding.',
    url='https://github.com/guyskk/base32j',
    author='guyskk',
    author_email='guyskk@qq.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    python_requires='>=3.6',
    py_modules=["base32j"],
)
