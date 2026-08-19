path = r"C:\pyth\minirag\DATA\true_data\parallel_work_queue.txt"

with open(path, "r",encoding="utf-8") as f:
    raw_text = f.read()

print(f"characters: {len(raw_text)}")

lines = raw_text.splitlines()
print(f"Lines : {len(lines)}")
print("----Formtting----")

kept = []
skipped_blank = 0
skipped_short = 0

for line in lines:
    clean = line.strip()

    if clean == "":
        skipped_blank = skipped_blank + 1
        continue

    if len(clean) < 15:
        skipped_short = skipped_short + 1
        continue

    kept.append(clean)

print(f"kept: {len(kept)}")
print(f"skipped blank: {skipped_blank}")
print(f"skipped short: {skipped_short}")

print("----Labelling----")

records = []
counts = {}

for i, line in enumerate(kept):
    lower = line.lower()

    if "fail" in lower or "error" in lower:
        label = "PROBLEM"
    elif "queue" in lower or "worker" in lower:
        label = "QUEUE"
    elif line.endswith(":"):
        label = "HEADING"
    else:
        label = "TEXT"

    record = {
        "id" : i,
        "label" : label,
        "text":line,
        "payload":{
            "source": "parallel_work_queue.txt",
            "source_type": "true",
            "length": len(line) 
        }
    }

    records.append(record)
    counts[label] = counts.get(label, 0) + 1

print(f"records built: {len(records)}")

print("--- counts ---")
for label, n in counts.items():
    print(f"{label}: {n}")

print("--- first record ---")
first = records[0]
print(first)
print(first["id"])
print(first["text"])
print(first["payload"]["source"])

print("--- problems only ---")
for record in records:
    if record["label"] == "PROBLEM":
        print(record["id"], record["text"][:60])

"""
Longest problem. Loop through records and 
find the PROBLEM record with the longest text. Print its id and text.

"""
longest_problem = None

for record in records:
    if record["label"] == "PROBLEM":
        if longest_problem is None or len(record["text"]) > len(longest_problem["text"]):
            longest_problem = record

print("--- longest problem ---")
print(longest_problem["id"])
print(longest_problem["text"])

"""
Sort the counts. Print the label counts from most common to least. 
Hint: sorted(counts.items(), key=lambda pair: pair[1], reverse=True) — 
you won't fully understand lambda yet, that's fine, just use it and note it in PATTERNS.md.

"""

print("--- sorted counts ---")

sorted_counts = sorted(
    counts.items(),
    key=lambda pair: pair[1],
    reverse=True
)

for label, n in sorted_counts:
    print(f"{label}: {n}")