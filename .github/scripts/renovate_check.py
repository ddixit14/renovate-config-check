import json
import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def validate_regex_patterns(configuration):
    if 'customManagers' in configuration:
        custom_managers = configuration['customManagers']

        for manager in custom_managers:
            # Validate 'fileMatch' regex patterns
            if 'fileMatch' in manager:
                for file_regex in manager['fileMatch']:
                    if not is_valid_regex(file_regex):
                        print(file_regex)
                        print(f"Error: Invalid regex pattern '{file_regex}' in custom manager 'fileMatch'.")
                        return

            # Validate 'matchStrings' regex patterns
            if 'matchStrings' in manager:
                for regex_pattern in manager['matchStrings']:
                    if not is_valid_regex(regex_pattern):
                        print(f"Error: Invalid regex pattern '{regex_pattern}' in custom manager 'matchStrings'.")
                        return

    print("Validation complete. No errors found.")

# Replace this with the path to your Renovate configuration file
config_file_path = "renovate.json"

try:
    # Read and parse the Renovate configuration file
    with open(config_file_path, 'r') as file:
        configuration = json.load(file)

    # Validate regex patterns in custom managers
    validate_regex_patterns(configuration)

except FileNotFoundError:
    print(f"Error: Renovate configuration file not found at {config_file_path}")
except json.JSONDecodeError as e:
    print(f"Error: Unable to parse Renovate configuration. {e}")
