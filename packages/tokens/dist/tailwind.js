"use strict";
/**
 * @vibe-ui/tokens/tailwind
 * Zero-config Tailwind CSS preset plugin for Vibe UI.
 */
Object.defineProperty(exports, "__esModule", { value: true });
exports.vibeUiTailwindPlugin = vibeUiTailwindPlugin;
const index_1 = require("./index");
function vibeUiTailwindPlugin({ addBase, addUtilities, theme }) {
    // Inject OKLCH CSS Custom Properties
    const rootVariables = {
        '--vibe-canvas': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.canvas,
        '--vibe-surface': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.surface,
        '--vibe-border': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.border,
        '--vibe-primary': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.primaryAccent,
        '--vibe-text-primary': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.textPrimary,
        '--vibe-text-muted': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.textMuted,
        '--vibe-ring': index_1.VISUAL_CHEMISTRIES.MINIMALIST_SAAS.colors.ring,
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
                'transition-timing-function': index_1.MOTION_CURVES.naturalSpring,
            },
            '.vibe-snap': {
                'transition-timing-function': index_1.MOTION_CURVES.responsiveSnap,
            },
            '.vibe-glass': {
                'backdrop-filter': 'blur(12px)',
                '-webkit-backdrop-filter': 'blur(12px)',
            },
        });
    }
}
exports.default = vibeUiTailwindPlugin;
