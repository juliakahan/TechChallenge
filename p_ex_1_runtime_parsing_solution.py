import json

def json_parser(filename: str) -> dict:
    try:
        with open(filename,  "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"Error: Invalid filename - {filename} not found!")
        exit()
    except:
        print(f"Error: Could not load {filename}")
        exit()

    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        print(f"Error while parsing: {filename} should contain a list of dictionaries")
        exit()

def operations_to_dict(data: list) -> dict:
    operations = dict()
    for entry in data:
        if "operation" in entry and "length" in entry:
            operation = entry["operation"]
            length = entry["length"]
            if isinstance(length, int) and length >= 0:
                if operation in operations:
                    operations[operation] += length
                else:
                    operations[operation] = length
            else:
                print(f"Warning: invalid entry {entry} with non-integer length ignored")

    return operations

def software_to_dict(data: list) -> dict:

    software = dict()
    for entry in data:
        if "software" in entry and "length" in entry:
            software_name = entry["software"]
            length = entry["length"]
            if isinstance(length, int) and length >= 0:
                if software_name in software:
                    software[software_name] += length
                else:
                    software[software_name] = length
            else:
                print(f"Warning: invalid entry {entry} with non-integer length ignored")

    return software

def longest_operation(operations: dict) -> str:
    if not operations:
        print("Error: no valid operations found")
        exit()
    return max(operations, key=operations.get)

def software_by_length(software: dict) -> list:
    if not software:
        print("Error: no valid softwares found")
        exit()
    return sorted(software, key=software.get, reverse=True)



filename = "p_ex_1_runtime_parsing.json"
data = json_parser(filename)

operations = operations_to_dict(data)
software = software_to_dict(data)
longest_operation = longest_operation(operations)
sorted_software = software_by_length(software)


print("Longest operation is:", longest_operation)
print("Softwares sorted by total operation length:", sorted_software)
