from setuptools import setup, find_packages


setup(
    name="scscore",
    version="0.1.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "": [
            "models/full_reaxys_model_1024bool/*.gz",
            "models/full_reaxys_model_1024unit/*.gz",
            "models/full_reaxys_model_2048bool/*.gz",
        ]
    },
    include_package_data=True,
)
