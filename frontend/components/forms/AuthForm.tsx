"use client";

import { useState } from "react";
import { z, ZodSchema } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

export type AuthFormProps<TSchema extends ZodSchema> = {
  title: string;
  description: string;
  submitLabel: string;
  schema: TSchema;
  onSubmit: (values: z.infer<TSchema>) => Promise<void>;
};

export function AuthForm<TSchema extends ZodSchema>({
  title,
  description,
  submitLabel,
  schema,
  onSubmit
}: AuthFormProps<TSchema>) {
  const [message, setMessage] = useState<string | null>(null);
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting }
  } = useForm<z.infer<TSchema>>({
    resolver: zodResolver(schema)
  });

  return (
    <form
      className="mx-auto mt-12 flex w-full max-w-md flex-col gap-4 rounded-lg border border-neutral-200 bg-white p-6 shadow-sm"
      onSubmit={handleSubmit(async (values) => {
        setMessage(null);
        try {
          await onSubmit(values);
          setMessage("Submitted successfully");
        } catch (error) {
          setMessage(error instanceof Error ? error.message : "An unexpected error occurred");
        }
      })}
    >
      <header className="space-y-1">
        <h1 className="text-2xl font-semibold">{title}</h1>
        <p className="text-sm text-neutral-600">{description}</p>
      </header>

      {Object.entries(schema.shape).map(([field]) => (
        <div className="flex flex-col gap-1" key={field}>
          <label className="text-sm font-medium capitalize" htmlFor={field}>
            {field.replace(/_/g, " ")}
          </label>
          <input
            id={field}
            className="rounded border border-neutral-300 px-3 py-2"
            type={field.toLowerCase().includes("password") ? "password" : "text"}
            {...register(field as keyof z.infer<TSchema>)}
          />
          {errors[field as keyof z.infer<TSchema>] && (
            <span className="text-sm text-red-600">
              {errors[field as keyof z.infer<TSchema>]?.message as string}
            </span>
          )}
        </div>
      ))}

      <button
        type="submit"
        className="mt-4 rounded bg-blue-600 px-4 py-2 font-medium text-white hover:bg-blue-700"
        disabled={isSubmitting}
      >
        {isSubmitting ? "Submitting…" : submitLabel}
      </button>

      {message && <p className="text-sm text-neutral-700">{message}</p>}
    </form>
  );
}
