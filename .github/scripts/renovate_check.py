import json
import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def validate_regex_patterns(configuration):
    # Check if 'regexPatterns' key is present in the configuration
    if 'regexPatterns' in configuration:
        regex_patterns = configuration['regexPatterns']

        # Validate each regex pattern
        for pattern_key, pattern_value in regex_patterns.items():
            if not is_valid_regex(pattern_value):
                print(f"Error: Invalid regex pattern '{pattern_value}' for key '{pattern_key}'.")

# Modify the existing function to include regex validation
def verify_renovate_configuration(repository_path):
    config_file_path = f"{repository_path}/renovate.json"

    try:
        with open(config_file_path, 'r') as file:
            configuration = json.load(file)

        # Check for required keys in the configuration
        required_keys = ['extends', 'packages']
        for key in required_keys:
            if key not in configuration:
                print(f"Error: '{key}' is missing in the Renovate configuration.")
                return

        # Validate regex patterns
        validate_regex_patterns(configuration)

        # If no errors were found, print the configuration
        print("Renovate Bot configuration is valid:")
        print(json.dumps(configuration, indent=2))

    except FileNotFoundError:
        print(f"Error: Renovate configuration file not found at {config_file_path}")
    except json.JSONDecodeError as e:
        print(f"Error: Unable to parse Renovate configuration. {e}")

# Replace this with the path to your local repository
repository_path = "/path/to/your/repository"

# Call the function to verify the configuration
verify_renovate_configuration(repository_path)
