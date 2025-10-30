"use client";

import { useState } from "react";

import type { LoginRequest, LoginResponse } from "@/lib/types";

export function useAuth() {
  const [session, setSession] = useState<LoginResponse | null>(null);

  function login(values: LoginRequest) {
    setSession({ access_token: "demo", expires_in: 900, refresh_token: null });
    console.info("Login placeholder", values);
  }

  function logout() {
    setSession(null);
  }

  return { session, login, logout };
}
