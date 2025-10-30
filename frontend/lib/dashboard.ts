import { httpClient } from "./httpClient";
import type { DashboardOverview } from "./types";

export type { DashboardWidget } from "./types";

export async function fetchDashboardOverview() {
  const { data } = await httpClient.get<DashboardOverview>("/api/dashboard/overview");
  return data;
}
