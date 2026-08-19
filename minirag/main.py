def read_document(path):
    """Read a text file and return its contents as one string."""
    with open(path, "r", encoding="utf-8") as f:    # open it, auto-close after
        return f.read()                             # hand the whole text back


def filter_lines(text, min_length=15):
    """Split text into lines, drop blanks and short ones."""
    kept = []                                       # empty box to collect into

    for line in text.splitlines():                  # splitlines = one item per line
        clean = line.strip()                        # kill leading/trailing spaces

        if clean == "":                             # blank line?
            continue                                # skip it, go to next line

        if len(clean) < min_length:                 # too short to be useful?
            continue                                # skip it too

        kept.append(clean)                          # survived both checks — keep it

    return kept                                     # hand back the surviving lines


def label_line(line):
    """Decide what kind of line this is. Returns one word."""
    lower = line.lower()                            # compare in lowercase so case doesn't matter

    if "error" in lower or "fail" in lower:
        return "PROBLEM"                            # returns exit the function right here
    if "queue" in lower or "worker" in lower:
        return "QUEUE"
    if line.endswith(":"):
        return "HEADING"

    return "TEXT"                                   # nothing matched — the fallback


def build_records(lines, source):
    """Turn plain lines into a list of dictionaries with metadata."""
    records = []

    for i, line in enumerate(lines):                # i = position number, line = the text
        record = {                                  # one dict per line
            "id": i,
            "text": line,
            "label": label_line(line),              # calling our own function inside another
            "payload": {                            # a dict nested inside a dict
                "source": source,
                "length": len(line)
            }
        }
        records.append(record)

    return records


def count_labels(records):
    """Count how many records carry each label."""
    counts = {}                                     # empty dict to tally into

    for record in records:
        label = record["label"]                     # dig the label out of the record
        counts[label] = counts.get(label, 0) + 1    # old count (or 0), plus one, stored back

    return counts


path = r"C:\pyth\minirag\DATA\true_data\parallel_work_queue.txt"

text = read_document(path)                          # step 1: get the text
lines = filter_lines(text)                          # step 2: clean it
records = build_records(lines, "parallel_work_queue.txt")   # step 3: structure it
counts = count_labels(records)                      # step 4: summarise it

print(f"lines kept: {len(lines)}")
print(f"records: {len(records)}")

for label, n in counts.items():                     # .items() gives key and value together
    print(f"{label}: {n}")