/**
 * Vibe UI Component Registry
 * Production-ready, accessible, AI-native React component templates.
 */
export interface ComponentTemplate {
    name: string;
    filename: string;
    description: string;
    code: string;
}
export declare const COMPONENT_REGISTRY: Record<string, ComponentTemplate>;
