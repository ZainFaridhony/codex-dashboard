import { AuthForm } from "@/components/forms/AuthForm";
import { loginSchema } from "@/lib/validators";

export default function LoginPage() {
  return (
    <AuthForm
      title="Login"
      description="Access your Codex Dashboard account"
      submitLabel="Sign In"
      schema={loginSchema}
      onSubmit={async (values) => {
        console.info("Login submitted", values);
      }}
    />
  );
}
