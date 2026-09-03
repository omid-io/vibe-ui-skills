const fs = require('fs');
const path = require('path');
const ts = require('../../examples/nextjs-starter/node_modules/typescript');

const distDir = path.join(__dirname, 'dist');
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
}

const files = [path.join(__dirname, 'src', 'extension.ts')];

const options = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.CommonJS,
  declaration: false,
  outDir: distDir,
  strict: false,
  esModuleInterop: true,
  skipLibCheck: true
};

// Create a synthetic mock for vscode module during compilation
const program = ts.createProgram(files, options);
program.emit();

console.log('✅ vibe-ui-vscode build complete: dist/extension.js generated!');
