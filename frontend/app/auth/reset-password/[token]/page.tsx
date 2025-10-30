import { AuthForm } from "@/components/forms/AuthForm";
import { resetPasswordSchema } from "@/lib/validators";

type ResetPasswordPageProps = {
  params: { token: string };
};

export default function ResetPasswordPage({ params }: ResetPasswordPageProps) {
  return (
    <AuthForm
      title="Reset password"
      description={`Reset token: ${params.token}`}
      submitLabel="Update password"
      schema={resetPasswordSchema}
      onSubmit={async (values) => {
        console.info("Reset password submitted", { token: params.token, ...values });
      }}
    />
  );
}
