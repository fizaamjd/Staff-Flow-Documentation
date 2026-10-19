from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
files = sorted((root / "Sprint 01 Documentation").glob("*.md")) + sorted(root.glob("*.pptx"))
records = [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "status": "empty-placeholder" if p.stat().st_size == 0 else "historical-artifact"} for p in files]
(root / "docs/archive-inventory.json").write_text(json.dumps(records, indent=2) + "\n")
print(f"Indexed {len(records)} historical artifacts")
