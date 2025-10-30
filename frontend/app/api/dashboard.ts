"use server";

import { fetchDashboardOverview } from "@/lib/dashboard";

export async function dashboardOverviewAction() {
  return fetchDashboardOverview();
}
