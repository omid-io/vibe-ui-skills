/**
 * @vibe-ui/tokens/tailwind
 * Zero-config Tailwind CSS preset plugin for Vibe UI.
 */

import { VISUAL_CHEMISTRIES, MOTION_CURVES } from './index';

export function vibeUiTailwindPlugin({ addBase, addUtilities, theme }: any) {
  // Inject OKLCH CSS Custom Properties
  const rootVariables: Record<string, string> = {
    '--vibe-canvas': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.canvas,
    '--vibe-surface': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.surface,
    '--vibe-border': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.border,
    '--vibe-primary': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.primaryAccent,
    '--vibe-text-primary': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.textPrimary,
    '--vibe-text-muted': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.textMuted,
    '--vibe-ring': VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.ring,
  };

  if (addBase) {
    addBase({
      ':root': rootVariables,
      '[dir="rtl"]': {
        'letter-spacing': 'normal !important',
      },
    });
  }

  if (addUtilities) {
    addUtilities({
      '.vibe-spring': {
        'transition-timing-function': MOTION_CURVES.naturalSpring,
      },
      '.vibe-snap': {
        'transition-timing-function': MOTION_CURVES.responsiveSnap,
      },
      '.vibe-glass': {
        'backdrop-filter': 'blur(12px)',
        '-webkit-backdrop-filter': 'blur(12px)',
      },
    });
  }
}

export default vibeUiTailwindPlugin;
