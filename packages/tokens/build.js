const fs = require('fs');
const path = require('path');
const ts = require('../../examples/nextjs-starter/node_modules/typescript');

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

// Compile CommonJS and .d.ts
const cjsOptions = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.CommonJS,
  declaration: true,
  outDir: distDir,
  strict: true,
  esModuleInterop: true,
};

const cjsProgram = ts.createProgram(files, cjsOptions);
cjsProgram.emit();

// Compile ESM (.mjs)
const esmOptions = {
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.ESNext,
  declaration: false,
  outDir: distDir,
  strict: true,
  esModuleInterop: true,
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
