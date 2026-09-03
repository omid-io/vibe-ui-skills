#!/usr/bin/env node
import * as fs from 'fs';
import * as path from 'path';
import * as readline from 'readline';
import { COMPONENT_REGISTRY } from './registry/components';
import { VISUAL_CHEMISTRIES } from './index';
const VERSION = '2.4.0';
function printBanner() {
    console.log(`
\x1b[35m  ▲ VIBE UI CLI v${VERSION}\x1b[0m
  \x1b[90mDeterministic UI contracts & component primitives for AI coding assistants\x1b[0m
`);
}
function printHelp() {
    printBanner();
    console.log(`\x1b[1mUSAGE:\x1b[0m
  npx @omid-io/tokens <command> [options]
  vibe-ui <command> [options]

\x1b[1mCOMMANDS:\x1b[0m
  \x1b[32minit\x1b[0m               Initialize Vibe UI contracts, OKLCH tokens & AI rules in current project
  \x1b[32madd <component>\x1b[0m     Add an accessible, AI-native component template to your project
  \x1b[32mlist\x1b[0m               List all available component primitives in the registry

\x1b[1mOPTIONS:\x1b[0m
  -v, --version      Show CLI version
  -h, --help         Show help menu

\x1b[1mEXAMPLES:\x1b[0m
  npx @omid-io/tokens init
  npx @omid-io/tokens add thinking-drawer
  npx @omid-io/tokens add telemetry-hud
`);
}
function prompt(rl, query) {
    return new Promise((resolve) => rl.question(query, resolve));
}
const CONTRACT_RULES = `# Vibe UI Design & Code Quality Contract
# Generated via npx @omid-io/tokens init

Follow strict anti-slop guidelines:
- Zero raw unicode emojis (use inline SVGs only)
- Strict WCAG 2.2 AA contrast (>= 4.5:1 body, >= 3.0:1 headings)
- Use typed OKLCH color spaces for perceptual accuracy
- Strict maximum of 3 backdrop-filter / glass layers
- Semantic RTL: preserve physical macro coordinate stability
`;
async function handleInit() {
    printBanner();
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    try {
        console.log('\x1b[1mInitialize Vibe UI in current workspace:\x1b[0m\n');
        // 1. Select Visual Chemistry
        console.log('\x1b[36m1. Select Visual Chemistry:\x1b[0m');
        console.log('  [1] Minimalist SaaS (Monochrome restraint, high signal - Recommended)');
        console.log('  [2] Luxury Glass 2.0 (Specular Fresnel, deep dark, gold accents)');
        console.log('  [3] Neobrutalism (Hard 3px black offset shadows, bold high saturation)');
        console.log('  [4] Swiss Editorial (Asymmetric grid, typography-first, high contrast)');
        console.log('  [5] Stripe Crisp Light (Developer docs, precision micro-borders)');
        const chemChoice = (await prompt(rl, 'Choice [1-5] (default: 1): ')).trim() || '1';
        const chemMap = {
            '1': 'MINIMALIST_SAAS',
            '2': 'LUXURY_GLASS_2',
            '3': 'NEOBRUTALISM',
            '4': 'SWISS_EDITORIAL',
            '5': 'STRIPE_CRISP_LIGHT',
        };
        const selectedChemKey = chemMap[chemChoice] || 'MINIMALIST_SAAS';
        const selectedChem = VISUAL_CHEMISTRIES[selectedChemKey];
        // 2. Select AI Editor
        console.log('\n\x1b[36m2. Select AI Coding Environment:\x1b[0m');
        console.log('  [1] Cursor (.cursorrules - Recommended)');
        console.log('  [2] Claude Code (CLAUDE.md)');
        console.log('  [3] Windsurf (.windsurfrules)');
        console.log('  [4] All of the above');
        const editorChoice = (await prompt(rl, 'Choice [1-4] (default: 1): ')).trim() || '1';
        // 3. Write contract rules
        const cwd = process.cwd();
        const createdFiles = [];
        if (editorChoice === '1' || editorChoice === '4') {
            fs.writeFileSync(path.join(cwd, '.cursorrules'), CONTRACT_RULES, 'utf-8');
            createdFiles.push('.cursorrules');
        }
        if (editorChoice === '2' || editorChoice === '4') {
            const claudePath = path.join(cwd, 'CLAUDE.md');
            if (fs.existsSync(claudePath)) {
                fs.appendFileSync(claudePath, `\n\n${CONTRACT_RULES}`, 'utf-8');
            }
            else {
                fs.writeFileSync(claudePath, CONTRACT_RULES, 'utf-8');
            }
            createdFiles.push('CLAUDE.md');
        }
        if (editorChoice === '3' || editorChoice === '4') {
            fs.writeFileSync(path.join(cwd, '.windsurfrules'), CONTRACT_RULES, 'utf-8');
            createdFiles.push('.windsurfrules');
        }
        // 4. Generate CSS Tokens file
        const cssContent = `:root {
  /* Vibe UI Chemistry: ${selectedChem.name} (${selectedChem.archetype}) */
  --vibe-canvas: ${selectedChem.colors.canvas};
  --vibe-surface: ${selectedChem.colors.surface};
  --vibe-surface-subtle: ${selectedChem.colors.surfaceSubtle};
  --vibe-border: ${selectedChem.colors.border};
  --vibe-text-primary: ${selectedChem.colors.textPrimary};
  --vibe-text-secondary: ${selectedChem.colors.textSecondary};
  --vibe-accent-primary: ${selectedChem.colors.primaryAccent};
  --vibe-accent-secondary: ${selectedChem.colors.secondaryAccent};
  --vibe-accent-highlight: ${selectedChem.colors.highlightAccent};
}
`;
        const cssPath = path.join(cwd, 'vibe-tokens.css');
        fs.writeFileSync(cssPath, cssContent, 'utf-8');
        createdFiles.push('vibe-tokens.css');
        console.log('\n\x1b[32m✔ Initialized successfully!\x1b[0m');
        console.log('\x1b[90mGenerated files:\x1b[0m');
        createdFiles.forEach((f) => console.log(`  + ${f}`));
        console.log(`
\x1b[1mNext Steps:\x1b[0m
1. Import \x1b[35mvibe-tokens.css\x1b[0m into your layout or globals.css
2. Run \x1b[32mnpx @omid-io/tokens add thinking-drawer\x1b[0m to add your first AI component
`);
    }
    finally {
        rl.close();
    }
}
function handleAdd(componentName) {
    printBanner();
    if (!componentName) {
        console.log('\x1b[33mError: Please specify a component to add.\x1b[0m\n');
        handleList();
        console.log('\nUsage: npx @omid-io/tokens add <component>');
        process.exit(1);
    }
    const comp = COMPONENT_REGISTRY[componentName.toLowerCase()];
    if (!comp) {
        console.log(`\x1b[31mError: Unknown component "${componentName}".\x1b[0m\n`);
        handleList();
        process.exit(1);
    }
    const cwd = process.cwd();
    const targetDir = path.join(cwd, 'components', 'vibe-ui');
    fs.mkdirSync(targetDir, { recursive: true });
    const targetFile = path.join(targetDir, comp.filename);
    fs.writeFileSync(targetFile, comp.code, 'utf-8');
    console.log(`\x1b[32m✔ Added component "${comp.name}"!\x1b[0m`);
    console.log(`  \x1b[90mLocation:\x1b[0m components/vibe-ui/${comp.filename}`);
    console.log(`  \x1b[90mDescription:\x1b[0m ${comp.description}\n`);
    console.log(`\x1b[1mUsage in your page or view:\x1b[0m`);
    console.log(`  import { ${comp.filename.replace('.tsx', '')} } from '@/components/vibe-ui/${comp.filename.replace('.tsx', '')}';\n`);
}
function handleList() {
    console.log('\x1b[1mAvailable Vibe UI Components:\x1b[0m');
    Object.values(COMPONENT_REGISTRY).forEach((comp) => {
        console.log(`  \x1b[32m${comp.name.padEnd(18)}\x1b[0m \x1b[90m${comp.description}\x1b[0m`);
    });
}
async function main() {
    const args = process.argv.slice(2);
    const cmd = args[0]?.toLowerCase();
    if (!cmd || cmd === '--help' || cmd === '-h') {
        printHelp();
        return;
    }
    if (cmd === '--version' || cmd === '-v') {
        console.log(`v${VERSION}`);
        return;
    }
    switch (cmd) {
        case 'init':
            await handleInit();
            break;
        case 'add':
            handleAdd(args[1]);
            break;
        case 'list':
            printBanner();
            handleList();
            break;
        default:
            console.log(`\x1b[31mUnknown command "${cmd}".\x1b[0m`);
            printHelp();
            process.exit(1);
    }
}
main().catch((err) => {
    console.error('\x1b[31mFatal CLI error:\x1b[0m', err);
    process.exit(1);
});
