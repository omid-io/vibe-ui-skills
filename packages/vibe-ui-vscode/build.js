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

const localTypesDir = path.resolve(__dirname, 'node_modules/@types');
const fallbackTypesDir = path.resolve(__dirname, '../../examples/nextjs-starter/node_modules/@types');
const detectedTypeRoots = [localTypesDir, fallbackTypesDir].filter(d => fs.existsSync(d));

const files = [
  path.join(__dirname, 'src', 'vscode.d.ts'),
  path.join(__dirname, 'src', 'extension.ts')
];

const options = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.CommonJS,
  declaration: false,
  outDir: distDir,
  strict: true,
  esModuleInterop: true,
  moduleResolution: ts.ModuleResolutionKind.Node10,
  typeRoots: detectedTypeRoots.length > 0 ? detectedTypeRoots : undefined,
  types: ['node'],
  skipLibCheck: true
};

const program = ts.createProgram(files, options);
const diagnostics = ts.getPreEmitDiagnostics(program);
if (diagnostics.length > 0) {
  const formatHost = {
    getCanonicalFileName: (f) => f,
    getCurrentDirectory: ts.sys.getCurrentDirectory,
    getNewLine: () => ts.sys.newLine,
  };
  console.error(ts.formatDiagnosticsWithColorAndContext(diagnostics, formatHost));
  process.exit(1);
}
program.emit();

console.log('✅ vibe-ui-vscode build complete: dist/extension.js generated!');
