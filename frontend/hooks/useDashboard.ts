"use client";

import { useQuery } from "@tanstack/react-query";

import { fetchDashboardOverview } from "@/lib/dashboard";

export function useDashboard() {
  return useQuery({
    queryKey: ["dashboard", "overview"],
    queryFn: fetchDashboardOverview
  });
}
