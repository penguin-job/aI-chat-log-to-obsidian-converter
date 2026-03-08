import os
import json
import re
from datetime import datetime


def sanitize_filename(title: str) -> str:
    """Replace characters that are invalid in Windows filenames."""
    return re.sub(r'[\\/:*?"<>|]', "_", title).strip() or "no_title"


def format_date(ts) -> str:
    """Convert UNIX timestamp to YYMMDD."""
    if ts is None:
        return "unknown_date"
    try:
        return datetime.utcfromtimestamp(ts).strftime("%y%m%d")
    except Exception:
        return "unknown_date"


def parts_to_text(parts) -> str:
    """Safely convert content.parts into plain text."""
    clean = []
    for part in parts or []:
        if isinstance(part, str):
            clean.append(part)
        elif isinstance(part, dict):
            clean.append(part.get("text", str(part)))
        else:
            clean.append(str(part))
    return "\n".join(clean).strip()


def extract_messages_linear(conv: dict):
    """
    Extract only the main conversation flow by tracing
    from current_node back to the root via parent links.
    """
    mapping = conv.get("mapping", {})
    current_node = conv.get("current_node")

    if not mapping or not current_node or current_node not in mapping:
        return []

    chain = []
    node_id = current_node
    seen = set()

    while node_id and node_id in mapping and node_id not in seen:
        seen.add(node_id)
        chain.append(node_id)
        node_id = mapping[node_id].get("parent")

    chain.reverse()

    messages = []
    for node_id in chain:
        node = mapping.get(node_id, {})
        message = node.get("message")
        if not message:
            continue

        content = message.get("content") or {}
        parts = content.get("parts") or []
        text = parts_to_text(parts)
        if not text:
            continue

        role = message.get("author", {}).get("role", "unknown")
        messages.append(f"**{role}**:\n{text}\n")

    return messages


def load_conversations(json_path: str):
    """Load exported conversation data from JSON."""
    with open(json_path, "r", encoding="utf-8") as file:
        raw = json.load(file)

    if isinstance(raw, dict) and "conversations" in raw:
        return raw["conversations"]
    return raw


def save_markdown(filepath: str, messages: list[str]) -> None:
    """Save extracted messages to a Markdown file."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("\n".join(messages))


def main():
    json_path = "conversations.json"
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(json_path):
        print(f"Error: '{json_path}' was not found.")
        print("Place conversations.json in the same folder as this script.")
        return

    conversations = load_conversations(json_path)

    count = 0
    skipped = 0

    for conv in conversations:
        title_raw = conv.get("title") or "no_title"
        title = sanitize_filename(title_raw)

        create_ts = conv.get("create_time")
        date_str = format_date(create_ts)

        filename = f"{date_str}_{title}.md"
        filepath = os.path.join(output_folder, filename)

        messages = extract_messages_linear(conv)
        if not messages:
            skipped += 1
            continue

        save_markdown(filepath, messages)
        count += 1
        print(f"Saved: {filepath}")

    print(f"\nCreated {count} Markdown file(s).")
    if skipped:
        print(f"Skipped: {skipped} conversation(s).")


if __name__ == "__main__":
    main()