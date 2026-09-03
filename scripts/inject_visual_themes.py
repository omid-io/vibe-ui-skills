#!/usr/bin/env python3
"""
scripts/inject_visual_themes.py
Injects custom visual CSS properties into STUDIO_SCENARIOS in index.html & showcase/index.html
and enhances renderStudioUI to apply bespoke typography, background, border, shadow,
and button styling for all 26 canonical style families.
"""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT_DIR / "index.html"
SHOWCASE_PATH = ROOT_DIR / "showcase" / "index.html"

STYLE_VISUAL_MAP = {
    "crypto": {
        "card_style": "background: #09090b; border: 1px solid #27272a; border-radius: 12px; padding: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); color: #f4f4f5;",
        "btn_style": "flex: 1; padding: 10px 16px; background: #059669; color: #fff; border: none; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: rgba(255,255,255,0.06); border: 1px solid #27272a; color: #a1a1aa; border-radius: 8px; font-size: 12px; cursor: pointer;",
        "val_color": "#ffffff",
        "subval_color": "#10b981",
        "font_family": "'Geist Mono', monospace"
    },
    "k8s": {
        "card_style": "background: #000000; border: 1px solid rgba(16,185,129,0.5); border-radius: 2px; padding: 20px; box-shadow: 0 0 15px rgba(16,185,129,0.15); color: #34d399;",
        "btn_style": "flex: 1; padding: 10px 16px; background: rgba(6,78,59,0.5); color: #a7f3d0; border: 1px solid #10b981; border-radius: 2px; font-size: 12px; font-weight: 700; font-family: monospace; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: transparent; border: 1px solid rgba(16,185,129,0.3); color: #6ee7b7; border-radius: 2px; font-size: 12px; font-family: monospace; cursor: pointer;",
        "val_color": "#34d399",
        "subval_color": "#10b981",
        "font_family": "'Geist Mono', monospace"
    },
    "luxury": {
        "card_style": "background: #fdfbf7; border: 1px solid #e7e5e4; border-radius: 4px; padding: 22px; color: #1c1917; box-shadow: 0 4px 16px rgba(0,0,0,0.04);",
        "btn_style": "flex: 1; padding: 12px 18px; background: #1c1917; color: #fdfbf7; border: 1px solid #1c1917; border-radius: 4px; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: transparent; border: 1px solid #d6d3d1; color: #57534e; border-radius: 4px; font-size: 11px; cursor: pointer;",
        "val_color": "#1c1917",
        "subval_color": "#78716c",
        "font_family": "'Playfair Display', serif"
    },
    "clinic": {
        "card_style": "background: #f0fdfa; border: 1px solid #ccfbf1; border-radius: 16px; padding: 20px; color: #0f172a; box-shadow: 0 4px 14px rgba(20,184,166,0.06);",
        "btn_style": "flex: 1; padding: 11px 16px; background: #0d9488; color: #fff; border: none; border-radius: 12px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: #ccfbf1; border: 1px solid #99f6e4; color: #115e59; border-radius: 12px; font-size: 12px; cursor: pointer;",
        "val_color": "#0f172a",
        "subval_color": "#0d9488",
        "font_family": "'Inter', sans-serif"
    },
    "stripe": {
        "card_style": "background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; color: #0f172a; box-shadow: 0 2px 10px rgba(0,0,0,0.04);",
        "btn_style": "flex: 1; padding: 10px 16px; background: #4f46e5; color: #fff; border: none; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: #f8fafc; border: 1px solid #e2e8f0; color: #475569; border-radius: 6px; font-size: 12px; cursor: pointer;",
        "val_color": "#0f172a",
        "subval_color": "#4f46e5",
        "font_family": "'Inter', sans-serif"
    },
    "minimal_swiss": {
        "card_style": "background: #ffffff; border: 2px solid #09090b; border-radius: 0px; padding: 22px; color: #09090b;",
        "btn_style": "flex: 1; padding: 11px 16px; background: #09090b; color: #ffffff; border: 2px solid #09090b; border-radius: 0px; font-size: 11px; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: transparent; border: 2px solid #09090b; color: #09090b; border-radius: 0px; font-size: 11px; font-weight: 700; cursor: pointer;",
        "val_color": "#09090b",
        "subval_color": "#52525b",
        "font_family": "'Inter', sans-serif"
    },
    "neobrutalism": {
        "card_style": "background: #fde047; border: 3px solid #000000; border-radius: 0px; padding: 22px; color: #000000; box-shadow: 6px 6px 0px 0px #000000;",
        "btn_style": "flex: 1; padding: 12px 18px; background: #000000; color: #ffffff; border: 2px solid #000000; border-radius: 0px; font-size: 12px; font-weight: 900; letter-spacing: 0.05em; text-transform: uppercase; box-shadow: 3px 3px 0px 0px #000000; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: #ffffff; border: 2px solid #000000; color: #000000; border-radius: 0px; font-size: 12px; font-weight: 800; cursor: pointer;",
        "val_color": "#000000",
        "subval_color": "#171717",
        "font_family": "'Inter', sans-serif"
    },
    "organic_nordic": {
        "card_style": "background: #fbf9f5; border: 1px solid #e7e5e4; border-radius: 12px; padding: 22px; color: #292524; box-shadow: 0 4px 12px rgba(0,0,0,0.03);",
        "btn_style": "flex: 1; padding: 11px 16px; background: #292524; color: #fbf9f5; border: none; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: #f5f5f4; border: 1px solid #e7e5e4; color: #57534e; border-radius: 8px; font-size: 12px; cursor: pointer;",
        "val_color": "#1c1917",
        "subval_color": "#78716c",
        "font_family": "'Playfair Display', serif"
    },
    "bauhaus_geometric": {
        "card_style": "background: #f7f5f0; border: 2px solid #09090b; border-radius: 0px; padding: 22px; color: #09090b;",
        "btn_style": "flex: 1; padding: 11px 16px; background: #1d4ed8; color: #fff; border: 2px solid #09090b; border-radius: 0px; font-size: 11px; font-weight: 800; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: #eab308; border: 2px solid #09090b; color: #000; border-radius: 0px; font-size: 11px; font-weight: 800; cursor: pointer;",
        "val_color": "#09090b",
        "subval_color": "#b91c1c",
        "font_family": "'Inter', sans-serif"
    },
    "modern_glass_2": {
        "card_style": "background: rgba(15,23,42,0.65); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(255,255,255,0.25); border-radius: 16px; padding: 22px; box-shadow: inset 0 1px 1px rgba(255,255,255,0.4), 0 12px 28px rgba(0,0,0,0.5); color: #ffffff;",
        "btn_style": "flex: 1; padding: 11px 16px; background: linear-gradient(135deg, #06b6d4, #3b82f6); color: #fff; border: none; border-radius: 10px; font-size: 12px; font-weight: 600; box-shadow: 0 4px 12px rgba(6,182,212,0.3); cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2); color: #e2e8f0; border-radius: 10px; font-size: 12px; cursor: pointer;",
        "val_color": "#ffffff",
        "subval_color": "#22d3ee",
        "font_family": "'Inter', sans-serif"
    },
    "retro_futurism": {
        "card_style": "background: #090514; border: 1px solid rgba(139,92,246,0.5); border-radius: 6px; padding: 20px; color: #ddd6fe; box-shadow: 0 0 18px rgba(139,92,246,0.3);",
        "btn_style": "flex: 1; padding: 11px 16px; background: #d946ef; color: #fff; border: none; border-radius: 4px; font-size: 12px; font-weight: 700; font-family: monospace; letter-spacing: 0.05em; text-transform: uppercase; box-shadow: 0 0 12px rgba(217,70,239,0.5); cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: rgba(139,92,246,0.15); border: 1px solid rgba(139,92,246,0.4); color: #c084fc; border-radius: 4px; font-size: 12px; font-family: monospace; cursor: pointer;",
        "val_color": "#f5d0fe",
        "subval_color": "#a855f7",
        "font_family": "'Geist Mono', monospace"
    },
    "editorial_magazine": {
        "card_style": "background: #faf8f5; border: 1px solid #d4d4d8; border-radius: 0px; padding: 22px; color: #09090b;",
        "btn_style": "flex: 1; padding: 11px 16px; background: transparent; border-bottom: 2px solid #09090b; color: #09090b; border-radius: 0px; font-size: 11px; font-weight: 700; text-transform: uppercase; text-align: left; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: transparent; border: 1px solid #d4d4d8; color: #52525b; border-radius: 0px; font-size: 11px; cursor: pointer;",
        "val_color": "#09090b",
        "subval_color": "#71717a",
        "font_family": "'Playfair Display', serif"
    },
    "industrial_utility": {
        "card_style": "background: #18181b; border: 2px solid #f59e0b; border-radius: 2px; padding: 20px; color: #fbbf24; font-family: monospace;",
        "btn_style": "flex: 1; padding: 11px 16px; background: rgba(220,38,38,0.7); color: #fff; border: 2px solid #ef4444; border-radius: 2px; font-size: 11px; font-weight: 900; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 11px 14px; background: #27272a; border: 1px solid #f59e0b; color: #fbbf24; border-radius: 2px; font-size: 11px; font-weight: 700; cursor: pointer;",
        "val_color": "#fef08a",
        "subval_color": "#f59e0b",
        "font_family": "'Geist Mono', monospace"
    },
    "biophilic_wellness": {
        "card_style": "background: #f4f7f4; border: 1px solid rgba(6,78,59,0.15); border-radius: 24px; padding: 22px; color: #022c22; box-shadow: 0 4px 16px rgba(6,78,59,0.05);",
        "btn_style": "flex: 1; padding: 12px 18px; background: #065f46; color: #ffffff; border: none; border-radius: 16px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: #d1fae5; border: 1px solid #a7f3d0; color: #065f46; border-radius: 16px; font-size: 12px; cursor: pointer;",
        "val_color": "#064e3b",
        "subval_color": "#059669",
        "font_family": "'Inter', sans-serif"
    },
    "futuristic_tech": {
        "card_style": "background: #080d14; border: 1px solid rgba(6,182,212,0.4); border-radius: 4px; padding: 20px; color: #67e8f9; box-shadow: 0 0 16px rgba(6,182,212,0.15);",
        "btn_style": "flex: 1; padding: 10px 16px; background: rgba(6,182,212,0.2); color: #a5f3fc; border: 1px solid #22d3ee; border-radius: 2px; font-size: 11px; font-weight: 700; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: transparent; border: 1px solid rgba(6,182,212,0.3); color: #67e8f9; border-radius: 2px; font-size: 11px; font-family: monospace; cursor: pointer;",
        "val_color": "#e0f2fe",
        "subval_color": "#22d3ee",
        "font_family": "'Geist Mono', monospace"
    },
    "retro_computing_80s": {
        "card_style": "background: #110c00; border: 1px solid rgba(245,158,11,0.6); border-radius: 0px; padding: 20px; color: #f59e0b; box-shadow: 0 0 16px rgba(245,158,11,0.2); font-family: monospace;",
        "btn_style": "flex: 1; padding: 10px 16px; background: rgba(245,158,11,0.15); color: #fbbf24; border: 1px solid #f59e0b; border-radius: 0px; font-size: 11px; font-weight: 700; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: transparent; border: 1px solid rgba(245,158,11,0.4); color: #d97706; border-radius: 0px; font-size: 11px; font-family: monospace; cursor: pointer;",
        "val_color": "#fbbf24",
        "subval_color": "#f59e0b",
        "font_family": "'Geist Mono', monospace"
    },
    "y2k_aesthetic": {
        "card_style": "background: rgba(224,242,254,0.7); backdrop-filter: blur(8px); border: 2px solid #7dd3fc; border-radius: 24px; padding: 22px; color: #082f49; box-shadow: inset 0 2px 4px rgba(255,255,255,0.8), 0 8px 20px rgba(14,165,233,0.15);",
        "btn_style": "flex: 1; padding: 11px 18px; background: linear-gradient(135deg, #38bdf8, #6366f1); color: #fff; border: none; border-radius: 9999px; font-size: 12px; font-weight: 700; box-shadow: 0 4px 10px rgba(56,189,248,0.4); cursor: pointer;",
        "sec_btn_style": "padding: 11px 16px; background: rgba(255,255,255,0.8); border: 1px solid #7dd3fc; color: #0369a1; border-radius: 9999px; font-size: 12px; font-weight: 700; cursor: pointer;",
        "val_color": "#0c4a6e",
        "subval_color": "#0284c7",
        "font_family": "'Inter', sans-serif"
    },
    "enterprise_dense": {
        "card_style": "background: #ffffff; border: 1px solid #cbd5e1; border-radius: 4px; padding: 18px; color: #0f172a; box-shadow: 0 1px 4px rgba(0,0,0,0.05);",
        "btn_style": "flex: 1; padding: 9px 14px; background: #0f172a; color: #fff; border: none; border-radius: 4px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "sec_btn_style": "padding: 9px 12px; background: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; border-radius: 4px; font-size: 12px; cursor: pointer;",
        "val_color": "#0f172a",
        "subval_color": "#475569",
        "font_family": "'Inter', sans-serif"
    },
    "financial_terminal": {
        "card_style": "background: #000000; border: 1px solid #262626; border-radius: 0px; padding: 18px; color: #e5e5e5; font-family: monospace;",
        "btn_style": "flex: 1; padding: 9px 14px; background: #171717; color: #f59e0b; border: 1px solid #525252; border-radius: 0px; font-size: 11px; font-weight: 700; font-family: monospace; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 9px 12px; background: transparent; border: 1px solid #262626; color: #737373; border-radius: 0px; font-size: 11px; font-family: monospace; cursor: pointer;",
        "val_color": "#10b981",
        "subval_color": "#ef4444",
        "font_family": "'Geist Mono', monospace"
    },
    "civic_institutional": {
        "card_style": "background: #f8f9fa; border: 2px solid #1e3a8a; border-radius: 4px; padding: 22px; color: #172554; box-shadow: 0 2px 8px rgba(30,58,138,0.06);",
        "btn_style": "flex: 1; padding: 12px 18px; background: #1e3a8a; color: #fff; border: none; border-radius: 4px; font-size: 12px; font-weight: 700; letter-spacing: 0.03em; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: #e0e7ff; border: 1px solid #c7d2fe; color: #1e3a8a; border-radius: 4px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "val_color": "#172554",
        "subval_color": "#1e3a8a",
        "font_family": "'Inter', sans-serif"
    },
    "playful_consumer": {
        "card_style": "background: #eef2ff; border: 2px solid #c7d2fe; border-radius: 20px; padding: 22px; color: #1e1b4b; box-shadow: 0 4px 16px rgba(99,102,241,0.08);",
        "btn_style": "flex: 1; padding: 12px 18px; background: #4f46e5; color: #fff; border: none; border-radius: 14px; font-size: 12px; font-weight: 700; box-shadow: 0 4px 12px rgba(79,70,229,0.3); cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: #ffffff; border: 1px solid #c7d2fe; color: #4338ca; border-radius: 14px; font-size: 12px; font-weight: 600; cursor: pointer;",
        "val_color": "#312e81",
        "subval_color": "#4f46e5",
        "font_family": "'Inter', sans-serif"
    },
    "mobile_native_consumer": {
        "card_style": "background: rgba(255,255,255,0.96); backdrop-filter: blur(14px); border: 1px solid rgba(228,228,231,0.8); border-radius: 24px; padding: 22px; color: #18181b; box-shadow: 0 12px 30px rgba(0,0,0,0.08);",
        "btn_style": "flex: 1; padding: 13px 18px; background: #18181b; color: #fff; border: none; border-radius: 16px; font-size: 12px; font-weight: 700; min-height: 48px; cursor: pointer;",
        "sec_btn_style": "padding: 13px 14px; background: #f4f4f5; border: 1px solid #e4e4e7; color: #52525b; border-radius: 16px; font-size: 12px; min-height: 48px; cursor: pointer;",
        "val_color": "#09090b",
        "subval_color": "#16a34a",
        "font_family": "'Inter', sans-serif"
    },
    "art_gallery": {
        "card_style": "background: #fcfbf9; border: none; border-radius: 0px; padding: 28px 22px; color: #000000;",
        "btn_style": "flex: 1; padding: 12px 18px; background: #000000; color: #ffffff; border: none; border-radius: 0px; font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: transparent; border-bottom: 1px solid #000; color: #000000; border-radius: 0px; font-size: 11px; cursor: pointer;",
        "val_color": "#000000",
        "subval_color": "#525252",
        "font_family": "'Playfair Display', serif"
    },
    "high_end_hospitality": {
        "card_style": "background: #0d0a07; border: 1px solid rgba(245,158,11,0.3); border-radius: 8px; padding: 22px; color: #fef3c7; box-shadow: 0 8px 24px rgba(0,0,0,0.6);",
        "btn_style": "flex: 1; padding: 12px 18px; background: rgba(245,158,11,0.15); color: #fde68a; border: 1px solid #f59e0b; border-radius: 6px; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: transparent; border: 1px solid rgba(245,158,11,0.25); color: #fcd34d; border-radius: 6px; font-size: 11px; cursor: pointer;",
        "val_color": "#fffbeb",
        "subval_color": "#f59e0b",
        "font_family": "'Playfair Display', serif"
    },
    "cultural_heritage": {
        "card_style": "background: #f5efe4; border: 1px solid rgba(67,45,32,0.25); border-radius: 2px; padding: 22px; color: #2b1d14; box-shadow: 0 2px 8px rgba(43,29,20,0.05);",
        "btn_style": "flex: 1; padding: 12px 18px; background: #2b1d14; color: #f5efe4; border: 1px solid #2b1d14; border-radius: 2px; font-size: 11px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 12px 14px; background: transparent; border: 1px solid rgba(67,45,32,0.3); color: #4a3325; border-radius: 2px; font-size: 11px; cursor: pointer;",
        "val_color": "#23170e",
        "subval_color": "#7d5840",
        "font_family": "'Playfair Display', serif"
    },
    "scientific_dashboard": {
        "card_style": "background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 20px; color: #6ee7b7; box-shadow: 0 4px 14px rgba(0,0,0,0.3); font-family: monospace;",
        "btn_style": "flex: 1; padding: 10px 16px; background: rgba(16,185,129,0.2); color: #a7f3d0; border: 1px solid #10b981; border-radius: 4px; font-size: 11px; font-weight: 700; font-family: monospace; letter-spacing: 0.05em; text-transform: uppercase; cursor: pointer;",
        "sec_btn_style": "padding: 10px 14px; background: #1e293b; border: 1px solid #334155; color: #94a3b8; border-radius: 4px; font-size: 11px; font-family: monospace; cursor: pointer;",
        "val_color": "#ffffff",
        "subval_color": "#34d399",
        "font_family": "'Geist Mono', monospace"
    }
}

def inject_file(file_path):
    content = file_path.read_text(encoding="utf-8")

    # 1. Update renderStudioUI default branch to read dynamic visual themes
    old_render = """      if (currentStudioState === 'default') {
        canvas.innerHTML = `
          <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-subtle); padding-bottom: 12px; margin-bottom: 14px;">
              <div>
                <h4 style="margin: 0; font-size: 15px; font-weight: 700; color: var(--text-vivid);">${titleText}</h4>
                <span style="font-size: 11px; color: var(--text-faint);">${subText}</span>
              </div>
              <span class="studio-badge" style="font-size: 10px; padding: 4px 8px;">${badgeText}</span>
            </div>
            <div style="margin: 16px 0; direction: ltr; text-align: left;">
              <div style="font-size: 24px; font-weight: 800; font-family: 'Geist Mono', monospace; color: var(--text-vivid);">${sc.value}</div>
              <div style="font-size: 12px; color: #10b981; font-family: 'Geist Mono', monospace; margin-top: 2px;">${subvalText}</div>
            </div>
            <div style="display: flex; gap: 8px; margin-top: 16px;">
              <button type="button" style="flex: 1; padding: 10px 16px; background: var(--accent); color: #fff; border: none; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;">${actionText}</button>
              <button type="button" style="padding: 10px 14px; background: rgba(255,255,255,0.06); border: 1px solid var(--border-subtle); color: var(--text-muted); border-radius: 8px; font-size: 12px; cursor: pointer;">${secActionText}</button>
            </div>
          </div>
        `;"""

    new_render = """      if (currentStudioState === 'default') {
        const cardStyle = sc.card_style || 'background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 20px;';
        const btnStyle = sc.btn_style || 'flex: 1; padding: 10px 16px; background: var(--accent); color: #fff; border: none; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;';
        const secBtnStyle = sc.sec_btn_style || 'padding: 10px 14px; background: rgba(255,255,255,0.06); border: 1px solid var(--border-subtle); color: var(--text-muted); border-radius: 8px; font-size: 12px; cursor: pointer;';
        const valColor = sc.val_color || 'var(--text-vivid)';
        const subvalColor = sc.subval_color || '#10b981';
        const fontFamily = sc.font_family || 'inherit';

        canvas.innerHTML = `
          <div style="${cardStyle} transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(128,128,128,0.2); padding-bottom: 12px; margin-bottom: 14px;">
              <div>
                <h4 style="margin: 0; font-size: 15px; font-weight: 700; color: inherit; font-family: ${fontFamily};">${titleText}</h4>
                <span style="font-size: 11px; opacity: 0.75; font-family: ${fontFamily};">${subText}</span>
              </div>
              <span class="studio-badge" style="font-size: 10px; padding: 4px 8px; font-family: monospace;">${badgeText}</span>
            </div>
            <div style="margin: 16px 0; direction: ltr; text-align: left; font-family: ${fontFamily};">
              <div style="font-size: 24px; font-weight: 800; color: ${valColor}; letter-spacing: -0.02em;">${sc.value}</div>
              <div style="font-size: 12px; color: ${subvalColor}; margin-top: 3px; font-weight: 500;">${subvalText}</div>
            </div>
            <div style="display: flex; gap: 8px; margin-top: 16px;">
              <button type="button" style="${btnStyle}">${actionText}</button>
              <button type="button" style="${secBtnStyle}">${secActionText}</button>
            </div>
          </div>
        `;"""

    if old_render in content:
        content = content.replace(old_render, new_render)
        print(f"Updated renderStudioUI in {file_path.name}")
    else:
        print(f"Notice: old_render not exact match in {file_path.name}, checking regex...")
        pat = r"if \(currentStudioState === 'default'\) \{.*?canvas\.innerHTML = `.*?<\/div>\s*`;"
        content, c = re.subn(pat, new_render, content, flags=re.DOTALL)
        print(f"Regex replaced renderStudioUI: {c} times")

    # 2. Inject properties into each scenario in STUDIO_SCENARIOS
    for key, styles in STYLE_VISUAL_MAP.items():
        # Look for "key": {
        pat = rf'"{key}": \{{'
        if pat in content:
            # Check if card_style already present
            check_pat = rf'"{key}": \{{[^}}]*"card_style":'
            if not re.search(check_pat, content):
                injected_props = (
                    f'\n            "card_style": "{styles["card_style"]}",\n'
                    f'            "btn_style": "{styles["btn_style"]}",\n'
                    f'            "sec_btn_style": "{styles["sec_btn_style"]}",\n'
                    f'            "val_color": "{styles["val_color"]}",\n'
                    f'            "subval_color": "{styles["subval_color"]}",\n'
                    f'            "font_family": "{styles["font_family"]}",'
                )
                content = content.replace(f'"{key}": {{', f'"{key}": {{{injected_props}')

    file_path.write_text(content, encoding="utf-8")
    print(f"Done injecting styles into {file_path.name}")

def main():
    inject_file(INDEX_PATH)
    inject_file(SHOWCASE_PATH)

if __name__ == "__main__":
    main()
