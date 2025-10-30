import { AuthForm } from "@/components/forms/AuthForm";
import { registerSchema } from "@/lib/validators";

export default function RegisterPage() {
  return (
    <AuthForm
      title="Register"
      description="Create a new Codex Dashboard account"
      submitLabel="Create Account"
      schema={registerSchema}
      onSubmit={async (values) => {
        console.info("Register submitted", values);
      }}
    />
  );
}
