import setuptools

setuptools.setup(
    name="extension_chatterbox",
    packages=setuptools.find_namespace_packages(),
    version="2.0.1",
    author="rsxdalv",
    description="Chatterbox TTS extension for text-to-speech generation.",
    url="https://github.com/rsxdalv/extension_chatterbox",
    project_urls={},
    scripts=[],
    install_requires=[
        "gradio",
        # "chatterbox-tts"
        # "chatterbox-tts @ git+https://github.com/rsxdalv/chatterbox@fast",
        "chatterbox-tts @ git+https://github.com/nilreml/chatterbox@fast",
        # "peft",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
