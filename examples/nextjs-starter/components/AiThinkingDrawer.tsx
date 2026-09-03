'use client';

import React, { useState } from 'react';
import { cn } from '@/lib/utils';

export interface ThinkingStep {
  id: string;
  label: string;
  status: 'completed' | 'in_progress' | 'pending';
  duration?: string;
}

export interface ToolExecutionChip {
  name: string;
  latency: string;
  status: 'cached' | 'executed' | 'verified';
}

export interface AiThinkingDrawerProps {
  initialOpen?: boolean;
  isOpen?: boolean;
  onToggle?: () => void;
  title?: string;
  durationMs?: number;
  steps?: ThinkingStep[];
  tools?: ToolExecutionChip[];
  className?: string;
  isRtl?: boolean;
}

const DEFAULT_STEPS: ThinkingStep[] = [
  {
    id: 's1',
    label: 'Ingested natural language prompt & calculated ambiguity budget (Tier 1)',
    status: 'completed',
    duration: '18ms',
  },
  {
    id: 's2',
    label: 'Validated design-spec.json against Draft 2020-12 schema definitions',
    status: 'completed',
    duration: '42ms',
  },
  {
    id: 's3',
    label: 'Calculated mathematical relative luminance in OKLCH space (contrast >= 4.5:1)',
    status: 'completed',
    duration: '112ms',
  },
  {
    id: 's4',
    label: 'Constructed responsive layout tree with physical macro coordinate locking',
    status: 'completed',
    duration: '256ms',
  },
];

const DEFAULT_TOOLS: ToolExecutionChip[] = [
  { name: 'query_rag()', latency: '48ms', status: 'cached' },
  { name: 'compile_spec()', latency: '124ms', status: 'executed' },
  { name: 'verify_a11y()', latency: '16ms', status: 'verified' },
];

export function AiThinkingDrawer({
  initialOpen = true,
  isOpen: controlledIsOpen,
  onToggle,
  title = 'Reasoning Trace & Execution Flow',
  durationMs = 428,
  steps = DEFAULT_STEPS,
  tools = DEFAULT_TOOLS,
  className,
  isRtl = false,
}: AiThinkingDrawerProps) {
  const [internalOpen, setInternalOpen] = useState(initialOpen);
  const isExpanded = controlledIsOpen !== undefined ? controlledIsOpen : internalOpen;

  const handleToggle = () => {
    if (onToggle) {
      onToggle();
    } else {
      setInternalOpen((prev) => !prev);
    }
  };

  return (
    <section
      aria-label="AI Reasoning Details"
      className={cn(
        'w-full rounded-xl border border-border bg-surface text-textPrimary shadow-sm transition-all duration-200 overflow-hidden',
        className
      )}
    >
      {/* Header Accordion Trigger */}
      <button
        type="button"
        id="ai-thinking-trigger"
        aria-expanded={isExpanded}
        aria-controls="ai-thinking-content"
        onClick={handleToggle}
        className="w-full flex items-center justify-between gap-3 px-4 py-3.5 text-start cursor-pointer transition-colors hover:bg-border/20 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent min-h-[44px]"
      >
        <div className="flex items-center gap-3 min-w-0">
          {/* Radar Pulse Container */}
          <span
            className="relative flex h-3.5 w-3.5 flex-shrink-0 items-center justify-center"
            aria-hidden="true"
          >
            <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent opacity-75" />
            <span className="relative inline-flex h-2 w-2 rounded-full bg-accent" />
          </span>

          {/* Reasoning Title & Execution Pill */}
          <div className="flex flex-wrap items-center gap-2 min-w-0">
            <span className="text-sm font-semibold tracking-wide truncate">
              {title}
            </span>
            <span className="ltr-code inline-flex items-center gap-1 rounded-full bg-border/40 px-2 py-0.5 text-xs font-mono font-medium text-textMuted">
              <svg
                className="h-3 w-3 text-accent flex-shrink-0"
                viewBox="0 0 16 16"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
                aria-hidden="true"
              >
                <circle cx="8" cy="8" r="6.25" />
                <path d="M8 4.5V8L10.5 9.5" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
              <span>{durationMs}ms</span>
            </span>
          </div>
        </div>

        {/* Chevron Affordance */}
        <div className="flex items-center gap-2 flex-shrink-0">
          <span className="text-xs text-textMuted hidden sm:inline-block">
            {isExpanded ? (isRtl ? 'بستن تحلیل' : 'Hide Trace') : (isRtl ? 'نمایش تحلیل' : 'View Trace')}
          </span>
          <svg
            className={cn(
              'h-4 w-4 text-textMuted transition-transform duration-200 ease-out',
              isExpanded && 'rotate-180'
            )}
            viewBox="0 0 16 16"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <path d="M3.5 6L8 10.5L12.5 6" />
          </svg>
        </div>
      </button>

      {/* Accordion Region with CSS Grid 0fr to 1fr Transition */}
      <div
        id="ai-thinking-content"
        role="region"
        aria-labelledby="ai-thinking-trigger"
        aria-live="polite"
        className={cn(
          'grid transition-[grid-template-rows] duration-300 ease-in-out',
          isExpanded ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'
        )}
      >
        <div className="overflow-hidden">
          <div className="border-t border-border/60 px-4 py-4 space-y-4 bg-canvas/30">
            {/* Thought Steps List */}
            <div className="space-y-2.5">
              <h4 className="text-xs font-semibold uppercase tracking-wider text-textMuted">
                {isRtl ? 'مراحل استنتاج منطقی' : 'Inference Steps'}
              </h4>
              <ol className="space-y-2 text-xs">
                {steps.map((step, idx) => (
                  <li
                    key={step.id || idx}
                    className="flex items-start gap-2.5 rounded-lg p-1.5 transition-colors hover:bg-border/20"
                  >
                    {/* Status Icon */}
                    <span className="flex-shrink-0 mt-0.5" aria-hidden="true">
                      {step.status === 'completed' && (
                        <span className="flex h-4 w-4 items-center justify-center rounded-full bg-accent/20 text-accent">
                          <svg
                            className="h-2.5 w-2.5"
                            viewBox="0 0 12 12"
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="2.5"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                          >
                            <path d="M2.5 6.5L4.5 8.5L9.5 3.5" />
                          </svg>
                        </span>
                      )}
                      {step.status === 'in_progress' && (
                        <span className="flex h-4 w-4 items-center justify-center rounded-full bg-accent/20 text-accent animate-spin">
                          <svg
                            className="h-2.5 w-2.5"
                            viewBox="0 0 12 12"
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="2"
                          >
                            <circle cx="6" cy="6" r="4.5" strokeDasharray="14" strokeDashoffset="4" />
                          </svg>
                        </span>
                      )}
                      {step.status === 'pending' && (
                        <span className="flex h-4 w-4 items-center justify-center rounded-full bg-border/40 text-textMuted">
                          <span className="h-1.5 w-1.5 rounded-full bg-current" />
                        </span>
                      )}
                    </span>

                    {/* Step Description */}
                    <div className="flex flex-1 items-baseline justify-between gap-2">
                      <span className="text-textPrimary leading-relaxed">
                        {step.label}
                      </span>
                      {step.duration && (
                        <span className="ltr-code flex-shrink-0 text-[11px] font-mono text-textMuted">
                          {step.duration}
                        </span>
                      )}
                    </div>
                  </li>
                ))}
              </ol>
            </div>

            {/* Active Tool Execution Chips */}
            <div className="pt-2 border-t border-border/40">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold uppercase tracking-wider text-textMuted">
                  {isRtl ? 'ابزارهای اجرایی ایجنت' : 'Executed Subagent Tools'}
                </span>
                <span className="ltr-code text-[11px] font-mono text-textMuted">
                  {tools.length} invocations
                </span>
              </div>
              <div className="flex flex-wrap gap-2">
                {tools.map((tool, idx) => (
                  <div
                    key={idx}
                    className="ltr-code inline-flex items-center gap-1.5 rounded-md border border-border bg-surface px-2.5 py-1 text-xs font-mono shadow-xs transition-colors hover:border-accent/40"
                  >
                    {/* Tool Pure SVG Icon */}
                    <svg
                      className="h-3 w-3 text-accent flex-shrink-0"
                      viewBox="0 0 16 16"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="1.5"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      aria-hidden="true"
                    >
                      <path d="M2.5 4.5L6.5 8L2.5 11.5" />
                      <path d="M8.5 11.5H13.5" />
                    </svg>

                    <span className="font-semibold text-textPrimary">
                      {tool.name}
                    </span>

                    <span className="text-border/80">|</span>

                    <span className="text-[11px] text-textMuted">
                      {tool.latency}
                    </span>

                    {/* Status Badge */}
                    <span
                      className={cn(
                        'ms-0.5 rounded px-1 py-0.2 text-[9px] font-semibold uppercase tracking-wider',
                        tool.status === 'verified' && 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400',
                        tool.status === 'cached' && 'bg-accent/15 text-accent',
                        tool.status === 'executed' && 'bg-amber-500/15 text-amber-600 dark:text-amber-400'
                      )}
                    >
                      {tool.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default AiThinkingDrawer;
