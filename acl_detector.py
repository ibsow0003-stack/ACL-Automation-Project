# ACL Detection Script
# This script checks for overly permissive ACL rules

def detect_permissive_rules(config_file):
    risky_rules = []

    try:
        with open(config_file, "r") as file:
            lines = file.readlines()

        for line in lines:
            # check for overly permissive rules
            if "permit ip any any" in line.lower():
                risky_rules.append(line.strip())

        return risky_rules

    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return []


# main execution
config = "router_config.txt"
results = detect_permissive_rules(config)

print("Potentially Risky ACL Rules:")

if results:
    for rule in results:
        print(rule)
else:
    print("No risky rules found.")
