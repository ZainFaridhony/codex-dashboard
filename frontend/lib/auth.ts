import { httpClient } from "./httpClient";
import type {
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  RegisterResponse,
  PasswordForgotRequest,
  PasswordResetRequest
} from "./types";

export async function register(payload: RegisterRequest) {
  const { data } = await httpClient.post<RegisterResponse>("/api/auth/register", payload);
  return data;
}

export async function login(payload: LoginRequest) {
  const { data } = await httpClient.post<LoginResponse>("/api/auth/login", payload);
  return data;
}

export async function forgotPassword(payload: PasswordForgotRequest) {
  await httpClient.post("/api/auth/password/forgot", payload);
}

export async function resetPassword(payload: PasswordResetRequest) {
  await httpClient.post("/api/auth/password/reset", payload);
}
