"use client";

import { useDashboard } from "@/hooks/useDashboard";
import { WidgetCard } from "./WidgetCard";

export function DashboardShell() {
  const { data, isLoading, error } = useDashboard();

  if (isLoading) {
    return <p>Loading dashboard…</p>;
  }

  if (error || !data) {
    return <p className="text-red-600">Unable to load dashboard data.</p>;
  }

  return (
    <section className="space-y-6 p-6">
      <header>
        <h1 className="text-3xl font-semibold">Welcome back, {data.user.first_name ?? "User"}</h1>
        <p className="text-sm text-neutral-600">Last login: {data.user.last_login ?? "Unknown"}</p>
      </header>
      <div className="grid gap-4 md:grid-cols-2">
        {data.widgets.map((widget) => (
          <WidgetCard key={widget.id} widget={widget} />
        ))}
      </div>
    </section>
  );
}
