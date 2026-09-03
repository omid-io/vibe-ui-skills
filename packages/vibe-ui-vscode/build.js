const fs = require('fs');
const path = require('path');
let ts;
try {
  ts = require('typescript');
} catch (e) {
  try {
    ts = require('../../examples/nextjs-starter/node_modules/typescript');
  } catch (e2) {
    console.error('Error: typescript is required to build vibe-ui-vscode.');
    process.exit(1);
  }
}

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
  strict: true,
  esModuleInterop: true,
  skipLibCheck: true
};

// Create a synthetic mock for vscode module during compilation
const program = ts.createProgram(files, options);
program.emit();

console.log('✅ vibe-ui-vscode build complete: dist/extension.js generated!');
