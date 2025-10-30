import { render, screen } from "@testing-library/react";

import LoginPage from "@/app/auth/login/page";

describe("LoginPage", () => {
  it("renders the login form", () => {
    render(<LoginPage />);
    expect(screen.getByText(/login/i)).toBeInTheDocument();
  });
});
