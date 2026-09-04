import zipfile
import json
from pathlib import Path

pkg_dir = Path(__file__).resolve().parent

with open(pkg_dir / "package.json", "r", encoding="utf-8") as f:
    pkg_data = json.load(f)
version = pkg_data.get("version", "2.4.2")
out_vsix = pkg_dir / f"vibe-ui-vscode-{version}.vsix"

vsix_manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Id="vibe-ui-vscode" Version="{version}" Language="en-US" Publisher="omid-io"/>
    <DisplayName>Vibe UI — Design Systems &amp; Contrast Linter</DisplayName>
    <Description>Deterministic design contracts, visual chemistries, and WCAG contrast linter for VS Code, Cursor &amp; Windsurf</Description>
    <Icon>extension/media/icon.png</Icon>
    <Categories>Linters,Programming Languages,Other</Categories>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
  </Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/CHANGELOG.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="extension/media/icon.png" Addressable="true"/>
  </Assets>
</PackageManifest>"""

content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json"/>
  <Default Extension="vsixmanifest" ContentType="text/xml"/>
  <Default Extension="md" ContentType="text/markdown"/>
  <Default Extension="png" ContentType="image/png"/>
  <Default Extension="svg" ContentType="image/svg+xml"/>
  <Default Extension="js" ContentType="application/javascript"/>
</Types>"""

files_to_pack = [
    ("package.json", "extension/package.json"),
    ("README.md", "extension/README.md"),
    ("CHANGELOG.md", "extension/CHANGELOG.md"),
    ("media/icon.png", "extension/media/icon.png"),
    ("media/icon.svg", "extension/media/icon.svg"),
    ("dist/extension.js", "extension/dist/extension.js"),
]

missing_files = [src_rel for src_rel, _ in files_to_pack if not (pkg_dir / src_rel).exists()]
if missing_files:
    raise FileNotFoundError(f"VSIX Packaging Error: Missing required build artifacts: {', '.join(missing_files)}. Run 'node build.js' first.")

with zipfile.ZipFile(out_vsix, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("extension.vsixmanifest", vsix_manifest)
    z.writestr("[Content_Types].xml", content_types)
    for src_rel, dest_rel in files_to_pack:
        src_path = pkg_dir / src_rel
        z.write(src_path, dest_rel)

print(f"[+] Packaged VS Code / Cursor Extension binary: {out_vsix} ({out_vsix.stat().st_size} bytes)")
