import sys
import json

def insert_vals(tests, temp):
    for test in tests:
        if "value" in test and test.get("id") in temp:
            test["value"] = temp[test["id"]]

        insert_vals(test.get("values", []), temp)

def main ():
    with open(sys.argv[1], encoding="utf-8") as f:
        vals = json.load(f)

    with open(sys.argv[2], encoding="utf-8") as f:
        tests = json.load(f)

    temp = {val["id"]: val["value"] for val in vals["values"]}
    insert_vals(tests["tests"], temp)

    with open(sys.argv[3], "w", encoding="utf-8") as f:
        json.dump(tests, f)

if __name__ == "__main__":
    main()