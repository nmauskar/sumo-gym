import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {
    "plot": [
        "matplotlib >=3.0",
        "scipy >=1.4",
        "iminuit >=2",
        "mplhep >=0.2.16",
    ],
    "test": [
        "pytest >=6",
        "pytest-mpl >=0.12",
    ],
}

extras_require["dev"] = [*extras_require["test"], *extras_require["plot"], "ipykernel"]

extras_require["docs"] = [
    *extras_require["plot"],
    "nbsphinx",
    "Sphinx >=3.0.0",
    "sphinx_copybutton",
    "sphinx_rtd_theme >=0.5.0",
    "sphinx_book_theme >=0.0.38",
    "ipython",
    "ipykernel",
    "pillow",
    "uncertainties>=3",
    "myst_parser>=0.14",
]

extras_require["all"] = sorted(set(sum(extras_require.values(), [])))

setuptools.setup(
    name="sumo_gym",
    version="0.0.1",
    author="Shuo Liu",
    author_email="ninomyemail@gmail.com",
    description="OpenAI-gym like toolkit for developing and comparing reinforcement learning algorithms on SUMO.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lovelybuggies/sumo-gym",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["gym"],
    extras_require=extras_require,
)
