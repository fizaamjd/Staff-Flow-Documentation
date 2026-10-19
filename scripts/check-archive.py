from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
records = json.loads((root / "docs/archive-inventory.json").read_text())
actual = {p.relative_to(root).as_posix() for p in (root / "Sprint 01 Documentation").glob("*.md")} | {p.relative_to(root).as_posix() for p in root.glob("*.pptx")}
assert actual == {r["path"] for r in records}, "Archive files changed; update the inventory intentionally"
for record in records:
    p = root / record["path"]
    assert p.stat().st_size == record["bytes"], record["path"]
    assert hashlib.sha256(p.read_bytes()).hexdigest() == record["sha256"], record["path"]
    assert bool(p.stat().st_size == 0) == (record["status"] == "empty-placeholder"), record["path"]
print(f"Archive integrity: {len(records)} artifacts, {sum(r['status']=='empty-placeholder' for r in records)} documented empty placeholders")
