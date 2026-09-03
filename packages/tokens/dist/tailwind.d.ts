/**
 * @vibe-ui/tokens/tailwind
 * Configurable OKLCH Tailwind CSS preset plugin for Vibe UI supporting all Visual Chemistries.
 */
import { VisualChemistryId } from './index';
export interface VibeUiPluginOptions {
    chemistry?: VisualChemistryId;
}
export declare function createVibeUiPlugin(options?: VibeUiPluginOptions): ({ addBase, addUtilities }: any) => void;
export declare function vibeUiTailwindPlugin(arg: any): void | (({ addBase, addUtilities }: any) => void);
export default vibeUiTailwindPlugin;
