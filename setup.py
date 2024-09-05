from setuptools import setup, find_packages


setup(
    name="scscore",
    author="Connor Coley",
    version="0.1.2",
    packages=find_packages("scscore"),
    package_data={
        "scscore": [
            "models/full_reaxys_model_1024bool/*.gz",
            "models/full_reaxys_model_1024unit/*.gz",
            "models/full_reaxys_model_2048bool/*.gz",
        ]
    },
    include_package_data=True,
)
