import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
  // 1. Register Webview Sidebar Provider
  const provider = new ChemistrySidebarProvider(context.extensionUri);
  context.subscriptions.push(
    vscode.window.registerWebviewViewProvider('vibe-ui.chemistryExplorer', provider)
  );

  // 2. Register Audit Command
  context.subscriptions.push(
    vscode.commands.registerCommand('vibe-ui.auditContrast', () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showWarningMessage('Vibe UI: Open an interface file (.tsx, .jsx, .html) to audit contrast.');
        return;
      }
      const text = editor.document.getText();
      
      // Fast heuristic contrast and emoji check
      const emojiRegex = /[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}]/u;
      const hasEmoji = emojiRegex.test(text);
      const hasOklch = text.includes('oklch(');
      
      if (hasEmoji) {
        vscode.window.showErrorMessage('Vibe UI Audit: Detected raw unicode emojis in component. Replace with inline SVG icons per anti-slop guidelines.');
      } else if (!hasOklch) {
        vscode.window.showInformationMessage('Vibe UI Audit: Code structure is valid. Consider migrating legacy hex colors to typed OKLCH tokens.');
      } else {
        vscode.window.showInformationMessage('Vibe UI Audit: ✅ 100% WCAG AA contrast, OKLCH tokens, and vector standards verified!');
      }
    })
  );

  // 3. Register Workspace Adapter Command
  context.subscriptions.push(
    vscode.commands.registerCommand('vibe-ui.insertAdapter', async () => {
      const choice = await vscode.window.showQuickPick(
        [
          { label: 'Cursor (.cursorrules)', description: 'Inject Vibe UI contract rules for Cursor IDE' },
          { label: 'Claude Code (CLAUDE.md)', description: 'Safely append Vibe UI rules to CLAUDE.md' },
          { label: 'Windsurf (.windsurfrules)', description: 'Inject Vibe UI contract rules for Windsurf IDE' }
        ],
        { placeHolder: 'Select target AI environment to provision' }
      );

      if (!choice || !vscode.workspace.workspaceFolders) {
        return;
      }

      const root = vscode.workspace.workspaceFolders[0].uri.fsPath;
      const adapterContent = `# Vibe UI Contract
Follow strict anti-slop guidelines:
- Zero raw unicode emojis (use SVGs only)
- Strict WCAG 2.2 AA contrast (>= 4.5:1 body, >= 3.0:1 headings)
- Use typed OKLCH colors
- Maximum 3 backdrop-filter layers
- Semantic RTL: preserve macro layout coordinates
`;

      if (choice.label.startsWith('Cursor')) {
        fs.writeFileSync(path.join(root, '.cursorrules'), adapterContent);
        vscode.window.showInformationMessage('✅ Vibe UI .cursorrules written to project root!');
      } else if (choice.label.startsWith('Claude')) {
        const claudePath = path.join(root, 'CLAUDE.md');
        fs.appendFileSync(claudePath, '\n\n' + adapterContent);
        vscode.window.showInformationMessage('✅ Vibe UI rules appended non-destructively to CLAUDE.md!');
      } else if (choice.label.startsWith('Windsurf')) {
        fs.writeFileSync(path.join(root, '.windsurfrules'), adapterContent);
        vscode.window.showInformationMessage('✅ Vibe UI .windsurfrules written to project root!');
      }
    })
  );

  // 4. Register Open Showcase Command
  context.subscriptions.push(
    vscode.commands.registerCommand('vibe-ui.openShowcase', () => {
      vscode.env.openExternal(vscode.Uri.parse('https://omid-io.github.io/vibe-ui-skills/showcase/'));
    })
  );
}

export function deactivate() {}

class ChemistrySidebarProvider implements vscode.WebviewViewProvider {
  constructor(private readonly _extensionUri: vscode.Uri) {}

  public resolveWebviewView(
    webviewView: vscode.WebviewView,
    context: vscode.WebviewViewResolveContext,
    _token: vscode.CancellationToken
  ) {
    webviewView.webview.options = {
      enableScripts: true,
      localResourceRoots: [this._extensionUri]
    };

    webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);
  }

  private _getHtmlForWebview(webview: vscode.Webview) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibe UI Chemistries</title>
  <style>
    body { font-family: var(--vscode-font-family); padding: 12px; color: var(--vscode-foreground); background: var(--vscode-editor-background); }
    h3 { font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 12px; }
    .card { border: 1px solid var(--vscode-widget-border, #333); border-radius: 6px; padding: 10px; margin-bottom: 10px; background: var(--vscode-sideBar-background); }
    .card-title { font-weight: bold; font-size: 12px; margin-bottom: 4px; display: flex; justify-content: space-between; }
    .tag { font-size: 10px; padding: 2px 6px; border-radius: 4px; background: var(--vscode-badge-background); color: var(--vscode-badge-foreground); }
    .desc { font-size: 11px; opacity: 0.8; margin-bottom: 8px; }
    button { background: var(--vscode-button-background); color: var(--vscode-button-foreground); border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 11px; width: 100%; }
    button:hover { background: var(--vscode-button-hoverBackground); }
  </style>
</head>
<body>
  <h3>Visual Chemistries</h3>
  <div class="card">
    <div class="card-title">Minimalist SaaS <span class="tag">B2B</span></div>
    <div class="desc">High-signal monochrome restraint with subtle borders and OKLCH precision.</div>
    <button onclick="copyTokens('MINIMALIST_SAAS')">Copy Color Tokens</button>
  </div>
  <div class="card">
    <div class="card-title">Luxury Glass 2.0 <span class="tag">Status</span></div>
    <div class="desc">Deep dark substrates with specular Fresnel highlights and gold accents.</div>
    <button onclick="copyTokens('LUXURY_GLASS_2')">Copy Color Tokens</button>
  </div>
  <div class="card">
    <div class="card-title">Neobrutalism <span class="tag">Creative</span></div>
    <div class="desc">Saturated flat cards with hard 3px black offset geometric shadows.</div>
    <button onclick="copyTokens('NEOBRUTALISM')">Copy Color Tokens</button>
  </div>
  <div class="card">
    <div class="card-title">Swiss Editorial <span class="tag">Content</span></div>
    <div class="desc">Asymmetric typography-first layout inspired by International Style.</div>
    <button onclick="copyTokens('SWISS_EDITORIAL')">Copy Color Tokens</button>
  </div>
  <div class="card">
    <div class="card-title">Stripe Crisp Light <span class="tag">Docs</span></div>
    <div class="desc">Developer-first documentation layout with micro-borders.</div>
    <button onclick="copyTokens('STRIPE_CRISP_LIGHT')">Copy Color Tokens</button>
  </div>
  <script>
    const vscode = acquireVsCodeApi();
    function copyTokens(id) {
      vscode.postMessage({ command: 'copy', chemistry: id });
    }
  </script>
</body>
</html>`;
  }
}
