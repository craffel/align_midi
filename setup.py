from setuptools import setup

setup(
    name='align_midi',
    version='0.0',
    description='Code for aligning MIDI data to audio',
    author='Colin Raffel',
    author_email='craffel@gmail.com',
    url='https://github.com/craffel/align_midi',
    packages=['align_midi'],
    long_description='Code for aligning MIDI data to audio',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
    ],
    keywords='audio music mir dsp',
    license='MIT',
    install_requires=[
        'numpy >= 1.7.0',
        'scipy',
        'librosa',
    ],
)
