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

# Replace this with the path to your Renovate configuration file
config_file_path = "renovate.json"

try:
    # Read and parse the Renovate configuration file
    with open(config_file_path, 'r') as file:
        configuration = json.load(file)

    # Validate regex patterns
    validate_regex_patterns(configuration)

    print("Validation complete. No errors found.")

except FileNotFoundError:
    print(f"Error: Renovate configuration file not found at {config_file_path}")
except json.JSONDecodeError as e:
    print(f"Error: Unable to parse Renovate configuration. {e}")
