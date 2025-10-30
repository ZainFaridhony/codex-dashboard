import "../styles/globals.css";
import type { Metadata } from "next";
import { ReactNode } from "react";

import { Header } from "@/components/layout/Header";

export const metadata: Metadata = {
  title: "Codex Dashboard",
  description: "Full-stack dashboard for authentication and analytics"
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-neutral-50 text-neutral-900">
        <Header />
        <main>{children}</main>
      </body>
    </html>
  );
}
