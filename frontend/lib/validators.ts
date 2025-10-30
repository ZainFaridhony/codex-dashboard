import { z } from "zod";

export const registerSchema = z.object({
  email: z.string().email(),
  password: z.string().min(12),
  first_name: z.string().optional(),
  last_name: z.string().optional()
});

export const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(1)
});

export const forgotPasswordSchema = z.object({
  email: z.string().email()
});

export const resetPasswordSchema = z.object({
  password: z.string().min(12)
});
