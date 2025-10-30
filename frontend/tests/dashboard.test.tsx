import { render, screen } from "@testing-library/react";

import DashboardPage from "@/app/dashboard/page";

jest.mock("@/hooks/useDashboard", () => ({
  useDashboard: () => ({
    data: {
      user: { first_name: "Test", last_login: "2024-01-01" },
      widgets: [],
      stats: { logins_30d: 0, tasks_completed: 0 }
    },
    isLoading: false,
    error: null
  })
}));

describe("DashboardPage", () => {
  it("renders dashboard shell", () => {
    render(<DashboardPage />);
    expect(screen.getByText(/welcome back/i)).toBeInTheDocument();
  });
});
