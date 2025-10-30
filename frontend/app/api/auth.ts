"use server";

import { forgotPassword, login, register, resetPassword } from "@/lib/auth";
import type {
  LoginRequest,
  RegisterRequest,
  PasswordForgotRequest,
  PasswordResetRequest
} from "@/lib/types";

export async function registerAction(payload: RegisterRequest) {
  return register(payload);
}

export async function loginAction(payload: LoginRequest) {
  return login(payload);
}

export async function forgotPasswordAction(payload: PasswordForgotRequest) {
  return forgotPassword(payload);
}

export async function resetPasswordAction(payload: PasswordResetRequest) {
  return resetPassword(payload);
}
