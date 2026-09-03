# @vibe-ui/tokens

> Typed OKLCH design tokens, physics curves, and zero-config Tailwind CSS preset for Vibe UI.

## Installation

```bash
npm install @vibe-ui/tokens
```

## Usage

### 1. Direct Token Imports

```typescript
import { VISUAL_CHEMISTRIES, MOTION_CURVES, getContrastRatio } from '@vibe-ui/tokens';

// Access typed OKLCH color spaces
const saasColors = VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors;
console.log(saasColors.primaryAccent); // 'oklch(0.65 0.22 260)'
```

### 2. Zero-Config Tailwind Plugin

In your `tailwind.config.js` or `tailwind.config.ts`:

```javascript
import vibeUiPlugin from '@vibe-ui/tokens/tailwind';

export default {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  plugins: [vibeUiPlugin],
};
```

This injects OKLCH CSS variables (`--vibe-canvas`, `--vibe-surface`, etc.) and physics utility classes (`.vibe-spring`, `.vibe-glass`).

## License

MIT © [Omid Zaferi](https://github.com/omid-io)
