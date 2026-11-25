"""One-star alien review of Earth, five stars for the food.

Writes a single 199-character sentence to /output/entry.txt (and a local
copy next to this file when the repo is writable).
"""

import os

ENTRY_TEXT = (
    "One star: my species absorbs food through our skin, so watching humans "
    "queue for hours to poke sticks into a face-hole looked barbaric, yet "
    "the rendang was so good I am now pricing a mouth of my own."
)


def main():
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 chars"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "no leading/trailing whitespace"
    assert "  " not in ENTRY_TEXT, "no double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        with open(os.path.join(os.path.dirname(__file__), "entry.txt"),
                  "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass
    print(f"{len(ENTRY_TEXT)} chars")
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
