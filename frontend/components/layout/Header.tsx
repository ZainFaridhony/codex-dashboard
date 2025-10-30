export function Header() {
  return (
    <header className="flex items-center justify-between border-b border-neutral-200 bg-white p-4 shadow-sm">
      <span className="text-lg font-semibold">Codex Dashboard</span>
      <nav className="flex gap-4 text-sm text-neutral-600">
        <a href="/">Home</a>
        <a href="/auth/login">Login</a>
        <a href="/auth/register">Register</a>
        <a href="/dashboard">Dashboard</a>
      </nav>
    </header>
  );
}
