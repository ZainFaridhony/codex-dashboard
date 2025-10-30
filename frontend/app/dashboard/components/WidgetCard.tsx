"use client";

import type { DashboardWidget } from "@/lib/dashboard";

export function WidgetCard({ widget }: { widget: DashboardWidget }) {
  return (
    <article className="rounded-lg border border-neutral-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-medium capitalize">{widget.type}</h2>
      <pre className="mt-2 overflow-x-auto text-sm text-neutral-700">
        {JSON.stringify(widget.data, null, 2)}
      </pre>
    </article>
  );
}
