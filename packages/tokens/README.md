# @omid-io/tokens

> Typed OKLCH design tokens, physics curves, and zero-config Tailwind CSS preset for Vibe UI.

## Installation

```bash
npm install @omid-io/tokens
```

## Quick Start with CLI

### 1. Initialize Workspace Contracts (`init`)

Scaffold AI editor contracts (`.cursorrules`, `CLAUDE.md`, `.windsurfrules`) and OKLCH CSS variables in 3 seconds:

```bash
npx @omid-io/tokens init
```

### 2. Add AI-Native Components (`add`)

Add accessible, zero-emoji, verified React 19 component templates directly into your project (`components/vibe-ui/`):

```bash
npx @omid-io/tokens add thinking-drawer
npx @omid-io/tokens add telemetry-hud
npx @omid-io/tokens add contrast-badge
```

### 3. List Registry Components (`list`)

```bash
npx @omid-io/tokens list
```

## Programmatic Usage

### 1. Direct Token Imports

```typescript
import { VISUAL_CHEMISTRIES, MOTION_CURVES, getContrastRatio } from '@omid-io/tokens';

// Access typed OKLCH color spaces
const saasColors = VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors;
console.log(saasColors.primaryAccent); // 'oklch(0.65 0.22 260)'
```

### 2. Zero-Config Tailwind Plugin

In your `tailwind.config.js` or `tailwind.config.ts`:

```javascript
import vibeUiPlugin from '@omid-io/tokens/tailwind';

export default {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  plugins: [vibeUiPlugin],
};
```

This injects OKLCH CSS variables (`--vibe-canvas`, `--vibe-surface`, etc.) and physics utility classes (`.vibe-spring`, `.vibe-glass`).

## License

MIT © [Omid Zaferi](https://github.com/omid-io)
