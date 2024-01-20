# End-to-End-ML-Project-with-MLflow

## Workflows

1. Update config.yaml => add required paths to the config.yaml
2. Update schema.yaml => add column names and types to schema.yaml
3. Update params.yaml
4. Update the entity => define a class with @dataclass decorator and map each name in config.yaml as well as schema with its corresponding object
5. Update the configuration manager in src config => read yaml files and create corresponding directories and returning files
6. Update the components => check data, uzip, download, or check if all columns are proper for validation
7. Update the pipeline => combine all the previous approaches and call the functions within classes
8. Update the main.py
9. Update the app.py
