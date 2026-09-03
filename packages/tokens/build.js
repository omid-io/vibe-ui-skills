const fs = require('fs');
const path = require('path');
let ts;
try {
  ts = require('typescript');
} catch (e) {
  try {
    ts = require('../../examples/nextjs-starter/node_modules/typescript');
  } catch (e2) {
    console.error('Error: typescript is required to build @omid-io/tokens.');
    process.exit(1);
  }
}

const distDir = path.join(__dirname, 'dist');
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
}

const files = [
  path.join(__dirname, 'src', 'index.ts'),
  path.join(__dirname, 'src', 'tailwind.ts'),
  path.join(__dirname, 'src', 'registry', 'components.ts'),
  path.join(__dirname, 'src', 'cli.ts')
];

const typesDir = path.resolve(__dirname, '../../examples/nextjs-starter/node_modules/@types');

// Compile CommonJS and .d.ts
const cjsOptions = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.CommonJS,
  declaration: true,
  outDir: distDir,
  strict: true,
  esModuleInterop: true,
  moduleResolution: ts.ModuleResolutionKind.Node10,
  typeRoots: [typesDir],
  types: ['node'],
  skipLibCheck: true,
};

const cjsProgram = ts.createProgram(files, cjsOptions);
const cjsDiagnostics = ts.getPreEmitDiagnostics(cjsProgram);
if (cjsDiagnostics.length > 0) {
  const formatHost = {
    getCanonicalFileName: (f) => f,
    getCurrentDirectory: ts.sys.getCurrentDirectory,
    getNewLine: () => ts.sys.newLine,
  };
  const message = ts.formatDiagnosticsWithColorAndContext(cjsDiagnostics, formatHost);
  console.error(message);
  process.exit(1);
}
cjsProgram.emit();

// Compile ESM (.mjs)
const esmOptions = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.ESNext,
  declaration: false,
  outDir: distDir,
  strict: true,
  esModuleInterop: true,
  moduleResolution: ts.ModuleResolutionKind.Node10,
  typeRoots: [typesDir],
  types: ['node'],
  skipLibCheck: true,
};

const esmProgram = ts.createProgram(files, esmOptions);
const emitResult = esmProgram.emit(undefined, (fileName, data) => {
  if (fileName.endsWith('.js')) {
    const mjsName = fileName.replace(/\.js$/, '.mjs');
    fs.writeFileSync(mjsName, data);
  } else {
    fs.writeFileSync(fileName, data);
  }
});

// Prepend shebang to dist/cli.js if not present
const cliPath = path.join(distDir, 'cli.js');
if (fs.existsSync(cliPath)) {
  let cliContent = fs.readFileSync(cliPath, 'utf-8');
  if (!cliContent.startsWith('#!/usr/bin/env node')) {
    cliContent = '#!/usr/bin/env node\n' + cliContent;
    fs.writeFileSync(cliPath, cliContent, 'utf-8');
  }
  try {
    fs.chmodSync(cliPath, 0o755);
  } catch (e) {}
}

console.log('✅ @omid-io/tokens build complete: CLI, ESM, CJS, and .d.ts generated in dist/');
