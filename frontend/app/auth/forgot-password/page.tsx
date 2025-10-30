import { AuthForm } from "@/components/forms/AuthForm";
import { forgotPasswordSchema } from "@/lib/validators";

export default function ForgotPasswordPage() {
  return (
    <AuthForm
      title="Forgot password"
      description="Enter your email to receive reset instructions"
      submitLabel="Send reset link"
      schema={forgotPasswordSchema}
      onSubmit={async (values) => {
        console.info("Forgot password submitted", values);
      }}
    />
  );
}
