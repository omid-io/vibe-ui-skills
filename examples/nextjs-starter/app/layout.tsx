import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Vibe UI — Production Starter (Next.js 15 & React 19)',
  description:
    'Contract-driven Next.js 15 production starter featuring typed OKLCH tokens, 5 visual chemistries, AI component primitives, and fixed-structure semantic RTL.',
  keywords: [
    'Vibe UI',
    'Next.js 15',
    'React 19',
    'Design System',
    'OKLCH',
    'AI Native Components',
    'Semantic RTL',
    'Accessibility',
  ],
  authors: [{ name: 'Omid Zaferi', url: 'https://github.com/omid-io' }],
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
  themeColor: '#09090b',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased selection:bg-accent selection:text-white min-h-screen font-sans">
        {children}
      </body>
    </html>
  );
}
