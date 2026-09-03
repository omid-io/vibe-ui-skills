#!/usr/bin/env python3
"""
scripts/fix_studio_syntax.py
Fixes JSON serialization in index.html & showcase/index.html so that newlines
are properly escaped as \\n in JavaScript string literals.
Verifies with Node.js syntax parsing.
"""

import json
import re
import sys
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
INDEX_PATH = ROOT_DIR / "index.html"
SHOWCASE_PATH = ROOT_DIR / "showcase" / "index.html"

# Import scenarios
import scripts.update_studio_26_styles as s
import scripts.inject_visual_themes as iv

def fix_file(file_path):
    scenarios = s.get_scenarios()
    
    # Inject visual styles into the scenario dictionary
    for key, styles in iv.STYLE_VISUAL_MAP.items():
        if key in scenarios:
            scenarios[key]["card_style"] = styles["card_style"]
            scenarios[key]["btn_style"] = styles["btn_style"]
            scenarios[key]["sec_btn_style"] = styles["sec_btn_style"]
            scenarios[key]["val_color"] = styles["val_color"]
            scenarios[key]["subval_color"] = styles["subval_color"]
            scenarios[key]["font_family"] = styles["font_family"]

    scenarios_js = json.dumps(scenarios, indent=6, ensure_ascii=False)

    content = file_path.read_text(encoding="utf-8")

    # Use lambda to prevent re.sub from treating backslashes as escape characters!
    pattern = r"const STUDIO_SCENARIOS\s*=\s*\{.*?\n\s*\};"
    replacement_str = f"const STUDIO_SCENARIOS = {scenarios_js};\n"

    new_content, count = re.subn(pattern, lambda m: replacement_str, content, flags=re.DOTALL)
    if count == 0:
        print(f"[FAIL] Could not match STUDIO_SCENARIOS in {file_path}")
        return False

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Fixed {file_path.name}")
    return True

def validate_syntax(file_path):
    node_script = f"""
    const fs = require('fs');
    const html = fs.readFileSync('{file_path.as_posix()}', 'utf8');
    const scriptStart = html.indexOf('<script>');
    const scriptEnd = html.lastIndexOf('</script>');
    const code = html.substring(scriptStart + 8, scriptEnd);
    try {{
      new Function(code);
      console.log('SUCCESS: {file_path.name} JavaScript parses cleanly with ZERO errors!');
    }} catch (err) {{
      console.error('ERROR in {file_path.name}:', err.message);
      process.exit(1);
    }}
    """
    res = subprocess.run(["node", "-e", node_script], capture_output=True, text=True)
    print(res.stdout.strip())
    if res.stderr.strip():
        print(res.stderr.strip())
    return res.returncode == 0

def main():
    fix_file(INDEX_PATH)
    fix_file(SHOWCASE_PATH)
    
    v1 = validate_syntax(INDEX_PATH)
    v2 = validate_syntax(SHOWCASE_PATH)

    if v1 and v2:
        print("🎉 ALL FILES VALIDATED 100% CLEAN BY NODE.JS VM!")
    else:
        print("❌ VALIDATION FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
